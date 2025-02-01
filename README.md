# mkdocs-random_walk-plugin

一个用于 mkdocs 文档漫游的插件，类似 Obsidian 自带的笔记漫游功能的简陋实现。

这只是我的一个 toy project：简单地配合 HTML + JS 前端，以及 Python 后端，实现随机跳转笔记的功能。所以我的代码实现比较粗糙，有些地方可能还可以写的更好，但鉴于本人的代码水平，目前就先这样吧...

其中 Python 部分是根据 [@TonyCrane](https://github.com/TonyCrane) 前辈的 [mkdocs-statistics-plugin](https://github.com/TonyCrane/mkdocs-statistics-plugin) 修改而来的，所以代码的一些部分与其十分相似。

可以把这个插件当作获取灵感的途径~~，也可以就把它当个打发闲暇时间的玩具。~~

预览：<https://note.noughtq.top/>（我的笔记首页“笔记漫游”链接）

我的配置（目前暂未更新）：<https://github.com/NoughtQ/notebook/blob/master/mkdocs.yml>


## 安装

可以通过 pypi 直接安装：

```sh
$ pip install mkdocs-random_walk-plugin
```

也可以通过源码安装：

```sh
$ git clone https://github.com/NoughtQ/mkdocs-random_walk-plugin.git
$ cd mkdocs-random_walk-plugin
$ pip install . 
```

## 使用

- 在 mkdocs.yml 中启用插件：

    ```yaml
    plugins:
      - random_walk
    ```

    配置选项及解释（优先级从上到下越来越高）：

    | 选项 | 类型 | 默认值 | 解释 |
    |:----|:----|:----|:----|
    |`include_path`|`list`|`None`|只统计匹配的路径（只包含字符串项的列表），路径相对 docs，为空则不启用）|
    |`exclude_path`|`list`|`None`|不统计匹配的路径（只包含字符串项的列表），路径相对 docs，为空则不启用）|
    |`black_list`|`list`|`None`|黑名单（比 `exclude_path` 更灵活）只包含字符串项的列表），路径相对 docs，为空则不启用）|

- 在被设置笔记漫游功能的 Markdown 文件（页面）上
  - 先在元数据处启用功能：

    ```md
    ---
    random_walk: true
    ---
    ```

  - 再设置 HTML 链接（注意不是 Markdown 链接）

    ```html
    <!-- href: 初始/默认链接 -->
    <!-- id: 指定为 randomLink，不要改成其他值 -->
    <!-- markdown: 设置该属性，便于在 <a> 元素内使用 Markdown 语法 -->
    <a href="#" id="randomLink" markdown="1">  
      笔记漫游
    </a>
    ```
  
  - 在网页点击该链接便可跳转到该页面所在目录下的任一页面，刷新页面后会重新生成随机链接


## 问题

目前在自己电脑上跑没有什么问题，但我不确保在各位的电脑上能够正常运行，所以如果发现 bug 的话请及时在 Issues 里提醒我，十分感谢！
