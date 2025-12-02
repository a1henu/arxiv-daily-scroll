---
layout: default
title: ZIP-RC: Zero-overhead Inference-time Prediction of Reward and Cost for Adaptive and Interpretable Generation
---

# ZIP-RC: Zero-overhead Inference-time Prediction of Reward and Cost for Adaptive and Interpretable Generation
**arXiv**：[2512.01457v1](https://arxiv.org/abs/2512.01457) · [PDF](https://arxiv.org/pdf/2512.01457.pdf)  
**作者**：Rohin Manvi, Joey Hong, Tim Seyde, Maxime Labonne, Mathias Lechner, Sergey Levine  

**一句话要点**：提出ZIP-RC方法，通过零开销推理时预测奖励与成本，实现自适应高效生成

**关键词**：自适应推理, 零开销预测, 奖励成本建模, 大语言模型自省, 推理效率优化

## 3 点简述
- 核心问题：大语言模型缺乏实时自省能力，无法预测自身成功概率与计算需求，导致推理效率低下和信任问题。
- 方法要点：在推理时复用未使用的logits，在同一前向传递中预测最终奖励和剩余长度，无需额外模型或开销，实现自适应采样决策。
- 实验或效果：在混合难度数学基准测试中，相比多数投票，ZIP-RC在相同或更低平均成本下提升准确率高达12%，并优化质量、计算和延迟的权衡。

## 摘要（原文）

> Large language models excel at reasoning but lack key aspects of introspection, including anticipating their own success and the computation required to achieve it. Humans use real-time introspection to decide how much effort to invest, when to make multiple attempts, when to stop, and when to signal success or failure. Without this, LLMs struggle to make intelligent meta-cognition decisions. Test-time scaling methods like Best-of-N drive up cost and latency by using a fixed budget of samples regardless of the marginal benefit of each one at any point in generation, and the absence of confidence signals can mislead people, prevent appropriate escalation to better tools, and undermine trustworthiness. Learned verifiers or reward models can provide confidence estimates, but do not enable adaptive inference and add substantial cost by requiring extra models or forward passes. We present ZIP-RC, an adaptive inference method that equips models with zero-overhead inference-time predictions of reward and cost. At every token, ZIP-RC reuses reserved or unused logits in the same forward pass as next-token prediction to output a joint distribution over final reward and remaining length -- no extra models, architecture change, or inference overhead. This full joint distribution is used to compute a sampling utility which is the linear combination of the expected maximum reward, total compute, and latency of set of samples if generated to completion. During inference, we maximize this utility with meta-actions that determine which prefix of tokens to continue or initiate sampling from. On mixed-difficulty mathematical benchmarks, ZIP-RC improves accuracy by up to 12% over majority voting at equal or lower average cost, and traces smooth Pareto frontiers between quality, compute, and latency. By providing real-time reward-cost introspection, ZIP-RC enables adaptive, efficient reasoning.

