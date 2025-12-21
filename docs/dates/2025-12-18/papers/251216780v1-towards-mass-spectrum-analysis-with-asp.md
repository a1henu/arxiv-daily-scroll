---
layout: default
title: Towards Mass Spectrum Analysis with ASP
---

# Towards Mass Spectrum Analysis with ASP
**arXiv**：[2512.16780v1](https://arxiv.org/abs/2512.16780) · [PDF](https://arxiv.org/pdf/2512.16780.pdf)  
**作者**：Nils Küchenmeister, Alex Ivliev, Markus Krötzsch  

**一句话要点**：提出基于答案集编程的分子结构发现方法，用于质谱数据分析

**关键词**：答案集编程, 质谱分析, 分子结构发现, 组合优化, 对称性打破

## 3 点简述
- 核心问题：基于质谱测量的元素和结构片段相对丰度，解决分子结构发现的组合搜索空间爆炸问题
- 方法要点：开发分子结构的规范表示和ASP实现，以约束搜索空间
- 实验或效果：在大规模已知分子结构上评估正确性，并与ASP对称性打破方法及商业工具比较性能

## 摘要（原文）

> We present a new use of Answer Set Programming (ASP) to discover the molecular structure of chemical samples based on the relative abundance of elements and structural fragments, as measured in mass spectrometry. To constrain the exponential search space for this combinatorial problem, we develop canonical representations of molecular structures and an ASP implementation that uses these definitions. We evaluate the correctness of our implementation over a large set of known molecular structures, and we compare its quality and performance to other ASP symmetry-breaking methods and to a commercial tool from analytical chemistry. Under consideration in Theory and Practice of Logic Programming (TPLP).

