# coding:utf-8


# 图片验证码的redis有效期, 单位：秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码的redis有效期, 单位：秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码的间隔, 单位：秒
SEND_SMS_CODE_INTERVAL = 60

# 登陆错误尝试次数
LOGIN_ERROR_MAX_TIMES = 5

# 登陆错误限制的时间

LOGIN_ERROR_FORBID_TIME = 600

# 七牛的域名
QINIU_URL_DOMAIN = "http://pqmb92yvl.bkt.clouddn.com/"

# 城区信息的缓存时间, 单位：秒
AREA_INFO_REDIS_CACHE_EXPIRES = 7200

# 房屋列表页面每页数据容量
HOUSE_LIST_PAGE_CAPACITY = 2

# 房屋列表页面页数缓存时间，单位秒
HOUES_LIST_PAGE_REDIS_CACHE_EXPIRES = 7200

# 支付宝的网关地址（支付地址域名）
ALIPAY_URL_PREFIX = "https://openapi.alipaydev.com/gateway.do?"

HOME_PAGE_MAX_HOUSES = 5