---
layout: default
title: Regret-Guided Search Control for Efficient Learning in AlphaZero
---

# Regret-Guided Search Control for Efficient Learning in AlphaZero
**arXiv**：[2602.20809v1](https://arxiv.org/abs/2602.20809) · [PDF](https://arxiv.org/pdf/2602.20809.pdf)  
**作者**：Yun-Jui Tsai, Wei-Yu Chen, Yan-Ru Ju, Yu-Hung Chang, Ti-Rong Wu  

**一句话要点**：提出后悔引导搜索控制以提升AlphaZero学习效率

**关键词**：强化学习, AlphaZero, 搜索控制, 后悔网络, 自对弈, 棋盘游戏

## 3 点简述
- 核心问题：强化学习代理学习效率低，需大量自对弈，而人类能从错误状态快速改进。
- 方法要点：引入后悔网络识别高后悔状态，优先重用这些状态作为新起点，而非均匀采样。
- 实验或效果：在多种棋盘游戏中超越AlphaZero和Go-Exploit，Elo提升显著，并提高对KataGo胜率。

## 摘要（原文）

> Reinforcement learning (RL) agents achieve remarkable performance but remain far less learning-efficient than humans. While RL agents require extensive self-play games to extract useful signals, humans often need only a few games, improving rapidly by repeatedly revisiting states where mistakes occurred. This idea, known as search control, aims to restart from valuable states rather than always from the initial state. In AlphaZero, prior work Go-Exploit applies this idea by sampling past states from self-play or search trees, but it treats all states equally, regardless of their learning potential. We propose Regret-Guided Search Control (RGSC), which extends AlphaZero with a regret network that learns to identify high-regret states, where the agent's evaluation diverges most from the actual outcome. These states are collected from both self-play trajectories and MCTS nodes, stored in a prioritized regret buffer, and reused as new starting positions. Across 9x9 Go, 10x10 Othello, and 11x11 Hex, RGSC outperforms AlphaZero and Go-Exploit by an average of 77 and 89 Elo, respectively. When training on a well-trained 9x9 Go model, RGSC further improves the win rate against KataGo from 69.3% to 78.2%, while both baselines show no improvement. These results demonstrate that RGSC provides an effective mechanism for search control, improving both efficiency and robustness of AlphaZero training. Our code is available at https://rlg.iis.sinica.edu.tw/papers/rgsc.

