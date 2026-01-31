---
layout: default
title: Cascaded Transfer: Learning Many Tasks under Budget Constraints
---

# Cascaded Transfer: Learning Many Tasks under Budget Constraints
**arXiv**：[2601.21513v1](https://arxiv.org/abs/2601.21513) · [PDF](https://arxiv.org/pdf/2601.21513.pdf)  
**作者**：Eloi Campagne, Yvenn Amara-Ouali, Yannig Goude, Mathilde Mougeot, Argyris Kalogeratos  

**一句话要点**：提出级联迁移学习以在预算约束下学习多个相关任务

**关键词**：多任务学习, 迁移学习, 预算约束, 级联结构, 最小生成树

## 3 点简述
- 核心问题：多任务学习中任务关系未知且需在预算限制下高效学习
- 方法要点：基于最小生成树组织任务级联，通过层次化参数传递分配训练预算
- 实验或效果：在合成和真实数据集上验证了方法在准确性和成本效益上的优势

## 摘要（原文）

> Many-Task Learning refers to the setting where a large number of related tasks need to be learned, the exact relationships between tasks are not known. We introduce the Cascaded Transfer Learning, a novel many-task transfer learning paradigm where information (e.g. model parameters) cascades hierarchically through tasks that are learned by individual models of the same class, while respecting given budget constraints. The cascade is organized as a rooted tree that specifies the order in which tasks are learned and refined. We design a cascaded transfer mechanism deployed over a minimum spanning tree structure that connects the tasks according to a suitable distance measure, and allocates the available training budget along its branches. Experiments on synthetic and real many-task settings show that the resulting method enables more accurate and cost effective adaptation across large task collections compared to alternative approaches.

