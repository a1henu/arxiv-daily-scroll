---
layout: default
title: Wavelet-Accelerated Physics-Informed Quantum Neural Network for Multiscale Partial Differential Equations
---

# Wavelet-Accelerated Physics-Informed Quantum Neural Network for Multiscale Partial Differential Equations
**arXiv**：[2512.08256v1](https://arxiv.org/abs/2512.08256) · [PDF](https://arxiv.org/pdf/2512.08256.pdf)  
**作者**：Deepak Gupta, Himanshu Pandey, Ratikanta Behera  

**一句话要点**：提出基于小波的物理信息量子神经网络框架，以高效求解多尺度偏微分方程

**关键词**：小波加速, 物理信息量子神经网络, 多尺度偏微分方程, 计算复杂度降低, 参数效率提升

## 3 点简述
- 传统物理信息神经网络及其量子版本在多尺度特征求解中面临精度挑战和计算开销大问题
- 该方法结合小波多分辨率特性于量子神经网络，无需自动微分，降低计算复杂度
- 数值实验显示，相比经典小波PINNs，参数减少超95%，比现有量子PINNs提速3-5倍

## 摘要（原文）

> This work proposes a wavelet-based physics-informed quantum neural network framework to efficiently address multiscale partial differential equations that involve sharp gradients, stiffness, rapid local variations, and highly oscillatory behavior. Traditional physics-informed neural networks (PINNs) have demonstrated substantial potential in solving differential equations, and their quantum counterparts, quantum-PINNs, exhibit enhanced representational capacity with fewer trainable parameters. However, both approaches face notable challenges in accurately solving multiscale features. Furthermore, their reliance on automatic differentiation for constructing loss functions introduces considerable computational overhead, resulting in longer training times. To overcome these challenges, we developed a wavelet-accelerated physics-informed quantum neural network that eliminates the need for automatic differentiation, significantly reducing computational complexity. The proposed framework incorporates the multiresolution property of wavelets within the quantum neural network architecture, thereby enhancing the network's ability to effectively capture both local and global features of multiscale problems. Numerical experiments demonstrate that our proposed method achieves superior accuracy while requiring less than five percent of the trainable parameters compared to classical wavelet-based PINNs, resulting in faster convergence. Moreover, it offers a speedup of three to five times compared to existing quantum PINNs, highlighting the potential of the proposed approach for efficiently solving challenging multiscale and oscillatory problems.

