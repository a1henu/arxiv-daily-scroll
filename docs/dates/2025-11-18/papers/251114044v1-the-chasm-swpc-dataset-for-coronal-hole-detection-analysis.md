---
layout: default
title: The CHASM-SWPC Dataset for Coronal Hole Detection & Analysis
---

# The CHASM-SWPC Dataset for Coronal Hole Detection & Analysis
**arXiv**：[2511.14044v1](https://arxiv.org/abs/2511.14044) · [PDF](https://arxiv.org/pdf/2511.14044.pdf)  
**作者**：Cutter Beck, Evan Smith, Khagendra Katuwal, Rudra Kafle, Jacob Whitehill  

**一句话要点**：提出CHASM-SWPC数据集与CHASM工具，用于训练和测试日冕洞自动检测模型。

**关键词**：日冕洞检测, 数据集构建, 半自动标注, 神经网络训练, 太阳物理

## 3 点简述
- 核心问题：日冕洞在EUV光谱中呈暗斑，需高质量数据集支持自动检测。
- 方法要点：开发半自动管道将SWPC手绘地图数字化为分割掩码。
- 实验或效果：训练CHRONNOS网络，准确率达0.9805，优于原模型。

## 摘要（原文）

> Coronal holes (CHs) are low-activity, low-density solar coronal regions with open magnetic field lines (Cranmer 2009). In the extreme ultraviolet (EUV) spectrum, CHs appear as dark patches. Using daily hand-drawn maps from the Space Weather Prediction Center (SWPC), we developed a semi-automated pipeline to digitize the SWPC maps into binary segmentation masks. The resulting masks constitute the CHASM-SWPC dataset, a high-quality dataset to train and test automated CH detection models, which is released with this paper. We developed CHASM (Coronal Hole Annotation using Semi-automatic Methods), a software tool for semi-automatic annotation that enables users to rapidly and accurately annotate SWPC maps. The CHASM tool enabled us to annotate 1,111 CH masks, comprising the CHASM-SWPC-1111 dataset. We then trained multiple CHRONNOS (Coronal Hole RecOgnition Neural Network Over multi-Spectral-data) architecture (Jarolim et al. 2021) neural networks using the CHASM-SWPC dataset and compared their performance. Training the CHRONNOS neural network on these data achieved an accuracy of 0.9805, a True Skill Statistic (TSS) of 0.6807, and an intersection-over-union (IoU) of 0.5668, which is higher than the original pretrained CHRONNOS model Jarolim et al. (2021) achieved an accuracy of 0.9708, a TSS of 0.6749, and an IoU of 0.4805, when evaluated on the CHASM-SWPC-1111 test set.

