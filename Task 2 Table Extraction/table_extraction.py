# -*- coding: utf-8 -*-
"""Table_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E-q2PMFZMKZJEKDj6MX6HF7ZkJJ2WmtM

# Task 2 Table Extraction
"""

!pip install tabula-py

"""#### Importing packages"""

from tabula import read_pdf
from tabulate import tabulate
import pandas as pd

file_path = "/content/Extracted pages from keppel-corporation m-limited-annual-report-2018.pdf"
pd.set_option('display.max_columns', None)

"""#### Reading PDF"""

def reding_tables(file_path):
  tables = df = read_pdf(file_path, pages = "all")
  return tables

"""#### Parsing Table"""

def parsing_table(tables):
  list_of_tables = {}
  for i in range(len(tables[0])):
    list_of_tables ["Table_" + str(i)] = pd.DataFrame(tables[i])
    list_of_tables ["Table_" + str(i)].dropna()
  return list_of_tables

"""#### Sample Results"""

table = pd.DataFrame(tables[6])
  table.dropna()

table = pd.DataFrame(tables[7])
  table.dropna()

"""# Table Extraction using Deep learning CV model Detectron 2"""

!pip install -U layoutparser
!pip install -U layoutparser
!pip install 'git+https://github.com/facebookresearch/detectron2.git@v0.4#egg=detectron2'
!pip install layoutparser[ocr]

import cv2
bgr_image = cv2.imread("/content/Extracted pages from keppel-corporation m-limited-annual-report-2018-3.jpg")
rgb_image = bgr_image[..., ::-1]
# Because CV by default loads image in BGR array, therefor we are converting it to RGB because Detectron 2 accepts RGB array

import layoutparser as lp
model = lp.Detectron2LayoutModel('lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config',extra_config=["MODEL.ROI_HEADS.SCORE_THRESH_TEST", 0.65],
                                 label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"})
# 'lp://PubLayNet/mask_rcnn_X_101_32x8d_FPN_3x/config'is our pretrained model and we are giving 0.65 confidence score for the bounding box to 
# be drawn around our regions of interest
# The label_map are the labels that this model is trained to detect.
extracted_layout = model.detect(rgb_image) 
lp.draw_box(rgb_image, extracted_layout,)

table_bounding_boxes = lp.Layout([b for b in extracted_layout if b.type=="Table" ])

"""#### Drawing Bounding Box Around Tables

"""

lp.draw_box(rgb_image, table_bounding_boxes,
            box_width=3, 
            show_element_id=True)

"""#### Cropping Table"""

segment_image = (table_bounding_boxes
                       .pad(left=5, right=5, top=5, bottom=5)
                       .crop_image(rgb_image))

import matplotlib.pyplot as plt

image = segment_image[0]
plt.imshow(image);



