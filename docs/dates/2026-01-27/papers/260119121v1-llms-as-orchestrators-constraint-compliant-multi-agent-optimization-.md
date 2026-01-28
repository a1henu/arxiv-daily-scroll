---
layout: default
title: LLMs as Orchestrators: Constraint-Compliant Multi-Agent Optimization for Recommendation Systems
---

# LLMs as Orchestrators: Constraint-Compliant Multi-Agent Optimization for Recommendation Systems
**arXiv**：[2601.19121v1](https://arxiv.org/abs/2601.19121) · [PDF](https://arxiv.org/pdf/2601.19121.pdf)  
**作者**：Guilin Zhang, Kai Zhao, Jeffrey Friedman, Xu Chu  

**一句话要点**：提出DualAgent-Rec框架，利用LLM协调双代理优化，解决推荐系统中硬约束下的多目标优化问题。

**关键词**：推荐系统, 多目标优化, 硬约束, LLM协调, 双代理框架, 帕累托搜索

## 3 点简述
- 核心问题：现有推荐系统在硬约束（如公平性、覆盖率）下多目标优化易违反约束，LLM协调方法未充分探索。
- 方法要点：分离为利用代理（硬约束下优化准确性）和探索代理（无约束帕累托搜索提升多样性），LLM协调器自适应分配资源并保证可行性。
- 实验或效果：在Amazon Reviews 2023数据集上实现100%约束满足，帕累托超体积提升4-6%，保持准确性与多样性平衡。

## 摘要（原文）

> Recommendation systems must optimize multiple objectives while satisfying hard business constraints such as fairness and coverage. For example, an e-commerce platform may require every recommendation list to include items from multiple sellers and at least one newly listed product; violating such constraints--even once--is unacceptable in production. Prior work on multi-objective recommendation and recent LLM-based recommender agents largely treat constraints as soft penalties or focus on item scoring and interaction, leading to frequent violations in real-world deployments. How to leverage LLMs for coordinating constrained optimization in recommendation systems remains underexplored. We propose DualAgent-Rec, an LLM-coordinated dual-agent framework for constrained multi-objective e-commerce recommendation. The framework separates optimization into an Exploitation Agent that prioritizes accuracy under hard constraints and an Exploration Agent that promotes diversity through unconstrained Pareto search. An LLM-based coordinator adaptively allocates resources between agents based on optimization progress and constraint satisfaction, while an adaptive epsilon-relaxation mechanism guarantees feasibility of final solutions. Experiments on the Amazon Reviews 2023 dataset demonstrate that DualAgent-Rec achieves 100% constraint satisfaction and improves Pareto hypervolume by 4-6% over strong baselines, while maintaining competitive accuracy-diversity trade-offs. These results indicate that LLMs can act as effective orchestration agents for deployable and constraint-compliant recommendation systems.

