---
layout: default
title: InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning
---

# InftyThink+: Effective and Efficient Infinite-Horizon Reasoning via Reinforcement Learning
**arXiv**：[2602.06960v1](https://arxiv.org/abs/2602.06960) · [PDF](https://arxiv.org/pdf/2602.06960.pdf)  
**作者**：Yuchen Yan, Liang Jiang, Jin Jiang, Shuaicheng Li, Zujie Wen, Zhiqiang Zhang, Jun Zhou, Jian Shao, Yueting Zhuang, Yongliang Shen  

**一句话要点**：提出InftyThink+强化学习框架以优化无限长推理中的迭代总结策略

**关键词**：迭代推理, 强化学习, 长链推理优化, 模型控制迭代, 轨迹级训练, 推理效率

## 3 点简述
- 核心问题：传统长链推理存在二次成本、上下文限制和中间信息丢失问题
- 方法要点：采用两阶段训练，结合监督冷启动和轨迹级强化学习优化总结时机与内容
- 实验或效果：在AIME24上准确率提升21%，推理延迟降低，泛化能力增强

## 摘要（原文）

> Large reasoning models achieve strong performance by scaling inference-time chain-of-thought, but this paradigm suffers from quadratic cost, context length limits, and degraded reasoning due to lost-in-the-middle effects. Iterative reasoning mitigates these issues by periodically summarizing intermediate thoughts, yet existing methods rely on supervised learning or fixed heuristics and fail to optimize when to summarize, what to preserve, and how to resume reasoning. We propose InftyThink+, an end-to-end reinforcement learning framework that optimizes the entire iterative reasoning trajectory, building on model-controlled iteration boundaries and explicit summarization. InftyThink+ adopts a two-stage training scheme with supervised cold-start followed by trajectory-level reinforcement learning, enabling the model to learn strategic summarization and continuation decisions. Experiments on DeepSeek-R1-Distill-Qwen-1.5B show that InftyThink+ improves accuracy by 21% on AIME24 and outperforms conventional long chain-of-thought reinforcement learning by a clear margin, while also generalizing better to out-of-distribution benchmarks. Moreover, InftyThink+ significantly reduces inference latency and accelerates reinforcement learning training, demonstrating improved reasoning efficiency alongside stronger performance.

