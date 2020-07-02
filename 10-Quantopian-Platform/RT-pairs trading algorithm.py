import numpy as np

# initialize - schedule function
def initialize(context):
    schedule_function(check_pairs, date_rules.every_day(), 
                      time_rules.market_close(minutes=60))
    
    context.aal = sid(45971)
    context.ual = sid(28051)
    
    context.long_on_spread = False
    context.shorting_spread = False
    
# check pairs
def check_pairs(context, data):
    
    aa = context.aal
    ual = context.ual
    
    prices = data.history([aa, ual], 'price', 30, '1d')
    
    short_prices = prices.iloc[-1:]
    
    # spread
    mav_30 = np.mean(prices[aa] - prices[ual])
    std_30 = np.std(prices[aa] - prices[ual])
    
    mav_1 = np.mean(short_prices[aa] - short_prices[ual])
    
    if std_30 > 0:
        z_score = (mav_1 - mav_30) / std_30
        
        if z_score > 1.0 and not context.shorting_spread:
            # spread = AA - UAL
            order_target_percent(aa, -0.5)
            order_target_percent(ual, 0.5)
            context.shorting_spread = True
            context.long_on_spread = False
            
        elif z_score < 1.0 and not context.long_on_spread:
            order_target_percent(aa, 0.5)
            order_target_percent(ual, -0.5)
            context.long_on_spread = True
            context.shorting_spread = False
            
        elif abs(z_score) < 0.1:
            order_target_percent(aa, 0)
            order_target_percent(ual, 0)
            context.long_on_spread = False
            context.shorting_spread = False
            
        record(zscore = z_score)    
            
