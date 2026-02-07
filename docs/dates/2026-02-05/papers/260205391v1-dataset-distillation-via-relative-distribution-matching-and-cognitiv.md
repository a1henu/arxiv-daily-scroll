---
layout: default
title: Dataset Distillation via Relative Distribution Matching and Cognitive Heritage
---

# Dataset Distillation via Relative Distribution Matching and Cognitive Heritage
**arXiv**：[2602.05391v1](https://arxiv.org/abs/2602.05391) · [PDF](https://arxiv.org/pdf/2602.05391.pdf)  
**作者**：Qianxin Xia, Jiawei Du, Yuhan Zhang, Jielei Wang, Guoming Lu  

**一句话要点**：提出统计流匹配与分类器继承策略，以高效实现数据集蒸馏，降低计算开销。

**关键词**：数据集蒸馏, 统计流匹配, 分类器继承, 计算效率, 监督学习, 图像合成

## 3 点简述
- 针对分类任务中数据集蒸馏的计算和内存开销问题，提出统计流匹配方法。
- 该方法通过对齐原始数据中目标类中心到非目标类中心的统计流，优化合成图像。
- 实验显示，在性能相当或更优下，GPU内存使用降低10倍，运行时间缩短4倍。

## 摘要（原文）

> Dataset distillation seeks to synthesize a highly compact dataset that achieves performance comparable to the original dataset on downstream tasks. For the classification task that use pre-trained self-supervised models as backbones, previous linear gradient matching optimizes synthetic images by encouraging them to mimic the gradient updates induced by real images on the linear classifier. However, this batch-level formulation requires loading thousands of real images and applying multiple rounds of differentiable augmentations to synthetic images at each distillation step, leading to substantial computational and memory overhead. In this paper, we introduce statistical flow matching , a stable and efficient supervised learning framework that optimizes synthetic images by aligning constant statistical flows from target class centers to non-target class centers in the original data. Our approach loads raw statistics only once and performs a single augmentation pass on the synthetic data, achieving performance comparable to or better than the state-of-the-art methods with 10x lower GPU memory usage and 4x shorter runtime. Furthermore, we propose a classifier inheritance strategy that reuses the classifier trained on the original dataset for inference, requiring only an extremely lightweight linear projector and marginal storage while achieving substantial performance gains.

