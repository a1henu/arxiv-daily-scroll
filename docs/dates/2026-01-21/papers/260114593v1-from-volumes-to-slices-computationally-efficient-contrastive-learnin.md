---
layout: default
title: From Volumes to Slices: Computationally Efficient Contrastive Learning for Sequential Abdominal CT Analysis
---

# From Volumes to Slices: Computationally Efficient Contrastive Learning for Sequential Abdominal CT Analysis
**arXiv**：[2601.14593v1](https://arxiv.org/abs/2601.14593) · [PDF](https://arxiv.org/pdf/2601.14593.pdf)  
**作者**：Po-Kai Chiu, Hung-Hsuan Chen  

**一句话要点**：提出2D-VoCo以解决腹部CT序列分析中3D自监督学习计算成本高的问题

**关键词**：腹部CT分析, 自监督学习, 对比学习, 计算效率, 医学图像分类, CNN-LSTM架构

## 3 点简述
- 核心问题：3D自监督方法如VoCo计算成本高，限制医学图像分析应用
- 方法要点：将VoCo框架适配为2D切片级自监督预训练，通过对比学习从无标签CT切片学习特征
- 实验或效果：在RSNA 2023腹部创伤数据集上，2D-VoCo预训练显著提升mAP、精度、召回率和RSNA分数

## 摘要（原文）

> The requirement for expert annotations limits the effectiveness of deep learning for medical image analysis. Although 3D self-supervised methods like volume contrast learning (VoCo) are powerful and partially address the labeling scarcity issue, their high computational cost and memory consumption are barriers. We propose 2D-VoCo, an efficient adaptation of the VoCo framework for slice-level self-supervised pre-training that learns spatial-semantic features from unlabeled 2D CT slices via contrastive learning. The pre-trained CNN backbone is then integrated into a CNN-LSTM architecture to classify multi-organ injuries. In the RSNA 2023 Abdominal Trauma dataset, 2D-VoCo pre-training significantly improves mAP, precision, recall, and RSNA score over training from scratch. Our framework provides a practical method to reduce the dependency on labeled data and enhance model performance in clinical CT analysis. We release the code for reproducibility. https://github.com/tkz05/2D-VoCo-CT-Classifier

