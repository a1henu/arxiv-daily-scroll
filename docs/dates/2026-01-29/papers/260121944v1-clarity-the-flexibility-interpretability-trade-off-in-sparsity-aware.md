---
layout: default
title: Clarity: The Flexibility-Interpretability Trade-Off in Sparsity-aware Concept Bottleneck Models
---

# Clarity: The Flexibility-Interpretability Trade-Off in Sparsity-aware Concept Bottleneck Models
**arXiv**：[2601.21944v1](https://arxiv.org/abs/2601.21944) · [PDF](https://arxiv.org/pdf/2601.21944.pdf)  
**作者**：Konstantinos P. Panousis, Diego Marcos  

**一句话要点**：提出清晰度概念以评估概念瓶颈模型在稀疏性下的灵活性与可解释性权衡

**关键词**：概念瓶颈模型, 稀疏性方法, 可解释性评估, 视觉语言模型, 清晰度度量

## 3 点简述
- 核心问题：视觉语言模型可解释性评估不足，稀疏性方法缺乏系统性分析
- 方法要点：引入清晰度度量，结合下游性能、稀疏性和精度，评估概念表示
- 实验或效果：比较不同稀疏策略，揭示灵活性与可解释性间的关键权衡

## 摘要（原文）

> The widespread adoption of Vision-Language Models (VLMs) across fields has amplified concerns about model interpretability. Distressingly, these models are often treated as black-boxes, with limited or non-existent investigation of their decision making process. Despite numerous post- and ante-hoc interepretability methods, systematic and objective evaluation of the learned representations remains limited, particularly for sparsity-aware methods that are increasingly considered to "induce interpretability". In this work, we focus on Concept Bottleneck Models and investigate how different modeling decisions affect the emerging representations. We introduce the notion of clarity, a measure, capturing the interplay between the downstream performance and the sparsity and precision of the concept representation, while proposing an interpretability assessment framework using datasets with ground truth concept annotations. We consider both VLM- and attribute predictor-based CBMs, and three different sparsity-inducing strategies: per example $\ell_1, \ell_0$ and Bernoulli-based formulations. Our experiments reveal a critical trade-off between flexibility and interpretability, under which a given method can exhibit markedly different behaviors even at comparable performance levels. The code will be made publicly available upon publication.

