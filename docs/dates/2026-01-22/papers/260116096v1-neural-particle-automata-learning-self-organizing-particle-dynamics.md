---
layout: default
title: Neural Particle Automata: Learning Self-Organizing Particle Dynamics
---

# Neural Particle Automata: Learning Self-Organizing Particle Dynamics
**arXiv**：[2601.16096v1](https://arxiv.org/abs/2601.16096) · [PDF](https://arxiv.org/pdf/2601.16096.pdf)  
**作者**：Hyunsoo Kim, Ehsan Pajouheshgar, Sabine Süsstrunk, Wenzel Jakob, Jinah Park  

**一句话要点**：提出神经粒子自动机以学习自组织粒子动力学，扩展神经细胞自动机至动态粒子系统。

**关键词**：神经粒子自动机, 自组织粒子动力学, 平滑粒子流体动力学, 点云分类, 粒子纹理合成, 可微模拟

## 3 点简述
- 核心问题：将神经细胞自动机从静态网格推广到动态粒子系统，解决邻居动态变化和计算效率挑战。
- 方法要点：使用可微平滑粒子流体动力学算子实现局部交互，支持可扩展端到端训练。
- 实验或效果：在形态发生、点云分类和粒子纹理合成等任务中展示自组织行为和鲁棒性。

## 摘要（原文）

> We introduce Neural Particle Automata (NPA), a Lagrangian generalization of Neural Cellular Automata (NCA) from static lattices to dynamic particle systems. Unlike classical Eulerian NCA where cells are pinned to pixels or voxels, NPA model each cell as a particle with a continuous position and internal state, both updated by a shared, learnable neural rule. This particle-based formulation yields clear individuation of cells, allows heterogeneous dynamics, and concentrates computation only on regions where activity is present. At the same time, particle systems pose challenges: neighborhoods are dynamic, and a naive implementation of local interactions scale quadratically with the number of particles. We address these challenges by replacing grid-based neighborhood perception with differentiable Smoothed Particle Hydrodynamics (SPH) operators backed by memory-efficient, CUDA-accelerated kernels, enabling scalable end-to-end training. Across tasks including morphogenesis, point-cloud classification, and particle-based texture synthesis, we show that NPA retain key NCA behaviors such as robustness and self-regeneration, while enabling new behaviors specific to particle systems. Together, these results position NPA as a compact neural model for learning self-organizing particle dynamics.

