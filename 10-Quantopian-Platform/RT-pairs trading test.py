import numpy as np

# initiate - schedule function
def initialize(context):
    schedule_function(check_std, date_rules.every_day(),
                      time_rules.market_close(minutes=60))
    
    context.jj = sid(4151)
    
    # context.long_port = False
    # context.short_port = False
    
def check_std(context, data):
    
    prices = data.history(context.jj, 'price', 20, '1d')
    
    current_price = data.current(context.jj, 'price')
    
    mav_20 = np.mean(prices)
    std_20 = np.std(prices)
    upper_band = mav_20 + std_20 * 2
    lower_band = mav_20 - std_20 * 2
    
    # long_flag =  bool(current_price < (mav_20 - (std_20 * 2)))
    # short_flag = bool(current_price > (mav_20 + (std_20 * 2)))
    
    if current_price < lower_band:
        order_target_percent(context.jj, 1.0)
        # context.long_port = True
        # context.short_port = False
        
    elif current_price > upper_band:
        order_target_percent(context.jj, -1.0)
        # context.long_port = False
        # context.short_port = True
        
    else:
        pass

    record(upper=upper_band,
           lower=lower_band,
           mvag_20=mav_20,
           price=current_price)
