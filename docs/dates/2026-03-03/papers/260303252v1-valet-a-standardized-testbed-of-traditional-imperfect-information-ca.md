---
layout: default
title: Valet: A Standardized Testbed of Traditional Imperfect-Information Card Games
---

# Valet: A Standardized Testbed of Traditional Imperfect-Information Card Games
**arXiv**：[2603.03252v1](https://arxiv.org/abs/2603.03252) · [PDF](https://arxiv.org/pdf/2603.03252.pdf)  
**作者**：Mark Goadrich, Achille Morenville, Éric Piette  

**一句话要点**：提出Valet测试床以标准化非完美信息纸牌游戏算法评估

**关键词**：非完美信息游戏, 纸牌游戏测试床, 算法评估标准化, RECYCLE描述语言, 蒙特卡洛树搜索基准

## 3 点简述
- 核心问题：现有AI算法评估依赖单一游戏性能，缺乏跨游戏鲁棒性比较。
- 方法要点：构建包含21款传统纸牌游戏的多样化测试床，使用RECYCLE语言标准化规则编码。
- 实验或效果：通过随机模拟分析游戏分支因子和时长，提供MCTS玩家基线分数分布验证适用性。

## 摘要（原文）

> AI algorithms for imperfect-information games are typically compared using performance metrics on individual games, making it difficult to assess robustness across game choices. Card games are a natural domain for imperfect information due to hidden hands and stochastic draws. To facilitate comparative research on imperfect-information game-playing algorithms and game systems, we introduce Valet, a diverse and comprehensive testbed of 21 traditional imperfect-information card games. These games span multiple genres, cultures, player counts, deck structures, mechanics, winning conditions, and methods of hiding and revealing information. To standardize implementations across systems, we encode the rules of each game in RECYCLE, a card game description language. We empirically characterize each game's branching factor and duration using random simulations, reporting baseline score distributions for a Monte Carlo Tree Search player against random opponents to demonstrate the suitability of Valet as a benchmarking suite.

