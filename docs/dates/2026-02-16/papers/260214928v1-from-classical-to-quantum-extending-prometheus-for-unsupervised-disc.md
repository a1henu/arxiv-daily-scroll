---
layout: default
title: From Classical to Quantum: Extending Prometheus for Unsupervised Discovery of Phase Transitions in Three Dimensions and Quantum Systems
---

# From Classical to Quantum: Extending Prometheus for Unsupervised Discovery of Phase Transitions in Three Dimensions and Quantum Systems
**arXiv**：[2602.14928v1](https://arxiv.org/abs/2602.14928) · [PDF](https://arxiv.org/pdf/2602.14928.pdf)  
**作者**：Brandon Yee, Wilson Collins, Maximilian Rutkowski  

**一句话要点**：扩展Prometheus框架至三维经典与量子系统，实现无监督相变发现

**关键词**：无监督学习, 相变发现, 量子多体系统, 变分自编码器, 临界指数, 量子临界点

## 3 点简述
- 核心问题：将无监督相变发现从二维经典系统扩展到三维经典和量子多体系统，解决高维可扩展性和量子涨落泛化问题。
- 方法要点：开发量子感知变分自编码器（Q-VAE），使用复数值波函数和基于保真度的损失函数，以处理量子系统。
- 实验或效果：在三维伊辛模型中，临界温度检测精度达0.01%，临界指数提取准确率≥70%；在量子系统中，量子临界点检测精度达2%，并成功识别无序横向场伊辛模型的无限随机临界性。

## 摘要（原文）

> We extend the Prometheus framework for unsupervised phase transition discovery from 2D classical systems to 3D classical and quantum many-body systems, addressing scalability in higher dimensions and generalization to quantum fluctuations. For the 3D Ising model ($L \leq 32$), the framework detects the critical temperature within 0.01\% of literature values ($T_c/J = 4.511 \pm 0.005$) and extracts critical exponents with $\geq 70\%$ accuracy ($β= 0.328 \pm 0.015$, $γ= 1.24 \pm 0.06$, $ν= 0.632 \pm 0.025$), correctly identifying the 3D Ising universality class via $χ^2$ comparison ($p = 0.72$) without analytical guidance. For quantum systems, we developed quantum-aware VAE (Q-VAE) architectures using complex-valued wavefunctions and fidelity-based loss. Applied to the transverse field Ising model, we achieve 2\% accuracy in quantum critical point detection ($h_c/J = 1.00 \pm 0.02$) and successfully discover ground state magnetization as the order parameter ($r = 0.97$). Notably, for the disordered transverse field Ising model, we detect exotic infinite-randomness criticality characterized by activated dynamical scaling $\ln ξ\sim \|h - h_c\|^{-ψ}$, extracting a tunneling exponent $ψ= 0.48 \pm 0.08$ consistent with theoretical predictions ($ψ= 0.5$). This demonstrates that unsupervised learning can identify qualitatively different types of critical behavior, not just locate critical points. Our systematic validation across classical thermal transitions ($T = 0$ to $T > 0$) and quantum phase transitions ($T = 0$, varying $h$) establishes that VAE-based discovery generalizes across fundamentally different physical domains, providing robust tools for exploring phase diagrams where analytical solutions are unavailable.

