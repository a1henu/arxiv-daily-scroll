---
layout: default
title: Multi-context principal component analysis
---

# Multi-context principal component analysis
**arXiv**：[2601.15239v1](https://arxiv.org/abs/2601.15239) · [PDF](https://arxiv.org/pdf/2601.15239.pdf)  
**作者**：Kexin Wang, Salil Bhate, João M. Pereira, Joe Kileel, Matylda Figlerowicz, Anna Seigal  

**一句话要点**：提出多上下文主成分分析以分解跨上下文共享的数据因子

**关键词**：多上下文主成分分析, 数据分解, 基因表达分析, 词嵌入, 变异因子, 跨上下文学习

## 3 点简述
- 核心问题：现有工具无法系统恢复跨上下文子集共享的数据变异因子
- 方法要点：开发理论算法框架，将数据分解为跨上下文子集共享的因子
- 实验或效果：应用于基因表达和词嵌入，揭示癌症类型共享变异轴和辩论阶段映射

## 摘要（原文）

> Principal component analysis (PCA) is a tool to capture factors that explain variation in data. Across domains, data are now collected across multiple contexts (for example, individuals with different diseases, cells of different types, or words across texts). While the factors explaining variation in data are undoubtedly shared across subsets of contexts, no tools currently exist to systematically recover such factors. We develop multi-context principal component analysis (MCPCA), a theoretical and algorithmic framework that decomposes data into factors shared across subsets of contexts. Applied to gene expression, MCPCA reveals axes of variation shared across subsets of cancer types and an axis whose variability in tumor cells, but not mean, is associated with lung cancer progression. Applied to contextualized word embeddings from language models, MCPCA maps stages of a debate on human nature, revealing a discussion between science and fiction over decades. These axes are not found by combining data across contexts or by restricting to individual contexts. MCPCA is a principled generalization of PCA to address the challenge of understanding factors underlying data across contexts.

