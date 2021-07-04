from rqalpha.apis import *


# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    logger.info("init")
    context.s1 = "000651.XSHE"
    update_universe(context.s1)
    #context.SHORTPERIOD = 20
    context.LONGPERIOD = 100


def calc_ma(prices):
    assert len(prices) > 0
    result = 0
    for tick in prices:
        result += tick['last']
    result = result / len(prices)
    return round(result, 2)


def handle_tick(context, tick):
    prices = history_ticks(context.s1, context.LONGPERIOD + 1)
    if len(prices) > 0:
        ma = calc_ma(prices)
        p = tick['last']
        logger.info("ma is: " + str(ma) + "; current price is: " + str(p))
        cur_position = get_position(context.s1).quantity
        cash = context.portfolio.cash

        if p > 1.005*ma and cash > 0:
            shares = round(cash / p)
            order_shares(context.s1, shares)
            logger.info("买入!!!!!!!!!!!!!!!!!!!!!")
        elif p < ma and cur_position > 0:
            order_target_value(context.s1, 0)
            logger.info("卖出!!!!!!!!!!!!!!!!!!!!!")

