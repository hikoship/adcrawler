# 一亩三分地论坛录取结果实时整理

Version 0.2 change log
* 可按论坛页数检索
* 改进异常处理
* 舍弃 Bootstrap，手写 CSS

Version 0.1
* 初版

---

### 使用

1. 安装 Python 2、[Tornado Web Server](http://www.tornadoweb.org/en/stable/) 和 [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)。
2. 运行 python adcrawler.py
3. 访问 [localhost:8000](http://localhost:8000) 查看效果
4. 选择自己关注的专业，将对应页面加入书签，下次访问可直接获取筛选后的信息。

或直接[查看演示](http://hgao.net:8000)，并存为书签。

### 目的
[一亩三分地论坛](http://www.1point3acres.com/bbs/)提供了一个让留学用户汇报录取结果的[页面](http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&filter=author&orderby=dateline&sortid=164)，但是不能自动根据专业分类，一些重点内容不够醒目，且对于移动端访问不够友好（Discuz! 在移动端不能看到发帖者的背景信息）

### 原理
抓取[录取汇报](http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&filter=author&orderby=dateline&sortid=164)首页进行分类、重排。

### 功能
按专业查看[录取汇报](http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&filter=author&orderby=dateline&sortid=164)页面，提供移动端访问支持。可能会增加的功能包括：

* 抓取背景定位帖里的三维
* 按录取学校查看
* 查看指定日期区间的录取结果
* 自动生成论坛播报汇总贴

### 其他
所有数据来源于[一亩三分地论坛](http://www.1point3acres.com/bbs/)的[录取汇报](http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&filter=author&orderby=dateline&sortid=164)首页。代码处于实验阶段，不保证可靠。请勿用于商业。
