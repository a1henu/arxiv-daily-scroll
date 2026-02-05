---
layout: default
title: Rethinking Weight Tying: Pseudo-Inverse Tying for Stable LM Training and Updates
---

# Rethinking Weight Tying: Pseudo-Inverse Tying for Stable LM Training and Updates
**arXiv**：[2602.04556v1](https://arxiv.org/abs/2602.04556) · [PDF](https://arxiv.org/pdf/2602.04556.pdf)  
**作者**：Jian Gu, Aldeida Aleti, Chunyang Chen, Hongyu Zhang  

**一句话要点**：提出伪逆绑定以稳定语言模型训练与更新，解决权重共享中的接口漂移问题。

**关键词**：权重绑定, 语言模型训练, 接口稳定性, 伪逆投影, 后训练干预, 紧凑模型

## 3 点简述
- 核心问题：权重共享导致嵌入与解嵌入接口漂移，影响训练稳定性和后训练干预。
- 方法要点：通过共享潜在令牌记忆的耦合投影同步接口，避免显式伪逆计算。
- 实验或效果：在256M-1.3B参数模型中提升训练稳定性、语义一致性和减少副作用。

## 摘要（原文）

> Weight tying is widely used in compact language models to reduce parameters by sharing the token table between the input embedding and the output projection. However, weight sharing does not guarantee a stable token interface: during training, the correspondence between encoding tokens into hidden states and decoding hidden states into logits can drift, worsening optimization sensitivity and making post-training interventions such as editing, patching, and lightweight adaptation less predictable. We propose Pseudo-Inverse Tying (PIT), which synchronizes embedding and unembedding as coupled projections of a shared latent token memory, guaranteeing a pseudo-inverse-consistent interface throughout training. PIT maintains an orthonormal shared memory, obtained by thin polar decomposition for teacher initialization or random orthonormal initialization from scratch, and introduces a fully learned symmetric positive definite hidden-space transform parameterized via a Cholesky factor. The output head applies this transform to hidden states before the vocabulary projection, while the embedding applies the inverse transform to token vectors using stable triangular solves, avoiding explicit pseudo-inverse recomputation and any vocabulary-sized auxiliary parameters. We evaluate PIT on on-device models spanning 256M-1.3B parameters across pretraining and adaptation, and consistently observe improved training stability, stronger layerwise semantic consistency, and substantially reduced side effects.

