---
layout: default
title: MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration
---

# MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration
**arXiv**：[2603.09101v1](https://arxiv.org/abs/2603.09101) · [PDF](https://arxiv.org/pdf/2603.09101.pdf)  
**作者**：Chenran Zhang, Ruiqi Wu, Tao Zhou, Yi Zhou  

**一句话要点**：提出MedKCO通过知识驱动认知编排解决医学视觉-语言预训练中的特征表示问题。

**关键词**：医学视觉-语言预训练, 课程学习, 对比学习, 认知编排, 医学影像分析

## 3 点简述
- 核心问题：现有医学VLP方法同时学习简单和复杂概念，导致特征表示不佳，尤其在分布偏移下。
- 方法要点：设计两级课程，基于诊断敏感性和类内样本代表性排序数据，并引入自步非对称对比损失动态调整目标。
- 实验或效果：在三个医学影像场景的多任务中评估，显著超越基线，代码已开源。

## 摘要（原文）

> Medical vision-language pretraining (VLP) models have recently been investigated for their generalization to diverse downstream tasks. However, current medical VLP methods typically force the model to learn simple and complex concepts simultaneously. This anti-cognitive process leads to suboptimal feature representations, especially under distribution shift. To address this limitation, we propose a Knowledge-driven Cognitive Orchestration for Medical VLP (MedKCO) that involves both the ordering of the pretraining data and the learning objective of vision-language contrast. Specifically, we design a two level curriculum by incorporating diagnostic sensitivity and intra-class sample representativeness for the ordering of the pretraining data. Moreover, considering the inter-class similarity of medical images, we introduce a self-paced asymmetric contrastive loss to dynamically adjust the participation of the pretraining objective. We evaluate the proposed pretraining method on three medical imaging scenarios in multiple vision-language downstream tasks, and compare it with several curriculum learning methods. Extensive experiments show that our method significantly surpasses all baselines. https://github.com/Mr-Talon/MedKCO.

