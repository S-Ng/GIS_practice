Just-for-fun project to 3D-print a model of Engadin skimarathon in Switzerland as a gift for a friend. Aiming to use new GIS coding skills to use publically available elevation data. The project has 5 steps: <br>

  1. Select area of interest from an open source Swiss elevation dataset (https://www.swisstopo.admin.ch/en/height-model-swissalti3d). I used "selection by polygon" at 2.0m resolution to obtain a csv file with links to tiles covering the entire Engadin Ski Marathon and surrounding mountains.<br>
  2. Merge linked GeoTiff tiles in exported csv file into one file. This is accomplished using the scripts from 241217 or 250210. <br>
  3. Add geospatial features in QGIS, ArcGIS, etc such as trails, cities, etc. Note that additional features need to be represented as elevation data merged with the exported GeoTiff so they will be part of the eventual 3D print! Also a good time to resample the pixel resolution. 2 meter resolution won't show up for a reasonably scaled 3D print but WILL make processing times horrific. Something like 30 meter resolution is better. This is also the time to re-mask your area of interest since the swisstopo site exports blocky edges on diagonals.<br>
  4. Convert edited GeoTiff to STL mesh for slicing and 3D printing. This is accomplished using the scripts from 241219 or 250211.<br>
  5. Slice and 3D print it!<br><br>

There are 4 python sripts in this repo. The 2 from 241217 and 241219 (dates yymmdd) are the scripts I originally used to create my gift. The 2 from 250210 and 250211 are cleaned versions I created for a requested code sample. In addition to generally cleaning and documenting my code even more clearly, in the 250210 script, I made initial tile merging a function. In the 250211 script, I got rid of unnecessary 3rd dimension from tif numpy array and subsequent variables
<br><br>
Finally, a link to the final STL file of the Engadin Valley Ski Marathon since GitHub can't accept files this big https://drive.google.com/file/d/1PZ9xz0Io_OOzmNcuIu7-9txUzJ184n1H/view?usp=sharing <br> Slice this for your 3D printer to make yourself a copy!
