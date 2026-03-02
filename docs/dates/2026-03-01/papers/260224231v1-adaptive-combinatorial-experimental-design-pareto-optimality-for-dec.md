---
layout: default
title: Adaptive Combinatorial Experimental Design: Pareto Optimality for Decision-Making and Inference
---

# Adaptive Combinatorial Experimental Design: Pareto Optimality for Decision-Making and Inference
**arXiv**：[2602.24231v1](https://arxiv.org/abs/2602.24231) · [PDF](https://arxiv.org/pdf/2602.24231.pdf)  
**作者**：Hongrui Xie, Junyu Cao, Kan Xu  

**一句话要点**：提出自适应组合实验设计框架，通过帕累托最优平衡组合多臂老虎机中的遗憾最小化与统计推断能力。

**关键词**：组合多臂老虎机, 自适应实验设计, 帕累托最优, 遗憾最小化, 统计推断, 反馈结构

## 3 点简述
- 核心问题：组合多臂老虎机中，最小化遗憾与准确推断奖励差距之间存在权衡。
- 方法要点：基于帕累托最优性，提出MixCombKL和MixCombUCB算法，分别适用于全臂和半臂反馈场景。
- 实验或效果：理论证明算法帕累托最优，提供有限时间遗憾和估计误差保证，丰富反馈能提升帕累托前沿。

## 摘要（原文）

> In this paper, we provide the first investigation into adaptive combinatorial experimental design, focusing on the trade-off between regret minimization and statistical power in combinatorial multi-armed bandits (CMAB). While minimizing regret requires repeated exploitation of high-reward arms, accurate inference on reward gaps requires sufficient exploration of suboptimal actions. We formalize this trade-off through the concept of Pareto optimality and establish equivalent conditions for Pareto-efficient learning in CMAB. We consider two relevant cases under different information structures, i.e., full-bandit feedback and semi-bandit feedback, and propose two algorithms MixCombKL and MixCombUCB respectively for these two cases. We provide theoretical guarantees showing that both algorithms are Pareto optimal, achieving finite-time guarantees on both regret and estimation error of arm gaps. Our results further reveal that richer feedback significantly tightens the attainable Pareto frontier, with the primary gains arising from improved estimation accuracy under our proposed methods. Taken together, these findings establish a principled framework for adaptive combinatorial experimentation in multi-objective decision-making.

