---
layout: default
title: Mechanistic Interpretability for Transformer-based Time Series Classification
---

# Mechanistic Interpretability for Transformer-based Time Series Classification
**arXiv**：[2511.21514v1](https://arxiv.org/abs/2511.21514) · [PDF](https://arxiv.org/pdf/2511.21514.pdf)  
**作者**：Matīss Kalnāre, Sofoklis Kitharidis, Thomas Bäck, Niki van Stein  

**一句话要点**：提出机制可解释性方法以解决时间序列分类中Transformer模型内部机制不透明问题

**关键词**：机制可解释性, 时间序列分类, Transformer模型, 注意力机制, 因果图, 稀疏自编码器

## 3 点简述
- 核心问题：Transformer模型在时间序列分类中内部决策机制复杂且难以理解
- 方法要点：从NLP引入激活修补、注意力显著性和稀疏自编码器进行机制可解释性分析
- 实验或效果：在基准数据集上构建因果图，揭示关键注意力头和时序位置的作用

## 摘要（原文）

> Transformer-based models have become state-of-the-art tools in various machine learning tasks, including time series classification, yet their complexity makes understanding their internal decision-making challenging. Existing explainability methods often focus on input-output attributions, leaving the internal mechanisms largely opaque. This paper addresses this gap by adapting various Mechanistic Interpretability techniques; activation patching, attention saliency, and sparse autoencoders, from NLP to transformer architectures designed explicitly for time series classification. We systematically probe the internal causal roles of individual attention heads and timesteps, revealing causal structures within these models. Through experimentation on a benchmark time series dataset, we construct causal graphs illustrating how information propagates internally, highlighting key attention heads and temporal positions driving correct classifications. Additionally, we demonstrate the potential of sparse autoencoders for uncovering interpretable latent features. Our findings provide both methodological contributions to transformer interpretability and novel insights into the functional mechanics underlying transformer performance in time series classification tasks.

