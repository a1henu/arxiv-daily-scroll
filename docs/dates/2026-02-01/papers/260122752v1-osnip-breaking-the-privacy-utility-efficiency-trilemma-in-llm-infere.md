---
layout: default
title: OSNIP: Breaking the Privacy-Utility-Efficiency Trilemma in LLM Inference via Obfuscated Semantic Null Space
---

# OSNIP: Breaking the Privacy-Utility-Efficiency Trilemma in LLM Inference via Obfuscated Semantic Null Space
**arXiv**：[2601.22752v1](https://arxiv.org/abs/2601.22752) · [PDF](https://arxiv.org/pdf/2601.22752.pdf)  
**作者**：Zhiyuan Cao, Zeyu Ma, Chenhao Yang, Han Zheng, Mingang Chen  

**一句话要点**：提出OSNIP框架，通过混淆语义零空间注入解决LLM推理中的隐私-效用-效率三难问题

**关键词**：隐私保护推理, LLM加密, 语义零空间, 客户端加密, 扰动注入, 三难问题

## 3 点简述
- 核心问题：LLM推理中隐私保护与模型效用、效率难以兼顾的三难困境
- 方法要点：在LLM高维潜在空间中定义混淆语义零空间，注入扰动以保护隐私
- 实验或效果：在12个基准测试中实现最优性能，显著降低攻击成功率并保持高模型效用

## 摘要（原文）

> We propose Obfuscated Semantic Null space Injection for Privacy (OSNIP), a lightweight client-side encryption framework for privacy-preserving LLM inference. Generalizing the geometric intuition of linear kernels to the high-dimensional latent space of LLMs, we formally define the ``Obfuscated Semantic Null Space'', a high-dimensional regime that preserves semantic fidelity while enforcing near-orthogonality to the original embedding. By injecting perturbations that project the original embedding into this space, OSNIP ensures privacy without any post-processing. Furthermore, OSNIP employs a key-dependent stochastic mapping that synthesizes individualized perturbation trajectories unique to each user. Evaluations on 12 generative and classification benchmarks show that OSNIP achieves state-of-the-art performance, sharply reducing attack success rates while maintaining strong model utility under strict security constraints.

