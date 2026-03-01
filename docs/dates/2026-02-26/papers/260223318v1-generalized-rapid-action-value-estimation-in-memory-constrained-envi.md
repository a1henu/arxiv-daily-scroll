---
layout: default
title: Generalized Rapid Action Value Estimation in Memory-Constrained Environments
---

# Generalized Rapid Action Value Estimation in Memory-Constrained Environments
**arXiv**：[2602.23318v1](https://arxiv.org/abs/2602.23318) · [PDF](https://arxiv.org/pdf/2602.23318.pdf)  
**作者**：Aloïs Rautureau, Tristan Cazenave, Éric Piette  

**一句话要点**：提出GRAVE2、GRAVER和GRAVER2算法，通过两级搜索和节点回收解决GRAVE在内存受限环境中的存储问题。

**关键词**：蒙特卡洛树搜索, 通用游戏博弈, 内存优化, 节点回收, 两级搜索

## 3 点简述
- 核心问题：GRAVE算法在通用游戏博弈中因存储额外统计信息导致内存占用高，限制实际应用。
- 方法要点：引入两级搜索和节点回收技术，分别或组合应用于GRAVE2、GRAVER和GRAVER2算法。
- 实验或效果：这些扩展显著减少存储节点数量，同时保持与GRAVE相当的博弈强度。

## 摘要（原文）

> Generalized Rapid Action Value Estimation (GRAVE) has been shown to be a strong variant within the Monte-Carlo Tree Search (MCTS) family of algorithms for General Game Playing (GGP). However, its reliance on storing additional win/visit statistics at each node makes its use impractical in memory-constrained environments, thereby limiting its applicability in practice. In this paper, we introduce the GRAVE2, GRAVER and GRAVER2 algorithms, which extend GRAVE through two-level search, node recycling, and a combination of both techniques, respectively. We show that these enhancements enable a drastic reduction in the number of stored nodes while matching the playing strength of GRAVE.

