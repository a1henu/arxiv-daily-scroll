---
layout: default
title: Unlocking the Address Book: Dissecting the Sparse Semantic Structure of LLM Key-Value Caches via Sparse Autoencoders
---

# Unlocking the Address Book: Dissecting the Sparse Semantic Structure of LLM Key-Value Caches via Sparse Autoencoders
**arXiv**：[2512.10547v1](https://arxiv.org/abs/2512.10547) · [PDF](https://arxiv.org/pdf/2512.10547.pdf)  
**作者**：Qingsen Ma, Dianyun Wang, Jiaming Lyu, Yaoye Wang, Lechen Ning, Sujie Zhu, Zhenbo Xu, Liuyu Xiang, Huining Li, Huijia Wu, Zhaofeng He  

**一句话要点**：提出STA-Attention框架，利用Top-K稀疏自编码器分解LLM键值缓存为可解释语义原子，以解决长上下文中的内存瓶颈问题。

**关键词**：键值缓存, 稀疏自编码器, 语义分解, 长上下文模型, 注意力机制, 机制可解释性

## 3 点简述
- 核心问题：键值缓存是长上下文大语言模型的主要内存瓶颈，通常被视为不透明的数值张量。
- 方法要点：采用Top-K稀疏自编码器分解键值缓存，揭示键值不对称性，并引入双预算策略选择性保留语义组件。
- 实验或效果：在多个模型上验证语义重构保持困惑度和零样本性能，桥接机制可解释性与注意力建模。

## 摘要（原文）

> The Key-Value (KV) cache is the primary memory bottleneck in long-context Large Language Models, yet it is typically treated as an opaque numerical tensor. In this work, we propose \textbf{STA-Attention}, a framework that utilizes Top-K Sparse Autoencoders (SAEs) to decompose the KV cache into interpretable ``semantic atoms.'' Unlike standard $L_1$-regularized SAEs, our Top-K approach eliminates shrinkage bias, preserving the precise dot-product geometry required for attention. Our analysis uncovers a fundamental \textbf{Key-Value Asymmetry}: while Key vectors serve as highly sparse routers dominated by a ``Semantic Elbow,'' deep Value vectors carry dense content payloads requiring a larger budget. Based on this structure, we introduce a Dual-Budget Strategy that selectively preserves the most informative semantic components while filtering representational noise. Experiments on Yi-6B, Mistral-7B, Qwen2.5-32B, and others show that our semantic reconstructions maintain perplexity and zero-shot performance comparable to the original models, effectively bridging the gap between mechanistic interpretability and faithful attention modeling.

