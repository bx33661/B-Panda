<meta name="referrer" content="no-referrer">

# B-Panda|自动化工具

---

> @Author: bx33661
>
> @课程：高级程序设计(python)
>
> @Blog：htttp://www.bx33661.com/

项目地址：

- 文档站：http://doc.bx33661.com/

- Github：https://github.com/bx33661/B-Panda
- Gitee：https://gitee.com/bx33661/B-Panda
- Docker Hub: https://hub.docker.com/r/bx33661/btools

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241201171117454.png" alt="image-20241201171117454" style="zoom: 25%;" />

## 基本介绍

本项目基于Python开发，主要包括`B-Panda|自动化工具箱`和`B-Panda|网站监控系统`。提供多种部署方式，支持传统安装和Docker容器化部署。

![image-20241206143321845](https://gitee.com/bx33661/image/raw/master/path/image-20241206143321845.png)

### 功能特点

- PDF文件处理：合并、拆分、压缩等操作
- 邮件自动化：批量发送、模板管理
- 文件查找：快速定位文件
- Base64编解码：在线转换工具
- 系统监控：实时监控系统状态
- 网络工具：IP查询、端口扫描、Ping测试等
- 网站监控：多站点状态监控

### 技术栈

- 后端：Python、Flask
- 前端：Bootstrap、Chart.js
- 容器化：Docker
- 监控：自研监控系统

## 部署指南

### 方式一：Docker 部署（推荐）

最简单的部署方式是使用 Docker：

```bash
# 拉取镜像
docker pull bx33661/btools:latest

# 运行容器
docker run -d -p 5000:5000 --name btools-web bx33661/btools:latest
```

使用 docker-compose 部署：

```bash
# 1. 创建 docker-compose.yml
version: '3.8'

services:
  web:
    image: bx33661/btools:latest
    container_name: btools-web
    restart: always
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    volumes:
      - ./logs:/app/logs

# 2. 启动服务
docker-compose up -d
```

### 方式二：传统部署

1. 克隆仓库并安装依赖：

```bash
# 克隆项目
git clone https://github.com/bx33661/B-Panda.git
cd BTools

# 安装依赖
pip install -r requirements.txt
```

2. 运行应用：

```bash
cd web/app
python app.py
```

### 方式三：自行构建 Docker 镜像

```bash
# 克隆项目
git clone https://github.com/bx33661/B-Panda.git
cd web/app

# 构建镜像
docker build -t btools:latest .

# 运行容器
docker run -d -p 5000:5000 --name btools-web btools:latest
```

## 使用说明

访问 http://localhost:5000 即可使用所有功能。

### B-Panda|自动化工具箱

网站截图（部分）：

![](https://gitee.com/bx33661/image/raw/master/path/image-20241206143321845.png)

![image-20241206143407405](https://gitee.com/bx33661/image/raw/master/path/image-20241206143407405.png)

具体工具界面：

- 系统资源监控：

![image-20241206143856572](https://gitee.com/bx33661/image/raw/master/path/image-20241206143856572.png)

- 网络工具页面

![网络工具页面](https://gitee.com/bx33661/image/raw/master/path/%E7%BD%91%E7%BB%9C%E5%B7%A5%E5%85%B7%E9%A1%B5%E9%9D%A2.png)

- Base64编解码

![Bs64页面](https://gitee.com/bx33661/image/raw/master/path/Bs64%E9%A1%B5%E9%9D%A2.png)

- Pdfer

![pdf](https://gitee.com/bx33661/image/raw/master/path/pdf.png)

网站监控系统

...

## 注意事项

1. Docker 部署时请确保端口 5000 未被占用
2. 生产环境建议使用 nginx 等反向代理
3. 需要持久化数据时，请正确配置 volumes
4. 建议定期备份重要数据

## 项目结构

```
BTools/
├── README.md                 # 项目说明文档
├── requirements.txt          # 全局依赖
└── web/                     # Web应用目录
    └── app/                 # Flask应用
        ├── app.py           # 应用入口
        ├── Dockerfile       # Docker配置文件
        ├── docker-compose.yml  # Docker Compose配置
        ├── requirements.txt    # 应用依赖
        ├── static/          # 静态文件目录
        │   ├── css/         # CSS样式文件
        │   ├── js/          # JavaScript文件
        │   └── images/      # 图片资源
        ├── templates/       # 模板文件目录
        │   ├── base.html    # 基础模板
        │   ├── index.html   # 首页模板
        │   ├── pdf.html     # PDF工具页面
        │   ├── email.html   # 邮件工具页面
        │   ├── find.html    # 文件查找页面
        │   ├── bs.html      # Base64工具页面
        │   ├── network.html # 网络工具页面
        │   └── monitor.html # 系统监控页面
        ├── routes/          # 路由模块
        │   ├── __init__.py
        │   ├── pdf_routes.py    # PDF相关路由
        │   ├── email_routes.py  # 邮件相关路由
        │   ├── find_routes.py   # 文件查找路由
        │   ├── bs_routes.py     # Base64相关路由
        │   ├── network_routes.py # 网络工具路由
        │   └── system_monitor_routes.py # 系统监控路由
        └── utils/           # 工具模块
            ├── __init__.py
            ├── pdf_utils.py     # PDF处理工具
            ├── email_utils.py   # 邮件处理工具
            ├── find_utils.py    # 文件查找工具
            ├── bs_utils.py      # Base64处理工具
            └── monitor_utils.py # 监控工具
```

### 主要目录说明：

- `/web/app/`: Flask应用主目录
  - `app.py`: 应用入口文件
  - `routes/`: 路由模块，处理不同功能的路由
  - `utils/`: 工具模块，包含各种功能的具体实现
  - `templates/`: HTML模板文件
  - `static/`: 静态资源文件

### 关键文件说明：

- `Dockerfile`: Docker镜像构建配置
- `docker-compose.yml`: Docker容器编排配置
- `requirements.txt`: Python依赖包列表
- `base.html`: 基础模板，定义了页面的基本结构
- `app.py`: 应用主文件，包含Flask应用初始化和配置

## 更新日志

### v1.0.0 (2024-03-xx)

- 初始版本发布
- 支持 Docker 部署
- 完整的工具箱功能
- 网站监控系统

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 联系作者

- 博客：http://www.bx33661.com/
- Github：https://github.com/bx33661
