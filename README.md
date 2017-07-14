# TOCItemMaker

使用 markdown 编写 TOC 的时候，对每一项的标题进行复制，然后运行脚本，生成可用的链接（针对 GitHub .md 文件），生成后的结果会拷贝到剪切板中

## 使用方法

- 运行环境 Python 3.5.1
- 安装 [pyperclip](https://github.com/asweigart/pyperclip)

    ```sh
    pip install pyperclip
    ```

- 复制需要转化为链接的 Title, 如：`创建.eslintrc.js`
- 进入到脚本文件夹，运行脚本 `python maker.py`
- 结果将会自动输出到剪切板，如：`创建eslintrcjs`

## 已发现的规则

- 不能含有的字符，需要使用空字符替换
    - `.`
    - `/`
    - `(`
    - `)`
    - `，`
    - `>`
    - `<`
- 需要使用 `-` 代替
    - ` ` (空格)


