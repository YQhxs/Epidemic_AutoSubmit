以下都使用 GitHub Actions 自动填报,需要创建 secrets： DAILYCHECK_USERNAME 和 DAILYCHECK_PASSWORD

# 疫情通

1.使用 `python configure.py` 生成 data.json 文件 2.使用 `python submit.py -u [username] -p [password]` 提交；

## Notes：

a.需要获取 geo_api_info:
定位结果（geo*api_info）填写内容格式如下，{"type":"complete","info":"SUCCESS","status":1,"$Da":"jsonp_936429*","position":{"Q":,"R":,"lng":,"lat":},"message":"Get geolocation failed.Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"","adcode":"","businessAreas":[],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"","streetNumber":"","country":"中国","province":"河南省","city":"周口市","district":"","township":""},"formattedAddress":"","roads":[],"crosses":[],"pois":[]}。
b.获取方式：
首先执行 `python configure.py` 时填在国外来跳过，然后执行 `python submit.py -u [username] -p [password] dump_geo` 取得定位结果.

# 晨午检

先使用 configure_3chk.py 设置需要填报的信息
然后使用 submit_3chk.py 提交，定位信息可用上面获取的

注意在对应的时间段进行提交

原作者 Apache553/xidian-ncov-report
