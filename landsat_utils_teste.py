from landsat import downloader, search

s = search.Search()

ls = s.search(paths_rows="215, 068",
             lat=None,
             lon=None,
             address=None,
             start_date="2015-01-01",
             end_date="2017-11-01",
             cloud_min=None,
             cloud_max=30,
             limit=1,
             geojson=True)

sceneID = ls["features"][0]["properties"]["sceneID"]
d = downloader.Downloader(usgs_user = "",
                          usgs_pass = "",
                          download_dir='~/Downloads/LC8')



d.download([sceneID])


print(ls)
print(s)







