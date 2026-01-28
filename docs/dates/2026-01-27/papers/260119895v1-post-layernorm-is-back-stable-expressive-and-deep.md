---
layout: default
title: Post-LayerNorm Is Back: Stable, ExpressivE, and Deep
---

# Post-LayerNorm Is Back: Stable, ExpressivE, and Deep
**arXiv**：[2601.19895v1](https://arxiv.org/abs/2601.19895) · [PDF](https://arxiv.org/pdf/2601.19895.pdf)  
**作者**：Chen Chen, Lai Wei  

**一句话要点**：提出Keel Transformer，通过Highway连接解决Post-LN深度训练不稳定问题

**关键词**：Post-LayerNorm, 深度Transformer, 梯度消失, Highway连接, 大语言模型扩展

## 3 点简述
- 核心问题：Post-LayerNorm因残差路径梯度消失，导致深度Transformer训练不稳定
- 方法要点：用Highway式连接替换ResNet残差路径，保持梯度流，防止信号消失
- 实验或效果：Keel在超过1000层深度稳定训练，困惑度优于Pre-LN，支持深度扩展

## 摘要（原文）

> Large language model (LLM) scaling is hitting a wall. Widening models yields diminishing returns, and extending context length does not improve fundamental expressivity. In contrast, depth scaling offers theoretically superior expressivity, yet current Transformer architectures struggle to train reliably at extreme depths. We revisit the Post-LayerNorm (Post-LN) formulation, whose instability at scale caused its replacement by Pre-LN in modern LLMs. We show that the central failure mode of Post-LN arises from the ResNet-style residual pathway, which introduces gradient vanishing in deep networks. We present Keel, a Post-LN Transformer that replaces this residual path with a Highway-style connection. This modification preserves the gradient flow through the residual branch, preventing signal vanishing from the top layers to the bottom. Unlike prior methods, Keel enables stable training at extreme depths without requiring specialized initialization or complex optimization tricks. Keel trains robustly at depths exceeding 1000 layers and consistently improves perplexity and depth-scaling characteristics over Pre-LN. These findings indicate that Post-LN, when paired with a Highway-style connection, provides a simple and effective foundation for building deeply scalable LLMs, opening the possibility for future infinite-depth architectures.

