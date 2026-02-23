---
layout: default
title: Machine-learning force-field models for dynamical simulations of metallic magnets
---

# Machine-learning force-field models for dynamical simulations of metallic magnets
**arXiv**：[2602.18213v1](https://arxiv.org/abs/2602.18213) · [PDF](https://arxiv.org/pdf/2602.18213.pdf)  
**作者**：Gia-Wei Chern, Yunhao Fan, Sheng Zhang, Puhan Zhang  

**一句话要点**：提出机器学习力场模型，用于巡游电子磁体的非平衡自旋动力学模拟

**关键词**：机器学习力场, 自旋动力学模拟, Landau-Lifshitz-Gilbert方程, 对称感知描述符, 巡游电子磁体, 非平衡现象

## 3 点简述
- 核心问题：巡游电子磁体中电子介导力的高效准确预测，以支持大规模Landau-Lifshitz-Gilbert模拟。
- 方法要点：基于局域性原理，开发深度神经网络模型，结合群论构建对称感知描述符，确保晶格和自旋旋转对称性。
- 实验或效果：应用于s-d交换模型，揭示三角晶格上四面体自旋序的异常粗化和方晶格系统中相分离动力学的冻结现象。

## 摘要（原文）

> We review recent advances in machine learning (ML) force-field methods for Landau-Lifshitz-Gilbert (LLG) simulations of itinerant electron magnets, focusing on scalability and transferability. Built on the principle of locality, a deep neural network model is developed to efficiently and accurately predict the electron-mediated forces governing spin dynamics. Symmetry-aware descriptors constructed through a group-theoretical approach ensure rigorous incorporation of both lattice and spin-rotation symmetries. The framework is demonstrated using the prototypical s-d exchange model widely employed in spintronics. ML-enabled large-scale simulations reveal novel nonequilibrium phenomena, including anomalous coarsening of tetrahedral spin order on the triangular lattice and the freezing of phase separation dynamics in lightly hole-doped, strong-coupling square-lattice systems. These results establish ML force-field frameworks as scalable, accurate, and versatile tools for modeling nonequilibrium spin dynamics in itinerant magnets.

