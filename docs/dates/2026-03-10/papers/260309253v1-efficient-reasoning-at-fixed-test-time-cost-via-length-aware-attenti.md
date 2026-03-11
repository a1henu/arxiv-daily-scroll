---
layout: default
title: Efficient Reasoning at Fixed Test-Time Cost via Length-Aware Attention Priors and Gain-Aware Training
---

# Efficient Reasoning at Fixed Test-Time Cost via Length-Aware Attention Priors and Gain-Aware Training
**arXiv**：[2603.09253v1](https://arxiv.org/abs/2603.09253) · [PDF](https://arxiv.org/pdf/2603.09253.pdf)  
**作者**：Rian Atri  

**一句话要点**：提出长度感知注意力先验和增益感知训练，以在固定测试成本下提升Transformer推理效率。

**关键词**：Transformer优化, 注意力机制, 推理效率, 计算约束, 正则化方法, 非凸优化

## 3 点简述
- 研究在严格计算约束下的高效推理问题，旨在不增加测试时间成本。
- 引入长度感知注意力先验和增益感知控制器，仅训练时使用，不增加推理参数。
- 在WikiText 2上实现验证交叉熵降低，同时匹配基线延迟和内存开销。

## 摘要（原文）

> We study efficient reasoning under tight compute. We ask how to make structured, correct decisions without increasing test time cost. We add two training only components to small and medium Transformers that also transfer to broader differentiable optimizers. First, a length aware attention prior built via fuzzy regime position alignment, RPA, yields a normalized pre softmax bias that guides attention like a structured regularizer while adding no new inference parameters. Second, a minimal gain aware controller, Guardian, nudges attention sharpness only when validation improvements warrant it, following a two timescale policy gradient view of nonconvex optimization. It is disabled at inference. A KL perspective shows softmax of z plus log pi as MAP with KL regularization, grounding the prior in a principled objective. Under strict compute parity on WikiText 2, we reduce validation cross entropy while matching baseline latency and memory. At inference, we add a precomputed, cached prior B of T as a single additive bias per head. The controller does not run. In practice, this incurs negligible overhead, a cached bias add per head, with no measurable p50 latency shift. Our results suggest that length aware priors and late phase gain control preserve scarce improvements, especially in long span, noisy logit regimes, while keeping test time costs effectively unchanged.

