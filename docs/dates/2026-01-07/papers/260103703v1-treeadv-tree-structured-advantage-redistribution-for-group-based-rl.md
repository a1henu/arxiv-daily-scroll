---
layout: default
title: TreeAdv: Tree-Structured Advantage Redistribution for Group-Based RL
---

# TreeAdv: Tree-Structured Advantage Redistribution for Group-Based RL
**arXiv**：[2601.03703v1](https://arxiv.org/abs/2601.03703) · [PDF](https://arxiv.org/pdf/2601.03703.pdf)  
**作者**：Lang Cao, Hui Ruan, Yongqian Li, Peng Chao, Wu Ning, Haonan Song, Renhong Chen, Yitong Li  

**一句话要点**：提出TreeAdv以解决基于组的强化学习中样本效率低和长度偏差问题

**关键词**：强化学习, 树结构优势重分配, 基于组的策略优化, 数学推理, 样本效率, 熵驱动采样

## 3 点简述
- 标准GRPO将轨迹视为独立序列，导致样本效率低和冗长偏差
- TreeAdv基于熵驱动采样构建树结构，在不确定性决策处分枝并共享低不确定性标记
- 在10个数学推理基准上，TreeAdv优于GRPO和GSPO，且生成标记更少

## 摘要（原文）

> Reinforcement learning with group-based objectives, such as Group Relative Policy Optimization (GRPO), is a common framework for aligning large language models on complex reasoning tasks. However, standard GRPO treats each rollout trajectory as an independent flat sequence and assigns a single sequence-level advantage to all tokens, which leads to sample inefficiency and a length bias toward verbose, redundant chains of thought without improving logical depth. We introduce TreeAdv (Tree-Structured Advantage Redistribution for Group-Based RL), which makes the tree structure of group rollouts explicit for both exploration and advantage assignment. Specifically, TreeAdv builds a group of trees (a forest) based on an entropy-driven sampling method where each tree branches at high-uncertainty decisions while sharing low-uncertainty tokens across rollouts. Then, TreeAdv aggregates token-level advantages for internal tree segments by redistributing the advantages of complete rollouts (all leaf nodes), and TreeAdv can easily apply to group-based objectives such as GRPO or GSPO. Across 10 math reasoning benchmarks, TreeAdv consistently outperforms GRPO and GSPO, while using substantially fewer generated tokens under identical supervision, data, and decoding budgets.

