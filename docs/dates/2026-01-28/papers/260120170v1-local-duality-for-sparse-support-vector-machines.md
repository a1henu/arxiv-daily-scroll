---
layout: default
title: Local Duality for Sparse Support Vector Machines
---

# Local Duality for Sparse Support Vector Machines
**arXiv**：[2601.20170v1](https://arxiv.org/abs/2601.20170) · [PDF](https://arxiv.org/pdf/2601.20170.pdf)  
**作者**：Penghe Zhang, Naihua Xiu, Houduo Qi  

**一句话要点**：提出局部对偶理论以解决稀疏支持向量机缺乏理论依据的问题

**关键词**：稀疏支持向量机, 局部对偶理论, 基数最小化, 支持向量机, 机器学习优化

## 3 点简述
- 核心问题：稀疏支持向量机（SSVM）通过添加基数函数到凸SVM对偶问题中，但缺乏理论支撑。
- 方法要点：建立SSVM的局部对偶理论，证明其与0/1损失SVM对偶等价，并关联铰链损失和斜坡损失SVM。
- 实验或效果：数值测试显示SSVM局部解优于铰链损失和斜坡损失SVM，提供超参数选择指导。

## 摘要（原文）

> Due to the rise of cardinality minimization in optimization, sparse support vector machines (SSVMs) have attracted much attention lately and show certain empirical advantages over convex SVMs. A common way to derive an SSVM is to add a cardinality function such as $\ell_0$-norm to the dual problem of a convex SVM. However, this process lacks theoretical justification. This paper fills the gap by developing a local duality theory for such an SSVM formulation and exploring its relationship with the hinge-loss SVM (hSVM) and the ramp-loss SVM (rSVM). In particular, we prove that the derived SSVM is exactly the dual problem of the 0/1-loss SVM, and the linear representer theorem holds for their local solutions. The local solution of SSVM also provides guidelines on selecting hyperparameters of hSVM and rSVM. {Under specific conditions, we show that a sequence of global solutions of hSVM converges to a local solution of 0/1-loss SVM. Moreover, a local minimizer of 0/1-loss SVM is a local minimizer of rSVM.} This explains why a local solution induced by SSVM outperforms hSVM and rSVM in the prior empirical study. We further conduct numerical tests on real datasets and demonstrate potential advantages of SSVM by working with locally nice solutions proposed in this paper.

