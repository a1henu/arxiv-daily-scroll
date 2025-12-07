---
layout: default
title: Evolutionary Architecture Search through Grammar-Based Sequence Alignment
---

# Evolutionary Architecture Search through Grammar-Based Sequence Alignment
**arXiv**：[2512.04992v1](https://arxiv.org/abs/2512.04992) · [PDF](https://arxiv.org/pdf/2512.04992.pdf)  
**作者**：Adri Gómez Martín, Felix Möller, Steven McDonagh, Monica Abella, Manuel Desco, Elliot J. Crowley, Aaron Klein, Linus Ericsson  

**一句话要点**：提出基于语法序列对齐的进化架构搜索方法，以高效计算神经架构距离并生成混合后代。

**关键词**：神经架构搜索, 进化算法, 序列对齐, 语法表示, 计算复杂度, 交叉操作

## 3 点简述
- 核心问题：神经架构搜索在表达性搜索空间中计算复杂度高，需有效算法识别和重用强大组件。
- 方法要点：引入两种Smith-Waterman算法变体，用于语法进化搜索中的编辑距离计算和杂交后代生成。
- 实验或效果：方法显著降低计算复杂度，实现竞争性结果，支持架构损失分析和种群多样性追踪。

## 摘要（原文）

> Neural architecture search (NAS) in expressive search spaces is a computationally hard problem, but it also holds the potential to automatically discover completely novel and performant architectures. To achieve this we need effective search algorithms that can identify powerful components and reuse them in new candidate architectures. In this paper, we introduce two adapted variants of the Smith-Waterman algorithm for local sequence alignment and use them to compute the edit distance in a grammar-based evolutionary architecture search. These algorithms enable us to efficiently calculate a distance metric for neural architectures and to generate a set of hybrid offspring from two parent models. This facilitates the deployment of crossover-based search heuristics, allows us to perform a thorough analysis on the architectural loss landscape, and track population diversity during search. We highlight how our method vastly improves computational complexity over previous work and enables us to efficiently compute shortest paths between architectures. When instantiating the crossover in evolutionary searches, we achieve competitive results, outperforming competing methods. Future work can build upon this new tool, discovering novel components that can be used more broadly across neural architecture design, and broadening its applications beyond NAS.

