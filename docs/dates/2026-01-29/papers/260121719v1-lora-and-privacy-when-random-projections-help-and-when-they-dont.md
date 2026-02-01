---
layout: default
title: LoRA and Privacy: When Random Projections Help (and When They Don't)
---

# LoRA and Privacy: When Random Projections Help (and When They Don't)
**arXiv**：[2601.21719v1](https://arxiv.org/abs/2601.21719) · [PDF](https://arxiv.org/pdf/2601.21719.pdf)  
**作者**：Yaxi Hu, Johanna Düngler, Bernhard Schölkopf, Amartya Sanyal  

**一句话要点**：提出Wishart投影机制，分析其在向量和矩阵查询下的差分隐私性质，并探讨LoRA更新的隐私影响。

**关键词**：差分隐私, 随机投影, LoRA, 隐私放大, 矩阵查询, Wishart分布

## 3 点简述
- 研究随机投影机制在差分隐私中的应用，特别关注Wishart分布作为随机性来源。
- 证明向量查询下无需加性噪声即可实现差分隐私，但矩阵查询在无噪声时存在隐私漏洞。
- 分析噪声变体在低秩投影下的隐私放大效应，并初步实验显示可降低噪声提升准确性。

## 摘要（原文）

> We introduce the (Wishart) projection mechanism, a randomized map of the form $S \mapsto M f(S)$ with $M \sim W_d(1/r I_d, r)$ and study its differential privacy properties. For vector-valued queries $f$, we prove non-asymptotic DP guarantees without any additive noise, showing that Wishart randomness alone can suffice. For matrix-valued queries, however, we establish a sharp negative result: in the noise-free setting, the mechanism is not DP, and we demonstrate its vulnerability by implementing a near perfect membership inference attack (AUC $> 0.99$). We then analyze a noisy variant and prove privacy amplification due to randomness and low rank projection, in both large- and small-rank regimes, yielding stronger privacy guarantees than additive noise alone. Finally, we show that LoRA-style updates are an instance of the matrix-valued mechanism, implying that LoRA is not inherently private despite its built-in randomness, but that low-rank fine-tuning can be more private than full fine-tuning at the same noise level. Preliminary experiments suggest that tighter accounting enables lower noise and improved accuracy in practice.

