---
layout: default
title: UrbanVerse: Learning Urban Region Representation Across Cities and Tasks
---

# UrbanVerse: Learning Urban Region Representation Across Cities and Tasks
**arXiv**：[2602.15750v1](https://arxiv.org/abs/2602.15750) · [PDF](https://arxiv.org/pdf/2602.15750.pdf)  
**作者**：Fengze Sun, Egemen Tanin, Shanika Karunasekera, Zuqing Li, Flora D. Salim, Jianzhong Qi  

**一句话要点**：提出UrbanVerse模型，通过跨城市区域表示学习和跨任务分析，提升城市分析泛化能力。

**关键词**：城市区域表示学习, 跨城市泛化, 跨任务分析, 图神经网络, 扩散模型, 城市分析

## 3 点简述
- 核心问题：现有城市区域表示学习方法在跨城市和跨任务泛化方面存在局限。
- 方法要点：基于图建模和随机游走学习区域序列，结合HCondDiffCT模块整合先验知识和任务语义。
- 实验或效果：在真实数据集上，跨城市设置下六个任务中优于现有方法，预测精度提升最高达35.89%。

## 摘要（原文）

> Recent advances in urban region representation learning have enabled a wide range of applications in urban analytics, yet existing methods remain limited in their capabilities to generalize across cities and analytic tasks. We aim to generalize urban representation learning beyond city- and task-specific settings, towards a foundation-style model for urban analytics. To this end, we propose UrbanVerse, a model for cross-city urban representation learning and cross-task urban analytics. For cross-city generalization, UrbanVerse focuses on features local to the target regions and structural features of the nearby regions rather than the entire city. We model regions as nodes on a graph, which enables a random walk-based procedure to form "sequences of regions" that reflect both local and neighborhood structural features for urban region representation learning. For cross-task generalization, we propose a cross-task learning module named HCondDiffCT. This module integrates region-conditioned prior knowledge and task-conditioned semantics into the diffusion process to jointly model multiple downstream urban prediction tasks. HCondDiffCT is generic. It can also be integrated with existing urban representation learning models to enhance their downstream task effectiveness. Experiments on real-world datasets show that UrbanVerse consistently outperforms state-of-the-art methods across six tasks under cross-city settings, achieving up to 35.89% improvements in prediction accuracy.

