---
layout: default
title: Architectural Trade-offs in Small Language Models Under Compute Constraints
---

# Architectural Trade-offs in Small Language Models Under Compute Constraints
**arXiv**：[2512.20877v1](https://arxiv.org/abs/2512.20877) · [PDF](https://arxiv.org/pdf/2512.20877.pdf)  
**作者**：Shivraj Singh Bhatti  

**一句话要点**：在计算约束下系统研究小语言模型的架构权衡，分析性能与效率的交互影响。

**关键词**：小语言模型, 架构权衡, 计算约束, 注意力机制, Transformer, 效率评估

## 3 点简述
- 核心问题：小语言模型在严格计算约束下，架构选择和训练预算如何决定性能。
- 方法要点：从线性预测器逐步引入非线性、自注意力和多层Transformer，评估字符级和词级建模。
- 实验或效果：基于测试负对数似然、参数数和FLOPs比较，发现注意力模型在效率上优于MLP，但深度或上下文增加可能降低性能。

## 摘要（原文）

> We present a systematic empirical study of small language models under strict compute constraints, analyzing how architectural choices and training budget interact to determine performance. Starting from a linear next-token predictor, we progressively introduce nonlinearities, self-attention, and multi-layer transformer architectures, evaluating each on character-level modeling of Tiny Shakespeare and word-level modeling of Penn Treebank (PTB) and WikiText-2. We compare models using test negative log-likelihood (NLL), parameter count, and approximate training FLOPs to characterize accuracy-efficiency trade-offs. Our results show that attention-based models dominate MLPs in per-FLOP efficiency even at small scale, while increasing depth or context without sufficient optimization can degrade performance. We further examine rotary positional embeddings (RoPE), finding that architectural techniques successful in large language models do not necessarily transfer to small-model regimes.

