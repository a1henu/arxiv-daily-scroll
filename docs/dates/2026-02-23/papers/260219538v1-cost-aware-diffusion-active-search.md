---
layout: default
title: Cost-Aware Diffusion Active Search
---

# Cost-Aware Diffusion Active Search
**arXiv**：[2602.19538v1](https://arxiv.org/abs/2602.19538) · [PDF](https://arxiv.org/pdf/2602.19538.pdf)  
**作者**：Arundhati Banerjee, Jeff Schneider  

**一句话要点**：提出基于扩散模型的成本感知主动搜索算法，以平衡探索与利用，无需构建完整搜索树。

**关键词**：主动搜索, 扩散模型, 成本感知决策, 探索与利用平衡, 离线强化学习

## 3 点简述
- 核心问题：主动搜索中需平衡探索未知环境与利用先验观察，现有前瞻算法计算成本高。
- 方法要点：利用扩散模型采样前瞻动作序列，避免构建搜索树，并解决乐观偏差问题。
- 实验或效果：在离线强化学习中，算法在完全恢复率和计算效率上优于标准基线。

## 摘要（原文）

> Active search for recovering objects of interest through online, adaptive decision making with autonomous agents requires trading off exploration of unknown environments with exploitation of prior observations in the search space. Prior work has proposed information gain and Thompson sampling based myopic, greedy approaches for agents to actively decide query or search locations when the number of targets is unknown. Decision making algorithms in such partially observable environments have also shown that agents capable of lookahead over a finite horizon outperform myopic policies for active search. Unfortunately, lookahead algorithms typically rely on building a computationally expensive search tree that is simulated and updated based on the agent's observations and a model of the environment dynamics. Instead, in this work, we leverage the sequence modeling abilities of diffusion models to sample lookahead action sequences that balance the exploration-exploitation trade-off for active search without building an exhaustive search tree. We identify the optimism bias in prior diffusion based reinforcement learning approaches when applied to the active search setting and propose mitigating solutions for efficient cost-aware decision making with both single and multi-agent teams. Our proposed algorithm outperforms standard baselines in offline reinforcement learning in terms of full recovery rate and is computationally more efficient than tree search in cost-aware active decision making.

