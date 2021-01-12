以下都使用 GitHub Actions 自动填报，分别是每天的 8:03,13:03,19:03 时间（实际再+85min）。仓库需创建 secrets： DAILYCHECK_USERNAME 和 DAILYCHECK_PASSWORD
晨午检和疫情通都在 submit.py 里如果想分开提交参照原作者

# 疫情通

1.使用 `python configure.py` 生成 data.json 和 data_3chk.json 文件 2.使用 `python submit.py -u [username] -p [password]` 提交；

## Notes：

a.需要获取 geo_api_info:
定位结果（geo_api_info）填写内容格式如下，
{
"type": "complete",
"info": "SUCCESS",
"status": 1,
"position": { "Q": "", "R": "", "lng": "", "lat": "" },
"message": "Get geolocation failed.Get ipLocation success.Get address success.",
"location_type": "ip",
"accuracy": null,
"isConverted": true,
"addressComponent": {
"citycode": "",
"adcode": "",
"businessAreas": [],
"neighborhoodType": "",
"neighborhood": "",
"building": "",
"buildingType": "",
"street": "",
"streetNumber": "",
"country": "中国",
"province": "河南省",
"city": "周口市",
"district": "",
"township": ""
},
"formattedAddress": "",
"roads": [],
"crosses": [],
"pois": []
}

b.获取方式：
首先执行 `python configure.py` 时填在国外来跳过，然后执行 `python submit.py -u [username] -p [password] dump_geo` 取得定位结果.

# 晨午检

先使用 configure_3chk.py 设置需要填报的信息，定位信息可用上面获取的 geo_api_info，生成 data_3chk.json 文件

原作者 Apache553/xidian-ncov-report
