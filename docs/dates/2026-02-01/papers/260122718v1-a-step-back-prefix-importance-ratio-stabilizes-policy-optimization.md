---
layout: default
title: A Step Back: Prefix Importance Ratio Stabilizes Policy Optimization
---

# A Step Back: Prefix Importance Ratio Stabilizes Policy Optimization
**arXiv**：[2601.22718v1](https://arxiv.org/abs/2601.22718) · [PDF](https://arxiv.org/pdf/2601.22718.pdf)  
**作者**：Shiye Lei, Zhihao Cheng, Dacheng Tao  

**一句话要点**：提出最小前缀比率以稳定大语言模型在离策略强化学习中的优化

**关键词**：强化学习, 大语言模型, 离策略优化, 训练稳定性, 数学推理

## 3 点简述
- 核心问题：离策略强化学习中，基于令牌级重要性采样的校正导致训练不稳定
- 方法要点：使用前缀重要性比率进行理论校正，并提出最小前缀比率作为稳定替代
- 实验或效果：在多个数学推理基准上，显著提升训练稳定性和峰值性能

## 摘要（原文）

> Reinforcement learning (RL) post-training has increasingly demonstrated strong ability to elicit reasoning behaviors in large language models (LLMs). For training efficiency, rollouts are typically generated in an off-policy manner using an older sampling policy and then used to update the current target policy. To correct the resulting discrepancy between the sampling and target policies, most existing RL objectives rely on a token-level importance sampling ratio, primarily due to its computational simplicity and numerical stability. However, we observe that token-level correction often leads to unstable training dynamics when the degree of off-policyness is large. In this paper, we revisit LLM policy optimization under off-policy conditions and show that the theoretically rigorous correction term is the prefix importance ratio, and that relaxing it to a token-level approximation can induce instability in RL post-training. To stabilize LLM optimization under large off-policy drift, we propose a simple yet effective objective, Minimum Prefix Ratio (MinPRO). MinPRO replaces the unstable cumulative prefix ratio with a non-cumulative surrogate based on the minimum token-level ratio observed in the preceding prefix. Extensive experiments on both dense and mixture-of-experts LLMs, across multiple mathematical reasoning benchmarks, demonstrate that MinPRO substantially improves training stability and peak performance in off-policy regimes.

