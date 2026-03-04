---
layout: default
title: Stabilized Adaptive Loss and Residual-Based Collocation for Physics-Informed Neural Networks
---

# Stabilized Adaptive Loss and Residual-Based Collocation for Physics-Informed Neural Networks
**arXiv**：[2603.03224v1](https://arxiv.org/abs/2603.03224) · [PDF](https://arxiv.org/pdf/2603.03224.pdf)  
**作者**：Divyavardhan Singh, Shubham Kamble, Dimple Sonone, Kishor Upla  

**一句话要点**：提出自适应损失平衡与残差配置方案，以提升PINNs在刚性或冲击主导问题中的求解精度。

**关键词**：物理信息神经网络, 自适应损失平衡, 残差配置, 偏微分方程求解, 刚性问题

## 3 点简述
- 传统PINNs在处理高刚性或冲击主导问题时存在训练不平衡和求解不准确的问题。
- 采用平滑梯度范数自适应平衡损失，并基于残差自适应配置点以提高高残差区域精度。
- 在Burgers方程和Allen-Cahn方程上，相对L2误差分别降低约44%和70%。

## 摘要（原文）

> Physics-Informed Neural Networks (PINNs) have been recognized as a mesh-free alternative to solve partial differential equations where physics information is incorporated. However, in dealing with problems characterized by high stiffness or shock-dominated dynamics, traditional PINNs have been found to have limitations, including unbalanced training and inaccuracy in solution, even with small physics residuals. In this research, we seek to address these limitations using the viscous Burgers' equation with low viscosity and the Allen-Cahn equation as test problems. In addressing unbalanced training, we have developed a new adaptive loss balancing scheme using smoothed gradient norms to ensure satisfaction of initial and boundary conditions. Further, to address inaccuracy in the solution, we have developed an adaptive residual-based collocation scheme to improve the accuracy of solutions in the regions with high physics residuals. The proposed new approach significantly improves solution accuracy with consistent satisfaction of physics residuals. For instance, in the case of Burgers' equation, the relative L2 error is reduced by about 44 percent compared to traditional PINNs, while for the Allen-Cahn equation, the relative L2 error is reduced by approximately 70 percent. Additionally, we show the trustworthy solution comparison of the proposed method using a robust finite difference solver.

