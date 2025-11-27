---
layout: default
title: Learning Cell-Aware Hierarchical Multi-Modal Representations for Robust Molecular Modeling
---

# Learning Cell-Aware Hierarchical Multi-Modal Representations for Robust Molecular Modeling
**arXiv**：[2511.21120v1](https://arxiv.org/abs/2511.21120) · [PDF](https://arxiv.org/pdf/2511.21120.pdf)  
**作者**：Mengran Li, Zelin Zang, Wenbin Xing, Junzhou Chen, Ronghui Zhang, Jiebo Luo, Stan Z. Li  

**一句话要点**：提出CHMR框架以解决分子建模中细胞感知多模态表示不完整和层次依赖不足问题

**关键词**：分子建模, 多模态表示, 层次依赖, 细胞感知, 向量量化, 生物医学建模

## 3 点简述
- 核心问题：现有方法忽视细胞响应，且多模态数据不完整和层次依赖建模不足
- 方法要点：联合建模分子与细胞响应的局部-全局依赖，通过树状向量量化捕获生物层次
- 实验或效果：在9个基准728个任务上，分类和回归任务平均提升3.6%和17.2%

## 摘要（原文）

> Understanding how chemical perturbations propagate through biological systems is essential for robust molecular property prediction. While most existing methods focus on chemical structures alone, recent advances highlight the crucial role of cellular responses such as morphology and gene expression in shaping drug effects. However, current cell-aware approaches face two key limitations: (1) modality incompleteness in external biological data, and (2) insufficient modeling of hierarchical dependencies across molecular, cellular, and genomic levels. We propose CHMR (Cell-aware Hierarchical Multi-modal Representations), a robust framework that jointly models local-global dependencies between molecules and cellular responses and captures latent biological hierarchies via a novel tree-structured vector quantization module. Evaluated on nine public benchmarks spanning 728 tasks, CHMR outperforms state-of-the-art baselines, yielding average improvements of 3.6% on classification and 17.2% on regression tasks. These results demonstrate the advantage of hierarchy-aware, multimodal learning for reliable and biologically grounded molecular representations, offering a generalizable framework for integrative biomedical modeling. The code is in https://github.com/limengran98/CHMR.

