---
layout: default
title: Decoupling Variance and Scale-Invariant Updates in Adaptive Gradient Descent for Unified Vector and Matrix Optimization
---

# Decoupling Variance and Scale-Invariant Updates in Adaptive Gradient Descent for Unified Vector and Matrix Optimization
**arXiv**：[2602.06880v1](https://arxiv.org/abs/2602.06880) · [PDF](https://arxiv.org/pdf/2602.06880.pdf)  
**作者**：Zitao Song, Cedar Site Bai, Zhe Zhang, Brian Bullins, David F. Gleich  

**一句话要点**：提出DeVA框架，通过解耦方差与尺度不变项，统一向量与矩阵优化，提升自适应梯度下降性能。

**关键词**：自适应梯度下降, 矩阵优化, 方差解耦, 谱优化, 收敛加速

## 3 点简述
- 核心问题：自适应方法如Adam难以直接推广到矩阵谱优化，导致向量与矩阵优化方法割裂。
- 方法要点：重新表述AdaGrad更新，解耦为方差适应项和尺度不变项，构建DeVA框架，实现从Adam到自适应谱下降的无缝过渡。
- 实验效果：在语言建模和图像分类任务中，DeVA优于Muon和SOAP等先进方法，减少约6.6%的token使用量。

## 摘要（原文）

> Adaptive methods like Adam have become the $\textit{de facto}$ standard for large-scale vector and Euclidean optimization due to their coordinate-wise adaptation with a second-order nature. More recently, matrix-based spectral optimizers like Muon (Jordan et al., 2024b) show the power of treating weight matrices as matrices rather than long vectors. Linking these is hard because many natural generalizations are not feasible to implement, and we also cannot simply move the Adam adaptation to the matrix spectrum. To address this, we reformulate the AdaGrad update and decompose it into a variance adaptation term and a scale-invariant term. This decoupling produces $\textbf{DeVA}$ ($\textbf{De}$coupled $\textbf{V}$ariance $\textbf{A}$daptation), a framework that bridges between vector-based variance adaptation and matrix spectral optimization, enabling a seamless transition from Adam to adaptive spectral descent. Extensive experiments across language modeling and image classification demonstrate that DeVA consistently outperforms state-of-the-art methods such as Muon and SOAP (Vyas et al., 2024), reducing token usage by around 6.6\%. Theoretically, we show that the variance adaptation term effectively improves the blockwise smoothness, facilitating faster convergence. Our implementation is available at https://github.com/Tsedao/Decoupled-Variance-Adaptation

