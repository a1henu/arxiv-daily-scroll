---
layout: default
title: Structure-Aware Prototype Guided Trusted Multi-View Classification
---

# Structure-Aware Prototype Guided Trusted Multi-View Classification
**arXiv**：[2511.21021v1](https://arxiv.org/abs/2511.21021) · [PDF](https://arxiv.org/pdf/2511.21021.pdf)  
**作者**：Haojian Huang, Jiahao Shi, Zhe Liu, Harold Haodong Chen, Han Fang, Hao Sun, Zhongjiang He  

**一句话要点**：提出结构感知原型引导的可信多视图分类框架，以解决多源信息异构和冲突问题。

**关键词**：可信多视图分类, 结构感知原型, 视图一致性, 邻居关系建模, 多源信息融合

## 3 点简述
- 核心问题：现有方法依赖全局密集邻居关系，计算成本高且无法保证视图间一致性。
- 方法要点：引入原型表示视图邻居结构，简化学习并动态对齐视图内和视图间结构。
- 实验或效果：在多个公共数据集上验证，实现竞争性下游性能和鲁棒性。

## 摘要（原文）

> Trustworthy multi-view classification (TMVC) addresses the challenge of achieving reliable decision-making in complex scenarios where multi-source information is heterogeneous, inconsistent, or even conflicting. Existing TMVC approaches predominantly rely on globally dense neighbor relationships to model intra-view dependencies, leading to high computational costs and an inability to directly ensure consistency across inter-view relationships. Furthermore, these methods typically aggregate evidence from different views through manually assigned weights, lacking guarantees that the learned multi-view neighbor structures are consistent within the class space, thus undermining the trustworthiness of classification outcomes. To overcome these limitations, we propose a novel TMVC framework that introduces prototypes to represent the neighbor structures of each view. By simplifying the learning of intra-view neighbor relations and enabling dynamic alignment of intra- and inter-view structure, our approach facilitates more efficient and consistent discovery of cross-view consensus. Extensive experiments on multiple public multi-view datasets demonstrate that our method achieves competitive downstream performance and robustness compared to prevalent TMVC methods.

