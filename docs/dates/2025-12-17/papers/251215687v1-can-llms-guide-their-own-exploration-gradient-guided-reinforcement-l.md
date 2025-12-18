---
layout: default
title: Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning
---

# Can LLMs Guide Their Own Exploration? Gradient-Guided Reinforcement Learning for LLM Reasoning
**arXiv**：[2512.15687v1](https://arxiv.org/abs/2512.15687) · [PDF](https://arxiv.org/pdf/2512.15687.pdf)  
**作者**：Zhenwen Liang, Sidi Lu, Wenhao Yu, Kishan Panaganti, Yujun Zhou, Haitao Mi, Dong Yu  

**一句话要点**：提出梯度引导强化学习框架G2RL，以模型自身梯度方向引导探索，提升大语言模型推理能力。

**关键词**：梯度引导强化学习, 大语言模型推理, 探索机制, 序列级特征, 性能提升, 自参考探索

## 3 点简述
- 当前强化学习探索机制与大语言模型学习方式不匹配，依赖外部启发式方法。
- G2RL利用模型最终层敏感度构建序列级特征，基于梯度方向新颖性奖励轨迹，实现自参考探索。
- 在数学和通用推理基准测试中，G2RL优于基于熵和外部嵌入的方法，提升多项性能指标。

## 摘要（原文）

> Reinforcement learning has become essential for strengthening the reasoning abilities of large language models, yet current exploration mechanisms remain fundamentally misaligned with how these models actually learn. Entropy bonuses and external semantic comparators encourage surface level variation but offer no guarantee that sampled trajectories differ in the update directions that shape optimization. We propose G2RL, a gradient guided reinforcement learning framework in which exploration is driven not by external heuristics but by the model own first order update geometry. For each response, G2RL constructs a sequence level feature from the model final layer sensitivity, obtainable at negligible cost from a standard forward pass, and measures how each trajectory would reshape the policy by comparing these features within a sampled group. Trajectories that introduce novel gradient directions receive a bounded multiplicative reward scaler, while redundant or off manifold updates are deemphasized, yielding a self referential exploration signal that is naturally aligned with PPO style stability and KL control. Across math and general reasoning benchmarks (MATH500, AMC, AIME24, AIME25, GPQA, MMLUpro) on Qwen3 base 1.7B and 4B models, G2RL consistently improves pass@1, maj@16, and pass@k over entropy based GRPO and external embedding methods. Analyzing the induced geometry, we find that G2RL expands exploration into substantially more orthogonal and often opposing gradient directions while maintaining semantic coherence, revealing that a policy own update space provides a far more faithful and effective basis for guiding exploration in large language model reinforcement learning.

