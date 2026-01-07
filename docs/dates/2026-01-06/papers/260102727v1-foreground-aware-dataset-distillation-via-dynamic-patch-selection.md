---
layout: default
title: Foreground-Aware Dataset Distillation via Dynamic Patch Selection
---

# Foreground-Aware Dataset Distillation via Dynamic Patch Selection
**arXiv**：[2601.02727v1](https://arxiv.org/abs/2601.02727) · [PDF](https://arxiv.org/pdf/2601.02727.pdf)  
**作者**：Longzhen Li, Guang Li, Ren Togo, Keisuke Maeda, Takahiro Ogawa, Miki Haseyama  

**一句话要点**：提出前景感知数据集蒸馏方法，通过动态补丁选择提升信息保留

**关键词**：数据集蒸馏, 前景感知, 动态补丁选择, Grounded SAM2, 图像合成, 模型泛化

## 3 点简述
- 传统数据集蒸馏方法存在计算开销大、生成图像不真实、架构泛化性差等问题
- 利用Grounded SAM2识别前景对象，设计动态补丁选择策略，根据前景占比选择信息最丰富的补丁或调整全图
- 在多个基准测试中，该方法优于现有方法，提升了蒸馏性能、信息代表性和架构鲁棒性

## 摘要（原文）

> In this paper, we propose a foreground-aware dataset distillation method that enhances patch selection in a content-adaptive manner. With the rising computational cost of training large-scale deep models, dataset distillation has emerged as a promising approach for constructing compact synthetic datasets that retain the knowledge of their large original counterparts. However, traditional optimization-based methods often suffer from high computational overhead, memory constraints, and the generation of unrealistic, noise-like images with limited architectural generalization. Recent non-optimization methods alleviate some of these issues by constructing distilled data from real image patches, but the used rigid patch selection strategies can still discard critical information about the main objects. To solve this problem, we first leverage Grounded SAM2 to identify foreground objects and compute per-image foreground occupancy, from which we derive a category-wise patch decision threshold. Guided by these thresholds, we design a dynamic patch selection strategy that, for each image, either selects the most informative patch from multiple candidates or directly resizes the full image when the foreground dominates. This dual-path mechanism preserves more key information about the main objects while reducing redundant background content. Extensive experiments on multiple benchmarks show that the proposed method consistently improves distillation performance over existing approaches, producing more informative and representative distilled datasets and enhancing robustness across different architectures and image compositions.

