---
layout: default
title: Generalizable Blood Cell Detection via Unified Dataset and Faster R-CNN
---

# Generalizable Blood Cell Detection via Unified Dataset and Faster R-CNN
**arXiv**：[2511.08465v1](https://arxiv.org/abs/2511.08465) · [PDF](https://arxiv.org/pdf/2511.08465.pdf)  
**作者**：Siddharth Sahay  

**一句话要点**：提出统一数据集与Faster R-CNN方法以解决血细胞检测中的数据稀缺与异质性问题

**关键词**：血细胞检测, 统一数据集, Faster R-CNN, 迁移学习, ResNet-50-FPN, 验证损失

## 3 点简述
- 核心问题：血细胞检测中数据稀缺和异质性阻碍模型泛化
- 方法要点：整合四个公共数据集，采用Faster R-CNN与ResNet-50-FPN骨干网络
- 实验或效果：迁移学习方案收敛更快，验证损失降至0.08666，优于基线

## 摘要（原文）

> This paper presents a comprehensive methodology and comparative performance analysis for the automated classification and object detection of peripheral blood cells (PBCs) in microscopic images. Addressing the critical challenge of data scarcity and heterogeneity, robust data pipeline was first developed to standardize and merge four public datasets (PBC, BCCD, Chula, Sickle Cell) into a unified resource. Then employed a state-of-the-art Faster R-CNN object detection framework, leveraging a ResNet-50-FPN backbone. Comparative training rigorously evaluated a randomly initialized baseline model (Regimen 1) against a Transfer Learning Regimen (Regimen 2), initialized with weights pre-trained on the Microsoft COCO dataset. The results demonstrate that the Transfer Learning approach achieved significantly faster convergence and superior stability, culminating in a final validation loss of 0.08666, a substantial improvement over the baseline. This validated methodology establishes a robust foundation for building high-accuracy, deployable systems for automated hematological diagnosis.

