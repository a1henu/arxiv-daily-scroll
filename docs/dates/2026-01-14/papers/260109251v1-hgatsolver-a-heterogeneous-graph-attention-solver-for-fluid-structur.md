---
layout: default
title: HGATSolver: A Heterogeneous Graph Attention Solver for Fluid-Structure Interaction
---

# HGATSolver: A Heterogeneous Graph Attention Solver for Fluid-Structure Interaction
**arXiv**：[2601.09251v1](https://arxiv.org/abs/2601.09251) · [PDF](https://arxiv.org/pdf/2601.09251.pdf)  
**作者**：Qin-Yi Zhang, Hong Wang, Siyao Liu, Haichuan Lin, Linying Cao, Xiao-Hu Zhou, Chen Chen, Shuangyi Wang, Zeng-Guang Hou  

**一句话要点**：提出HGATSolver以解决流固耦合系统中异质动力学建模与预测不稳定的问题

**关键词**：流固耦合, 异质图注意力, 物理条件门控, 跨域梯度平衡, 代理建模, 多物理系统

## 3 点简述
- 核心问题：流固耦合系统涉及异质物理域，现有方法难以统一建模，且界面耦合导致响应不一致和学习难度差异，引发预测不稳定
- 方法要点：采用异质图注意力编码系统，通过节点和边类型区分物理域，引入物理条件门控机制稳定显式时间步进，并使用跨域梯度平衡损失动态优化目标
- 实验或效果：在两个构建的FSI基准和公共数据集上验证，HGATSolver达到最先进性能，为耦合多物理系统代理建模提供有效框架

## 摘要（原文）

> Fluid-structure interaction (FSI) systems involve distinct physical domains, fluid and solid, governed by different partial differential equations and coupled at a dynamic interface. While learning-based solvers offer a promising alternative to costly numerical simulations, existing methods struggle to capture the heterogeneous dynamics of FSI within a unified framework. This challenge is further exacerbated by inconsistencies in response across domains due to interface coupling and by disparities in learning difficulty across fluid and solid regions, leading to instability during prediction. To address these challenges, we propose the Heterogeneous Graph Attention Solver (HGATSolver). HGATSolver encodes the system as a heterogeneous graph, embedding physical structure directly into the model via distinct node and edge types for fluid, solid, and interface regions. This enables specialized message-passing mechanisms tailored to each physical domain. To stabilize explicit time stepping, we introduce a novel physics-conditioned gating mechanism that serves as a learnable, adaptive relaxation factor. Furthermore, an Inter-domain Gradient-Balancing Loss dynamically balances the optimization objectives across domains based on predictive uncertainty. Extensive experiments on two constructed FSI benchmarks and a public dataset demonstrate that HGATSolver achieves state-of-the-art performance, establishing an effective framework for surrogate modeling of coupled multi-physics systems.

