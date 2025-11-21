---
layout: default
title: Weakly Supervised Segmentation and Classification of Alpha-Synuclein Aggregates in Brightfield Midbrain Images
---

# Weakly Supervised Segmentation and Classification of Alpha-Synuclein Aggregates in Brightfield Midbrain Images
**arXiv**：[2511.16268v1](https://arxiv.org/abs/2511.16268) · [PDF](https://arxiv.org/pdf/2511.16268.pdf)  
**作者**：Erwan Dereure, Robin Louiset, Laura Parkkinen, David A Menassa, David Holcman  

**一句话要点**：提出弱监督分割与分类方法以自动分析帕金森病中α-突触核蛋白聚集物

**关键词**：弱监督分割, α-突触核蛋白聚集物, 帕金森病, 全玻片图像, ResNet50分类器, 免疫组化图像

## 3 点简述
- 核心问题：帕金森病中α-突触核蛋白聚集物的自动分割与分类，以理解其空间分布。
- 方法要点：基于弱监督分割和ResNet50分类器，处理免疫组化标记变异。
- 实验或效果：在区分Lewy体和神经突形态时，平衡准确率达到80%。

## 摘要（原文）

> Parkinson's disease (PD) is a neurodegenerative disorder associated with the accumulation of misfolded alpha-synuclein aggregates, forming Lewy bodies and neuritic shape used for pathology diagnostics. Automatic analysis of immunohistochemistry histopathological images with Deep Learning provides a promising tool for better understanding the spatial organization of these aggregates. In this study, we develop an automated image processing pipeline to segment and classify these aggregates in whole-slide images (WSIs) of midbrain tissue from PD and incidental Lewy Body Disease (iLBD) cases based on weakly supervised segmentation, robust to immunohistochemical labelling variability, with a ResNet50 classifier. Our approach allows to differentiate between major aggregate morphologies, including Lewy bodies and neurites with a balanced accuracy of $80\%$. This framework paves the way for large-scale characterization of the spatial distribution and heterogeneity of alpha-synuclein aggregates in brightfield immunohistochemical tissue, and for investigating their poorly understood relationships with surrounding cells such as microglia and astrocytes.

