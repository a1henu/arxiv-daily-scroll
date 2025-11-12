---
layout: default
title: Federated CLIP for Resource-Efficient Heterogeneous Medical Image Classification
---

# Federated CLIP for Resource-Efficient Heterogeneous Medical Image Classification
**arXiv**：[2511.07929v1](https://arxiv.org/abs/2511.07929) · [PDF](https://arxiv.org/pdf/2511.07929.pdf)  
**作者**：Yihang Wu, Ahmad Chaddad  

**一句话要点**：提出FedMedCLIP以解决医疗图像分类中联邦学习的异构数据与资源成本问题

**关键词**：联邦学习, 医疗图像分类, CLIP模型, 特征适应, 模型压缩, KL蒸馏

## 3 点简述
- 核心问题：医疗图像分类中数据隐私、异构性和高资源成本限制联邦学习部署
- 方法要点：引入掩码特征适应模块和私有分类器，结合KL蒸馏正则化与模型压缩
- 实验或效果：在四个公开数据集上性能提升8%，通信速度提升120倍

## 摘要（原文）

> Despite the remarkable performance of deep models in medical imaging, they still require source data for training, which limits their potential in light of privacy concerns. Federated learning (FL), as a decentralized learning framework that trains a shared model with multiple hospitals (a.k.a., FL clients), provides a feasible solution. However, data heterogeneity and resource costs hinder the deployment of FL models, especially when using vision language models (VLM). To address these challenges, we propose a novel contrastive language-image pre-training (CLIP) based FL approach for medical image classification (FedMedCLIP). Specifically, we introduce a masked feature adaptation module (FAM) as a communication module to reduce the communication load while freezing the CLIP encoders to reduce the computational overhead. Furthermore, we propose a masked multi-layer perceptron (MLP) as a private local classifier to adapt to the client tasks. Moreover, we design an adaptive Kullback-Leibler (KL) divergence-based distillation regularization method to enable mutual learning between FAM and MLP. Finally, we incorporate model compression to transmit the FAM parameters while using ensemble predictions for classification. Extensive experiments on four publicly available medical datasets demonstrate that our model provides feasible performance (e.g., 8\% higher compared to second best baseline on ISIC2019) with reasonable resource cost (e.g., 120$\times$ faster than FedAVG).

