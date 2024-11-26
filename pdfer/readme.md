### PDF自动化工具说明文档

#### 1. 概述

PDF自动化工具是一个命令行工具，可以帮助你执行常见的PDF操作，如合并PDF文件、添加水印、提取文本、拆分PDF文件、加密PDF文件、旋转PDF页面、裁剪PDF页面、压缩PDF文件以及提取特定页面。

#### 2. 安装

在使用PDF自动化工具之前，你需要确保安装了以下依赖项：

- **Python 3.6 或更高版本**
- **PyPDF2 库**

你可以使用以下命令来安装 `PyPDF2` 库：

```bash
pip install PyPDF2
```

#### 3. 使用方法

PDF自动化工具通过命令行参数来执行不同的操作。以下是基本的使用方法：

```bash
python pdfer1.py -a <操作类型> -i <输入文件或文件夹路径> -o <输出文件路径> [-w <水印文本>] [-p <密码>] [-d <旋转角度>] [-b <裁剪边界>] [-r <页面范围>]
```

#### 4. 操作类型

以下是支持的操作类型及其详细说明：

##### 4.1 合并PDF文件 (`merge`)

将多个PDF文件合并成一个PDF文件。

**参数**:

- `-a merge`
- `-i <输入文件或文件夹路径>`: 输入文件夹路径，文件夹中应包含要合并的PDF文件。
- `-o <输出文件路径>`: 输出合并后的PDF文件路径。

**示例**:

```bash
python pdfer1.py -a merge -i ./input_folder -o ./output/merged.pdf
```

##### 4.2 添加水印 (`add_watermark`)

在PDF文件的每一页添加水印文本。

**参数**:

- `-a add_watermark`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出添加水印后的PDF文件路径。
- `-w <水印文本>`: 水印文本内容。

**示例**:

```bash
python pdfer1.py -a add_watermark -i ./input.pdf -o ./output/watermarked.pdf -w "Confidential"
```

##### 4.3 提取文本 (`extract_text`)

从PDF文件中提取文本内容。

**参数**:

- `-a extract_text`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出提取的文本文件路径。

**示例**:

```bash
python pdfer1.py -a extract_text -i ./input.pdf -o ./output/extracted_text.txt
```

##### 4.4 拆分PDF文件 (`split`)

将一个PDF文件拆分成多个PDF文件，每个文件包含一页。

**

个PDF文件拆分成多个PDF文件，每个文件包含一页。

**参数**:

- `-a split`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出文件夹路径，拆分后的PDF文件将保存在此文件夹中。

**示例**:

```bash
python pdfer1.py -a split -i ./input.pdf -o ./output/split_folder
```

##### 4.5 加密PDF文件 (`encrypt`)

对PDF文件进行加密，设置访问密码。

**参数**:

- `-a encrypt`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出加密后的PDF文件路径。
- `-p <密码>`: 加密密码。

**示例**:

```bash
python pdfer1.py -a encrypt -i ./input.pdf -o ./output/encrypted.pdf -p your_password
```

##### 4.6 旋转PDF页面 (`rotate`)

旋转PDF文件中的每一页或特定页面。

**参数**:

- `-a rotate`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出旋转后的PDF文件路径。
- `-d <旋转角度>`: 旋转角度（90, 180, 270）。

**示例**:

```bash
python pdfer1.py -a rotate -i ./input.pdf -o ./output/rotated.pdf -d 90
```

##### 4.7 裁剪PDF页面 (`crop`)

裁剪PDF文件中的每一页或特定页面。

**参数**:

- `-a crop`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出裁剪后的PDF文件路径。
- `-b <边界>`: 裁剪边界（格式：`left,top,right,bottom`）。

**示例**:

```bash
python pdfer1.py -a crop -i ./input.pdf -o ./output/cropped.pdf -b 50,50,50,50
```

##### 4.8 压缩PDF文件 (`compress`)

压缩PDF文件以减小文件大小。

**参数**:

- `-a compress`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出压缩后的PDF文件路径。

**示例**:

```bash
python pdfer1.py -a compress -i ./input.pdf -o ./output/compressed.pdf
```

##### 4.9 提取特定页面 (`extract_pages`)

从PDF文件中提取特定页面。

**参数**:

- `-a extract_pages`
- `-i <输入文件或文件夹路径>`: 输入PDF文件路径。
- `-o <输出文件路径>`: 输出提取页面后的PDF文件路径。
- `-r <页面范围>`: 页面范围（格式：`start-end` 或 `page_number`）。

**示例**:

```bash
python pdfer1.py -a extract_pages -i ./input.pdf -o ./output/extracted_pages.pdf -r 1-3
```

#### 5. 示例命令

以下是一些示例命令，展示了如何使用PDF自动化工具执行不同的操作：

##### 5.1 合并PDF文件

```bash
python pdfer1.py -a merge -i ./input_folder -o ./output/merged.pdf
```

##### 5.2 添加水印

```bash
python pdfer1.py -a add_watermark -i ./input.pdf -o ./output/watermarked.pdf -w "Confidential"
```

##### 5.3 提取文本

```bash
python pdfer1.py -a extract_text -i ./input.pdf -o ./output/extracted_text.txt
```

##### 5.4 拆分PDF文件

```bash
python pdfer1.py -a split -i ./input.pdf -o ./output/split_folder
```

##### 5.5 加密PDF文件

```bash
python pdfer1.py -a encrypt -i ./input.pdf -o ./output/encrypted.pdf -p your_password
```

##### 5.6 旋转PDF页面

```bash
python pdfer1.py -a rotate -i ./input.pdf -o ./output/rotated.pdf -d 90
```

##### 5.7 裁剪PDF页面

```bash
python pdfer1.py -a crop -i ./input.pdf -o ./output/cropped.pdf -b 50,50,50,50
```

##### 5.8 压缩PDF文件

```bash
python pdfer1.py -a compress -i ./input.pdf -o ./output/compressed.pdf
```

##### 5.9 提取特定页面

```bash
python pdfer1.py -a extract_pages -i ./input.pdf -o ./output/extracted_pages.pdf -r 1-3
```

#### 6. 常见问题

- **Q: 如何解决合并PDF文件时的顺序问题？**

  - A: 确保输入文件夹中的PDF文件按正确的顺序命名，例如 `01.pdf`, `02.pdf`, `03.pdf` 等。
- **Q: 如何处理加密PDF文件时的密码强度？**

  - A: 选择一个足够复杂的密码，包含字母、数字和特殊字符，以确保PDF文件的安全性。
- **Q: 如何处理提取文本时的格式问题？**

  - A: 提取的文本可能不包含原始PDF文件中的格式信息，如字体、颜色和布局。如果需要保留格式，可以考虑使用其他工具或库。

#### 7. 联系信息

如果你有任何问题或建议，请联系开发者：

- **邮箱**: support@bx33661.com
- **网站**: https://www.bx33661.com/

希望这份说明文档能帮助你更好地使用PDF自动化工具！如果有任何问题，请随时联系支持团队。
