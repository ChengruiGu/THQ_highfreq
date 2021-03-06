from rqalpha.apis import *


# 在这个方法中编写任何的初始化逻辑。context对象将会在你的算法策略的任何方法之间做传递。
def init(context):
    logger.info("init")
    context.s1 = "000157.XSHE"
    update_universe(context.s1)
    # 是否已发送了order
    context.fired = False
    context.count = 0


def before_trading(context):
    context.count = 0


# 你选择的证券的数据更新将会触发此段逻辑，例如日或分钟历史数据切片或者是实时数据切片更新
def handle_bar(context, bar_dict):
    # 开始编写你的主要的算法逻辑

    # bar_dict[order_book_id] 可以拿到某个证券的bar信息
    # context.portfolio 可以拿到现在的投资组合状态信息

    # 使用order_shares(id_or_ins, amount)方法进行落单

    # TODO: 开始编写你的算法吧！
    if not context.fired:
        # order_percent并且传入1代表买入该股票并且使其占有投资组合的100%
        order_percent(context.s1, 1)
        context.fired = True
        logger.info(bar_dict)


def handle_tick(context, tick):
    logger.info(tick['datetime'])
    logger.info(tick['last'])
    context.count += 1
    logger.info(context.count)

# __config__ = {
#     "base": {
#         "start_date": "2020-10-09",
#         "end_date": "2020-10-10",
#         "frequency": "tick",
#         "matching_type": "last",
#         "benchmark": None,
#         "accounts": {
#             "stock": 1000000
#         }
#     },
#     "extra": {
#         "log_level": "verbose",
#     },
# }

