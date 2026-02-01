---
layout: default
title: Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
---

# Mechanistic Data Attribution: Tracing the Training Origins of Interpretable LLM Units
**arXiv**：[2601.21996v1](https://arxiv.org/abs/2601.21996) · [PDF](https://arxiv.org/pdf/2601.21996.pdf)  
**作者**：Jianhui Chen, Yuzhang Luo, Liangming Pan  

**一句话要点**：提出可扩展的机制数据归因框架，以追踪大语言模型中可解释单元的因果训练起源。

**关键词**：机制可解释性, 数据归因, 影响函数, 可解释单元, 上下文学习, 数据增强

## 3 点简述
- 核心问题：机制可解释性已识别大语言模型中的可解释电路，但其在训练数据中的因果起源尚不明确。
- 方法要点：引入机制数据归因，利用影响函数将可解释单元回溯到特定训练样本。
- 实验或效果：通过干预高影响样本，验证了可解释头部的形成与模型上下文学习能力的因果关联。

## 摘要（原文）

> While Mechanistic Interpretability has identified interpretable circuits in LLMs, their causal origins in training data remain elusive. We introduce Mechanistic Data Attribution (MDA), a scalable framework that employs Influence Functions to trace interpretable units back to specific training samples. Through extensive experiments on the Pythia family, we causally validate that targeted intervention--removing or augmenting a small fraction of high-influence samples--significantly modulates the emergence of interpretable heads, whereas random interventions show no effect. Our analysis reveals that repetitive structural data (e.g., LaTeX, XML) acts as a mechanistic catalyst. Furthermore, we observe that interventions targeting induction head formation induce a concurrent change in the model's in-context learning (ICL) capability. This provides direct causal evidence for the long-standing hypothesis regarding the functional link between induction heads and ICL. Finally, we propose a mechanistic data augmentation pipeline that consistently accelerates circuit convergence across model scales, providing a principled methodology for steering the developmental trajectories of LLMs.

