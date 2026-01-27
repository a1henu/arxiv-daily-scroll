---
layout: default
title: Grasp-and-Lift: Executable 3D Hand-Object Interaction Reconstruction via Physics-in-the-Loop Optimization
---

# Grasp-and-Lift: Executable 3D Hand-Object Interaction Reconstruction via Physics-in-the-Loop Optimization
**arXiv**：[2601.18121v1](https://arxiv.org/abs/2601.18121) · [PDF](https://arxiv.org/pdf/2601.18121.pdf)  
**作者**：Byeonggyeol Choi, Woojin Oh, Jongwoo Lim  

**一句话要点**：提出基于物理模拟的优化框架，将视觉对齐轨迹转换为物理可执行的手-物交互轨迹。

**关键词**：手-物交互重建, 物理模拟优化, 轨迹转换, 黑盒优化, 可执行运动生成

## 3 点简述
- 现有手-物交互数据集在物理模拟中常产生不合理的交互，如穿透和不稳定抓取。
- 使用基于关键帧的低维参数化和CMA-ES优化器，将物理引擎作为黑盒目标函数进行优化。
- 相比现有方法，在重放时降低姿态误差，更准确地恢复物理交互，生成高保真数据。

## 摘要（原文）

> Dexterous hand manipulation increasingly relies on large-scale motion datasets with precise hand-object trajectory data. However, existing resources such as DexYCB and HO3D are primarily optimized for visual alignment but often yield physically implausible interactions when replayed in physics simulators, including penetration, missed contact, and unstable grasps.
>   We propose a simulation-in-the-loop refinement framework that converts these visually aligned trajectories into physically executable ones. Our core contribution is to formulate this as a tractable black-box optimization problem. We parameterize the hand's motion using a low-dimensional, spline-based representation built on sparse temporal keyframes. This allows us to use a powerful gradient-free optimizer, CMA-ES, to treat the high-fidelity physics engine as a black-box objective function. Our method finds motions that simultaneously maximize physical success (e.g., stable grasp and lift) while minimizing deviation from the original human demonstration.
>   Compared to MANIPTRANS-recent transfer pipelines, our approach achieves lower hand and object pose errors during replay and more accurately recovers hand-object physical interactions. Our approach provides a general and scalable method for converting visual demonstrations into physically valid trajectories, enabling the generation of high-fidelity data crucial for robust policy learning.

