---
layout: default
title: Beyond Activation Patterns: A Weight-Based Out-of-Context Explanation of Sparse Autoencoder Features
---

# Beyond Activation Patterns: A Weight-Based Out-of-Context Explanation of Sparse Autoencoder Features
**arXiv**：[2601.22447v1](https://arxiv.org/abs/2601.22447) · [PDF](https://arxiv.org/pdf/2601.22447.pdf)  
**作者**：Yiting Liu, Zhi-Hong Deng  

**一句话要点**：提出基于权重的解释框架，以无激活数据方式增强稀疏自编码器特征的可解释性。

**关键词**：稀疏自编码器, 特征解释, 权重分析, 注意力机制, 语言模型

## 3 点简述
- 核心问题：现有稀疏自编码器特征解释方法依赖激活模式，忽略特征在计算中的功能作用。
- 方法要点：引入权重交互框架，通过直接权重交互测量功能效应，无需激活数据。
- 实验或效果：在Gemma-2和Llama-3.1模型上验证，发现特征直接预测输出、参与注意力机制及分布差异。

## 摘要（原文）

> Sparse autoencoders (SAEs) have emerged as a powerful technique for decomposing language model representations into interpretable features. Current interpretation methods infer feature semantics from activation patterns, but overlook that features are trained to reconstruct activations that serve computational roles in the forward pass. We introduce a novel weight-based interpretation framework that measures functional effects through direct weight interactions, requiring no activation data. Through three experiments on Gemma-2 and Llama-3.1 models, we demonstrate that (1) 1/4 of features directly predict output tokens, (2) features actively participate in attention mechanisms with depth-dependent structure, and (3) semantic and non-semantic feature populations exhibit distinct distribution profiles in attention circuits. Our analysis provides the missing out-of-context half of SAE feature interpretability.

