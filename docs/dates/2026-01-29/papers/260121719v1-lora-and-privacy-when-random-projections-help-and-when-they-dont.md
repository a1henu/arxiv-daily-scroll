---
layout: default
title: LoRA and Privacy: When Random Projections Help (and When They Don't)
---

# LoRA and Privacy: When Random Projections Help (and When They Don't)
**arXiv**：[2601.21719v1](https://arxiv.org/abs/2601.21719) · [PDF](https://arxiv.org/pdf/2601.21719.pdf)  
**作者**：Yaxi Hu, Johanna Düngler, Bernhard Schölkopf, Amartya Sanyal  

**一句话要点**：提出Wishart投影机制，分析其在向量和矩阵查询下的差分隐私性质，并应用于LoRA微调隐私评估。

**关键词**：差分隐私, 随机投影, Wishart分布, LoRA微调, 隐私放大, 矩阵查询

## 3 点简述
- 核心问题：研究随机投影在差分隐私中的作用，特别是无噪声设置下的隐私保证与漏洞。
- 方法要点：针对向量查询证明非渐近DP保证，对矩阵查询展示负面结果并分析噪声变体的隐私放大。
- 实验或效果：初步实验表明，更紧的隐私核算能降低噪声并提升准确性，LoRA微调在相同噪声水平下比全微调更私密。

## 摘要（原文）

> We introduce the (Wishart) projection mechanism, a randomized map of the form $S \mapsto M f(S)$ with $M \sim W_d(1/r I_d, r)$ and study its differential privacy properties. For vector-valued queries $f$, we prove non-asymptotic DP guarantees without any additive noise, showing that Wishart randomness alone can suffice. For matrix-valued queries, however, we establish a sharp negative result: in the noise-free setting, the mechanism is not DP, and we demonstrate its vulnerability by implementing a near perfect membership inference attack (AUC $> 0.99$). We then analyze a noisy variant and prove privacy amplification due to randomness and low rank projection, in both large- and small-rank regimes, yielding stronger privacy guarantees than additive noise alone. Finally, we show that LoRA-style updates are an instance of the matrix-valued mechanism, implying that LoRA is not inherently private despite its built-in randomness, but that low-rank fine-tuning can be more private than full fine-tuning at the same noise level. Preliminary experiments suggest that tighter accounting enables lower noise and improved accuracy in practice.

