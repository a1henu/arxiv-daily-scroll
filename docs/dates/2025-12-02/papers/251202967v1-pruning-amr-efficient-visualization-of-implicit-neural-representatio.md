---
layout: default
title: Pruning AMR: Efficient Visualization of Implicit Neural Representations via Weight Matrix Analysis
---

# Pruning AMR: Efficient Visualization of Implicit Neural Representations via Weight Matrix Analysis
**arXiv**：[2512.02967v1](https://arxiv.org/abs/2512.02967) · [PDF](https://arxiv.org/pdf/2512.02967.pdf)  
**作者**：Jennifer Zvonek, Andrew Gillette  

**一句话要点**：提出PruningAMR算法，通过权重矩阵分析实现隐式神经表示的高效可视化

**关键词**：隐式神经表示, 自适应网格细化, 权重矩阵分析, 内存优化, 可视化算法

## 3 点简述
- 核心问题：隐式神经表示在可视化时需离散化到规则网格，导致内存消耗大
- 方法要点：使用插值分解剪枝方法分析权重矩阵，识别几何特征以指导自适应网格细化
- 实验或效果：从预训练INR生成可变分辨率可视化，显著节省内存，无需访问训练数据

## 摘要（原文）

> An implicit neural representation (INR) is a neural network that approximates a spatiotemporal function. Many memory-intensive visualization tasks, including modern 4D CT scanning methods, represent data natively as INRs. While INRs are prized for being more memory-efficient than traditional data stored on a lattice, many visualization tasks still require discretization to a regular grid. We present PruningAMR, an algorithm that builds a mesh with resolution adapted to geometric features encoded by the INR. To identify these geometric features, we use an interpolative decomposition pruning method on the weight matrices of the INR. The resulting pruned network is used to guide adaptive mesh refinement, enabling automatic mesh generation tailored to the underlying resolution of the function. Starting from a pre-trained INR--without access to its training data--we produce a variable resolution visualization with substantial memory savings.

