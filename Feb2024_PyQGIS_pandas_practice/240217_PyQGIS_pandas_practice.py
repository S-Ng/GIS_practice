### Import airport shp file
systemFilePath = 'C:/Users/ngsim/Documents_SN/GIS/240205_airport_python_basic/'   # file path to relevant folder
if not QgsProject.instance().mapLayersByName('ne_10m_airports'):  # if airport layer hasn't already been created
    layer = iface.addVectorLayer(systemFilePath + 'ne_10m_airports.shp', '', 'ogr')   # then add airport .shp file
else:
    print ("Airport shp file already loaded")
layer = QgsProject.instance().mapLayersByName("ne_10m_airports")[0]  # select airport layer. epsg:4326
layer.renderer().symbol().setColor(QColor.fromRgb(255,127,80))  # change the color of airports

### Output airport name, iata code, and lat/long as txt file (executed following online tutorial)
#layer = iface.activeLayer()   # select active layer
txtFilePath = systemFilePath + '240217_airportLatLong.txt'   # text file name
txtfile = open(txtFilePath, 'w')   # open txt file path to write
txtfile.write('Name,Iata Code,Latitude,Longitude\n')   # add header
for i in layer.getFeatures():   # for all airports
    geomPt = i.geometry().asPoint()   # get lat and long
    line = '%s, %s, %0.4f, %0.4f\n' % (i['name'], i['iata_code'], geomPt.y(), geomPt.x())   # construct line with airport data
    txtfile.write(line)    # add line to txt file
txtfile.close()   # we're done adding to this txt file now

### Let's highlight all the airports in the tropics using pandas, just for fun
import pandas as pd
df = pd.read_csv(txtFilePath)  # import txt file as pandas dataframe
#print(df)

# Export low lat airports to CSV
lowLat = df.loc[:,'Latitude'].between(-10,10)  # select only airports within 10 degrees of the equator
csvFilePath = systemFilePath + '240217_lowLat.csv'   # csv file path
df[lowLat].to_csv(csvFilePath,index=False)  # export CSV to later upload as a new layer

# Upload low lat airport CSV into QGIS layer
uri = ("file:///" + csvFilePath + 
        "?encoding=%s&delimiter=%s&xField=%s&yField=%s&crs=%s"
        % ("UTF-8",",", "Longitude", "Latitude","epsg:4326"))   # uri path & parameters
lowLatLayerName = "240217_lowLatLayer"
lowLatLayer = QgsVectorLayer(uri, lowLatLayerName, "delimitedtext")   # import CSV as layer

if not lowLatLayer.isValid():  # print alert if layer didn't load correctly
    print ("Layer not loaded")
    
if not QgsProject.instance().mapLayersByName(lowLatLayerName):  # if low lat layer hasn't already been created
    QgsProject.instance().addMapLayer(lowLatLayer)  # then add layer to map
else:
    print ("lowLatLayer already created")
    
# Change color of low lat airport points
layer = QgsProject.instance().mapLayersByName(lowLatLayerName)[0]  # select new low lat layer
layer.renderer().symbol().setColor(QColor.fromRgb(0,128,0))  # change the color of the lowLatLayer - must refresh map

