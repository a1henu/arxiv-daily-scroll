---
layout: default
title: Mechanistic Knobs in LLMs: Retrieving and Steering High-Order Semantic Features via Sparse Autoencoders
---

# Mechanistic Knobs in LLMs: Retrieving and Steering High-Order Semantic Features via Sparse Autoencoders
**arXiv**：[2601.02978v1](https://arxiv.org/abs/2601.02978) · [PDF](https://arxiv.org/pdf/2601.02978.pdf)  
**作者**：Ruikang Zhang, Shuo Wang, Qi Su  

**一句话要点**：提出基于稀疏自编码器的框架，以检索和操控大语言模型中的高阶语义特征，实现行为级控制。

**关键词**：大语言模型, 机制可解释性, 稀疏自编码器, 特征检索, 行为操控, 语义属性

## 3 点简述
- 核心问题：如何可靠地将大语言模型内部特征链接到复杂行为级语义属性的控制。
- 方法要点：采用基于对比特征检索的稀疏自编码器框架，结合统计激活分析和生成验证。
- 实验或效果：以五大人格特质为例，实现精确双向行为操控，优于现有方法如对比激活加法。

## 摘要（原文）

> Recent work in Mechanistic Interpretability (MI) has enabled the identification and intervention of internal features in Large Language Models (LLMs). However, a persistent challenge lies in linking such internal features to the reliable control of complex, behavior-level semantic attributes in language generation. In this paper, we propose a Sparse Autoencoder-based framework for retrieving and steering semantically interpretable internal features associated with high-level linguistic behaviors. Our method employs a contrastive feature retrieval pipeline based on controlled semantic oppositions, combing statistical activation analysis and generation-based validation to distill monosemantic functional features from sparse activation spaces. Using the Big Five personality traits as a case study, we demonstrate that our method enables precise, bidirectional steering of model behavior while maintaining superior stability and performance compared to existing activation steering methods like Contrastive Activation Addition (CAA). We further identify an empirical effect, which we term Functional Faithfulness, whereby intervening on a specific internal feature induces coherent and predictable shifts across multiple linguistic dimensions aligned with the target semantic attribute. Our findings suggest that LLMs internalize deeply integrated representations of high-order concepts, and provide a novel, robust mechanistic path for the regulation of complex AI behaviors.

