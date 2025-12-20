---
layout: default
title: Riemannian Stochastic Interpolants for Amorphous Particle Systems
---

# Riemannian Stochastic Interpolants for Amorphous Particle Systems
**arXiv**：[2512.16607v1](https://arxiv.org/abs/2512.16607) · [PDF](https://arxiv.org/pdf/2512.16607.pdf)  
**作者**：Louis Grenioux, Leonardo Galliano, Ludovic Berthier, Giulio Biroli, Marylou Gabrié  

**一句话要点**：提出等变黎曼随机插值框架以生成非晶材料平衡构型

**关键词**：非晶材料生成, 黎曼随机插值, 等变流匹配, 周期边界条件, 图神经网络, 粒子系统模拟

## 3 点简述
- 核心问题：非晶材料（玻璃）的平衡构型采样缓慢且困难，缺乏原子周期性。
- 方法要点：结合黎曼随机插值和等变流匹配，严格纳入周期边界条件和多组分粒子系统对称性。
- 实验或效果：在模型非晶系统上，几何和对称性约束显著提升生成性能。

## 摘要（原文）

> Modern generative models hold great promise for accelerating diverse tasks involving the simulation of physical systems, but they must be adapted to the specific constraints of each domain. Significant progress has been made for biomolecules and crystalline materials. Here, we address amorphous materials (glasses), which are disordered particle systems lacking atomic periodicity. Sampling equilibrium configurations of glass-forming materials is a notoriously slow and difficult task. This obstacle could be overcome by developing a generative framework capable of producing equilibrium configurations with well-defined likelihoods. In this work, we address this challenge by leveraging an equivariant Riemannian stochastic interpolation framework which combines Riemannian stochastic interpolant and equivariant flow matching. Our method rigorously incorporates periodic boundary conditions and the symmetries of multi-component particle systems, adapting an equivariant graph neural network to operate directly on the torus. Our numerical experiments on model amorphous systems demonstrate that enforcing geometric and symmetry constraints significantly improves generative performance.

