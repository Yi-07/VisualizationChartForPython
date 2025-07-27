"""

演示全国疫情可视化地图开发

"""
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts,TitleOpts

# 读取数据文件
f=open("D:/Metaverse Study/python/可视化案例数据/地图数据/疫情.txt","r",encoding="UTF-8")
data=f.read()

# 关闭文件
f.close()

# 取到各省数据
#将各省的json数据都转成python的字典
data_dict=json.loads(data)
province_data_list=data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并将各个省的数据都封装入列表内
data_list = []  # 绘图需要用的数据列表

for province_data in province_data_list:
    province_name = province_data["name"]  # 省份名称
    province_confirm = province_data["total"]["confirm"]  # 确诊人数

    if province_name == "新疆":
        data_list.append((province_name + "维吾尔自治区", province_confirm))

    elif province_name == "西藏" or province_name == "内蒙古":
        data_list.append((province_name + "自治区", province_confirm))

    elif province_name == "广西":
        data_list.append((province_name + "壮族自治区", province_confirm))

    elif province_name == "宁夏":
        data_list.append((province_name + "回族自治区", province_confirm))

    elif province_name == "北京" or province_name == "重庆":
        data_list.append((province_name + "市", province_confirm))

    elif province_name == "香港" or province_name == "澳门":
        data_list.append((province_name + "特别行政区", province_confirm))

    else:
        data_list.append((province_name + "省", province_confirm))
# print(data_list)

# 创建地图对象
map=Map()

# 添加数据
map.add("各省份确诊人数",data_list,"china")

# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情确诊病例人数分布图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,         # 是否显示
        is_piecewise=True,    # 是否分段
        pieces=[
            {"min":1,"max":99,"label":"1-99","color":"#CCFFFF"},
            {"min":100,"max":999,"label":"100-999","color":"#FFFF99"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999","color":"#CC3333"},
            {"min":100000,"label":">=100000","color":"#990033"},
        ]
    )
)

# 绘图
map.render("中国新冠疫情各省份确诊病例分布图.html")