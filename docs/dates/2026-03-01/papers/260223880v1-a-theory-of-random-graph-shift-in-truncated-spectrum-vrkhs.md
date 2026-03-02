---
layout: default
title: A Theory of Random Graph Shift in Truncated-Spectrum vRKHS
---

# A Theory of Random Graph Shift in Truncated-Spectrum vRKHS
**arXiv**：[2602.23880v1](https://arxiv.org/abs/2602.23880) · [PDF](https://arxiv.org/pdf/2602.23880.pdf)  
**作者**：Zhang Wan, Tingting Mu, Samuel Kaski  

**一句话要点**：提出基于随机图模型和截断谱vRKHS的图分类域适应理论，以分析图分布偏移。

**关键词**：图分类, 域适应, 随机图模型, 向量值再生核希尔伯特空间, 谱分析, 泛化界

## 3 点简述
- 核心问题：图分类中的域适应，因图非欧几里得特性和专用架构，导致分布偏移分析复杂。
- 方法要点：假设随机图模型为数据生成过程，在vRKHS中推导泛化界，分解偏移惩罚为域差异、谱几何和振幅项。
- 实验或效果：在真实数据和模拟中实证验证理论项，支持对图分布偏移的细粒度分析。

## 摘要（原文）

> This paper develops a theory of graph classification under domain shift through a random-graph generative lens, where we consider intra-class graphs sharing the same random graph model (RGM) and the domain shift induced by changes in RGM components. While classic domain adaptation (DA) theories have well-underpinned existing techniques to handle graph distribution shift, the information of graph samples, which are itself structured objects, is less explored. The non-Euclidean nature of graphs and specialized architectures for graph learning further complicate a fine-grained analysis of graph distribution shifts. In this paper, we propose a theory that assumes RGM as the data generative process, exploiting its connection to hypothesis complexity in function space perspective for such fine-grained analysis. Building on a vector-valued reproducing kernel Hilbert space (vRKHS) formulation, we derive a generalization bound whose shift penalty admits a factorization into (i) a domain discrepancy term, (ii) a spectral-geometry term summarized by the accessible truncated spectrum, and (iii) an amplitude term that aggregates convergence and construction-stability effects. We empirically verify the insights on these terms in both real data and simulations.

