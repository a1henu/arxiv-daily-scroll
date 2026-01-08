---
layout: default
title: ReLA: Representation Learning and Aggregation for Job Scheduling with Reinforcement Learning
---

# ReLA: Representation Learning and Aggregation for Job Scheduling with Reinforcement Learning
**arXiv**：[2601.03646v1](https://arxiv.org/abs/2601.03646) · [PDF](https://arxiv.org/pdf/2601.03646.pdf)  
**作者**：Zhengyi Kwan, Zhang Wei, Aik Beng Ng, Zhengkui Wang, Simon See  

**一句话要点**：提出ReLA强化学习调度器，通过表示学习与聚合优化制造系统中的作业调度问题。

**关键词**：作业调度, 强化学习, 表示学习, 注意力机制, 多尺度架构, 最优性差距

## 3 点简述
- 核心问题：现有作业调度方法在问题规模增大时存在运行时间长或调度质量不足的局限。
- 方法要点：基于自注意力、卷积和交叉注意力的多尺度表示学习模块，聚合实体表示以支持强化学习决策。
- 实验或效果：在中小型和大规模实例上，ReLA显著降低最优性差距，分别达13.0%和78.6%，平均差距降至7.3%和2.1%。

## 摘要（原文）

> Job scheduling is widely used in real-world manufacturing systems to assign ordered job operations to machines under various constraints. Existing solutions remain limited by long running time or insufficient schedule quality, especially when problem scale increases. In this paper, we propose ReLA, a reinforcement-learning (RL) scheduler built on structured representation learning and aggregation. ReLA first learns diverse representations from scheduling entities, including job operations and machines, using two intra-entity learning modules with self-attention and convolution and one inter-entity learning module with cross-attention. These modules are applied in a multi-scale architecture, and their outputs are aggregated to support RL decision-making. Across experiments on small, medium, and large job instances, ReLA achieves the best makespan in most tested settings over the latest solutions. On non-large instances, ReLA reduces the optimality gap of the SOTA baseline by 13.0%, while on large-scale instances it reduces the gap by 78.6%, with the average optimality gaps lowered to 7.3% and 2.1%, respectively. These results confirm that ReLA's learned representations and aggregation provide strong decision support for RL scheduling, and enable fast job completion and decision-making for real-world applications.

