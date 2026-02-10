---
layout: default
title: GSS: Gated Subspace Steering for Selective Memorization Mitigation in LLMs
---

# GSS: Gated Subspace Steering for Selective Memorization Mitigation in LLMs
**arXiv**：[2602.08901v1](https://arxiv.org/abs/2602.08901) · [PDF](https://arxiv.org/pdf/2602.08901.pdf)  
**作者**：Xuanqi Zhang, Haoyang Shang, Xiaoxiao Li  

**一句话要点**：提出GSS方法以选择性缓解大语言模型中的记忆化问题

**关键词**：大语言模型, 记忆化缓解, 子空间导向, 选择性干预, 隐私保护

## 3 点简述
- 核心问题：大语言模型会逐字记忆训练序列，损害泛化与隐私
- 方法要点：基于最优子空间导向，通过探测-导向机制实现上下文感知干预
- 实验或效果：在四个基准上匹配或超越现有方法，计算量减少100-1000倍

## 摘要（原文）

> Large language models (LLMs) can memorize and reproduce training sequences verbatim -- a tendency that undermines both generalization and privacy. Existing mitigation methods apply interventions uniformly, degrading performance on the majority of tokens that generalize normally. We show empirically that memorization is sparse, intermittent, and token-conditioned, suggesting that effective mitigation requires context-aware intervention rather than static parameter modification. To this end, we propose a novel and effective selective memorization mitigation method -- Gated Subspace Steering (GSS), which decomposes intervention into a probe (detecting memorization-relevant activations) and a steer (applying targeted correction only when the probe exceeds a threshold). The optimal probe-steer pair emerges from a principled optimization framework based on optimal subspace steering. Experiments on four benchmarks show GSS matches or exceeds state-of-the-art memorization reduction while requiring $100-1000 \times$ less compute than optimization-based alternatives. Furthermore, we provide new theoretical insights into the geometry of memorization in neural representations.

