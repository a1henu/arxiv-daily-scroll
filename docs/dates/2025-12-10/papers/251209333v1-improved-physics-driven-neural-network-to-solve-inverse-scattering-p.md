---
layout: default
title: Improved Physics-Driven Neural Network to Solve Inverse Scattering Problems
---

# Improved Physics-Driven Neural Network to Solve Inverse Scattering Problems
**arXiv**：[2512.09333v1](https://arxiv.org/abs/2512.09333) · [PDF](https://arxiv.org/pdf/2512.09333.pdf)  
**作者**：Yutong Du, Zicheng Liu, Bo Wu, Jingwei Kou, Hang Li, Changyou Li, Yali Zong, Bo Qi  

**一句话要点**：提出改进物理驱动神经网络以解决电磁逆散射问题

**关键词**：电磁逆散射, 物理驱动神经网络, 激活函数优化, 动态计算域, 迁移学习, 实时推理

## 3 点简述
- 核心问题：电磁逆散射问题求解，涉及从散射数据反演目标属性，传统方法计算成本高或精度不足。
- 方法要点：引入高斯局部振荡抑制窗口激活函数稳定收敛，采用动态散射子区域识别策略自适应优化计算域，结合迁移学习提升实际场景适用性。
- 实验或效果：数值模拟和实验显示，该方法在重建精度、鲁棒性和效率上优于现有先进方法。

## 摘要（原文）

> This paper presents an improved physics-driven neural network (IPDNN) framework for solving electromagnetic inverse scattering problems (ISPs). A new Gaussian-localized oscillation-suppressing window (GLOW) activation function is introduced to stabilize convergence and enable a lightweight yet accurate network architecture. A dynamic scatter subregion identification strategy is further developed to adaptively refine the computational domain, preventing missed detections and reducing computational cost. Moreover, transfer learning is incorporated to extend the solver's applicability to practical scenarios, integrating the physical interpretability of iterative algorithms with the real-time inference capability of neural networks. Numerical simulations and experimental results demonstrate that the proposed solver achieves superior reconstruction accuracy, robustness, and efficiency compared with existing state-of-the-art methods.

