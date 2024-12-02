# B-Panda|自动化工具

---

> @Author:bx33661
>
> @课程：高级程序设计
>
> @Blog：htttp://www.bx33661.com/

项目地址：

- Github：
- Gitee：

<img src="https://gitee.com/bx33661/image/raw/master/path/image-20241201171117454.png" alt="image-20241201171117454" style="zoom: 25%;" />

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
