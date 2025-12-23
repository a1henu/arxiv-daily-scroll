---
layout: default
title: Attention Is Not What You Need
---

# Attention Is Not What You Need
**arXiv**：[2512.19428v1](https://arxiv.org/abs/2512.19428) · [PDF](https://arxiv.org/pdf/2512.19428.pdf)  
**作者**：Zhang Chong  

**一句话要点**：提出基于Grassmann流形的无注意力架构，用于序列建模以替代自注意力机制。

**关键词**：序列建模, Grassmann流形, 无注意力架构, 语言建模, 自然语言推理, 几何表示

## 3 点简述
- 核心问题：探讨自注意力在序列建模中是否必要，指出其数学不透明性。
- 方法要点：使用Grassmann流形编码局部令牌对，通过低秩子空间变形传播信息。
- 实验或效果：在Wikitext-2和SNLI任务上，性能接近或略优于Transformer模型。

## 摘要（原文）

> We revisit a basic question in sequence modeling: is explicit self-attention actually necessary for strong performance and reasoning? We argue that standard multi-head attention is best seen as a form of tensor lifting: hidden vectors are mapped into a high-dimensional space of pairwise interactions, and learning proceeds by constraining this lifted tensor through gradient descent. This mechanism is extremely expressive but mathematically opaque, because after many layers it becomes very hard to describe the model with a small family of explicit invariants.
>   To explore an alternative, we propose an attention-free architecture based on Grassmann flows. Instead of forming an L by L attention matrix, our Causal Grassmann layer (i) linearly reduces token states, (ii) encodes local token pairs as two-dimensional subspaces on a Grassmann manifold via Plucker coordinates, and (iii) fuses these geometric features back into the hidden states through gated mixing. Information therefore propagates by controlled deformations of low-rank subspaces over multi-scale local windows, so the core computation lives on a finite-dimensional manifold rather than in an unstructured tensor space.
>   On the Wikitext-2 language modeling benchmark, purely Grassmann-based models with 13 to 18 million parameters achieve validation perplexities within about 10 to 15 percent of size-matched Transformers. On the SNLI natural language inference task, a Grassmann-Plucker head on top of DistilBERT slightly outperforms a Transformer head, with best validation and test accuracies of 0.8550 and 0.8538 compared to 0.8545 and 0.8511. We analyze the complexity of Grassmann mixing, show linear scaling in sequence length for fixed rank, and argue that such manifold-based designs offer a more structured route toward geometric and invariant-based interpretations of neural reasoning.

