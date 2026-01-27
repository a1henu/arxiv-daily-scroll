---
layout: default
title: Learning Fair Domain Adaptation with Virtual Label Distribution
---

# Learning Fair Domain Adaptation with Virtual Label Distribution
**arXiv**：[2601.18171v1](https://arxiv.org/abs/2601.18171) · [PDF](https://arxiv.org/pdf/2601.18171.pdf)  
**作者**：Yuguang Zhang, Lijun Sheng, Jian Liang, Ran He  

**一句话要点**：提出虚拟标签分布感知学习以提升无监督域适应中的类别公平性

**关键词**：无监督域适应, 类别公平性, 自适应重加权, KL散度, 虚拟标签分布, 决策边界调整

## 3 点简述
- 核心问题：无监督域适应方法常忽视类别间性能差异，导致分类器偏向易分类别。
- 方法要点：采用自适应重加权策略增强难分类别影响，并引入KL散度重平衡策略调整决策边界。
- 实验或效果：作为即插即用模块集成到现有方法中，显著改善最差性能并保持高整体准确率。

## 摘要（原文）

> Unsupervised Domain Adaptation (UDA) aims to mitigate performance degradation when training and testing data are sampled from different distributions. While significant progress has been made in enhancing overall accuracy, most existing methods overlook performance disparities across categories-an issue we refer to as category fairness. Our empirical analysis reveals that UDA classifiers tend to favor certain easy categories while neglecting difficult ones. To address this, we propose Virtual Label-distribution-aware Learning (VILL), a simple yet effective framework designed to improve worst-case performance while preserving high overall accuracy. The core of VILL is an adaptive re-weighting strategy that amplifies the influence of hard-to-classify categories. Furthermore, we introduce a KL-divergence-based re-balancing strategy, which explicitly adjusts decision boundaries to enhance category fairness. Experiments on commonly used datasets demonstrate that VILL can be seamlessly integrated as a plug-and-play module into existing UDA methods, significantly improving category fairness.

