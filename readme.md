# B-Panda|自动化工具

---

> @Author:bx33661
>
> @课程：高级程序设计
>
> @Blog：htttp://www.bx33661.com/

项目地址：

- Github：https://github.com/bx33661/B-Panda
- Gitee：https://gitee.com/bx33661/B-Panda

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241201171117454.png" alt="image-20241201171117454" style="zoom: 25%;" />

**具体文档：**

**http://doc.bx33661.com/**

## 基本介绍

本项目基于Python开发，主要包括`B-Panda|自动化工具箱`和`B-Panda|网站监控系统`

- B-Panda|自动化工具箱

> 目前有web端和本地脚本模块，两种使用形式

目前只有三个功能：

- PDFer

这个主要是对PDF文件进行文本提取，水印添加，拆分，加密等操作

- Emailer

这个主要是对邮件进行定时发送和特定对应自动回复（目前只支持qq邮箱）

- Finder

这个主要是对本地文件和特定文件内容进行查找（灵感来源于：everything）

![image-20241201171321478](https://gitee.com/bx33661/image/raw/master/path/image-20241201171321478.png)



- B-Panda|网站监控系统

> 由于我最近运营着几个个人网站，需要对网站运行情况进行监控，
>
> 灵感来源于[**Uptime Kuma**](http://43.134.9.57:3001/dashboard)
>
> 一个优美的监控系统

主要是对网站状态进行定时监控，记录

技术栈：

Python、Flask，chart.js

![image-20241201165753647](https://gitee.com/bx33661/image/raw/master/path/image-20241201165753647.png)



## 使用说明

### B-Panda|自动化工具箱

- Finder

【web界面】

![image-20241202103915489](https://gitee.com/bx33661/image/raw/master/path/image-20241202103915489.png)

【脚本界面】

![image-20241201172344826](https://gitee.com/bx33661/image/raw/master/path/image-20241201172344826.png)

- Pdfer

【web界面】

![image-20241202081204667](https://gitee.com/bx33661/image/raw/master/path/image-20241202081204667.png)

【脚本界面】

![image-20241201172431125](https://gitee.com/bx33661/image/raw/master/path/image-20241201172431125.png)

- Emailer

【web界面】

![image-20241202081320031](https://gitee.com/bx33661/image/raw/master/path/image-20241202081320031.png)

【脚本界面】

![image-20241201172539974](https://gitee.com/bx33661/image/raw/master/path/image-20241201172539974.png)

1. 克隆仓库，安装所需要包

```bash
git clone https://github.com/bx33661/B-Panda.git
cd BTools
#安装包
pip install -r requirements.txt
```

2. 运行web控制台

```bash
cd web
cd app
python app.py
```

![image-20241202081029481](https://gitee.com/bx33661/image/raw/master/path/image-20241202081029481.png)



### **B-Panda - 实时网站监控工具**

B-Panda 是一个强大且简易使用的在线工具，旨在帮助用户实时监控其网站的状态和性能。通过这个平台，您可以轻松地查看网站的响应时间、状态码以及其他关键的性能指标，从而确保网站运行稳定，提供最佳的用户体验。

![image-20241201165753647](https://gitee.com/bx33661/image/raw/master/path/image-20241201165753647.png)

#### **主要功能**：

- **实时监控**：定时检查您网站的状态，包括返回的状态码（如200成功、404未找到、500服务器错误等）和响应时间。
- **多站点支持**：您可以同时监控多个网站，并查看每个网站的详细历史数据。
- **直观的图表展示**：所有监控数据都通过易于理解的图表呈现，您可以快速判断网站的健康状况。
- **快速反馈**：一旦添加新的监控网站，系统会在每次监控后及时反馈结果，帮助您快速发现潜在的问题。

#### **适用场景**：

- **开发者与运维人员**：确保开发和运营中的网站处于正常运行状态。
- **网站管理员**：快速检测网站性能瓶颈，进行性能优化。时刻了解网站的健康状况，减少潜在的业务中断风险。

#### **如何使用**：

```python
git clone https://github.com/bx33661/B-Panda.git
cd app
```

运行文件

```python 
python app.py
```

![image-20241202102055652](https://gitee.com/bx33661/image/raw/master/path/image-20241202102055652.png)



