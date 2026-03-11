---
layout: default
title: ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph
---

# ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph
**arXiv**：[2603.09266v1](https://arxiv.org/abs/2603.09266) · [PDF](https://arxiv.org/pdf/2603.09266.pdf)  
**作者**：Junhao Cai, Deyu Zeng, Junhao Pang, Lini Li, Zongze Wu, Xiaopin Zhong  

**一句话要点**：提出ForgeDreamer框架，通过多专家LoRA集成和跨视图超图增强解决工业文本到3D生成的领域适应和几何推理问题。

**关键词**：文本到3D生成, 工业应用, LoRA集成, 超图建模, 几何增强, 领域适应

## 3 点简述
- 核心问题：现有方法在工业应用中面临领域适应挑战和几何推理不足，导致知识干扰和结构依赖捕捉不充分。
- 方法要点：引入多专家LoRA集成机制消除知识干扰，并开发跨视图超图几何增强方法捕获多视角结构依赖。
- 实验或效果：在自定义工业数据集上实验显示，相比先进方法，具有更优的语义泛化和几何保真度。

## 摘要（原文）

> Current text-to-3D generation methods excel in natural scenes but struggle with industrial applications due to two critical limitations: domain adaptation challenges where conventional LoRA fusion causes knowledge interference across categories, and geometric reasoning deficiencies where pairwise consistency constraints fail to capture higher-order structural dependencies essential for precision manufacturing. We propose a novel framework named ForgeDreamer addressing both challenges through two key innovations. First, we introduce a Multi-Expert LoRA Ensemble mechanism that consolidates multiple category-specific LoRA models into a unified representation, achieving superior cross-category generalization while eliminating knowledge interference. Second, building on enhanced semantic understanding, we develop a Cross-View Hypergraph Geometric Enhancement approach that captures structural dependencies spanning multiple viewpoints simultaneously. These components work synergistically improved semantic understanding, enables more effective geometric reasoning, while hypergraph modeling ensures manufacturing-level consistency. Extensive experiments on a custom industrial dataset demonstrate superior semantic generalization and enhanced geometric fidelity compared to state-of-the-art approaches. Our code and data are provided in the supplementary material attached in the appendix for review purposes.

