---
layout: default
title: Towards Mass Spectrum Analysis with ASP
---

# Towards Mass Spectrum Analysis with ASP
**arXiv**：[2512.16780v1](https://arxiv.org/abs/2512.16780) · [PDF](https://arxiv.org/pdf/2512.16780.pdf)  
**作者**：Nils Küchenmeister, Alex Ivliev, Markus Krötzsch  

**一句话要点**：提出基于答案集编程的分子结构发现方法，用于质谱数据分析。

**关键词**：答案集编程, 质谱分析, 分子结构发现, 组合优化, 对称性打破

## 3 点简述
- 核心问题：质谱数据中分子结构的组合搜索空间指数级增长，需高效约束。
- 方法要点：开发分子结构的规范表示，并基于此实现答案集编程以限制搜索。
- 实验或效果：在大规模已知分子结构上验证正确性，并与对称性打破方法及商业工具比较性能。

## 摘要（原文）

> We present a new use of Answer Set Programming (ASP) to discover the molecular structure of chemical samples based on the relative abundance of elements and structural fragments, as measured in mass spectrometry. To constrain the exponential search space for this combinatorial problem, we develop canonical representations of molecular structures and an ASP implemen- tation that uses these definitions. We evaluate the correctness of our implementation over a large set of known molecular structures, and we compare its quality and performance to other ASP symmetry-breaking methods and to a commercial tool from analytical chemistry. Under consideration in Theory and Practice of Logic Programming (TPLP).

