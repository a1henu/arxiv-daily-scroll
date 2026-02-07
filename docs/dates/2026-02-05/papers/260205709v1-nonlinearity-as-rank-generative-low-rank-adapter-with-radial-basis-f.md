---
layout: default
title: Nonlinearity as Rank: Generative Low-Rank Adapter with Radial Basis Functions
---

# Nonlinearity as Rank: Generative Low-Rank Adapter with Radial Basis Functions
**arXiv**：[2602.05709v1](https://arxiv.org/abs/2602.05709) · [PDF](https://arxiv.org/pdf/2602.05709.pdf)  
**作者**：Yihao Ouyang, Shiwei Li, Haozhao Wang, Xiandi Luo, Zhuoqi Hu, Yuetong Song, Qiyu Qin, Yichen Li, Ruixuan Li  

**一句话要点**：提出GenLoRA以解决低秩适配中参数冗余问题，通过非线性基向量生成提升参数效率。

**关键词**：低秩适配, 参数效率, 径向基函数, 微调优化, 生成式模型

## 3 点简述
- 标准LoRA采用显式基向量存储，增加模型容量导致参数大幅增长。
- GenLoRA用径向基函数生成基向量，减少参数冗余，实现更高参数效率。
- 实验表明GenLoRA在较小参数预算下获得更高有效秩，微调性能更优。

## 摘要（原文）

> Low-rank adaptation (LoRA) approximates the update of a pretrained weight matrix using the product of two low-rank matrices. However, standard LoRA follows an explicit-rank paradigm, where increasing model capacity requires adding more rows or columns (i.e., basis vectors) to the low-rank matrices, leading to substantial parameter growth. In this paper, we find that these basis vectors exhibit significant parameter redundancy and can be compactly represented by lightweight nonlinear functions. Therefore, we propose Generative Low-Rank Adapter (GenLoRA), which replaces explicit basis vector storage with nonlinear basis vector generation. Specifically, GenLoRA maintains a latent vector for each low-rank matrix and employs a set of lightweight radial basis functions (RBFs) to synthesize the basis vectors. Each RBF requires far fewer parameters than an explicit basis vector, enabling higher parameter efficiency in GenLoRA. Extensive experiments across multiple datasets and architectures show that GenLoRA attains higher effective LoRA ranks under smaller parameter budgets, resulting in superior fine-tuning performance. The code is available at https://anonymous.4open.science/r/GenLoRA-1519.

