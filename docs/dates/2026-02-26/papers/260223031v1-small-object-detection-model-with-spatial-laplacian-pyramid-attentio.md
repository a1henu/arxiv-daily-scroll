---
layout: default
title: Small Object Detection Model with Spatial Laplacian Pyramid Attention and Multi-Scale Features Enhancement in Aerial Images
---

# Small Object Detection Model with Spatial Laplacian Pyramid Attention and Multi-Scale Features Enhancement in Aerial Images
**arXiv**：[2602.23031v1](https://arxiv.org/abs/2602.23031) · [PDF](https://arxiv.org/pdf/2602.23031.pdf)  
**作者**：Zhangjian Ji, Huijia Yan, Shaotong Qiao, Kai Feng, Wei Wei  

**一句话要点**：提出基于空间拉普拉斯金字塔注意力和多尺度特征增强的小目标检测模型，用于航拍图像

**关键词**：小目标检测, 航拍图像, 空间拉普拉斯金字塔注意力, 多尺度特征增强, 可变形卷积, 特征金字塔网络

## 3 点简述
- 核心问题：航拍图像中小目标尺寸小、分布密集且不均匀，导致检测效率低。
- 方法要点：引入空间拉普拉斯金字塔注意力模块增强小目标特征表示，设计多尺度特征增强模块提升语义理解，并使用可变形卷积对齐特征金字塔网络中的特征。
- 实验或效果：在VisDrone和DOTA数据集上验证，改进模型在航拍图像小目标检测中表现优于原算法。

## 摘要（原文）

> Detecting objects in aerial images confronts some significant challenges, including small size, dense and non-uniform distribution of objects over high-resolution images, which makes detection inefficient. Thus, in this paper, we proposed a small object detection algorithm based on a Spatial Laplacian Pyramid Attention and Multi-Scale Feature Enhancement in aerial images. Firstly, in order to improve the feature representation of ResNet-50 on small objects, we presented a novel Spatial Laplacian Pyramid Attention (SLPA) module, which is integrated after each stage of ResNet-50 to identify and emphasize important local regions. Secondly, to enhance the model's semantic understanding and features representation, we designed a Multi-Scale Feature Enhancement Module (MSFEM), which is incorporated into the lateral connections of C5 layer for building Feature Pyramid Network (FPN). Finally, the features representation quality of traditional feature pyramid network will be affected because the features are not aligned when the upper and lower layers are fused. In order to handle it, we utilized deformable convolutions to align the features in the fusion processing of the upper and lower levels of the Feature Pyramid Network, which can help enhance the model's ability to detect and recognize small objects. The extensive experimental results on two benchmark datasets: VisDrone and DOTA demonstrate that our improved model performs better for small object detection in aerial images compared to the original algorithm.

