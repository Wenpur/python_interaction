from flask import Flask, render_template
from jinja2 import Markup
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Tab, Line, Map, Timeline, Scatter, EffectScatter

app = Flask(__name__, static_folder="templates")

df1 = pd.read_csv('Financial_education.csv') #地方财政教育支出(亿元)
df2 = pd.read_csv('Schools.csv')             #特殊教育学校数(所)
df3 = pd.read_csv('Teachers.csv')            #特殊教育专任教师数(万人)
df4 = pd.read_csv('Recruit_students.csv')    #特殊教育招生数(万人)
df5 = pd.read_csv('Students_in_school.csv')  #各省特殊教育在校学生数(万人)
df6 = pd.read_csv('All.csv')    #全国特殊教育在校学生生数(人)
df7 = pd.read_csv('data.csv')


"""函数中所需要运用的定义代码"""

A =list(df6.loc[0].values)#全国特殊教育在校学生生数(人)
A.pop(0)
A

y =list(df6.loc[1].values)#年度全国财政教育支出
y.pop(0)
y

year = df1.columns.values  #  有效年份
x = year.tolist()
x.pop(0)
x

"""编写地图、散点图等交互图片函数"""
def all() -> Bar:
    bar = (
        Bar()
            .add_xaxis(x[::-1])  #设置横坐标数据，设为年份
            .add_yaxis("全国特殊教育在校学生人数", A[::-1], color='#33CCFF')  # 设置纵坐标数据，添加数据，设置条形颜色
            .extend_axis(
            yaxis=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}万人"),
            )
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(title='图1-1', subtitle="财政教育支出与特殊教育在校学生",   # 设置标题与副标题样式，进行图例说明
                                      subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16)),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],   #添加拖动元件
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value}亿元")
            ),
        )
    )
    line = (
        Line()  #添加折线图
            .add_xaxis(x)
            .add_yaxis("年度全国财政教育支出", y, yaxis_index=1)
    )
    bar.overlap(line)
    return bar     #返回数据
all().render_notebook()

def finacial_education_map() -> Timeline:
    kd = Timeline()   #添加时间轴
    for i in range(2009, 2019):           #选取时间段为2009-2018年,由于range(start, stop[, step])，所以是（2009,2019)
        map1 = (
            Map()
                .add(
                "地方财政教育支出(亿元)", list(zip(list(df1.provinces), list(df1["{}".format(i)]))), "china",  #选取中国地图
                is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title='图1', subtitle="{}各省财政教育支出".format(i),
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=18, )),
                # 设置标题与副标题样式，进行图例说明
                visualmap_opts=opts.VisualMapOpts(min_=df1["2009"].min(), max_=df1["2018"].max(), series_index=0),
                                #设置最大最小值
            )
        )
        kd.add(map1, "{}".format(i))
    return kd  #返回数据
finacial_education_map().render_notebook()

def schools_map() -> Timeline:
    kd = Timeline()  #添加时间轴
    for i in range(2009, 2019):     #选取时间段为2009-2018年,由于range(start, stop[, step])，所以是（2009,2019)
        map1 = (
            Map()
                .add(
                "特殊教育学校数(所)", list(zip(list(df2.provinces), list(df2["{}".format(i)]))), "china",   #选取中国地图
                is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="图1-2", subtitle="{}特殊教育学校数".format(i),
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16, )),
                # 设置标题与副标题样式，进行图例说明
                visualmap_opts=opts.VisualMapOpts(min_=1, max_=162),
                # 设置最大最小值
            )
        )
        kd.add(map1, "{}".format(i))
    return kd  #返回数据
schools_map().render_notebook()

def recruit_students_map() -> Timeline:
    kd = Timeline()  #添加时间轴
    for i in range(2009, 2019):    #选取时间段为2009-2018年,由于range(start, stop[, step])，所以是（2009,2019)
        map1 = (
            Map()
                .add(
                "特殊教育招生数(万人)", list(zip(list(df4.provinces), list(df4["{}".format(i)]))), "china",   #选取中国地图
                is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="图1-3", subtitle="{}特殊教育招生数".format(i),
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16, )),
                # 设置标题与副标题样式，进行图例说明
                visualmap_opts=opts.VisualMapOpts(min_=0.00, max_=1.03),
                # 设置最大最小值
            )
        )
        kd.add(map1, "{}".format(i))
    return kd  #返回数据


recruit_students_map().render_notebook()

def teachers_map() -> Timeline:
    kd = Timeline()   #添加时间轴
    for i in range(2009, 2019):    #选取时间段为2009-2018年,由于range(start, stop[, step])，所以是（2009,2019)
        map1 = (
            Map()
                .add(
                "特殊教育专任教师数(万人)", list(zip(list(df3.provinces), list(df3["{}".format(i)]))), "china",   #选取中国地图
                is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title='图1-4', subtitle="{}特殊教育专任教师数(万人)".format(i),
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=16, )),
                # 设置标题与副标题样式，进行图例说明
                visualmap_opts=opts.VisualMapOpts(min_=0.00, max_=0.60),
                # 设置最大最小值
            )
        )
        kd.add(map1, "{}".format(i))
    return kd   #返回数据


teachers_map().render_notebook()

def four_compare() -> Scatter:
    c = (
        Scatter()
            .add_xaxis(x[::1])  #设置横坐标数据，设为年份
            .add_yaxis("四川特殊教育招生数(万人)", [1.03, 1.04, 0.96, 0.81, 0.80, 0.82, 0.84, 0.68, 0.67, 0.65], color="#1E90FF")
            .add_yaxis("四川特殊教育专任教师数(万人)", [0.30, 0.28, 0.25, 0.24, 0.22, 0.21, 0.19, 0.18, 0.17, 0.16], color="#1E90FF")
            .add_yaxis("广东特殊教育招生数(万人)", [0.91, 0.89, 0.69, 0.73, 0.53, 0.39, 0.46, 0.36, 0.37, 0.360], color="#FF8247")
            .add_yaxis("广东特殊教育专任教师数(万人)", [0.48, 0.45, 0.41, 0.36, 0.30, 0.27, 0.25, 0.22, 0.20, 0.19], color="#FF8247")
            .add_yaxis("河南特殊教育招生数(万人)", [0.99, 0.65, 0.51, 0.39, 0.36, 0.33, 0.3, 0.32, 0.32, 0.31], color="#AB82FF")
            .add_yaxis("河南特殊教育专任教师数(万人)", [0.40, 0.38, 0.36, 0.35, 0.35, 0.33, 0.32, 0.3, 0.29, 0.29], color="#AB82FF")
            .add_yaxis("山东特殊教育招生数(万人)", [0.54, 0.44, 0.4, 0.36, 0.33, 0.36, 0.34, 0.36, 0.28, 0.54], color="#EE0000")
            .add_yaxis("山东特殊教育专任教师数(万人)", [0.52, 0.5, 0.49, 0.48, 0.47, 0.46, 0.46, 0.45, 0.44], color="#EE0000")
        # 设置纵坐标数据，分别添加4个省份的数据
            .set_global_opts(
            title_opts=opts.TitleOpts(title='图1-5', subtitle='四个不同省份对比',   # 设置标题与副标题样式，进行图例说明
                                      subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=10)),
            visualmap_opts=opts.VisualMapOpts(type_="size", max_=1.50, min_=0.0),
        ) # 设置最大最小值
    )
    return c   #返回数据


four_compare().render_notebook()


def effectscatter_symbol() -> EffectScatter:
    c = (
        EffectScatter()
            .add_xaxis(x[::1])   #设置横坐标数据，设为年份
            .add_yaxis("四川特殊教育招生数(万人)", [1.03, 1.04, 0.96, 0.81, 0.80, 0.82, 0.84, 0.68, 0.67, 0.65], color="#1E90FF",
                       symbol_size=16, symbol="arrow")
            .add_yaxis("四川特殊教育专任教师数(万人)", [0.30, 0.28, 0.25, 0.24, 0.22, 0.21, 0.19, 0.18, 0.17, 0.16], color="#AB82FF",
                       symbol_size=16, symbol="arrow")
            .add_yaxis("四川特殊教育在校学生数(万人)", [5.69, 5.35, 4.78, 4.33, 4.23, 4.37, 4.43, 4.09, 4.18, 4.18], color="#EE2222",
                       symbol_size=16, symbol="arrow")   # 设置纵坐标数据
            .set_global_opts(
            title_opts=opts.TitleOpts(title='图1-6', subtitle="四川特殊教育基本情况",   # 设置标题与副标题样式，进行图例说明
                                      subtitle_textstyle_opts=opts.TextStyleOpts(color="black", font_size=15)),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        )
    )
    return c  #返回数据


effectscatter_symbol().render_notebook()


tab = Tab() #添加tab
tab.add(teachers_map(), "特殊教育专任教师数")
tab.add(schools_map(), "各省特殊教育学校数")
tab.add(recruit_students_map(), "各省特殊教育招生数")
tab.add(all(),"教育支出与特殊教育在校学生详情")
tab.add(finacial_education_map(),"地方财政教育支出")
tab.add(four_compare(),"四个不同省份对比")
tab.add(effectscatter_symbol(),"四川特殊教育基本情况")
tab.render_notebook()

@app.route('/',endpoint='r1',redirect_to='/index')
def root():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/local_expense')
def local_expense() :
    c = tab = Tab()
    tab.add(finacial_education_map(), "地方财政教育支出")

    result= Markup(c.render_embed())
    conculsion = "小结：从图1，我们可以看出，这10年间全国各地的财政教育支出都是随年增长的，从地图可以看出广东、四川、山东、河南是全国各省中颜色从浅变深变化最明显的4个城，" \
                 "他们的财政教育支出增加的速度很快。"
    return render_template('select.html',
                           result=result,
                           conculsion=conculsion)

@app.route("/detail")
def detail():
    c = tab = Tab()
    tab.add(schools_map(), "各省特殊教育学校数")
    tab.add(teachers_map(), "特殊教育专任教师数")
    tab.add(recruit_students_map(), "各省特殊教育招生数")
    tab.add(all(),"教育支出与特殊教育在校学生详情")

    result = Markup(c.render_embed())
    return render_template('select.html',
                           result=result)


@app.route("/data")
def data():
    return  render_template('data.html')

@app.route("/scatter")
def scatter():
    c = tab = Tab()
    tab.add(four_compare(), "四个不同省份对比")
    result = Markup(c.render_embed())
    return  render_template('scatter.html',
                            result=result,)

@app.route("/effectScatter")
def effectScatter():
    c = tab = Tab()
    tab.add(effectscatter_symbol(),"四川特殊教育基本情况")
    result = Markup(c.render_embed())
    return  render_template('effectScatter.html',
                            result=result,)
if __name__ == "__main__":
    app.run(port=5050)




