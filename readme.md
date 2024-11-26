<<<<<<< HEAD
# 

这是一个Python自动化项目。
主要包含以下模块：

1. finder

> 主要是对本地文件进行快速查找

2. emailer

> 邮件自动化

3. pdfer

> 对pdf进行自动化处理

## 功能

- 在指定目录中查找文件
- 支持按文件名、文件类型和文件内容进行查找
- 输出查找结果到指定文件

## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/python-automation.git
   ```
2. 进入项目目录：
   ```bash
   cd python-automation/finder
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

```bash
用法: python 1.py <目录路径> <关键词> [模式] [-o <输出文件路径>]
模式: name (文件名匹配), content (文件内容匹配)。默认模式为 'name'。
示例:
  python finder.py C:\\Downloads\\ dx
  python finder.py C:\\Downloads\\ dx content
  python finder.py C:\\Downloads\\ dx content -o results.txt
  python finder.py -h  
```

## 贡献

欢迎贡献代码！请提交Pull Request或报告问题。

## 许可证

此项目使用MIT许可证。详情请参阅LICENSE文件。
=======
> Python高级程序设计
![LOGO](logo.png)
>>>>>>> 949b840f06e65754ac54ffdc788df4e6053522fc
