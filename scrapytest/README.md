# WebCrawler-study

|目录|路径|说明|
|:---|:---|:---|
| scrapytest |  | 工程名称 |
|  | scrapy.cfg | 项目的配置文件 |
|  | ./ | 该项目的python模块。之后您将在此加入代码 | 
|  | ./items.py | 需要提取的数据结构定义文件 (用于保存所抓取的数据的容器，其存储方式类似于 Python 的字典） | 
|  | ./middlewares.py | 是和Scrapy的请求/响应处理相关联的框架 | 
|  | ./pipelines.py | 用来对items里面提取的数据做进一步处理，如保存等 | 
|  | ./settings.py | 项目的配置文件 |
|  | ./spiders/ | 放置spider代码的目录（用于编写爬虫） |

>#### 制作 Scrapy 爬虫 一共需要4步：
    1. 新建项目 (scrapy startproject xxx)：新建一个新的爬虫项目
    2. 明确目标 （编写items.py）：明确你想要抓取的目标
    3. 制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
    4. 存储内容 （pipelines.py）：设计管道存储爬取内容
>scrapy.cfg ：项目的配置文件
>
>imageNet ：项目的Python模块，将会从这里引用代码
>
>items.py ：项目的目标文件
>
>pipelines.py ：项目的管道文件
>
>settings.py ：项目的设置文件
>
>spiders/：存储爬虫代码目录
>


#### Scrapy的运作流程
     - 代码写好，程序开始运行...

    引擎：Hi！Spider, 你要处理哪一个网站？
   
    Spider：老大要我处理xxxx.com。
    引擎：你把第一个需要处理的URL给我吧。
    
    Spider：给你，第一个URL是xxxxxxx.com。
    
    引擎：调度器，我这有request请求你帮我排序入队一下。

    调度器：好的，正在处理你等一下。
    
    引擎：调度器，把你处理好的request请求给我。

    调度器：给你，这是我处理好的request

    引擎：下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求

    下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个request下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）

    引擎：Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这儿responses默认是交给def parse()这个函数处理的）

    Spider：（处理完毕数据之后对于需要跟进的URL），Hi！引擎，我这里有两个结果，这个是我需要跟进的URL，还有这个是我获取到的Item数据。

    引擎：管道 我这儿有个item你帮我处理一下！调度器！这是需要跟进URL你帮我处理下。然后从第四步开始循环，直到获取完老大需要全部信息。

    管道:调度器：好的，现在就做！

```
..\study\scrapytest\testscrapy> scrapy check # 检查代码
..\scrapytest\testscrapy>scrapy crawl spidertieba -o test.json  -s FEED_EXPORT_ENCODING=UTF-8 # 输出json并制定编码

```    
    


