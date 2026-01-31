---
layout: default
title: Routing the Lottery: Adaptive Subnetworks for Heterogeneous Data
---

# Routing the Lottery: Adaptive Subnetworks for Heterogeneous Data
**arXiv**：[2601.22141v1](https://arxiv.org/abs/2601.22141) · [PDF](https://arxiv.org/pdf/2601.22141.pdf)  
**作者**：Grzegorz Stefanski, Alberto Presta, Michal Byra  

**一句话要点**：提出自适应剪枝框架RTL，通过发现多个专用子网络以应对数据异质性。

**关键词**：自适应剪枝, 彩票假设, 数据异质性, 子网络相似性, 模块化深度学习

## 3 点简述
- 核心问题：现有剪枝方法假设单一通用子网络，忽略真实数据的异质性。
- 方法要点：RTL框架发现多个自适应子网络，每个针对特定类别、语义簇或环境条件。
- 实验或效果：在多样数据集上，RTL在平衡准确率和召回率上优于基线，参数减少达10倍。

## 摘要（原文）

> In pruning, the Lottery Ticket Hypothesis posits that large networks contain sparse subnetworks, or winning tickets, that can be trained in isolation to match the performance of their dense counterparts. However, most existing approaches assume a single universal winning ticket shared across all inputs, ignoring the inherent heterogeneity of real-world data. In this work, we propose Routing the Lottery (RTL), an adaptive pruning framework that discovers multiple specialized subnetworks, called adaptive tickets, each tailored to a class, semantic cluster, or environmental condition. Across diverse datasets and tasks, RTL consistently outperforms single- and multi-model baselines in balanced accuracy and recall, while using up to 10 times fewer parameters than independent models and exhibiting semantically aligned. Furthermore, we identify subnetwork collapse, a performance drop under aggressive pruning, and introduce a subnetwork similarity score that enables label-free diagnosis of oversparsification. Overall, our results recast pruning as a mechanism for aligning model structure with data heterogeneity, paving the way toward more modular and context-aware deep learning.

