2 files to process swiss elevation data into an STL mesh file for 3d printing.
1st file (241217_access_merge_elevation_data) takes csv file exported from https://www.swisstopo.admin.ch/en/height-model-swissalti3d . File opens links to tiled elevation tifs and merges them into a single tif for the desired area selected from the website.
2nd file (241219_Tif_to_STL) takes the merged tif file with elevation data and processes it into a triangulated mesh for export as an STL. This script is based on code from ChatGPT, which I practiced using to expedite my code-writing process.
