---
layout: default
title: Parity, Sensitivity, and Transformers
---

# Parity, Sensitivity, and Transformers
**arXiv**：[2602.05896v1](https://arxiv.org/abs/2602.05896) · [PDF](https://arxiv.org/pdf/2602.05896.pdf)  
**作者**：Alexander Kozachinskiy, Tomasz Steifer, Przemysław Wałȩga  

**一句话要点**：提出单层多头Transformer无法解决PARITY问题，并给出新构造以解决此限制。

**关键词**：Transformer架构, PARITY问题, 计算复杂性, 位置编码, 因果掩码, 下界证明

## 3 点简述
- 研究Transformer架构计算能力，聚焦PARITY问题解决限制。
- 构造新Transformer模型，使用softmax、长度无关位置编码，无layernorm。
- 证明单层单头Transformer无法解决PARITY，提供首个下界结果。

## 摘要（原文）

> The transformer architecture is almost a decade old. Despite that, we still have a limited understanding of what this architecture can or cannot compute. For instance, can a 1-layer transformer solve PARITY -- or more generally -- which kinds of transformers can do it? Known constructions for PARITY have at least 2 layers and employ impractical features: either a length-dependent positional encoding, or hardmax, or layernorm without the regularization parameter, or they are not implementable with causal masking.
>   We give a new construction of a transformer for PARITY with softmax, length-independent and polynomially bounded positional encoding, no layernorm, working both with and without causal masking. We also give the first lower bound for transformers solving PARITY -- by showing that it cannot be done with only one layer and one head.

