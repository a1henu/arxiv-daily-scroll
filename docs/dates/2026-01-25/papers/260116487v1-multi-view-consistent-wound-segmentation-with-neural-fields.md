---
layout: default
title: Multi-View Consistent Wound Segmentation With Neural Fields
---

# Multi-View Consistent Wound Segmentation With Neural Fields
**arXiv**：[2601.16487v1](https://arxiv.org/abs/2601.16487) · [PDF](https://arxiv.org/pdf/2601.16487.pdf)  
**作者**：Remi Chierchia, Léo Lebrat, David Ahmedt-Aristizabal, Yulia Arzhaeva, Olivier Salvado, Clinton Fookes, Rodrigo Santa Cruz  

**一句话要点**：提出WoundNeRF方法，基于NeRF SDF从多视角图像实现伤口分割，以解决3D结构一致性问题。

**关键词**：伤口分割, NeRF SDF, 多视角一致性, 3D重建, 计算机视觉医疗应用

## 3 点简述
- 核心问题：从2D图像推断多视角一致的3D伤口分割结构仍具挑战。
- 方法要点：采用NeRF SDF方法，从自动生成的标注中估计鲁棒的伤口分割。
- 实验或效果：与先进Vision Transformer和基于光栅化的算法比较，展示准确分割恢复潜力。

## 摘要（原文）

> Wound care is often challenged by the economic and logistical burdens that consistently afflict patients and hospitals worldwide. In recent decades, healthcare professionals have sought support from computer vision and machine learning algorithms. In particular, wound segmentation has gained interest due to its ability to provide professionals with fast, automatic tissue assessment from standard RGB images. Some approaches have extended segmentation to 3D, enabling more complete and precise healing progress tracking. However, inferring multi-view consistent 3D structures from 2D images remains a challenge. In this paper, we evaluate WoundNeRF, a NeRF SDF-based method for estimating robust wound segmentations from automatically generated annotations. We demonstrate the potential of this paradigm in recovering accurate segmentations by comparing it against state-of-the-art Vision Transformer networks and conventional rasterisation-based algorithms. The code will be released to facilitate further development in this promising paradigm.

