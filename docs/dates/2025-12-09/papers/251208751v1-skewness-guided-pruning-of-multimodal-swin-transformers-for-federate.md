---
layout: default
title: Skewness-Guided Pruning of Multimodal Swin Transformers for Federated Skin Lesion Classification on Edge Devices
---

# Skewness-Guided Pruning of Multimodal Swin Transformers for Federated Skin Lesion Classification on Edge Devices
**arXiv**：[2512.08751v1](https://arxiv.org/abs/2512.08751) · [PDF](https://arxiv.org/pdf/2512.08751.pdf)  
**作者**：Kuniko Paxton, Koorosh Aslansefat, Dhavalkumar Thakker, Yiannis Papadopoulos  

**一句话要点**：提出基于偏度引导的剪枝方法，用于联邦学习下边缘设备的多模态皮肤病变分类。

**关键词**：联邦学习, 模型剪枝, 多模态Swin Transformer, 皮肤病变分类, 边缘计算

## 3 点简述
- 核心问题：高精度医学视觉模型计算量大、隐私限制，难以部署于边缘设备。
- 方法要点：基于输出分布偏度，选择性剪枝多模态Swin Transformer的自注意力和多层感知机层。
- 实验或效果：在联邦学习环境中验证，模型大小减少约36%，准确率无损失。

## 摘要（原文）

> In recent years, high-performance computer vision models have achieved remarkable success in medical imaging, with some skin lesion classification systems even surpassing dermatology specialists in diagnostic accuracy. However, such models are computationally intensive and large in size, making them unsuitable for deployment on edge devices. In addition, strict privacy constraints hinder centralized data management, motivating the adoption of Federated Learning (FL). To address these challenges, this study proposes a skewness-guided pruning method that selectively prunes the Multi-Head Self-Attention and Multi-Layer Perceptron layers of a multimodal Swin Transformer based on the statistical skewness of their output distributions. The proposed method was validated in a horizontal FL environment and shown to maintain performance while substantially reducing model complexity. Experiments on the compact Swin Transformer demonstrate approximately 36\% model size reduction with no loss in accuracy. These findings highlight the feasibility of achieving efficient model compression and privacy-preserving distributed learning for multimodal medical AI on edge devices.

