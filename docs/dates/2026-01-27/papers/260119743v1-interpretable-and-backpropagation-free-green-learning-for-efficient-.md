---
layout: default
title: Interpretable and backpropagation-free Green Learning for efficient multi-task echocardiographic segmentation and classification
---

# Interpretable and backpropagation-free Green Learning for efficient multi-task echocardiographic segmentation and classification
**arXiv**：[2601.19743v1](https://arxiv.org/abs/2601.19743) · [PDF](https://arxiv.org/pdf/2601.19743.pdf)  
**作者**：Jyun-Ping Kao, Jiaxing Yang, C. -C. Jay Kuo, Jonghye Woo  

**一句话要点**：提出无反向传播的多任务绿色学习框架，用于高效多任务超声心动图分割与分类

**关键词**：超声心动图分割, 左心室射血分数分类, 绿色学习, 多任务学习, 无监督特征提取, 计算效率

## 3 点简述
- 核心问题：超声心动图评估左心室射血分数存在观察者间变异大，现有深度学习模型计算密集且缺乏可解释性。
- 方法要点：结合无监督VoxelHop编码器进行层次时空特征提取，多级回归解码器和XG-Boost分类器实现多任务处理。
- 实验或效果：在EchoNet-Dynamic数据集上，分类准确率94.3%，Dice系数0.912，参数显著减少，计算效率高。

## 摘要（原文）

> Echocardiography is a cornerstone for managing heart failure (HF), with Left Ventricular Ejection Fraction (LVEF) being a critical metric for guiding therapy. However, manual LVEF assessment suffers from high inter-observer variability, while existing Deep Learning (DL) models are often computationally intensive and data-hungry "black boxes" that impede clinical trust and adoption. Here, we propose a backpropagation-free multi-task Green Learning (MTGL) framework that performs simultaneous Left Ventricle (LV) segmentation and LVEF classification. Our framework integrates an unsupervised VoxelHop encoder for hierarchical spatio-temporal feature extraction with a multi-level regression decoder and an XG-Boost classifier. On the EchoNet-Dynamic dataset, our MTGL model achieves state-of-the-art classification and segmentation performance, attaining a classification accuracy of 94.3% and a Dice Similarity Coefficient (DSC) of 0.912, significantly outperforming several advanced 3D DL models. Crucially, our model achieves this with over an order of magnitude fewer parameters, demonstrating exceptional computational efficiency. This work demonstrates that the GL paradigm can deliver highly accurate, efficient, and interpretable solutions for complex medical image analysis, paving the way for more sustainable and trustworthy artificial intelligence in clinical practice.

