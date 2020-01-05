# Python项目：

撰写人|谢文慧
---|:--:
工作内容|实现前后端交互
---|:--:
合作搭档|梁嘉颖
---|:--:
研究项目|中国各省财政教育支出与特殊教育发展情况
---|:--:
时间|2019.12-2020.1

## pythonanyweher URL:
[数据可视化](http://wenpur.pythonanywhere.com/)

## 数据传递描述
Web APP动作描述
1. 总共有6个路由，"/index","/local_expense","/detail","/data","/scatter","/effectScatter" 
2."/"根路由重定向给"/index"，因为在HTML有option的标签，option的value属性无法直接实现"/"根路由的跳转
3. 不同的网页能够实现跳转，主要是每个HTML的页面有select标签，在select标签下，其属性option都有value，value的值可以说路由也可以说.html，
所以能够实现一个页面可以任意跳转到不同的网页
4.“/index”跳转可以看到首页，也就是项目的介绍；“/local_expense”跳转可以看“地方财政教育支出”；“/detail”看“视图详情”；“/scatter”看“四个不同省份的
对比”；“/effectScatter”看“四川特殊教育基本情况”；“data”就是数据

