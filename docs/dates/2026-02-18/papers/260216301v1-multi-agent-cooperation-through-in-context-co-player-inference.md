---
layout: default
title: Multi-agent cooperation through in-context co-player inference
---

# Multi-agent cooperation through in-context co-player inference
**arXiv**：[2602.16301v1](https://arxiv.org/abs/2602.16301) · [PDF](https://arxiv.org/pdf/2602.16301.pdf)  
**作者**：Marissa A. Weis, Maciej Wołczyk, Rajai Nasser, Rif A. Saurous, Blaise Agüera y Arcas, João Sacramento, Alexander Meulemans  

**一句话要点**：提出基于序列模型上下文学习的多智能体合作方法，通过推断对手学习动态实现合作

**关键词**：多智能体强化学习, 上下文学习, 序列模型, 合作行为, 对手推断

## 3 点简述
- 核心问题：自利智能体在多智能体强化学习中难以实现合作，现有方法依赖硬编码假设或时间尺度分离
- 方法要点：利用序列模型的上下文学习能力，通过训练对抗多样对手分布，诱导上下文最优响应策略
- 实验或效果：发现合作机制自然涌现，上下文适应使智能体易受勒索，相互压力驱动合作行为学习

## 摘要（原文）

> Achieving cooperation among self-interested agents remains a fundamental challenge in multi-agent reinforcement learning. Recent work showed that mutual cooperation can be induced between "learning-aware" agents that account for and shape the learning dynamics of their co-players. However, existing approaches typically rely on hardcoded, often inconsistent, assumptions about co-player learning rules or enforce a strict separation between "naive learners" updating on fast timescales and "meta-learners" observing these updates. Here, we demonstrate that the in-context learning capabilities of sequence models allow for co-player learning awareness without requiring hardcoded assumptions or explicit timescale separation. We show that training sequence model agents against a diverse distribution of co-players naturally induces in-context best-response strategies, effectively functioning as learning algorithms on the fast intra-episode timescale. We find that the cooperative mechanism identified in prior work-where vulnerability to extortion drives mutual shaping-emerges naturally in this setting: in-context adaptation renders agents vulnerable to extortion, and the resulting mutual pressure to shape the opponent's in-context learning dynamics resolves into the learning of cooperative behavior. Our results suggest that standard decentralized reinforcement learning on sequence models combined with co-player diversity provides a scalable path to learning cooperative behaviors.

