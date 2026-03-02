---
layout: default
title: Learning Generation Orders for Masked Discrete Diffusion Models via Variational Inference
---

# Learning Generation Orders for Masked Discrete Diffusion Models via Variational Inference
**arXiv**：[2602.23968v1](https://arxiv.org/abs/2602.23968) · [PDF](https://arxiv.org/pdf/2602.23968.pdf)  
**作者**：David Fox, Sam Bowyer, Song Liu, Laurence Aitchison, Raul Santos-Rodriguez, Mengyue Yang  

**一句话要点**：提出基于变分推断的生成顺序学习方法，以优化掩码离散扩散模型的并行生成与样本质量平衡。

**关键词**：掩码离散扩散模型, 并行生成, 变分推断, 生成顺序学习, 样本质量优化

## 3 点简述
- 核心问题：掩码离散扩散模型在并行生成与样本质量间难以取得最优平衡，现有方法多依赖固定启发式策略。
- 方法要点：通过变分推断框架学习生成顺序，设计近似后验参数化以支持训练中的并行性和高效采样。
- 实验或效果：在GSM8K数据集上初步实验，高度并行生成下性能优于标准方法，如4步生成达到33.1%准确率。

## 摘要（原文）

> Masked discrete diffusion models (MDMs) are a promising new approach to generative modelling, offering the ability for parallel token generation and therefore greater efficiency than autoregressive counterparts. However, achieving an optimal balance between parallel generation and sample quality remains an open problem. Current approaches primarily address this issue through fixed, heuristic parallel sampling methods. There exist some recent learning based approaches to this problem, but its formulation from the perspective of variational inference remains underexplored. In this work, we propose a variational inference framework for learning parallel generation orders for MDMs. As part of our method, we propose a parameterisation for the approximate posterior of generation orders which facilitates parallelism and efficient sampling during training. Using this method, we conduct preliminary experiments on the GSM8K dataset, where our method performs competitively against heuristic sampling strategies in the regime of highly parallel generation. For example, our method achieves 33.1\% accuracy with an average of only only 4 generation steps, compared to 23.7-29.0\% accuracy achieved by standard competitor methods in the same number of steps. We believe further experiments and analysis of the method will yield valuable insights into the problem of parallel generation with MDMs.

