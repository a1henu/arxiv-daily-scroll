---
layout: default
title: 4KDehazeFlow: Ultra-High-Definition Image Dehazing via Flow Matching
---

# 4KDehazeFlow: Ultra-High-Definition Image Dehazing via Flow Matching
**arXiv**：[2511.09055v1](https://arxiv.org/abs/2511.09055) · [PDF](https://arxiv.org/pdf/2511.09055.pdf)  
**作者**：Xingchi Chen, Pu Wang, Xuerui Li, Chaopeng Li, Juxiang Zhou, Jianhou Gan, Dianjie Lu, Guijuan Zhang, Wenqi Ren, Zhuoran Zheng  

**一句话要点**：提出4KDehazeFlow以解决超高清图像去雾中的场景适应性和计算效率问题

**关键词**：图像去雾, 流匹配, 超高清图像, 3D查找表, ODE求解器

## 3 点简述
- 超高清图像去雾面临场景适应性差和计算复杂度高的问题
- 基于流匹配和可学习3D查找表实现高效非线性颜色变换
- 实验显示PSNR提升2dB，在浓雾和颜色保真度上表现优异

## 摘要（原文）

> Ultra-High-Definition (UHD) image dehazing faces challenges such as limited scene adaptability in prior-based methods and high computational complexity with color distortion in deep learning approaches. To address these issues, we propose 4KDehazeFlow, a novel method based on Flow Matching and the Haze-Aware vector field. This method models the dehazing process as a progressive optimization of continuous vector field flow, providing efficient data-driven adaptive nonlinear color transformation for high-quality dehazing. Specifically, our method has the following advantages: 1) 4KDehazeFlow is a general method compatible with various deep learning networks, without relying on any specific network architecture. 2) We propose a learnable 3D lookup table (LUT) that encodes haze transformation parameters into a compact 3D mapping matrix, enabling efficient inference through precomputed mappings. 3) We utilize a fourth-order Runge-Kutta (RK4) ordinary differential equation (ODE) solver to stably solve the dehazing flow field through an accurate step-by-step iterative method, effectively suppressing artifacts. Extensive experiments show that 4KDehazeFlow exceeds seven state-of-the-art methods. It delivers a 2dB PSNR increase and better performance in dense haze and color fidelity.

