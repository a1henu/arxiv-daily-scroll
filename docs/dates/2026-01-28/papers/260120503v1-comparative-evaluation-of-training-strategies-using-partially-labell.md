---
layout: default
title: Comparative evaluation of training strategies using partially labelled datasets for segmentation of white matter hyperintensities and stroke lesions in FLAIR MRI
---

# Comparative evaluation of training strategies using partially labelled datasets for segmentation of white matter hyperintensities and stroke lesions in FLAIR MRI
**arXiv**：[2601.20503v1](https://arxiv.org/abs/2601.20503) · [PDF](https://arxiv.org/pdf/2601.20503.pdf)  
**作者**：Jesse Phitidis, Alison Q. Smithard, William N. Whiteley, Joanna M. Wardlaw, Miguel O. Bernabeu, Maria Valdés Hernández  

**一句话要点**：提出六种训练策略，利用部分标注数据提升FLAIR MRI中白质高信号和缺血性卒中病灶的联合分割性能。

**关键词**：医学图像分割, 部分标注数据, 白质高信号, 缺血性卒中病灶, FLAIR MRI, 伪标签训练

## 3 点简述
- 核心问题：FLAIR MRI中白质高信号和缺血性卒中病灶视觉混淆，且常共存，导致分割模型开发困难。
- 方法要点：研究六种训练策略，结合私有和公开的部分标注数据集，共2052个MRI体积，探索伪标签等方法。
- 实验或效果：多种方法能有效利用部分标注数据提升性能，其中伪标签策略效果最佳。

## 摘要（原文）

> White matter hyperintensities (WMH) and ischaemic stroke lesions (ISL) are imaging features associated with cerebral small vessel disease (SVD) that are visible on brain magnetic resonance imaging (MRI) scans. The development and validation of deep learning models to segment and differentiate these features is difficult because they visually confound each other in the fluid-attenuated inversion recovery (FLAIR) sequence and often appear in the same subject. We investigated six strategies for training a combined WMH and ISL segmentation model using partially labelled data. We combined privately held fully and partially labelled datasets with publicly available partially labelled datasets to yield a total of 2052 MRI volumes, with 1341 and 1152 containing ground truth annotations for WMH and ISL respectively. We found that several methods were able to effectively leverage the partially labelled data to improve model performance, with the use of pseudolabels yielding the best result.

