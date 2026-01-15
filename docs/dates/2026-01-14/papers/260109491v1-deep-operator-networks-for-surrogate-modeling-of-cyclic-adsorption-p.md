---
layout: default
title: Deep Operator Networks for Surrogate Modeling of Cyclic Adsorption Processes with Varying Initial Conditions
---

# Deep Operator Networks for Surrogate Modeling of Cyclic Adsorption Processes with Varying Initial Conditions
**arXiv**：[2601.09491v1](https://arxiv.org/abs/2601.09491) · [PDF](https://arxiv.org/pdf/2601.09491.pdf)  
**作者**：Beatrice Ceccanti, Mattia Galanti, Ivo Roghair, Martin van Sint Annaland  

**一句话要点**：应用DeepONet作为替代模型加速变初始条件循环吸附过程的模拟与优化

**关键词**：DeepONet, 循环吸附过程, 替代建模, 算子学习, PDE求解, 泛化能力

## 3 点简述
- 核心问题：循环吸附过程模拟需重复求解瞬态PDE，计算成本高，且需泛化到广泛初始条件。
- 方法要点：使用DeepONet学习从初始条件到解场的非线性算子，构建混合训练数据集以增强泛化能力。
- 实验或效果：模型在训练分布内外及未见函数形式上均能准确预测，验证了其作为高效替代模型的潜力。

## 摘要（原文）

> Deep Operator Networks are emerging as fundamental tools among various neural network types to learn mappings between function spaces, and have recently gained attention due to their ability to approximate nonlinear operators. In particular, DeepONets offer a natural formulation for PDE solving, since the solution of a partial differential equation can be interpreted as an operator mapping an initial condition to its corresponding solution field. In this work, we applied DeepONets in the context of process modeling for adsorption technologies, to assess their feasibility as surrogates for cyclic adsorption process simulation and optimization. The goal is to accelerate convergence of cyclic processes such as Temperature-Vacuum Swing Adsorption (TVSA), which require repeated solution of transient PDEs, which are computationally expensive. Since each step of a cyclic adsorption process starts from the final state of the preceding step, effective surrogate modeling requires generalization across a wide range of initial conditions. The governing equations exhibit steep traveling fronts, providing a demanding benchmark for operator learning. To evaluate functional generalization under these conditions, we construct a mixed training dataset composed of heterogeneous initial conditions and train DeepONets to approximate the corresponding solution operators. The trained models are then tested on initial conditions outside the parameter ranges used during training, as well as on completely unseen functional forms. The results demonstrate accurate predictions both within and beyond the training distribution, highlighting DeepONets as potential efficient surrogates for accelerating cyclic adsorption simulations and optimization workflows.

