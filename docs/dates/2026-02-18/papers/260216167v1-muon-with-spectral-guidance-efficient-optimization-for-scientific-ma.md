---
layout: default
title: Muon with Spectral Guidance: Efficient Optimization for Scientific Machine Learning
---

# Muon with Spectral Guidance: Efficient Optimization for Scientific Machine Learning
**arXiv**：[2602.16167v1](https://arxiv.org/abs/2602.16167) · [PDF](https://arxiv.org/pdf/2602.16167.pdf)  
**作者**：Binghang Lu, Jiahao Zhang, Guang Lin  

**一句话要点**：提出SpecMuon优化器以解决科学机器学习中的梯度病态和稳定性问题

**关键词**：科学机器学习, 优化算法, 物理信息神经网络, 谱分析, 梯度流, 稳定性保证

## 3 点简述
- 核心问题：物理信息神经网络和神经算子因梯度病态、多尺度谱行为和物理约束导致的优化困难
- 方法要点：结合Muon正交化几何与模式级松弛标量辅助变量机制，沿主导谱方向自适应调节步长
- 实验或效果：在Burgers方程和分数偏微分方程等基准问题上，相比Adam、AdamW和Muon，实现更快收敛和更高稳定性

## 摘要（原文）

> Physics-informed neural networks and neural operators often suffer from severe optimization difficulties caused by ill-conditioned gradients, multi-scale spectral behavior, and stiffness induced by physical constraints. Recently, the Muon optimizer has shown promise by performing orthogonalized updates in the singular-vector basis of the gradient, thereby improving geometric conditioning. However, its unit-singular-value updates may lead to overly aggressive steps and lack explicit stability guarantees when applied to physics-informed learning. In this work, we propose SpecMuon, a spectral-aware optimizer that integrates Muon's orthogonalized geometry with a mode-wise relaxed scalar auxiliary variable (RSAV) mechanism. By decomposing matrix-valued gradients into singular modes and applying RSAV updates individually along dominant spectral directions, SpecMuon adaptively regulates step sizes according to the global loss energy while preserving Muon's scale-balancing properties. This formulation interprets optimization as a multi-mode gradient flow and enables principled control of stiff spectral components. We establish rigorous theoretical properties of SpecMuon, including a modified energy dissipation law, positivity and boundedness of auxiliary variables, and global convergence with a linear rate under the Polyak-Lojasiewicz condition. Numerical experiments on physics-informed neural networks, DeepONets, and fractional PINN-DeepONets demonstrate that SpecMuon achieves faster convergence and improved stability compared with Adam, AdamW, and the original Muon optimizer on benchmark problems such as the one-dimensional Burgers equation and fractional partial differential equations.

