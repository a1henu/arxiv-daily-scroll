---
layout: default
title: Physics-informed post-processing of stabilized finite element solutions for transient convection-dominated problems
---

# Physics-informed post-processing of stabilized finite element solutions for transient convection-dominated problems
**arXiv**：[2603.03259v1](https://arxiv.org/abs/2603.03259) · [PDF](https://arxiv.org/pdf/2603.03259.pdf)  
**作者**：Süleyman Cengizci, Ömür Uğur, Srinivasan Natesan  

**一句话要点**：提出混合框架PASSC，结合稳定有限元与PINN后处理，提升瞬态对流主导问题终端时刻精度

**关键词**：瞬态对流主导问题, 稳定有限元方法, 物理信息神经网络, 后处理技术, 混合计算框架, 精度提升

## 3 点简述
- 核心问题：瞬态对流主导问题中，稳定有限元方法仍可能产生振荡，而纯PINN难以捕捉尖锐结构且训练成本高
- 方法要点：扩展PASSC至瞬态问题，在终端时刻附近选择性应用PINN，利用残差约束和自适应损失加权进行后处理
- 实验或效果：在五个基准问题上，相比纯稳定有限元方法，终端时刻精度显著提升

## 摘要（原文）

> The numerical simulation of convection-dominated transient transport phenomena poses significant computational challenges due to sharp gradients and propagating fronts across the spatiotemporal domain. Classical discretization methods often generate spurious oscillations, requiring advanced stabilization techniques. However, even stabilized finite element methods may require additional regularization to accurately resolve localized steep layers. On the other hand, standalone physics-informed neural networks (PINNs) struggle to capture sharp solution structures in convection-dominated regimes and typically require a large number of training epochs. This work presents a hybrid computational framework that extends the PINN-Augmented SUPG with Shock-Capturing (PASSC) methodology from steady to unsteady problems. The approach combines a semi-discrete stabilized finite element method with a PINN-based correction strategy for transient convection-diffusion-reaction equations. Stabilization is achieved using the Streamline-Upwind Petrov-Galerkin (SUPG) formulation augmented with a YZbeta shock-capturing operator. Rather than training over the entire space-time domain, the neural network is applied selectively near the terminal time, enhancing the finite element solution using the last K_s temporal snapshots while enforcing residual constraints from the governing equations and boundary conditions. The network incorporates residual blocks with random Fourier features and employs progressive training with adaptive loss weighting. Numerical experiments on five benchmark problems, including boundary and interior layers, traveling waves, and nonlinear Burgers dynamics, demonstrate significant accuracy improvements at the terminal time compared to standalone stabilized finite element solutions.

