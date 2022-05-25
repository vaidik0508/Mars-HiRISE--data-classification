Mars orbital image (HiRISE) labeled data set version 3
--------------------------------------------
Authors: Kiri L. Wagstaff, Steven Lu, Gary Doran, Lukas Mandrake
Contact: you.lu@jpl.nasa.gov

This data set contains a total of 73,031 landmarks. 10,433 landmarks were detected and extracted from 180 HiRISE browse images, and 62,598 landmarks were augmented from 10,433 original landmarks. For each original landmark, we cropped a square bounding box that includes the full extent of the landmark plus a 30-pixel margin to left, right, top and bottom. Each cropped landmark was resized to 227x227 pixels, and then was augmented to generate 6 additional landmarks using the following methods:

1. 90 degrees clockwise rotation
2. 180 degrees clockwise rotation
3. 270 degrees clockwise rotation
4. Horizontal flip
5. Vertical flip
6. Random brightness adjustment


Contents:
- map-proj-v3/: Directory containing individual cropped landmark images
- labels-map-proj-v3.txt: Class labels (ids) for each landmark image
- landmarks_map-proj-v3_classmap.csv: Dictionary that maps class ids to semantic names


Attribution:
If you use this data set in your own work, please cite this DOI: 10.5281/zenodo.2538136