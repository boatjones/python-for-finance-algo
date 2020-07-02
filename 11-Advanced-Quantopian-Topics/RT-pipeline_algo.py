from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
# from quantopian.research import run_pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.filters import Q1500US
from quantopian.pipeline.data import morningstar
from quantopian.pipeline.factors import SimpleMovingAverage, AverageDollarVolume
from quantopian.pipeline.classifiers.morningstar import Sector


def initialize(context):
    
    schedule_function(my_rebalance, date_rules.week_start(), 
                      time_rules.market_open(hours=1))
    
    my_pipe = make_pipeline()
    attach_pipeline(my_pipe, 'my_pipeline')
    
def my_rebalance(context,data):
    for security in context.portfolio.positions:
        if security not in context.longs and security not in context.shorts and data.can_trade(security):
            order_target_percent(security, 0)

    for security in context.longs:
        if data.can_trade(security):
            order_target_percent(security, context.long_weight)
            
    for security in context.shorts:
        if data.can_trade(security):
            order_target_percent(security, context.short_weight)

def my_compute_weights(context):
    if len(context.longs) == 0:
        long_weight = 0
    else:
        long_weight = 0.5 / len(context.longs)
    
    if len(context.shorts) == 0:
        short_weight = 0
    else:
        short_weight = -0.5 / len(context.shorts)
    
    return(long_weight, short_weight)

def before_trading_start(context,data):
    context.output = pipeline_output('my_pipeline')
    
    # long
    # print(context.output)
    context.longs = context.output[context.output['longs']].index.tolist()
    
    # short
    context.shorts = context.output[context.output['shorts']].index.tolist()
    
    context.long_weight, context.short_weight = my_compute_weights(context)

def make_pipeline():
    
    # Get the universe of 1500 most liquid stocks Q1500US
    base_universe = Q1500US()
    
    # Get the energy sector stocks from it
    sector = morningstar.asset_classification.morningstar_sector_code.latest
    energy_sector = sector.eq(309)
    
    # make mask of 1500 US & energy stocks
    base_energy = base_universe & energy_sector
    
    # get Average Dollar Volume info over past 30 days
    dollar_volume = AverageDollarVolume(window_length=30)
    
    # get top 5% of average dollar volume
    high_dollar_volume = dollar_volume.percentile_between(95,100)
    
    # Combine the filters
    top_five_base_energy = base_energy & high_dollar_volume
    
    # get 10 day mean close
    mean_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], 
                                  window_length=10, 
                                  mask=top_five_base_energy)
    
    # get 30 day mean close
    mean_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], 
                                  window_length=30,
                                  mask=top_five_base_energy)
    
    # percent difference between 10 & 30 day close
    percent_diff = ((mean_10 - mean_30) / mean_30) * 100
    
    # make list of shorts
    shorts = percent_diff < 0
    
    # make list of longs
    longs = percent_diff > 0
    
    # make a final filter for shorts or longs
    securities_to_trade = (shorts | longs)
    
    # return pipeline
    return Pipeline(columns={'shorts':shorts, 
                             'longs':longs,
                             'perc_diff':percent_diff}, 
                    screen=securities_to_trade)
