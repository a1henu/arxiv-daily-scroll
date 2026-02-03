---
layout: default
title: Interpretable Tabular Foundation Models via In-Context Kernel Regression
---

# Interpretable Tabular Foundation Models via In-Context Kernel Regression
**arXiv**：[2602.02162v1](https://arxiv.org/abs/2602.02162) · [PDF](https://arxiv.org/pdf/2602.02162.pdf)  
**作者**：Ratmir Miftachov, Bruno Charron, Simon Valentin  

**一句话要点**：提出KernelICL框架，通过核回归增强表格基础模型的可解释性

**关键词**：表格基础模型, 可解释性, 核回归, 上下文学习, TALENT基准

## 3 点简述
- 核心问题：表格基础模型如TabPFN和TabICL性能优越但架构不透明，缺乏可解释性
- 方法要点：基于上下文学习类似核回归的洞察，用核函数替换最终预测层，实现透明加权平均预测
- 实验或效果：在55个TALENT基准数据集上，KernelICL性能与现有模型相当，证明可解释性不牺牲性能

## 摘要（原文）

> Tabular foundation models like TabPFN and TabICL achieve state-of-the-art performance through in-context learning, yet their architectures remain fundamentally opaque. We introduce KernelICL, a framework to enhance tabular foundation models with quantifiable sample-based interpretability. Building on the insight that in-context learning is akin to kernel regression, we make this mechanism explicit by replacing the final prediction layer with kernel functions (Gaussian, dot-product, kNN) so that every prediction is a transparent weighted average of training labels. We introduce a two-dimensional taxonomy that formally unifies standard kernel methods, modern neighbor-based approaches, and attention mechanisms under a single framework, and quantify inspectability via the perplexity of the weight distribution over training samples. On 55 TALENT benchmark datasets, KernelICL achieves performance on par with existing tabular foundation models, demonstrating that explicit kernel constraints on the final layer enable inspectable predictions without sacrificing performance.

