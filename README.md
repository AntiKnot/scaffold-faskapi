# scaffold fastapi
脚手架系列用于快速启动项目的基础项目，fork之后可以放遍二次开发。用于学习练习新特。

# what FastAPI
Starlette ~~ Flask
FastApi = Starlette + Pydantic + JsonSchema + OpenAPI + Typing!
APIFlask = Flask + Marshmallow

# quick start
install requirement & start server
```shell script
make init
make run
```
api docs
http://127.0.0.1:8000/docs

Alternative API docs
http://127.0.0.1:8000/redoc

# ps
- fastAPI 能正常工作对代码的类型函数参数使用强依赖
- fastAPI 的开发基本是围绕这合理的API设计和文档展开的
- 基本构成
    Query # ?
    Path # url
    BaseModel # json object
    Field # model field meta info
    Body # response meta info
    Config # json object meta info
    Cookie
    Header
    Form # OAuth
    File

# Refs
- https://github.com/tiangolo/full-stack-fastapi-postgresql
- https://github.com/wxy2077/MallAP
