---
layout: default
title: AI-enhanced tuning of quantum dot Hamiltonians toward Majorana modes
---

# AI-enhanced tuning of quantum dot Hamiltonians toward Majorana modes
**arXiv**：[2601.02149v1](https://arxiv.org/abs/2601.02149) · [PDF](https://arxiv.org/pdf/2601.02149.pdf)  
**作者**：Mateusz Krawczyk, Jarosław Pawłowski  

**一句话要点**：提出基于神经网络的量子点哈密顿量自调谐方法，以在结构中实现马约拉纳模式

**关键词**：量子点模拟器, 马约拉纳模式, 神经网络调谐, 电导图分析, 无监督学习, 物理信息损失

## 3 点简述
- 核心问题：量子点模拟器中马约拉纳模式的获取需精确调谐哈密顿量参数，传统方法效率低。
- 方法要点：使用深度视觉变换器网络，基于电导图无监督学习参数与结构关系，结合物理信息损失函数。
- 实验或效果：单步更新即可从广泛初始参数生成非平凡零模式，迭代调谐可覆盖更大参数空间。

## 摘要（原文）

> We propose a neural network-based model capable of learning the broad landscape of working regimes in quantum dot simulators, and using this knowledge to autotune these devices - based on transport measurements - toward obtaining Majorana modes in the structure. The model is trained in an unsupervised manner on synthetic data in the form of conductance maps, using a physics-informed loss that incorporates key properties of Majorana zero modes. We show that, with appropriate training, a deep vision-transformer network can efficiently memorize relation between Hamiltonian parameters and structures on conductance maps and use it to propose parameters update for a quantum dot chain that drive the system toward topological phase. Starting from a broad range of initial detunings in parameter space, a single update step is sufficient to generate nontrivial zero modes. Moreover, by enabling an iterative tuning procedure - where the system acquires updated conductance maps at each step - we demonstrate that the method can address a much larger region of the parameter space.

