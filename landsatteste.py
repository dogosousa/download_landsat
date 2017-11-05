from landsat import landsat, downloader
import geopandas as gpd


l = landsat.Search()

s = l.search(paths_rows="215, 068",
             lat=None,
             lon=None,
             address=None,
             start_date="2015-01-01",
             end_date="2015-12-31",
             cloud_min=None,
             cloud_max=16,
             limit=1,
             geojson=True)

df = gpd.GeoDataFrame.from_features(s)

lc = [x for x in df['sceneID']]

d = downloader.Downloader(download_dir='~/Download/LC8',
                          usgs_user='', usgs_pass='')
print(s)
d.download(lc)