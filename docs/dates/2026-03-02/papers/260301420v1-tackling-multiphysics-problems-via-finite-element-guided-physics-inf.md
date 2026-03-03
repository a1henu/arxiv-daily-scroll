---
layout: default
title: Tackling multiphysics problems via finite element-guided physics-informed operator learning
---

# Tackling multiphysics problems via finite element-guided physics-informed operator learning
**arXiv**：[2603.01420v1](https://arxiv.org/abs/2603.01420) · [PDF](https://arxiv.org/pdf/2603.01420.pdf)  
**作者**：Yusuke Yamazaki, Reza Najian Asl, Markus Apel, Mayu Muramatsu, Shahed Rezaei  

**一句话要点**：提出有限元引导的物理信息算子学习框架，用于任意域上的多物理场耦合问题求解。

**关键词**：多物理场模拟, 物理信息算子学习, 有限元方法, 神经算子, JAX平台, 耦合偏微分方程

## 3 点简述
- 核心问题：解决任意域上多物理场耦合偏微分方程的求解，避免依赖标注模拟数据。
- 方法要点：基于有限元加权残差公式，在JAX平台Folax上实现，支持离散化无关预测。
- 实验或效果：在非线性热力学问题中验证，FNO在规则域高效，iFOL适用于复杂几何，训练样本质量影响性能。

## 摘要（原文）

> This work presents a finite element-guided physics-informed operator learning framework for multiphysics problems with coupled partial differential equations (PDEs) on arbitrary domains. Implemented with Folax, a JAX-based operator-learning platform, the proposed framework learns a mapping from the input parameter space to the solution space with a weighted residual formulation based on the finite element method, enabling discretization-independent prediction beyond the training resolution without relying on labaled simulation data. The present framework for multiphysics problems is verified on nonlinear thermo-mechanical problems. Two- and three-dimensional representative volume elements with varying heterogeneous microstructures, and a close-to-reality industrial casting example under varying boundary conditions are investigated as the example problems. We investigate the potential of several neural operator backbones, including Fourier neural operators (FNOs), deep operator networks (DeepONets), and a newly proposed implicit finite operator learning (iFOL) approach based on conditional neural fields. The results demonstrate that FNOs yield highly accurate solution operators on regular domains, where the global topology can be efficiently learned in the spectral domain, and iFOL offers efficient parametric operator learning capabilities for complex and irregular geometries. Furthermore, studies on training strategies, network decomposition, and training sample quality reveal that a monolithic training strategy using a single network is sufficient for accurate predictions, while training sample quality strongly influences performance. Overall, the present approach highlights the potential of physics-informed operator learning with a finite element-based loss as a unified and scalable approach for coupled multiphysics simulations.

