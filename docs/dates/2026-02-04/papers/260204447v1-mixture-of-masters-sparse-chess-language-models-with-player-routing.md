---
layout: default
title: Mixture of Masters: Sparse Chess Language Models with Player Routing
---

# Mixture of Masters: Sparse Chess Language Models with Player Routing
**arXiv**：[2602.04447v1](https://arxiv.org/abs/2602.04447) · [PDF](https://arxiv.org/pdf/2602.04447.pdf)  
**作者**：Giacomo Frisoni, Lorenzo Molfetta, Davide Freddi, Gianluca Moro  

**一句话要点**：提出稀疏专家混合模型以解决国际象棋语言模型风格同质化问题

**关键词**：稀疏专家混合模型, 国际象棋语言模型, 风格动态切换, 门控网络, 强化学习

## 3 点简述
- 核心问题：密集国际象棋语言模型易导致风格平均化，抑制罕见有效策略。
- 方法要点：采用混合专家架构，每个专家模拟顶尖棋手风格，通过门控网络动态选择。
- 实验或效果：在未见标准对局中优于密集模型和基线，提升生成多样性和可控性。

## 摘要（原文）

> Modern chess language models are dense transformers trained on millions of games played by thousands of high-rated individuals. However, these monolithic networks tend to collapse into mode-averaged behavior, where stylistic boundaries are blurred, and rare but effective strategies are suppressed. To counteract homogenization, we introduce Mixture-of-Masters (MoM), the first chess mixture-of-experts model with small-sized GPT experts emulating world-class grandmasters. Each expert is trained with a combination of self-supervised learning and reinforcement learning guided by chess-specific rewards. For each move, a post-hoc learnable gating network selects the most appropriate persona to channel depending on the game state, allowing MoM to switch its style dynamically$--$e.g., Tal's offensive vocation or Petrosian's defensive solidity. When evaluated against Stockfish on unseen standard games, MoM outperforms both dense individual expert networks and popular GPT baselines trained on aggregated data, while ensuring generation variety, control, and interpretability.

