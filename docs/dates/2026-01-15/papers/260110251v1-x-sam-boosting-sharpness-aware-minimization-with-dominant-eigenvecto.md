---
layout: default
title: X-SAM: Boosting Sharpness-Aware Minimization with Dominant-Eigenvector Gradient Correction
---

# X-SAM: Boosting Sharpness-Aware Minimization with Dominant-Eigenvector Gradient Correction
**arXiv**：[2601.10251v1](https://arxiv.org/abs/2601.10251) · [PDF](https://arxiv.org/pdf/2601.10251.pdf)  
**作者**：Hongru Duan, Yongle Chen, Lei Guan  

**一句话要点**：提出X-SAM以解决SAM在训练中梯度可能指向尖锐区域的问题，通过主导特征向量梯度校正提升泛化能力。

**关键词**：锐度感知最小化, 梯度校正, Hessian特征向量, 泛化提升, 优化算法

## 3 点简述
- 核心问题：SAM优化行为可能偏离理论预期，梯度仍指向尖锐区域，削弱正则化效果。
- 方法要点：从谱和几何角度分析，提出X-SAM，通过沿顶部特征向量正交分解校正梯度，直接正则化Hessian最大特征值。
- 实验或效果：理论证明收敛性和泛化优势，实验验证X-SAM在理论和实践上的改进。

## 摘要（原文）

> Sharpness-Aware Minimization (SAM) aims to improve generalization by minimizing a worst-case perturbed loss over a small neighborhood of model parameters. However, during training, its optimization behavior does not always align with theoretical expectations, since both sharp and flat regions may yield a small perturbed loss. In such cases, the gradient may still point toward sharp regions, failing to achieve the intended effect of SAM. To address this issue, we investigate SAM from a spectral and geometric perspective: specifically, we utilize the angle between the gradient and the leading eigenvector of the Hessian as a measure of sharpness. Our analysis illustrates that when this angle is less than or equal to ninety degrees, the effect of SAM's sharpness regularization can be weakened. Furthermore, we propose an explicit eigenvector-aligned SAM (X-SAM), which corrects the gradient via orthogonal decomposition along the top eigenvector, enabling more direct and efficient regularization of the Hessian's maximum eigenvalue. We prove X-SAM's convergence and superior generalization, with extensive experimental evaluations confirming both theoretical and practical advantages.

