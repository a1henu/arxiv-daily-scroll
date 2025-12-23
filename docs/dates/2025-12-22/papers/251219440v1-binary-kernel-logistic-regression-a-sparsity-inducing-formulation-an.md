---
layout: default
title: Binary Kernel Logistic Regression: a sparsity-inducing formulation and a convergent decomposition training algorithm
---

# Binary Kernel Logistic Regression: a sparsity-inducing formulation and a convergent decomposition training algorithm
**arXiv**：[2512.19440v1](https://arxiv.org/abs/2512.19440) · [PDF](https://arxiv.org/pdf/2512.19440.pdf)  
**作者**：Antonio Consolo, Andrea Manno, Edoardo Amaldi  

**一句话要点**：提出稀疏诱导的二元核逻辑回归及其收敛分解训练算法，以平衡预测准确性与稀疏性。

**关键词**：核逻辑回归, 稀疏诱导, 分解算法, 二元分类, 收敛性分析, 概率估计

## 3 点简述
- 核心问题：核逻辑回归缺乏稀疏性，影响模型效率与应用。
- 方法要点：扩展Keerthi等人训练公式，结合二阶信息的序列最小优化分解算法。
- 实验或效果：在12个数据集上验证，实现准确性与稀疏性的竞争性权衡。

## 摘要（原文）

> Kernel logistic regression (KLR) is a widely used supervised learning method for binary and multi-class classification, which provides estimates of the conditional probabilities of class membership for the data points. Unlike other kernel methods such as Support Vector Machines (SVMs), KLRs are generally not sparse. Previous attempts to deal with sparsity in KLR include a heuristic method referred to as the Import Vector Machine (IVM) and ad hoc regularizations such as the $\ell_{1/2}$-based one. Achieving a good trade-off between prediction accuracy and sparsity is still a challenging issue with a potential significant impact from the application point of view. In this work, we revisit binary KLR and propose an extension of the training formulation proposed by Keerthi et al., which is able to induce sparsity in the trained model, while maintaining good testing accuracy. To efficiently solve the dual of this formulation, we devise a decomposition algorithm of Sequential Minimal Optimization type which exploits second-order information, and for which we establish global convergence. Numerical experiments conducted on 12 datasets from the literature show that the proposed binary KLR approach achieves a competitive trade-off between accuracy and sparsity with respect to IVM, $\ell_{1/2}$-based regularization for KLR, and SVM while retaining the advantages of providing informative estimates of the class membership probabilities.

