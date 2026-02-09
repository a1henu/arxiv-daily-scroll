---
layout: default
title: Progress Constraints for Reinforcement Learning in Behavior Trees
---

# Progress Constraints for Reinforcement Learning in Behavior Trees
**arXiv**：[2602.06525v1](https://arxiv.org/abs/2602.06525) · [PDF](https://arxiv.org/pdf/2602.06525.pdf)  
**作者**：Finn Rietz, Mart Kartašev, Johannes A. Stork, Petter Ögren  

**一句话要点**：提出进度约束机制以解决行为树与强化学习集成中的控制器冲突问题

**关键词**：行为树, 强化学习, 进度约束, 控制器集成, 样本效率, 安全探索

## 3 点简述
- 核心问题：行为树与强化学习直接集成可能导致控制器相互抵消，降低整体性能
- 方法要点：基于理论收敛结果，使用可行性估计器约束动作集，防止子目标被破坏
- 实验或效果：在概念验证和高保真仓库环境中，相比现有方法，提升了性能、样本效率和约束满足度

## 摘要（原文）

> Behavior Trees (BTs) provide a structured and reactive framework for decision-making, commonly used to switch between sub-controllers based on environmental conditions. Reinforcement Learning (RL), on the other hand, can learn near-optimal controllers but sometimes struggles with sparse rewards, safe exploration, and long-horizon credit assignment. Combining BTs with RL has the potential for mutual benefit: a BT design encodes structured domain knowledge that can simplify RL training, while RL enables automatic learning of the controllers within BTs. However, naive integration of BTs and RL can lead to some controllers counteracting other controllers, possibly undoing previously achieved subgoals, thereby degrading the overall performance. To address this, we propose progress constraints, a novel mechanism where feasibility estimators constrain the allowed action set based on theoretical BT convergence results. Empirical evaluations in a 2D proof-of-concept and a high-fidelity warehouse environment demonstrate improved performance, sample efficiency, and constraint satisfaction, compared to prior methods of BT-RL integration.

