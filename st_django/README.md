# bysms项目
## 目录结构
* /bysms是项目根目录
  * manage.py是一个工具脚本，用作项目管理，通常会使用它执行管理操作
  * /bysms目录 是python包，manager.py会使用它
    * /setting.py 是Django项目的配置文件，非常重要的配置文件
    * /urls.py 存放了一张白哦，声明了前端发过来的各种http请求，分别有那些函数处理
    * /wsgi.py 
      * web server      -- 负责搞笑的http请求处理环境 -- 接受前端请求后会调用application中的接口
      * web application --      处理业务逻辑        -- 处理完之后返回给web server 并返回给前端
* 我们diango框架是一个web appliaction 框架 
  * 内部也有一个简单的web server协助我们链接前端
> 启动服务：python manage.py runserver localhost:80