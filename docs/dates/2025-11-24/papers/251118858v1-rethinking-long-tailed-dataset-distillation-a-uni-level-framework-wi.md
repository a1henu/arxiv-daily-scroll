---
layout: default
title: Rethinking Long-tailed Dataset Distillation: A Uni-Level Framework with Unbiased Recovery and Relabeling
---

# Rethinking Long-tailed Dataset Distillation: A Uni-Level Framework with Unbiased Recovery and Relabeling
**arXiv**：[2511.18858v1](https://arxiv.org/abs/2511.18858) · [PDF](https://arxiv.org/pdf/2511.18858.pdf)  
**作者**：Xiao Cui, Yulei Qin, Xinyue Li, Wengang Zhou, Hongsheng Li, Houqiang Li  

**一句话要点**：提出统一框架，通过无偏恢复和软重标解决长尾数据集蒸馏问题

**关键词**：数据集蒸馏, 长尾分布, 无偏恢复, 软重标, 统计对齐, 模型偏差

## 3 点简述
- 长尾分布导致模型表示偏差和统计估计错误，影响蒸馏效果
- 方法包括增强专家模型、重校准BN统计和多轮初始化合成图像
- 在多个长尾基准测试中，准确率显著提升，如CIFAR-100-LT提高15.6%

## 摘要（原文）

> Dataset distillation creates a small distilled set that enables efficient training by capturing key information from the full dataset. While existing dataset distillation methods perform well on balanced datasets, they struggle under long-tailed distributions, where imbalanced class frequencies induce biased model representations and corrupt statistical estimates such as Batch Normalization (BN) statistics. In this paper, we rethink long-tailed dataset distillation by revisiting the limitations of trajectory-based methods, and instead adopt the statistical alignment perspective to jointly mitigate model bias and restore fair supervision. To this end, we introduce three dedicated components that enable unbiased recovery of distilled images and soft relabeling: (1) enhancing expert models (an observer model for recovery and a teacher model for relabeling) to enable reliable statistics estimation and soft-label generation; (2) recalibrating BN statistics via a full forward pass with dynamically adjusted momentum to reduce representation skew; (3) initializing synthetic images by incrementally selecting high-confidence and diverse augmentations via a multi-round mechanism that promotes coverage and diversity. Extensive experiments on four long-tailed benchmarks show consistent improvements over state-of-the-art methods across varying degrees of class imbalance.Notably, our approach improves top-1 accuracy by 15.6% on CIFAR-100-LT and 11.8% on Tiny-ImageNet-LT under IPC=10 and IF=10.

