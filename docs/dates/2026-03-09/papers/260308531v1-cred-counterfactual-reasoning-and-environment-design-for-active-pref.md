---
layout: default
title: CRED: Counterfactual Reasoning and Environment Design for Active Preference Learning
---

# CRED: Counterfactual Reasoning and Environment Design for Active Preference Learning
**arXiv**：[2603.08531v1](https://arxiv.org/abs/2603.08531) · [PDF](https://arxiv.org/pdf/2603.08531.pdf)  
**作者**：Yi-Shiuan Tung, Gyanig Kumar, Wei Jiang, Bradley Hayes, Alessandro Roncone  

**一句话要点**：提出CRED方法，通过环境设计与反事实推理优化主动偏好学习中的轨迹生成

**关键词**：主动偏好学习, 轨迹生成, 环境设计, 反事实推理, 奖励函数学习

## 3 点简述
- 核心问题：现有主动偏好学习方法因轨迹多样性受限，难以高效学习人类奖励函数
- 方法要点：联合优化环境设计与轨迹选择，利用反事实推理生成揭示奖励差异的轨迹对
- 实验或效果：在奖励准确性和样本效率上显著优于现有方法，用户评分更高

## 摘要（原文）

> As a robot's operational environment and tasks to perform within it grow in complexity, the explicit specification and balancing of optimization objectives to achieve a preferred behavior profile moves increasingly farther out of reach. These systems benefit strongly by being able to align their behavior to reflect human preferences and respond to corrections, but manually encoding this feedback is infeasible. Active preference learning (APL) learns human reward functions by presenting trajectories for ranking. However, existing methods sample from fixed trajectory sets or replay buffers that limit query diversity and often fail to identify informative comparisons. We propose CRED, a novel trajectory generation method for APL that improves reward inference by jointly optimizing environment design and trajectory selection to efficiently query and extract preferences from users. CRED "imagines" new scenarios through environment design and leverages counterfactual reasoning -- by sampling possible rewards from its current belief and asking "What if this were the true preference?" -- to generate trajectory pairs that expose differences between competing reward functions. Comprehensive experiments and a user study show that CRED significantly outperforms state-of-the-art methods in reward accuracy and sample efficiency and receives higher user ratings.

