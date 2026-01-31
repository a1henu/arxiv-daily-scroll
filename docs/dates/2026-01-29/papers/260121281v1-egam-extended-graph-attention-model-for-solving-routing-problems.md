---
layout: default
title: EGAM: Extended Graph Attention Model for Solving Routing Problems
---

# EGAM: Extended Graph Attention Model for Solving Routing Problems
**arXiv**：[2601.21281v1](https://arxiv.org/abs/2601.21281) · [PDF](https://arxiv.org/pdf/2601.21281.pdf)  
**作者**：Licheng Wang, Yuzi Yan, Mingtao Huang, Yuan Shen  

**一句话要点**：提出扩展图注意力模型以解决路由优化问题

**关键词**：神经组合优化, 图注意力模型, 路由问题, 强化学习, 多头注意力

## 3 点简述
- 针对神经组合优化中图注意力模型仅考虑节点特征的局限性
- 采用多头点积注意力更新节点和边嵌入，增强模型表达能力
- 实验表明在多种路由问题上匹配或超越现有方法，尤其擅长高约束问题

## 摘要（原文）

> Neural combinatorial optimization (NCO) solvers, implemented with graph neural networks (GNNs), have introduced new approaches for solving routing problems. Trained with reinforcement learning (RL), the state-of-the-art graph attention model (GAM) achieves near-optimal solutions without requiring expert knowledge or labeled data. In this work, we generalize the existing graph attention mechanism and propose the extended graph attention model (EGAM). Our model utilizes multi-head dot-product attention to update both node and edge embeddings, addressing the limitations of the conventional GAM, which considers only node features. We employ an autoregressive encoder-decoder architecture and train it with policy gradient algorithms that incorporate a specially designed baseline. Experiments show that EGAM matches or outperforms existing methods across various routing problems. Notably, the proposed model demonstrates exceptional performance on highly constrained problems, highlighting its efficiency in handling complex graph structures.

