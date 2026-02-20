---
layout: default
title: Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom's Taxonomy
---

# Mechanistic Interpretability of Cognitive Complexity in LLMs via Linear Probing using Bloom's Taxonomy
**arXiv**：[2602.17229v1](https://arxiv.org/abs/2602.17229) · [PDF](https://arxiv.org/pdf/2602.17229.pdf)  
**作者**：Bianca Raimondi, Maurizio Gabbrielli  

**一句话要点**：提出基于布鲁姆分类法的线性探测方法，揭示LLM内部认知复杂度的线性可分离性

**关键词**：大语言模型, 可解释性, 布鲁姆分类法, 线性探测, 认知复杂度, 残差流

## 3 点简述
- 核心问题：大语言模型的黑箱特性需超越表面性能的新评估框架，以理解其内部认知复杂度表示
- 方法要点：使用布鲁姆分类法作为层次化视角，分析LLM高维激活向量，探测认知水平是否在残差流中线性可分
- 实验或效果：线性分类器在所有布鲁姆水平上平均准确率约95%，表明认知难度在模型前向传播早期被解析

## 摘要（原文）

> The black-box nature of Large Language Models necessitates novel evaluation frameworks that transcend surface-level performance metrics. This study investigates the internal neural representations of cognitive complexity using Bloom's Taxonomy as a hierarchical lens. By analyzing high-dimensional activation vectors from different LLMs, we probe whether different cognitive levels, ranging from basic recall (Remember) to abstract synthesis (Create), are linearly separable within the model's residual streams. Our results demonstrate that linear classifiers achieve approximately 95% mean accuracy across all Bloom levels, providing strong evidence that cognitive level is encoded in a linearly accessible subspace of the model's representations. These findings provide evidence that the model resolves the cognitive difficulty of a prompt early in the forward pass, with representations becoming increasingly separable across layers.

