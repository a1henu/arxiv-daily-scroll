---
layout: default
title: Simulation-Ready Cluttered Scene Estimation via Physics-aware Joint Shape and Pose Optimization
---

# Simulation-Ready Cluttered Scene Estimation via Physics-aware Joint Shape and Pose Optimization
**arXiv**：[2602.20150v1](https://arxiv.org/abs/2602.20150) · [PDF](https://arxiv.org/pdf/2602.20150.pdf)  
**作者**：Wei-Cheng Huang, Jiaheng Han, Xiaohan Ye, Zherong Pan, Kris Hauser  

**一句话要点**：提出基于物理约束的联合形状与姿态优化方法，以解决杂乱场景中仿真就绪场景估计的挑战。

**关键词**：场景估计, 物理约束优化, 形状可微模型, 杂乱环境, 仿真就绪重建

## 3 点简述
- 核心问题：现有方法在杂乱环境中计算成本高、鲁棒性差，难以扩展到多交互物体。
- 方法要点：利用形状可微接触模型实现全局可微优化，结合增强拉格朗日海森矩阵的结构稀疏性设计高效求解器。
- 实验或效果：在最多5个物体和22个凸包的杂乱场景中，鲁棒重建物理有效的仿真就绪形状与姿态。

## 摘要（原文）

> Estimating simulation-ready scenes from real-world observations is crucial for downstream planning and policy learning tasks. Regretfully, existing methods struggle in cluttered environments, often exhibiting prohibitive computational cost, poor robustness, and restricted generality when scaling to multiple interacting objects. We propose a unified optimization-based formulation for real-to-sim scene estimation that jointly recovers the shapes and poses of multiple rigid objects under physical constraints. Our method is built on two key technical innovations. First, we leverage the recently introduced shape-differentiable contact model, whose global differentiability permits joint optimization over object geometry and pose while modeling inter-object contacts. Second, we exploit the structured sparsity of the augmented Lagrangian Hessian to derive an efficient linear system solver whose computational cost scales favorably with scene complexity. Building on this formulation, we develop an end-to-end real-to-sim scene estimation pipeline that integrates learning-based object initialization, physics-constrained joint shape-pose optimization, and differentiable texture refinement. Experiments on cluttered scenes with up to 5 objects and 22 convex hulls demonstrate that our approach robustly reconstructs physically valid, simulation-ready object shapes and poses.

