---
layout: default
title: Federated Vision Transformer with Adaptive Focal Loss for Medical Image Classification
---

# Federated Vision Transformer with Adaptive Focal Loss for Medical Image Classification
**arXiv**：[2602.01633v1](https://arxiv.org/abs/2602.01633) · [PDF](https://arxiv.org/pdf/2602.01633.pdf)  
**作者**：Xinyuan Zhao, Yihang Wu, Ahmad Chaddad, Tareef Daqqaq, Reem Kateb  

**一句话要点**：提出联邦视觉Transformer与自适应焦点损失，以解决医学图像分类中的数据隐私和类别不平衡问题。

**关键词**：联邦学习, 视觉Transformer, 自适应焦点损失, 医学图像分类, 类别不平衡, 客户端异构性

## 3 点简述
- 核心问题：数据隐私限制和本地客户端数据异构性及类别不平衡影响模型泛化。
- 方法要点：设计动态自适应焦点损失和客户端感知加权聚合策略，优化本地训练。
- 实验或效果：在三个公开数据集上优于多种基线模型，准确率提升0.98%至41.69%。

## 摘要（原文）

> While deep learning models like Vision Transformer (ViT) have achieved significant advances, they typically require large datasets. With data privacy regulations, access to many original datasets is restricted, especially medical images. Federated learning (FL) addresses this challenge by enabling global model aggregation without data exchange. However, the heterogeneity of the data and the class imbalance that exist in local clients pose challenges for the generalization of the model. This study proposes a FL framework leveraging a dynamic adaptive focal loss (DAFL) and a client-aware aggregation strategy for local training. Specifically, we design a dynamic class imbalance coefficient that adjusts based on each client's sample distribution and class data distribution, ensuring minority classes receive sufficient attention and preventing sparse data from being ignored. To address client heterogeneity, a weighted aggregation strategy is adopted, which adapts to data size and characteristics to better capture inter-client variations. The classification results on three public datasets (ISIC, Ocular Disease and RSNA-ICH) show that the proposed framework outperforms DenseNet121, ResNet50, ViT-S/16, ViT-L/32, FedCLIP, Swin Transformer, CoAtNet, and MixNet in most cases, with accuracy improvements ranging from 0.98\% to 41.69\%. Ablation studies on the imbalanced ISIC dataset validate the effectiveness of the proposed loss function and aggregation strategy compared to traditional loss functions and other FL approaches. The codes can be found at: https://github.com/AIPMLab/ViT-FLDAF.

