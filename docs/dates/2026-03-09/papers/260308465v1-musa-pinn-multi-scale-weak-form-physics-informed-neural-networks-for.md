---
layout: default
title: MUSA-PINN: Multi-scale Weak-form Physics-Informed Neural Networks for Fluid Flow in Complex Geometries
---

# MUSA-PINN: Multi-scale Weak-form Physics-Informed Neural Networks for Fluid Flow in Complex Geometries
**arXiv**：[2603.08465v1](https://arxiv.org/abs/2603.08465) · [PDF](https://arxiv.org/pdf/2603.08465.pdf)  
**作者**：Weizheng Zhang, Xunjie Xie, Hao Pan, Xiaowei Duan, Bingteng Sun, Qiang Du, Lin lu  

**一句话要点**：提出多尺度弱形式物理信息神经网络以解决复杂几何中流体流动的收敛问题

**关键词**：物理信息神经网络, 弱形式方法, 多尺度建模, 流体流动, 复杂几何, 积分守恒定律

## 3 点简述
- 标准PINN在复杂几何中因点式约束的局部性导致梯度不稳定和守恒违反
- MUSA-PINN将PDE约束重构为分层球形控制体积上的积分守恒定律
- 在TPMS几何的稳态不可压缩流实验中，相对误差降低高达93%并保持质量守恒

## 摘要（原文）

> While Physics-Informed Neural Networks (PINNs) offer a mesh-free approach to solving PDEs, standard point-wise residual minimization suffers from convergence pathologies in topologically complex domains like Triply Periodic Minimal Surfaces (TPMS). The locality bias of point-wise constraints fails to propagate global information through tortuous channels, causing unstable gradients and conservation violations. To address this, we propose the Multi-scale Weak-form PINN (MUSA-PINN), which reformulates PDE constraints as integral conservation laws over hierarchical spherical control volumes. We enforce continuity and momentum conservation via flux-balance residuals on control surfaces. Our method utilizes a three-scale subdomain strategy-comprising large volumes for long-range coupling, skeleton-aware meso-scale volumes aligned with transport pathways, and small volumes for local refinement-alongside a two-stage training schedule prioritizing continuity. Experiments on steady incompressible flow in TPMS geometries show MUSA-PINN outperforms state-of-the-art baselines, reducing relative errors by up to 93% and preserving mass conservation.

