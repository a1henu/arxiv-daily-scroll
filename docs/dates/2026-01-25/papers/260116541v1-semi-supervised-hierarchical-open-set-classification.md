---
layout: default
title: Semi-Supervised Hierarchical Open-Set Classification
---

# Semi-Supervised Hierarchical Open-Set Classification
**arXiv**：[2601.16541v1](https://arxiv.org/abs/2601.16541) · [PDF](https://arxiv.org/pdf/2601.16541.pdf)  
**作者**：Erik Wallin, Fredrik Kahl, Lars Hammarstrand  

**一句话要点**：提出基于伪标签的师生框架，以解决半监督分层开放集分类问题。

**关键词**：分层开放集分类, 半监督学习, 伪标签, 师生框架, 未知类处理

## 3 点简述
- 核心问题：在类层次结构中处理未知类，并利用未标注数据提升性能。
- 方法要点：引入子树伪标签和年龄门控机制，增强伪标签可靠性。
- 实验或效果：在iNaturalist19基准上，仅每类20个标注样本即可匹配全监督性能。

## 摘要（原文）

> Hierarchical open-set classification handles previously unseen classes by assigning them to the most appropriate high-level category in a class taxonomy. We extend this paradigm to the semi-supervised setting, enabling the use of large-scale, uncurated datasets containing a mixture of known and unknown classes to improve the hierarchical open-set performance. To this end, we propose a teacher-student framework based on pseudo-labeling. Two key components are introduced: 1) subtree pseudo-labels, which provide reliable supervision in the presence of unknown data, and 2) age-gating, a mechanism that mitigates overconfidence in pseudo-labels. Experiments show that our framework outperforms self-supervised pretraining followed by supervised adaptation, and even matches the fully supervised counterpart when using only 20 labeled samples per class on the iNaturalist19 benchmark. Our code is available at https://github.com/walline/semihoc.

