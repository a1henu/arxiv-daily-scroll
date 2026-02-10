---
layout: default
title: WorldCompass: Reinforcement Learning for Long-Horizon World Models
---

# WorldCompass: Reinforcement Learning for Long-Horizon World Models
**arXiv**：[2602.09022v1](https://arxiv.org/abs/2602.09022) · [PDF](https://arxiv.org/pdf/2602.09022.pdf)  
**作者**：Zehan Wang, Tengfei Wang, Haiyu Zhang, Xuhui Zuo, Junta Wu, Haoyuan Wang, Wenqiang Sun, Zhenwei Wang, Chenjie Cao, Hengshuang Zhao, Chunchao Guo, Zhou Zhao  

**一句话要点**：提出WorldCompass强化学习后训练框架，以提升长时程交互视频世界模型的探索准确性和一致性。

**关键词**：强化学习, 长时程世界模型, 视频生成, 交互准确性, 奖励函数设计, 后训练框架

## 3 点简述
- 核心问题：长时程交互视频世界模型在探索中可能缺乏准确性和一致性，需要基于交互信号进行优化。
- 方法要点：引入片段级展开策略、互补奖励函数和高效强化学习算法，针对自回归视频生成范式设计。
- 实验或效果：在WorldPlay模型上评估，显著提高了交互准确性和视觉保真度，适用于多种场景。

## 摘要（原文）

> This work presents WorldCompass, a novel Reinforcement Learning (RL) post-training framework for the long-horizon, interactive video-based world models, enabling them to explore the world more accurately and consistently based on interaction signals. To effectively "steer" the world model's exploration, we introduce three core innovations tailored to the autoregressive video generation paradigm: 1) Clip-level rollout Strategy: We generate and evaluate multiple samples at a single target clip, which significantly boosts rollout efficiency and provides fine-grained reward signals. 2) Complementary Reward Functions: We design reward functions for both interaction-following accuracy and visual quality, which provide direct supervision and effectively suppress reward-hacking behaviors. 3) Efficient RL Algorithm: We employ the negative-aware fine-tuning strategy coupled with various efficiency optimizations to efficiently and effectively enhance model capacity. Evaluations on the SoTA open-source world model, WorldPlay, demonstrate that WorldCompass significantly improves interaction accuracy and visual fidelity across various scenarios.

