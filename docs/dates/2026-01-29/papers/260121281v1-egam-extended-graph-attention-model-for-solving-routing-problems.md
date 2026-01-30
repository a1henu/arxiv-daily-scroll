---
layout: default
title: EGAM: Extended Graph Attention Model for Solving Routing Problems
---

# EGAM: Extended Graph Attention Model for Solving Routing Problems
**arXiv**：[2601.21281v1](https://arxiv.org/abs/2601.21281) · [PDF](https://arxiv.org/pdf/2601.21281.pdf)  
**作者**：Licheng Wang, Yuzi Yan, Mingtao Huang, Yuan Shen  

**一句话要点**：提出扩展图注意力模型以解决路由问题，通过多头部点积注意力更新节点和边嵌入。

**关键词**：神经组合优化, 图注意力机制, 路由问题, 强化学习, 自回归模型

## 3 点简述
- 核心问题：传统图注意力模型仅考虑节点特征，在路由问题中处理复杂图结构受限。
- 方法要点：采用多头部点积注意力机制，在自回归编码器-解码器架构中更新节点和边嵌入。
- 实验或效果：在多种路由问题上匹配或超越现有方法，尤其在高度约束问题上表现优异。

## 摘要（原文）

> Neural combinatorial optimization (NCO) solvers, implemented with graph neural networks (GNNs), have introduced new approaches for solving routing problems. Trained with reinforcement learning (RL), the state-of-the-art graph attention model (GAM) achieves near-optimal solutions without requiring expert knowledge or labeled data. In this work, we generalize the existing graph attention mechanism and propose the extended graph attention model (EGAM). Our model utilizes multi-head dot-product attention to update both node and edge embeddings, addressing the limitations of the conventional GAM, which considers only node features. We employ an autoregressive encoder-decoder architecture and train it with policy gradient algorithms that incorporate a specially designed baseline. Experiments show that EGAM matches or outperforms existing methods across various routing problems. Notably, the proposed model demonstrates exceptional performance on highly constrained problems, highlighting its efficiency in handling complex graph structures.

