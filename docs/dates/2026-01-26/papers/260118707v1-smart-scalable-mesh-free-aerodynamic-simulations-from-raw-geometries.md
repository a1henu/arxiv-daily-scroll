---
layout: default
title: SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model
---

# SMART: Scalable Mesh-free Aerodynamic Simulations from Raw Geometries using a Transformer-based Surrogate Model
**arXiv**：[2601.18707v1](https://arxiv.org/abs/2601.18707) · [PDF](https://arxiv.org/pdf/2601.18707.pdf)  
**作者**：Jan Hagnberger, Mathias Niepert  

**一句话要点**：提出SMART模型，基于Transformer从原始点云预测物理场，无需仿真网格，用于复杂几何的流体模拟。

**关键词**：无网格模拟, Transformer模型, 点云编码, 物理场预测, 工业仿真

## 3 点简述
- 核心问题：现有无网格方法误差高，而依赖仿真网格的方法生成成本大。
- 方法要点：使用点云编码几何和参数，通过跨层交互更新潜在特征和物理场。
- 实验或效果：在实验中竞争或超越依赖网格的方法，适用于工业级模拟。

## 摘要（原文）

> Machine learning-based surrogate models have emerged as more efficient alternatives to numerical solvers for physical simulations over complex geometries, such as car bodies. Many existing models incorporate the simulation mesh as an additional input, thereby reducing prediction errors. However, generating a simulation mesh for new geometries is computationally costly. In contrast, mesh-free methods, which do not rely on the simulation mesh, typically incur higher errors. Motivated by these considerations, we introduce SMART, a neural surrogate model that predicts physical quantities at arbitrary query locations using only a point-cloud representation of the geometry, without requiring access to the simulation mesh. The geometry and simulation parameters are encoded into a shared latent space that captures both structural and parametric characteristics of the physical field. A physics decoder then attends to the encoder's intermediate latent representations to map spatial queries to physical quantities. Through this cross-layer interaction, the model jointly updates latent geometric features and the evolving physical field. Extensive experiments show that SMART is competitive with and often outperforms existing methods that rely on the simulation mesh as input, demonstrating its capabilities for industry-level simulations.

