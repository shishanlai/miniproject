from Api.apiFactory import ApiFactory

#
# # 调用轮播图
# print("轮播图：{}".format(ApiFactory.get_home_api().banner_api().json()))
#
# # 调用主题
# print("主题:{}".format(ApiFactory.get_home_api().theme_api().json()))
#
# # 调用最近新品
# print("最近新品:{}".format(ApiFactory.get_home_api().recent_product_api().json()))

# # 获取商品分类
# print("商品分类:{}".format(ApiFactory.get_product_api().get_product_classify().json()))
#
# # 获取商品分类下商品
# print("商品分类:{}".format(ApiFactory.get_product_api().get_products_goods().json()))
#
# # 获取商品信息
# print("商品分类:{}".format(ApiFactory.get_product_api().get_product_info().json()))

# 获取token
# print("获取的token:{}".format(ApiFactory.get_user_api().get_token_api().json()))

# 验证token
# print("验证获取的token:{}".format(ApiFactory.get_user_api().token_verify_api().json()))
#
# #获取位置信息
# print("验证获取的token:{}".format(ApiFactory.get_user_api().get_adress_info_api().json()))
# 获取订单列表
print("创建订单:{}".format(ApiFactory.get_order_api().get_order_list_api().json()))
# 创建订单
print("创建订单:{}".format(ApiFactory.get_order_api().create_list_api().json()))
# 查看订单
print("创建订单:{}".format(ApiFactory.get_order_api().look_list_api().json()))
