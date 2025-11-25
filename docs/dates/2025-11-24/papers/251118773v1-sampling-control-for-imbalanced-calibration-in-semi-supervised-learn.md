---
layout: default
title: Sampling Control for Imbalanced Calibration in Semi-Supervised Learning
---

# Sampling Control for Imbalanced Calibration in Semi-Supervised Learning
**arXiv**：[2511.18773v1](https://arxiv.org/abs/2511.18773) · [PDF](https://arxiv.org/pdf/2511.18773.pdf)  
**作者**：Senmao Tian, Xiang Wei, Shunli Zhang  

**一句话要点**：提出SC-SSL框架，通过解耦采样控制解决半监督学习中的类别不平衡问题

**关键词**：半监督学习, 类别不平衡, 采样控制, 模型校准, 分布不匹配

## 3 点简述
- 核心问题：类别不平衡与分布不匹配导致半监督学习分类偏差，现有方法处理粗糙
- 方法要点：引入解耦采样控制，自适应调整采样概率，并应用优化偏置向量校准logits
- 实验或效果：在多个基准数据集上验证一致性和先进性能

## 摘要（原文）

> Class imbalance remains a critical challenge in semi-supervised learning (SSL), especially when distributional mismatches between labeled and unlabeled data lead to biased classification. Although existing methods address this issue by adjusting logits based on the estimated class distribution of unlabeled data, they often handle model imbalance in a coarse-grained manner, conflating data imbalance with bias arising from varying class-specific learning difficulties. To address this issue, we propose a unified framework, SC-SSL, which suppresses model bias through decoupled sampling control. During training, we identify the key variables for sampling control under ideal conditions. By introducing a classifier with explicit expansion capability and adaptively adjusting sampling probabilities across different data distributions, SC-SSL mitigates feature-level imbalance for minority classes. In the inference phase, we further analyze the weight imbalance of the linear classifier and apply post-hoc sampling control with an optimization bias vector to directly calibrate the logits. Extensive experiments across various benchmark datasets and distribution settings validate the consistency and state-of-the-art performance of SC-SSL.

