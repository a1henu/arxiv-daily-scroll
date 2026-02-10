---
layout: default
title: Data Reconstruction: Identifiability and Optimization with Sample Splitting
---

# Data Reconstruction: Identifiability and Optimization with Sample Splitting
**arXiv**：[2602.08723v1](https://arxiv.org/abs/2602.08723) · [PDF](https://arxiv.org/pdf/2602.08723.pdf)  
**作者**：Yujie Shen, Zihan Wang, Jian Qian, Qi Lei  

**一句话要点**：提出样本分割方法以优化数据重构的识别性与优化问题

**关键词**：数据重构, KKT条件, 识别性分析, 优化方法, 样本分割, 神经网络

## 3 点简述
- 研究基于KKT条件的数据重构中识别性与优化两大互补问题
- 提供两层网络多项式激活下KKT系统唯一解的理论条件
- 引入样本分割方法提升重构性能，实验验证其有效性

## 摘要（原文）

> Training data reconstruction from KKT conditions has shown striking empirical success, yet it remains unclear when the resulting KKT equations have unique solutions and, even in identifiable regimes, how to reliably recover solutions by optimization. This work hereby focuses on these two complementary questions: identifiability and optimization. On the identifiability side, we discuss the sufficient conditions for KKT system of two-layer networks with polynomial activations to uniquely determine the training data, providing a theoretical explanation of when and why reconstruction is possible. On the optimization side, we introduce sample splitting, a curvature-aware refinement step applicable to general reconstruction objectives (not limited to KKT-based formulations): it creates additional descent directions to escape poor stationary points and refine solutions. Experiments demonstrate that augmenting several existing reconstruction methods with sample splitting consistently improves reconstruction performance.

