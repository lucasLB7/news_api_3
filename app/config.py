class Config:
    BASE_URL = "https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey={}"


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
