---
layout: default
title: NEAT: Neighborhood-Guided, Efficient, Autoregressive Set Transformer for 3D Molecular Generation
---

# NEAT: Neighborhood-Guided, Efficient, Autoregressive Set Transformer for 3D Molecular Generation
**arXiv**：[2512.05844v1](https://arxiv.org/abs/2512.05844) · [PDF](https://arxiv.org/pdf/2512.05844.pdf)  
**作者**：Daniel Rose, Roxane Axel Jacob, Johannes Kirchmair, Thierry Langer  

**一句话要点**：提出NEAT以解决3D分子生成中自回归模型对原子顺序的依赖问题

**关键词**：3D分子生成, 自回归模型, 置换不变性, 集合变换器, 流模型

## 3 点简述
- 核心问题：自回归模型在3D分子生成中需假设原子顺序，与分子图的无序性不匹配
- 方法要点：NEAT将分子图视为原子集合，通过邻域引导的自回归流模型学习顺序无关的边界令牌分布
- 实验或效果：NEAT在3D分子生成中达到先进性能，具有高计算效率和原子级置换不变性

## 摘要（原文）

> Autoregressive models are a promising alternative to diffusion-based models for 3D molecular structure generation. However, a key limitation is the assumption of a token order: while text has a natural sequential order, the next token prediction given a molecular graph prefix should be invariant to atom permutations. Previous works sidestepped this mismatch by using canonical orders or focus atoms. We argue that this is unnecessary. We introduce NEAT, a Neighborhood-guided, Efficient, Autoregressive, Set Transformer that treats molecular graphs as sets of atoms and learns the order-agnostic distribution over admissible tokens at the graph boundary with an autoregressive flow model. NEAT approaches state-of-the-art performance in 3D molecular generation with high computational efficiency and atom-level permutation invariance, establishing a practical foundation for scalable molecular design.

