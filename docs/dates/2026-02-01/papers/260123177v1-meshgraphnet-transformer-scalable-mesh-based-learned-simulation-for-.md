---
layout: default
title: MeshGraphNet-Transformer: Scalable Mesh-based Learned Simulation for Solid Mechanics
---

# MeshGraphNet-Transformer: Scalable Mesh-based Learned Simulation for Solid Mechanics
**arXiv**：[2601.23177v1](https://arxiv.org/abs/2601.23177) · [PDF](https://arxiv.org/pdf/2601.23177.pdf)  
**作者**：Mikel M. Iparraguirre, Iciar Alfaro, David Gonzalez, Elias Cueto  

**一句话要点**：提出MeshGraphNet-Transformer以解决固体力学中大规模高分辨率网格模拟的长程信息传播效率问题

**关键词**：网格图网络, Transformer架构, 固体力学模拟, 长程信息传播, 工业规模网格, 物理注意力

## 3 点简述
- 核心问题：标准MeshGraphNet在大型高分辨率网格上因迭代消息传递导致长程信息传播效率低下，影响工业规模模拟。
- 方法要点：结合Transformer的全局建模能力和MeshGraphNet的几何归纳偏置，通过物理注意力Transformer同时更新所有节点状态，直接捕获长程物理交互。
- 实验或效果：在冲击动力学等工业规模网格上成功建模自接触、塑性和多变量输出，超越现有方法，精度更高且参数更少。

## 摘要（原文）

> We present MeshGraphNet-Transformer (MGN-T), a novel architecture that combines the global modeling capabilities of Transformers with the geometric inductive bias of MeshGraphNets, while preserving a mesh-based graph representation. MGN-T overcomes a key limitation of standard MGN, the inefficient long-range information propagation caused by iterative message passing on large, high-resolution meshes. A physics-attention Transformer serves as a global processor, updating all nodal states simultaneously while explicitly retaining node and edge attributes. By directly capturing long-range physical interactions, MGN-T eliminates the need for deep message-passing stacks or hierarchical, coarsened meshes, enabling efficient learning on high-resolution meshes with varying geometries, topologies, and boundary conditions at an industrial scale.
>   We demonstrate that MGN-T successfully handles industrial-scale meshes for impact dynamics, a setting in which standard MGN fails due message-passing under-reaching. The method accurately models self-contact, plasticity, and multivariate outputs, including internal, phenomenological plastic variables. Moreover, MGN-T outperforms state-of-the-art approaches on classical benchmarks, achieving higher accuracy while maintaining practical efficiency, using only a fraction of the parameters required by competing baselines.

