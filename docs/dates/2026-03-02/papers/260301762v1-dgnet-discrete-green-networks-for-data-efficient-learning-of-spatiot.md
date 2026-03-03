---
layout: default
title: DGNet: Discrete Green Networks for Data-Efficient Learning of Spatiotemporal PDEs
---

# DGNet: Discrete Green Networks for Data-Efficient Learning of Spatiotemporal PDEs
**arXiv**：[2603.01762v1](https://arxiv.org/abs/2603.01762) · [PDF](https://arxiv.org/pdf/2603.01762.pdf)  
**作者**：Yingjie Tan, Quanming Yao, Yaqing Wang  

**一句话要点**：提出DGNet以数据高效学习时空偏微分方程，利用离散格林函数嵌入结构归纳偏置。

**关键词**：时空偏微分方程, 数据高效学习, 格林函数, 结构归纳偏置, 零样本泛化

## 3 点简述
- 核心问题：现有神经PDE求解器数据效率低，在有限数据下性能下降，泛化能力差。
- 方法要点：基于格林函数理论，将格林函数转化为图离散形式，嵌入叠加原理到混合物理-神经架构中。
- 实验或效果：在多种时空PDE场景中，仅用数十条训练轨迹即达到最先进精度，并实现零样本泛化。

## 摘要（原文）

> Spatiotemporal partial differential equations (PDEs) underpin a wide range of scientific and engineering applications. Neural PDE solvers offer a promising alternative to classical numerical methods. However, existing approaches typically require large numbers of training trajectories, while high-fidelity PDE data are expensive to generate. Under limited data, their performance degrades substantially, highlighting their low data efficiency. A key reason is that PDE dynamics embody strong structural inductive biases that are not explicitly encoded in neural architectures, forcing models to learn fundamental physical structure from data. A particularly salient manifestation of this inefficiency is poor generalization to unseen source terms. In this work, we revisit Green's function theory-a cornerstone of PDE theory-as a principled source of structural inductive bias for PDE learning. Based on this insight, we propose DGNet, a discrete Green network for data-efficient learning of spatiotemporal PDEs. The key idea is to transform the Green's function into a graph-based discrete formulation, and embed the superposition principle into the hybrid physics-neural architecture, which reduces the burden of learning physical priors from data, thereby improving sample efficiency. Across diverse spatiotemporal PDE scenarios, DGNet consistently achieves state-of-the-art accuracy using only tens of training trajectories. Moreover, it exhibits robust zero-shot generalization to unseen source terms, serving as a stress test that highlights its data-efficient structural design.

