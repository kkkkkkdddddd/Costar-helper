


---



项目名称

本项目基于Python开发，后端使用Django框架，前端使用Vue.js。以下是项目的安装和运行步骤。


环境依赖

在开始之前，请确保已安装以下依赖项：


• Python

• Django(v4.2)

• Django REST Framework(v3.14)

• OpenAI(v1.12.0)

• Django CORS Headers(v4.3)


安装步骤


Step 1:安装依赖库

使用以下命令安装项目所需的Python库：


```bash
pip install -r requirements.txt
```


或者，您可以手动检查并安装依赖项。


Step 2:启动后端服务

运行以下命令启动Django后端服务：


```bash
python manage.py runserver
```


后端服务启动后，您可以通过浏览器访问后端接口。


Step 3:使用前端

前端文件位于`frontend/index`目录中。直接打开`index.html`文件即可使用前端功能。请提前把index.html文件放入frontend文件夹


硅基流动API

本项目支持使用硅基流动API。以下是API的详细信息：


• API Key:`<your_api_key>`(请替换为您的实际API Key)

• API URL:`https://api.siliconflow.cn/v1`

请确保在项目中正确配置API Key和URL，以便正常调用硅基流动API。


注意事项


• 如果在启动后端服务时遇到问题，请检查依赖项是否正确安装。

• 如果无法访问硅基流动API，请检查网络连接或API Key的有效性。


