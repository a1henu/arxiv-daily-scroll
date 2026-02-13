---
layout: default
title: Krause Synchronization Transformers
---

# Krause Synchronization Transformers
**arXiv**：[2602.11534v1](https://arxiv.org/abs/2602.11534) · [PDF](https://arxiv.org/pdf/2602.11534.pdf)  
**作者**：Jingkun Liu, Yisong Yue, Max Welling, Yue Song  

**一句话要点**：提出Krause注意力机制，基于有界置信共识动态，以缓解Transformer中的表示崩溃和注意力汇问题。

**关键词**：注意力机制, Transformer动态, 有界置信共识, 计算复杂度, 表示学习

## 3 点简述
- 核心问题：Transformer自注意力因全局归一化导致强同步动态，引发表示崩溃和注意力汇。
- 方法要点：引入Krause注意力，基于距离的局部稀疏交互，替代相似性全局聚合，降低计算复杂度。
- 实验或效果：在视觉、自回归生成和大语言模型实验中，展示性能提升和计算效率增益。

## 摘要（原文）

> Self-attention in Transformers relies on globally normalized softmax weights, causing all tokens to compete for influence at every layer. When composed across depth, this interaction pattern induces strong synchronization dynamics that favor convergence toward a dominant mode, a behavior associated with representation collapse and attention sink phenomena. We introduce Krause Attention, a principled attention mechanism inspired by bounded-confidence consensus dynamics. Krause Attention replaces similarity-based global aggregation with distance-based, localized, and selectively sparse interactions, promoting structured local synchronization instead of global mixing. We relate this behavior to recent theory modeling Transformer dynamics as interacting particle systems, and show how bounded-confidence interactions naturally moderate attention concentration and alleviate attention sinks. Restricting interactions to local neighborhoods also reduces runtime complexity from quadratic to linear in sequence length. Experiments across vision (ViT on CIFAR/ImageNet), autoregressive generation (MNIST/CIFAR-10), and large language models (Llama/Qwen) demonstrate consistent gains with substantially reduced computation, highlighting bounded-confidence dynamics as a scalable and effective inductive bias for attention.

