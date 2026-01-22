---
layout: default
title: Filtered 2D Contour-Based Reconstruction of 3D STL Model from CT-DICOM Images
---

# Filtered 2D Contour-Based Reconstruction of 3D STL Model from CT-DICOM Images
**arXiv**：[2601.14997v1](https://arxiv.org/abs/2601.14997) · [PDF](https://arxiv.org/pdf/2601.14997.pdf)  
**作者**：K. Punnam Chandar, Y. Ravi Kumar  

**一句话要点**：提出基于过滤2D轮廓的方法，从CT-DICOM图像重建3D STL模型以改善几何精度

**关键词**：3D重建, CT图像处理, STL模型, 轮廓过滤, Delaunay三角剖分, 医学图像分割

## 3 点简述
- 核心问题：从CT-DICOM图像重建3D STL模型时，分割产生的2D轮廓数据点包含异常值，导致几何偏差。
- 方法要点：使用过滤后的2D轮廓数据点，通过Delaunay三角剖分和逐层连接来重建3D STL模型。
- 实验或效果：在基本形状和人体骨盆骨ROI上进行验证，过滤后的模型几何精度优于未过滤模型。

## 摘要（原文）

> Reconstructing a 3D Stereo-lithography (STL) Model from 2D Contours of scanned structure in Digital Imaging and Communication in Medicine (DICOM) images is crucial to understand the geometry and deformity. Computed Tomography (CT) images are processed to enhance the contrast, reduce the noise followed by smoothing. The processed CT images are segmented using thresholding technique. 2D contour data points are extracted from segmented CT images and are used to construct 3D STL Models. The 2D contour data points may contain outliers as a result of segmentation of low resolution images and the geometry of the constructed 3D structure deviate from the actual. To cope with the imperfections in segmentation process, in this work we propose to use filtered 2D contour data points to reconstruct 3D STL Model. The filtered 2D contour points of each image are delaunay triangulated and joined layer-by-layer to reconstruct the 3D STL model. The 3D STL Model reconstruction is verified on i) 2D Data points of basic shapes and ii) Region of Interest (ROI) of human pelvic bone and are presented as case studies. The 3D STL model constructed from 2D contour data points of ROI of segmented pelvic bone with and without filtering are presented. The 3D STL model reconstructed from filtered 2D data points improved the geometry of model compared to the model reconstructed without filtering 2D data points.

