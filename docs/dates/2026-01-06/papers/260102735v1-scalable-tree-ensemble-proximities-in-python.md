---
layout: default
title: Scalable Tree Ensemble Proximities in Python
---

# Scalable Tree Ensemble Proximities in Python
**arXiv**：[2601.02735v1](https://arxiv.org/abs/2601.02735) · [PDF](https://arxiv.org/pdf/2601.02735.pdf)  
**作者**：Adrien Aumon, Guy Wolf, Kevin R. Moon, Jake S. Rhodes  

**一句话要点**：提出可分离加权叶碰撞邻近度框架，以解决树集成邻近度计算的可扩展性问题。

**关键词**：树集成邻近度, 稀疏矩阵分解, 可扩展计算, Python实现, 随机森林

## 3 点简述
- 树集成方法如随机森林的邻近度计算存在二次复杂度，限制可扩展性。
- 定义可分离加权叶碰撞邻近度族，通过稀疏矩阵分解避免显式成对比较。
- 实验显示在标准CPU上实现低内存、高效计算，可处理数十万样本数据集。

## 摘要（原文）

> Tree ensemble methods such as Random Forests naturally induce supervised similarity measures through their decision tree structure, but existing implementations of proximities derived from tree ensembles typically suffer from quadratic time or memory complexity, limiting their scalability. In this work, we introduce a general framework for efficient proximity computation by defining a family of Separable Weighted Leaf-Collision Proximities. We show that any proximity measure in this family admits an exact sparse matrix factorization, restricting computation to leaf-level collisions and avoiding explicit pairwise comparisons. This formulation enables low-memory, scalable proximity computation using sparse linear algebra in Python. Empirical benchmarks demonstrate substantial runtime and memory improvements over traditional approaches, allowing tree ensemble proximities to scale efficiently to datasets with hundreds of thousands of samples on standard CPU hardware.

