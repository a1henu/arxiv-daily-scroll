---
layout: default
title: Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning
---

# Spark: Strategic Policy-Aware Exploration via Dynamic Branching for Long-Horizon Agentic Learning
**arXiv**：[2601.20209v1](https://arxiv.org/abs/2601.20209) · [PDF](https://arxiv.org/pdf/2601.20209.pdf)  
**作者**：Jinyang Wu, Shuo Yang, Changpeng Yang, Yuhao Shen, Shuai Zhang, Zhengqi Wen, Jianhua Tao  

**一句话要点**：提出Spark框架，通过关键状态动态分支实现资源高效探索，以解决长视野智能体学习中的样本稀缺问题。

**关键词**：强化学习, 长视野任务, 资源高效探索, 动态分支, 智能体泛化, 关键状态决策

## 3 点简述
- 核心问题：长视野任务中高质量轨迹稀缺，现有方法资源分配不均，导致计算浪费和样本质量不足。
- 方法要点：在关键决策点自适应分支探索，优先采样质量，减少对人工先验的依赖，实现自主扩展。
- 实验或效果：在具身规划等任务中，以更少样本获得更高成功率，并在未见场景中展现强泛化能力。

## 摘要（原文）

> Reinforcement learning has empowered large language models to act as intelligent agents, yet training them for long-horizon tasks remains challenging due to the scarcity of high-quality trajectories, especially under limited resources. Existing methods typically scale up rollout sizes and indiscriminately allocate computational resources among intermediate steps. Such attempts inherently waste substantial computation budget on trivial steps while failing to guarantee sample quality. To address this, we propose \textbf{Spark} (\textbf{S}trategic \textbf{P}olicy-\textbf{A}ware explo\textbf{R}ation via \textbf{K}ey-state dynamic branching), a novel framework that selectively branches at critical decision states for resource-efficient exploration. Our key insight is to activate adaptive branching exploration at critical decision points to probe promising trajectories, thereby achieving precise resource allocation that prioritizes sampling quality over blind coverage. This design leverages the agent's intrinsic decision-making signals to reduce dependence on human priors, enabling the agent to autonomously expand exploration and achieve stronger generalization. Experiments across diverse tasks (e.g., embodied planning), demonstrate that \textsc{Spark} achieves superior success rates with significantly fewer training samples, exhibiting robust generalization even in unseen scenarios.

