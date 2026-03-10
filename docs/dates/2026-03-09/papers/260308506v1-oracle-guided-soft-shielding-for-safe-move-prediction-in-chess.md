---
layout: default
title: Oracle-Guided Soft Shielding for Safe Move Prediction in Chess
---

# Oracle-Guided Soft Shielding for Safe Move Prediction in Chess
**arXiv**：[2603.08506v1](https://arxiv.org/abs/2603.08506) · [PDF](https://arxiv.org/pdf/2603.08506.pdf)  
**作者**：Prajit T Rajendran, Fabio Arnez, Huascar Espinoza, Agnes Delaborde, Chokri Mraidha  

**一句话要点**：提出Oracle-Guided Soft Shielding框架，用于国际象棋中平衡性能与安全的走子预测。

**关键词**：安全决策, 模仿学习, 国际象棋AI, 失误预测, 软屏蔽

## 3 点简述
- 核心问题：模仿学习在分布偏移下脆弱，强化学习收敛慢且易产生安全关键错误。
- 方法要点：结合策略模型和失误预测模型，通过效用函数选择低风险走子。
- 实验或效果：在数百局对弈中，相比基线方法显著降低失误率，支持更广探索。

## 摘要（原文）

> In high stakes environments, agents relying purely on imitation learning or reinforcement learning often struggle to avoid safety-critical errors during exploration. Existing reinforcement learning approaches for environments such as chess require hundreds of thousands of episodes and substantial computational resources to converge. Imitation learning, on the other hand, is more sample efficient but is brittle under distributional shift and lacks mechanisms for proactive risk avoidance. In this work, we propose Oracle-Guided Soft Shielding (OGSS), a simple yet effective framework for safer decision-making, enabling safe exploration by learning a probabilistic safety model from oracle feedback in an imitation learning setting. Focusing on the domain of chess, we train a model to predict strong moves based on past games, and separately learn a blunder prediction model from Stockfish evaluations to estimate the tactical risk of each move. During inference, the agent first generates a set of candidate moves and then uses the blunder model to determine high-risk options, and uses a utility function combining the predicted move likelihood from the policy model and the blunder probability to select actions that strike a balance between performance and safety. This enables the agent to explore and play competitively while significantly reducing the chance of tactical mistakes. Across hundreds of games against a strong chess engine, we compare our approach with other methods in the literature, such as action pruning, SafeDAgger, and uncertainty-based sampling. Our results demonstrate that OGSS variants maintain a lower blunder rate even as the agent's exploration ratio is increased by several folds, highlighting its ability to support broader exploration without compromising tactical soundness.

