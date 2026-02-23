---
layout: default
title: Deepmechanics
---

# Deepmechanics
**arXiv**：[2602.18060v1](https://arxiv.org/abs/2602.18060) · [PDF](https://arxiv.org/pdf/2602.18060.pdf)  
**作者**：Abhay Shinde, Aryan Amit Barsainyan, Jose Siguenza, Ankita Vaishnobi Bisoi, Rakshit Kr. Singh, Bharath Ramsundar  

**一句话要点**：基于DeepChem框架对物理信息深度学习模型在经典力学系统进行基准测试

**关键词**：物理信息深度学习, 基准测试, 经典力学系统, DeepChem框架, 稳定性分析

## 3 点简述
- 核心问题：物理信息深度学习模型在多样物理现象中缺乏系统基准测试，尤其在保守和耗散系统稳定性方面。
- 方法要点：使用DeepChem框架评估HNN、LNN和SRNN三种架构在六个经典力学系统上的性能。
- 实验或效果：所有模型在混沌或非保守系统中均难以保持稳定性，表明需进一步研究以提升鲁棒性。

## 摘要（原文）

> Physics-informed deep learning models have emerged as powerful tools for learning dynamical systems. These models directly encode physical principles into network architectures. However, systematic benchmarking of these approaches across diverse physical phenomena remains limited, particularly in conservative and dissipative systems. In addition, benchmarking that has been done thus far does not integrate out full trajectories to check stability. In this work, we benchmark three prominent physics-informed architectures such as Hamiltonian Neural Networks (HNN), Lagrangian Neural Networks (LNN), and Symplectic Recurrent Neural Networks (SRNN) using the DeepChem framework, an open-source scientific machine learning library. We evaluate these models on six dynamical systems spanning classical conservative mechanics (mass-spring system, simple pendulum, double pendulum, and three-body problem, spring-pendulum) and non-conservative systems with contact (bouncing ball). We evaluate models by computing error on predicted trajectories and evaluate error both quantitatively and qualitatively. We find that all benchmarked models struggle to maintain stability for chaotic or nonconservative systems. Our results suggest that more research is needed for physics-informed deep learning models to learn robust models of classical mechanical systems.

