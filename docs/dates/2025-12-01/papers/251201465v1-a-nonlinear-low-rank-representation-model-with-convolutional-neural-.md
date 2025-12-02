---
layout: default
title: A Nonlinear Low-rank Representation Model with Convolutional Neural Network for Imputing Water Quality Data
---

# A Nonlinear Low-rank Representation Model with Convolutional Neural Network for Imputing Water Quality Data
**arXiv**：[2512.01465v1](https://arxiv.org/abs/2512.01465) · [PDF](https://arxiv.org/pdf/2512.01465.pdf)  
**作者**：Hongnan Si, Tong Li, Yujie Chen, Xin Liao  

**一句话要点**：提出神经塔克卷积网络模型以解决水质数据缺失问题

**关键词**：水质数据填补, 塔克分解, 卷积神经网络, 时空特征提取, 数据缺失处理

## 3 点简述
- 水质监测中数据缺失影响分析，需高效填补方法
- 模型编码多模态实体为嵌入向量，构建塔克交互张量捕获特征交互
- 在三个真实数据集上实验，模型精度优于现有填补方法

## 摘要（原文）

> Water quality monitoring is a core component of ecological environmental protection. However, due to sensor failure or other inevitable factors, data missing often exists in long-term monitoring, posing great challenges in water quality analysis. This paper proposes a Neural Tucker Convolutional Network (NTCN) model for water quality data imputation, which features the following key components: a) Encode different mode entities into respective embedding vectors, and construct a Tucker interaction tensor by outer product operations to capture the complex mode-wise feature interactions; b) Use 3D convolution to extract fine-grained spatiotemporal features from the interaction tensor. Experiments on three real-world water quality datasets show that the proposed NTCN model outperforms several state-of-the-art imputation models in terms of accuracy.

