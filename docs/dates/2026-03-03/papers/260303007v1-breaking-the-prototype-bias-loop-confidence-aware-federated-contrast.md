---
layout: default
title: Breaking the Prototype Bias Loop: Confidence-Aware Federated Contrastive Learning for Highly Imbalanced Clients
---

# Breaking the Prototype Bias Loop: Confidence-Aware Federated Contrastive Learning for Highly Imbalanced Clients
**arXiv**：[2603.03007v1](https://arxiv.org/abs/2603.03007) · [PDF](https://arxiv.org/pdf/2603.03007.pdf)  
**作者**：Tian-Shuang Wu, Shen-Huan Lyu, Ning Chen, Yi-Xiao He, Bing Tang, Baoliu Ye, Qingfu Zhang  

**一句话要点**：提出置信感知联邦对比学习以解决客户端高度不平衡下的原型偏差循环问题

**关键词**：联邦学习, 对比学习, 类不平衡, 原型偏差, 置信感知聚合, 数据异质性

## 3 点简述
- 核心问题：本地类不平衡和数据异质性导致原型偏差循环，影响联邦对比学习性能。
- 方法要点：采用置信感知聚合机制，结合生成增强和几何一致性正则化，稳定类间结构。
- 实验或效果：在多种不平衡和异质性场景下，CAFedCL在准确性和客户端公平性上优于基线方法。

## 摘要（原文）

> Local class imbalance and data heterogeneity across clients often trap prototype-based federated contrastive learning in a prototype bias loop: biased local prototypes induced by imbalanced data are aggregated into biased global prototypes, which are repeatedly reused as contrastive anchors, accumulating errors across communication rounds. To break this loop, we propose Confidence-Aware Federated Contrastive Learning (CAFedCL), a novel framework that improves the prototype aggregation mechanism and strengthens the contrastive alignment guided by prototypes. CAFedCL employs a confidence-aware aggregation mechanism that leverages predictive uncertainty to downweight high-variance local prototypes. In addition, generative augmentation for minority classes and geometric consistency regularization are integrated to stabilize the structure between classes. From a theoretical perspective, we provide an expectation-based analysis showing that our aggregation reduces estimation variance, thereby bounding global prototype drift and ensuring convergence. Extensive experiments under varying levels of class imbalance and data heterogeneity demonstrate that CAFedCL consistently outperforms representative federated baselines in both accuracy and client fairness.

