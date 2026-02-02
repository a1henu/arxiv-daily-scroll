---
layout: default
title: Spectral Gradient Descent Mitigates Anisotropy-Driven Misalignment: A Case Study in Phase Retrieval
---

# Spectral Gradient Descent Mitigates Anisotropy-Driven Misalignment: A Case Study in Phase Retrieval
**arXiv**：[2601.22652v1](https://arxiv.org/abs/2601.22652) · [PDF](https://arxiv.org/pdf/2601.22652.pdf)  
**作者**：Guillaume Braun, Han Bao, Wei Huang, Masaaki Imaizumi  

**一句话要点**：提出谱梯度下降以缓解各向异性驱动的错位问题，在相位检索案例中验证

**关键词**：谱梯度下降, 相位检索, 各向异性输入, 梯度下降分析, 神经网络训练, 方差诱导错位

## 3 点简述
- 核心问题：梯度下降在强各向异性输入下因方差诱导错位而性能下降
- 方法要点：谱梯度下降通过去除尺度信息抑制高方差方向的放大效应
- 实验或效果：理论分析和数值实验显示谱梯度下降稳定对齐并加速噪声收缩

## 摘要（原文）

> Spectral gradient methods, such as the Muon optimizer, modify gradient updates by preserving directional information while discarding scale, and have shown strong empirical performance in deep learning. We investigate the mechanisms underlying these gains through a dynamical analysis of a nonlinear phase retrieval model with anisotropic Gaussian inputs, equivalent to training a two-layer neural network with the quadratic activation and fixed second-layer weights. Focusing on a spiked covariance setting where the dominant variance direction is orthogonal to the signal, we show that gradient descent (GD) suffers from a variance-induced misalignment: during the early escaping stage, the high-variance but uninformative spike direction is multiplicatively amplified, degrading alignment with the true signal under strong anisotropy. In contrast, spectral gradient descent (SpecGD) removes this spike amplification effect, leading to stable alignment and accelerated noise contraction. Numerical experiments confirm the theory and show that these phenomena persist under broader anisotropic covariances.

