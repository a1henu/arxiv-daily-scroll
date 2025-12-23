---
layout: default
title: Clustering-based Transfer Learning for Dynamic Multimodal MultiObjective Evolutionary Algorithm
---

# Clustering-based Transfer Learning for Dynamic Multimodal MultiObjective Evolutionary Algorithm
**arXiv**：[2512.18947v1](https://arxiv.org/abs/2512.18947) · [PDF](https://arxiv.org/pdf/2512.18947.pdf)  
**作者**：Li Yan, Bolun Liu, Chao Li, Jing Liang, Kunjie Yu, Caitong Yue, Xuzhao Chai, Boyang Qu  

**一句话要点**：提出基于聚类的自动编码器预测动态响应机制，以解决动态多模态多目标优化中的多样性与收敛平衡问题。

**关键词**：动态多目标优化, 多模态优化, 聚类学习, 自动编码器, 进化算法, 种群多样性

## 3 点简述
- 核心问题：动态多模态多目标优化需同时追踪多个等效帕累托最优集并在时变环境中保持种群多样性。
- 方法要点：利用自动编码器处理匹配聚类生成高多样性初始种群，并集成自适应小生境策略以平衡收敛与多样性。
- 实验或效果：在12个动态多模态多目标测试函数实例上，算法在决策空间保持多样性更有效，在目标空间实现更优收敛。

## 摘要（原文）

> Dynamic multimodal multiobjective optimization presents the dual challenge of simultaneously tracking multiple equivalent pareto optimal sets and maintaining population diversity in time-varying environments. However, existing dynamic multiobjective evolutionary algorithms often neglect solution modality, whereas static multimodal multiobjective evolutionary algorithms lack adaptability to dynamic changes. To address above challenge, this paper makes two primary contributions. First, we introduce a new benchmark suite of dynamic multimodal multiobjective test functions constructed by fusing the properties of both dynamic and multimodal optimization to establish a rigorous evaluation platform. Second, we propose a novel algorithm centered on a Clustering-based Autoencoder prediction dynamic response mechanism, which utilizes an autoencoder model to process matched clusters to generate a highly diverse initial population. Furthermore, to balance the algorithm's convergence and diversity, we integrate an adaptive niching strategy into the static optimizer. Empirical analysis on 12 instances of dynamic multimodal multiobjective test functions reveals that, compared with several state-of-the-art dynamic multiobjective evolutionary algorithms and multimodal multiobjective evolutionary algorithms, our algorithm not only preserves population diversity more effectively in the decision space but also achieves superior convergence in the objective space.

