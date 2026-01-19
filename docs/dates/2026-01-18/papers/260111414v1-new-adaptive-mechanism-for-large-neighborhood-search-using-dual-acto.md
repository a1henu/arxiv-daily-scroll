---
layout: default
title: New Adaptive Mechanism for Large Neighborhood Search using Dual Actor-Critic
---

# New Adaptive Mechanism for Large Neighborhood Search using Dual Actor-Critic
**arXiv**：[2601.11414v1](https://arxiv.org/abs/2601.11414) · [PDF](https://arxiv.org/pdf/2601.11414.pdf)  
**作者**：Shaohua Yu, Wenhao Mao, Zigao Wu, Jakob Puchinger  

**一句话要点**：提出基于双Actor-Critic的自适应大邻域搜索机制，以解决组合优化中算子交互忽略问题。

**关键词**：自适应大邻域搜索, 双Actor-Critic, 组合优化, 图神经网络, 马尔可夫决策过程

## 3 点简述
- 核心问题：经典ALNS自适应机制未考虑销毁与修复算子间的交互影响。
- 方法要点：引入双Actor-Critic模型，将算子选择建模为独立马尔可夫决策过程。
- 实验或效果：DAC-ALNS显著提升求解效率，并展示优秀的问题迁移能力。

## 摘要（原文）

> Adaptive Large Neighborhood Search (ALNS) is a widely used heuristic method for solving combinatorial optimization problems. ALNS explores the solution space by iteratively using destroy and repair operators with probabilities, which are adjusted by an adaptive mechanism to find optimal solutions. However, the classic ALNS adaptive mechanism does not consider the interaction between destroy and repair operators when selecting them. To overcome this limitation, this study proposes a novel adaptive mechanism. This mechanism enhances the adaptability of the algorithm through a Dual Actor-Critic (DAC) model, which fully considers the fact that the quality of new solutions is jointly determined by the destroy and repair operators. It effectively utilizes the interaction between these operators during the weight adjustment process, greatly improving the adaptability of the ALNS algorithm. In this mechanism, the destroy and repair processes are modeled as independent Markov Decision Processes to guide the selection of operators more accurately. Furthermore, we use Graph Neural Networks to extract key features from problem instances and perform effective aggregation and normalization to enhance the algorithm's transferability to different sizes and characteristics of problems. Through a series of experiments, we demonstrate that the proposed DAC-ALNS algorithm significantly improves solution efficiency and exhibits excellent transferability.

