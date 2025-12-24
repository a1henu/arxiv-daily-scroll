---
layout: default
title: Deep Eigenspace Network and Its Application to Parametric Non-selfadjoint Eigenvalue Problems
---

# Deep Eigenspace Network and Its Application to Parametric Non-selfadjoint Eigenvalue Problems
**arXiv**：[2512.20058v1](https://arxiv.org/abs/2512.20058) · [PDF](https://arxiv.org/pdf/2512.20058.pdf)  
**作者**：H. Li, J. Sun, Z. Zhang  

**一句话要点**：提出深度特征空间网络以解决参数非自伴特征值问题中的谱不稳定性和模式切换问题

**关键词**：算子学习, 非自伴特征值问题, 深度特征空间网络, 傅里叶神经算子, 谱稳定性, 零样本泛化

## 3 点简述
- 针对非自伴算子的谱不稳定性和模式切换，学习稳定的不变特征子空间映射而非单个特征函数
- 集成傅里叶神经算子、几何自适应POD基和显式带状交叉模式混合机制，捕捉非结构化网格上的复杂谱依赖
- 应用于参数非自伴Steklov特征值问题，理论证明特征子空间对参数的Lipschitz连续性，数值实验验证高精度和零样本泛化能力

## 摘要（原文）

> We consider operator learning for efficiently solving parametric non-selfadjoint eigenvalue problems. To overcome the spectral instability and mode switching inherent in non-selfadjoint operators, we introduce a hybrid framework that learns the stable invariant eigensubspace mapping rather than individual eigenfunctions. We proposed a Deep Eigenspace Network (DEN) architecture integrating Fourier Neural Operators, geometry-adaptive POD bases, and explicit banded cross-mode mixing mechanisms to capture complex spectral dependencies on unstructured meshes. We apply DEN to the parametric non-selfadjoint Steklov eigenvalue problem and provide theoretical proofs for the Lipschitz continuity of the eigensubspace with respect to the parameters. In addition, we derive error bounds for the reconstruction of the eigenspace. Numerical experiments validate DEN's high accuracy and zero-shot generalization capabilities across different discretizations.

