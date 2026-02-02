---
layout: default
title: OOVDet: Low-Density Prior Learning for Zero-Shot Out-of-Vocabulary Object Detection
---

# OOVDet: Low-Density Prior Learning for Zero-Shot Out-of-Vocabulary Object Detection
**arXiv**：[2601.22685v1](https://arxiv.org/abs/2601.22685) · [PDF](https://arxiv.org/pdf/2601.22685.pdf)  
**作者**：Binyi Su, Chenghao Huang, Haiyong Chen  

**一句话要点**：提出OOVDet框架，通过低密度先验学习解决零样本外词汇对象检测中的过拟合问题。

**关键词**：零样本检测, 外词汇对象检测, 低密度先验, 高斯核密度估计, 不确定性估计

## 3 点简述
- 核心问题：零样本外词汇检测中，模型易过拟合内词汇类别，导致外词汇对象被高置信度误分类。
- 方法要点：合成区域级外词汇提示和伪外词汇图像，基于低密度先验约束构建决策边界。
- 实验或效果：实验结果显示，该方法显著提升零样本场景下的外词汇检测性能。

## 摘要（原文）

> Zero-shot out-of-vocabulary detection (ZS-OOVD) aims to accurately recognize objects of in-vocabulary (IV) categories provided at zero-shot inference, while simultaneously rejecting undefined ones (out-of-vocabulary, OOV) that lack corresponding category prompts. However, previous methods are prone to overfitting the IV classes, leading to the OOV or undefined classes being misclassified as IV ones with a high confidence score. To address this issue, this paper proposes a zero-shot OOV detector (OOVDet), a novel framework that effectively detects predefined classes while reliably rejecting undefined ones in zero-shot scenes. Specifically, due to the model's lack of prior knowledge about the distribution of OOV data, we synthesize region-level OOV prompts by sampling from the low-likelihood regions of the class-conditional Gaussian distributions in the hidden space, motivated by the assumption that unknown semantics are more likely to emerge in low-density areas of the latent space. For OOV images, we further propose a Dirichlet-based gradient attribution mechanism to mine pseudo-OOV image samples, where the attribution gradients are interpreted as Dirichlet evidence to estimate prediction uncertainty, and samples with high uncertainty are selected as pseudo-OOV images. Building on these synthesized OOV prompts and pseudo-OOV images, we construct the OOV decision boundary through a low-density prior constraint, which regularizes the optimization of OOV classes using Gaussian kernel density estimation in accordance with the above assumption.
>   Experimental results show that our method significantly improves the OOV detection performance in zero-shot scenes. The code is available at https://github.com/binyisu/OOV-detector.

