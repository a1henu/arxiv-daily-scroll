---
layout: default
title: Forget Less by Learning from Parents Through Hierarchical Relationships
---

# Forget Less by Learning from Parents Through Hierarchical Relationships
**arXiv**：[2601.01892v1](https://arxiv.org/abs/2601.01892) · [PDF](https://arxiv.org/pdf/2601.01892.pdf)  
**作者**：Arjun Ramesh Kaushik, Naresh Kumar Devulapally, Vishnu Suresh Lokhande, Nalini K. Ratha, Venu Govindaraju  

**一句话要点**：提出FLLP框架，通过双曲空间中的父子关系学习缓解定制扩散模型的灾难性遗忘问题。

**关键词**：定制扩散模型, 灾难性遗忘, 双曲空间, 父子关系学习, 洛伦兹流形, 顺序学习

## 3 点简述
- 核心问题：定制扩散模型在顺序学习新概念时易发生灾难性遗忘，现有方法忽视概念间正面交互。
- 方法要点：在洛伦兹流形中嵌入概念表示，利用父子关系引导新概念适应，促进知识保留与整合。
- 实验或效果：在三个公共数据集和一个合成基准上验证，显示在鲁棒性和泛化性方面持续改进。

## 摘要（原文）

> Custom Diffusion Models (CDMs) offer impressive capabilities for personalization in generative modeling, yet they remain vulnerable to catastrophic forgetting when learning new concepts sequentially. Existing approaches primarily focus on minimizing interference between concepts, often neglecting the potential for positive inter-concept interactions. In this work, we present Forget Less by Learning from Parents (FLLP), a novel framework that introduces a parent-child inter-concept learning mechanism in hyperbolic space to mitigate forgetting. By embedding concept representations within a Lorentzian manifold, naturally suited to modeling tree-like hierarchies, we define parent-child relationships in which previously learned concepts serve as guidance for adapting to new ones. Our method not only preserves prior knowledge but also supports continual integration of new concepts. We validate FLLP on three public datasets and one synthetic benchmark, showing consistent improvements in both robustness and generalization.

