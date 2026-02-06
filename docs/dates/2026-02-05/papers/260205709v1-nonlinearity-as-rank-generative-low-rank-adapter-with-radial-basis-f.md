---
layout: default
title: Nonlinearity as Rank: Generative Low-Rank Adapter with Radial Basis Functions
---

# Nonlinearity as Rank: Generative Low-Rank Adapter with Radial Basis Functions
**arXiv**：[2602.05709v1](https://arxiv.org/abs/2602.05709) · [PDF](https://arxiv.org/pdf/2602.05709.pdf)  
**作者**：Yihao Ouyang, Shiwei Li, Haozhao Wang, Xiandi Luo, Zhuoqi Hu, Yuetong Song, Qiyu Qin, Yichen Li, Ruixuan Li  

**一句话要点**：提出GenLoRA，用径向基函数生成低秩基向量以提升参数效率

**关键词**：低秩适配, 参数效率, 径向基函数, 微调, 生成模型, 模型压缩

## 3 点简述
- 标准LoRA显式存储基向量导致参数冗余和增长问题
- GenLoRA通过非线性函数生成基向量，减少存储参数
- 实验显示在更小参数预算下实现更高有效秩和更好微调性能

## 摘要（原文）

> Low-rank adaptation (LoRA) approximates the update of a pretrained weight matrix using the product of two low-rank matrices. However, standard LoRA follows an explicit-rank paradigm, where increasing model capacity requires adding more rows or columns (i.e., basis vectors) to the low-rank matrices, leading to substantial parameter growth. In this paper, we find that these basis vectors exhibit significant parameter redundancy and can be compactly represented by lightweight nonlinear functions. Therefore, we propose Generative Low-Rank Adapter (GenLoRA), which replaces explicit basis vector storage with nonlinear basis vector generation. Specifically, GenLoRA maintains a latent vector for each low-rank matrix and employs a set of lightweight radial basis functions (RBFs) to synthesize the basis vectors. Each RBF requires far fewer parameters than an explicit basis vector, enabling higher parameter efficiency in GenLoRA. Extensive experiments across multiple datasets and architectures show that GenLoRA attains higher effective LoRA ranks under smaller parameter budgets, resulting in superior fine-tuning performance. The code is available at https://anonymous.4open.science/r/GenLoRA-1519.

