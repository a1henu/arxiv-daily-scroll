---
layout: default
title: Adaptive Weighted LSSVM for Multi-View Classification
---

# Adaptive Weighted LSSVM for Multi-View Classification
**arXiv**：[2512.02653v1](https://arxiv.org/abs/2512.02653) · [PDF](https://arxiv.org/pdf/2512.02653.pdf)  
**作者**：Farnaz Faramarzi Lighvan, Mehrdad Asadi, Lynn Houthuys  

**一句话要点**：提出自适应加权LS-SVM以促进多视图分类中的互补学习

**关键词**：多视图学习, LS-SVM, 互补学习, 核方法, 隐私保护

## 3 点简述
- 核心问题：现有核方法缺乏视图间显式协作，限制全局性能提升
- 方法要点：通过迭代全局耦合，使各视图关注其他视图的困难样本
- 实验或效果：在多数数据集上优于现有方法，适用于隐私保护场景

## 摘要（原文）

> Multi-view learning integrates diverse representations of the same instances to improve performance. Most existing kernel-based multi-view learning methods use fusion techniques without enforcing an explicit collaboration type across views or co-regularization which limits global collaboration. We propose AW-LSSVM, an adaptive weighted LS-SVM that promotes complementary learning by an iterative global coupling to make each view focus on hard samples of others from previous iterations. Experiments demonstrate that AW-LSSVM outperforms existing kernel-based multi-view methods on most datasets, while keeping raw features isolated, making it also suitable for privacy-preserving scenarios.

