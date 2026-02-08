---
layout: default
title: Dataset Distillation via Relative Distribution Matching and Cognitive Heritage
---

# Dataset Distillation via Relative Distribution Matching and Cognitive Heritage
**arXiv**：[2602.05391v1](https://arxiv.org/abs/2602.05391) · [PDF](https://arxiv.org/pdf/2602.05391.pdf)  
**作者**：Qianxin Xia, Jiawei Du, Yuhan Zhang, Jielei Wang, Guoming Lu  

**一句话要点**：提出统计流匹配与分类器继承策略，以高效实现数据集蒸馏于分类任务

**关键词**：数据集蒸馏, 统计流匹配, 分类器继承, 自监督学习, 计算效率

## 3 点简述
- 针对基于预训练自监督模型的数据集蒸馏，现有线性梯度匹配方法计算开销大
- 引入统计流匹配，通过对齐原始数据中类别中心间的统计流来优化合成图像
- 实验显示，该方法在性能相当或更优下，显著降低GPU内存和运行时间

## 摘要（原文）

> Dataset distillation seeks to synthesize a highly compact dataset that achieves performance comparable to the original dataset on downstream tasks. For the classification task that use pre-trained self-supervised models as backbones, previous linear gradient matching optimizes synthetic images by encouraging them to mimic the gradient updates induced by real images on the linear classifier. However, this batch-level formulation requires loading thousands of real images and applying multiple rounds of differentiable augmentations to synthetic images at each distillation step, leading to substantial computational and memory overhead. In this paper, we introduce statistical flow matching , a stable and efficient supervised learning framework that optimizes synthetic images by aligning constant statistical flows from target class centers to non-target class centers in the original data. Our approach loads raw statistics only once and performs a single augmentation pass on the synthetic data, achieving performance comparable to or better than the state-of-the-art methods with 10x lower GPU memory usage and 4x shorter runtime. Furthermore, we propose a classifier inheritance strategy that reuses the classifier trained on the original dataset for inference, requiring only an extremely lightweight linear projector and marginal storage while achieving substantial performance gains.

