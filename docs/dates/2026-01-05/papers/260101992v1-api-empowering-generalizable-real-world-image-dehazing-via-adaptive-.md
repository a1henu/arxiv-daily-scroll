---
layout: default
title: API: Empowering Generalizable Real-World Image Dehazing via Adaptive Patch Importance Learning
---

# API: Empowering Generalizable Real-World Image Dehazing via Adaptive Patch Importance Learning
**arXiv**：[2601.01992v1](https://arxiv.org/abs/2601.01992) · [PDF](https://arxiv.org/pdf/2601.01992.pdf)  
**作者**：Chen Zhu, Huiwen Zhang, Yujie Li, Mu He, Xiaotian Qiao  

**一句话要点**：提出自适应补丁重要性学习框架以解决真实世界图像去雾泛化问题

**关键词**：图像去雾, 自适应补丁重要性, 真实世界泛化, 数据增强, 对比学习, 低层视觉

## 3 点简述
- 核心问题：现有方法在复杂真实雾霾场景下性能下降，源于训练数据有限和雾霾密度分布复杂。
- 方法要点：引入自适应补丁重要性框架，包括自动雾霾生成模块和密度感知去雾模块，并设计多负样本对比损失。
- 实验或效果：在多个真实世界基准测试中达到先进性能，定量指标和视觉质量均表现优异，泛化能力强。

## 摘要（原文）

> Real-world image dehazing is a fundamental yet challenging task in low-level vision. Existing learning-based methods often suffer from significant performance degradation when applied to complex real-world hazy scenes, primarily due to limited training data and the intrinsic complexity of haze density distributions.To address these challenges, we introduce a novel Adaptive Patch Importance-aware (API) framework for generalizable real-world image dehazing. Specifically, our framework consists of an Automatic Haze Generation (AHG) module and a Density-aware Haze Removal (DHR) module. AHG provides a hybrid data augmentation strategy by generating realistic and diverse hazy images as additional high-quality training data. DHR considers hazy regions with varying haze density distributions for generalizable real-world image dehazing in an adaptive patch importance-aware manner. To alleviate the ambiguity of the dehazed image details, we further introduce a new Multi-Negative Contrastive Dehazing (MNCD) loss, which fully utilizes information from multiple negative samples across both spatial and frequency domains. Extensive experiments demonstrate that our framework achieves state-of-the-art performance across multiple real-world benchmarks, delivering strong results in both quantitative metrics and qualitative visual quality, and exhibiting robust generalization across diverse haze distributions.

