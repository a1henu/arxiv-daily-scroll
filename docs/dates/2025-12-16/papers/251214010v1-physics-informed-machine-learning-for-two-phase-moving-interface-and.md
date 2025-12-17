---
layout: default
title: Physics-Informed Machine Learning for Two-Phase Moving-Interface and Stefan Problems
---

# Physics-Informed Machine Learning for Two-Phase Moving-Interface and Stefan Problems
**arXiv**：[2512.14010v1](https://arxiv.org/abs/2512.14010) · [PDF](https://arxiv.org/pdf/2512.14010.pdf)  
**作者**：Che-Chia Chang, Te-Sheng Lin, Ming-Chih Lai  

**一句话要点**：提出物理信息神经网络框架以解决两相Stefan移动界面问题

**关键词**：物理信息机器学习, Stefan问题, 移动界面, 神经网络框架, 相变模拟

## 3 点简述
- Stefan问题是经典自由边界问题，涉及相变过程，计算挑战在于移动界面和非线性温度-相耦合。
- 方法使用两个神经网络：一个表示移动界面，另一个表示温度场，通过增强输入准确捕捉界面处的导数跳跃。
- 数值实验显示该方法在精度和有效性上优于其他神经网络方法，并能捕捉不稳定界面演化。

## 摘要（原文）

> The Stefan problem is a classical free-boundary problem that models phase-change processes and poses computational challenges due to its moving interface and nonlinear temperature-phase coupling. In this work, we develop a physics-informed neural network framework for solving two-phase Stefan problems. The proposed method explicitly tracks the interface motion and enforces the discontinuity in the temperature gradient across the interface while maintaining global consistency of the temperature field. Our approach employs two neural networks: one representing the moving interface and the other for the temperature field. The interface network allows rapid categorization of thermal diffusivity in the spatial domain, which is a crucial step for selecting training points for the temperature network. The temperature network's input is augmented with a modified zero-level set function to accurately capture the jump in its normal derivative across the interface. Numerical experiments on two-phase dynamical Stefan problems demonstrate the superior accuracy and effectiveness of our proposed method compared with the ones obtained by other neural network methodology in literature. The results indicate that the proposed framework offers a robust and flexible alternative to traditional numerical methods for solving phase-change problems governed by moving boundaries. In addition, the proposed method can capture an unstable interface evolution associated with the Mullins-Sekerka instability.

