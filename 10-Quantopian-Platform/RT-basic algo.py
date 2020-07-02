def initialize(context):
    context.amzn= sid(16841)
    context.ibm = sid(3766)
    
    schedule_function(rebalance, date_rules.every_day(), 
                      time_rules.market_open())
    schedule_function(record_vars, date_rules.every_day(),
                      time_rules.market_close())
    
def rebalance(context, data):
    order_target_percent(context.amzn, 0.5)
    order_target_percent(context.ibm, -0.5)
    
def record_vars(context, data):
    record(amzn_close = data.current(context.amzn, 'close'))
    record(ibm_close = data.current(context.ibm, 'close'))
