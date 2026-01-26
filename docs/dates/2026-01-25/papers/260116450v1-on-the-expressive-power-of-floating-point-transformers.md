---
layout: default
title: On the Expressive Power of Floating-Point Transformers
---

# On the Expressive Power of Floating-Point Transformers
**arXiv**：[2601.16450v1](https://arxiv.org/abs/2601.16450) · [PDF](https://arxiv.org/pdf/2601.16450.pdf)  
**作者**：Sejun Park, Yeachan Park, Geonho Hwang  

**一句话要点**：分析浮点Transformer的表达能力，揭示其在有限序列长度下的表示特性与非等变性

**关键词**：Transformer表达能力, 浮点运算, 置换等变性, 位置编码, 序列长度限制

## 3 点简述
- 研究浮点Transformer在计算机实现中的表达能力，区别于理想实数模型
- 证明浮点Transformer可表示非置换等变函数，并在有界序列长度下表示所有置换等变函数
- 发现浮点Transformer的最小等变结构，并指出非平凡位置编码可能损害表示能力

## 摘要（原文）

> The study on the expressive power of transformers shows that transformers are permutation equivariant, and they can approximate all permutation-equivariant continuous functions on a compact domain. However, these results are derived under real parameters and exact operations, while real implementations on computers can only use a finite set of numbers and inexact machine operations with round-off errors. In this work, we investigate the representability of floating-point transformers that use floating-point parameters and floating-point operations. Unlike existing results under exact operations, we first show that floating-point transformers can represent a class of non-permutation-equivariant functions even without positional encoding. Furthermore, we prove that floating-point transformers can represent all permutation-equivariant functions when the sequence length is bounded, but they cannot when the sequence length is large. We also found the minimal equivariance structure in floating-point transformers, and show that all non-trivial additive positional encoding can harm the representability of floating-point transformers.

