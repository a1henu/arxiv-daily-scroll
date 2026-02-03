---
layout: default
title: Understanding the Reversal Curse Mitigation in Masked Diffusion Models through Attention and Training Dynamics
---

# Understanding the Reversal Curse Mitigation in Masked Diffusion Models through Attention and Training Dynamics
**arXiv**：[2602.02133v1](https://arxiv.org/abs/2602.02133) · [PDF](https://arxiv.org/pdf/2602.02133.pdf)  
**作者**：Sangwoo Shin, BumJun Kim, Kyelim Lee, Moongyu Jeon, Albert No  

**一句话要点**：揭示掩码扩散模型通过注意力机制与训练动态缓解逆转诅咒的机制

**关键词**：逆转诅咒, 掩码扩散模型, 注意力机制, 训练动态, 语言模型, Transformer编码器

## 3 点简述
- 研究掩码扩散语言模型（MDMs）相比自回归模型（ARMs）在逆转诅咒问题上的缓解现象
- 提出缓解源于单层Transformer编码器的权重共享，使正反向注意力分数正相关，梯度对齐
- 通过控制实验和大规模模型验证，解释MDMs部分克服ARMs中持续存在的失败模式

## 摘要（原文）

> Autoregressive language models (ARMs) suffer from the reversal curse: after learning that "$A$ is $B$", they often fail on the reverse query "$B$ is $A$". Masked diffusion-based language models (MDMs) exhibit this failure in a much weaker form, but the underlying reason has remained unclear. A common explanation attributes this mitigation to the any-order training objective. However, observing "[MASK] is $B$" during training does not necessarily teach the model to handle the reverse prompt "$B$ is [MASK]". We show that the mitigation arises from architectural structure and its interaction with training. In a one-layer Transformer encoder, weight sharing couples the two directions by making forward and reverse attention scores positively correlated. In the same setting, we further show that the corresponding gradients are aligned, so minimizing the forward loss also reduces the reverse loss. Experiments on both controlled toy tasks and large-scale diffusion language models support these mechanisms, explaining why MDMs partially overcome a failure mode that persists in strong ARMs.

