# coding:utf-8
import redis


class Config(object):
    '''配置信息'''
    DEBUG = True

    SECRET_KEY = "ASDFGHJKL"

    '''数据库'''
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期，单位秒


class DevelopmentConfig(Config):
    '''开发模式的配置信息'''
    DEBUG = True


class ProducetionConfig(Config):
    '''生产环境配置信息'''
    pass

# manage 工厂模式里面的参数config_name需要和配置信息里面的类有对应关系
config_map = {
    "develop":DevelopmentConfig,
    "product":ProducetionConfig
}