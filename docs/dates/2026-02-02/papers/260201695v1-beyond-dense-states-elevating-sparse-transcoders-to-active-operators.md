---
layout: default
title: Beyond Dense States: Elevating Sparse Transcoders to Active Operators for Latent Reasoning
---

# Beyond Dense States: Elevating Sparse Transcoders to Active Operators for Latent Reasoning
**arXiv**：[2602.01695v1](https://arxiv.org/abs/2602.01695) · [PDF](https://arxiv.org/pdf/2602.01695.pdf)  
**作者**：Yadong Wang, Haodong Chen, Yu Tian, Chuanxing Geng, Dong Liang, Xiang Chen  

**一句话要点**：提出LSTR框架，将稀疏转码器提升为主动推理算子，以解决密集潜在推理中可解释性和可控性不足的问题。

**关键词**：潜在推理, 稀疏表示, 可解释性, 链式思维压缩, 语义特征, 因果干预

## 3 点简述
- 核心问题：现有潜在推理方法依赖密集潜在转移，导致可解释性和可控性差。
- 方法要点：引入LSTR框架，通过残差跳跃架构解耦线性流形传输与稀疏语义更新，实现可控语义分辨率。
- 实验或效果：实验显示LSTR在保持推理准确性和压缩效率的同时，显著提升可解释性，稀疏特征在推理中作为可解释且因果有效的算子。

## 摘要（原文）

> Latent reasoning compresses the chain-of-thought (CoT) into continuous hidden states, yet existing methods rely on dense latent transitions that remain difficult to interpret and control. Meanwhile, sparse representation models uncover human-interpretable semantic features but remain largely confined to post-hoc analysis. We reconcile this tension by proposing LSTR (Latent Sparse Transcoder Reasoning), a latent reasoning framework that elevates functional sparse transcoders into active reasoning operators to perform multi-step computation through sparse semantic transitions. At its core, LSTR employs a Latent Transition Transcoder (LTT) with a residual skip architecture that decouples linear manifold transport from sparse semantic updates, enabling controllable semantic resolution via explicit sparsity constraints. Extensive experiments show that LSTR preserves reasoning accuracy and compression efficiency while substantially improving interpretability over dense latent baselines. Causal interventions and trajectory analyses further demonstrate that these sparse features act as both interpretable and causally effective operators in the reasoning process.

