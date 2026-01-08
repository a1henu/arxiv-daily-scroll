---
layout: default
title: Equivariant Neural Networks for Force-Field Models of Lattice Systems
---

# Equivariant Neural Networks for Force-Field Models of Lattice Systems
**arXiv**：[2601.04104v1](https://arxiv.org/abs/2601.04104) · [PDF](https://arxiv.org/pdf/2601.04104.pdf)  
**作者**：Yunhao Fan, Gia-Wei Chern  

**一句话要点**：提出基于等变神经网络的对称性保持框架，用于晶格系统力场建模，以提升通用性和可转移性。

**关键词**：等变神经网络, 晶格系统力场, 对称性保持, 机器学习力场, Holstein模型, 动力学模拟

## 3 点简述
- 核心问题：现有机器学习力场方法依赖手工构建的对称性描述符，系统特定性强，限制跨晶格哈密顿量的通用性和可转移性。
- 方法要点：引入等变神经网络框架，直接嵌入晶格模型的离散点群和内部对称性，实现从局部构型到力的数据驱动映射。
- 实验或效果：以Holstein哈密顿量为例，构建等变神经网络力场模型，大规模动力学模拟准确捕捉对称破缺相的中尺度演化。

## 摘要（原文）

> Machine-learning (ML) force fields enable large-scale simulations with near-first-principles accuracy at substantially reduced computational cost. Recent work has extended ML force-field approaches to adiabatic dynamical simulations of condensed-matter lattice models with coupled electronic and structural or magnetic degrees of freedom. However, most existing formulations rely on hand-crafted, symmetry-aware descriptors, whose construction is often system-specific and can hinder generality and transferability across different lattice Hamiltonians. Here we introduce a symmetry-preserving framework based on equivariant neural networks (ENNs) that provides a general, data-driven mapping from local configurations of dynamical variables to the associated on-site forces in a lattice Hamiltonian. In contrast to ENN architectures developed for molecular systems -- where continuous Euclidean symmetries dominate -- our approach aims to embed the discrete point-group and internal symmetries intrinsic to lattice models directly into the neural-network representation of the force field. As a proof of principle, we construct an ENN-based force-field model for the adiabatic dynamics of the Holstein Hamiltonian on a square lattice, a canonical system for electron-lattice physics. The resulting ML-enabled large-scale dynamical simulations faithfully capture mesoscale evolution of the symmetry-breaking phase, illustrating the utility of lattice-equivariant architectures for linking microscopic electronic processes to emergent dynamical behavior in condensed-matter lattice systems.

