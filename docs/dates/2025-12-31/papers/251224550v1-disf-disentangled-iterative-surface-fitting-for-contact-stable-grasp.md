---
layout: default
title: DISF: Disentangled Iterative Surface Fitting for Contact-stable Grasp Planning with Grasp Pose Alignment to the Object Center of Mass
---

# DISF: Disentangled Iterative Surface Fitting for Contact-stable Grasp Planning with Grasp Pose Alignment to the Object Center of Mass
**arXiv**：[2512.24550v1](https://arxiv.org/abs/2512.24550) · [PDF](https://arxiv.org/pdf/2512.24550.pdf)  
**作者**：Tomoya Yamanokuchi, Alberto Bacchin, Emilio Olivastri, Ryotaro Arifuku, Takamitsu Matsubara, Emanuele Menegatti  

**一句话要点**：提出解耦迭代表面拟合算法以解决基于表面拟合的抓取规划中接触稳定性不足的问题

**关键词**：抓取规划, 表面拟合, 接触稳定性, 质心对齐, 解耦优化, 机器人抓取

## 3 点简述
- 核心问题：现有表面拟合抓取规划算法过度关注几何对齐，忽略接触点分布的稳定性，导致抓取不稳定
- 方法要点：通过解耦抓取姿态优化为旋转对齐、平移精调与夹爪开度调整三步，集成接触稳定性与几何兼容性
- 实验或效果：在仿真与真实机器人实验中验证，减少质心偏差并提高抓取成功率，优于基线方法

## 摘要（原文）

> In this work, we address the limitation of surface fitting-based grasp planning algorithm, which primarily focuses on geometric alignment between the gripper and object surface while overlooking the stability of contact point distribution, often resulting in unstable grasps due to inadequate contact configurations. To overcome this limitation, we propose a novel surface fitting algorithm that integrates contact stability while preserving geometric compatibility. Inspired by human grasping behavior, our method disentangles the grasp pose optimization into three sequential steps: (1) rotation optimization to align contact normals, (2) translation refinement to improve the alignment between the gripper frame origin and the object Center of Mass (CoM), and (3) gripper aperture adjustment to optimize contact point distribution. We validate our approach in simulation across 15 objects under both Known-shape (with clean CAD-derived dataset) and Observed-shape (with YCB object dataset) settings, including cross-platform grasp execution on three robot--gripper platforms. We further validate the method in real-world grasp experiments on a UR3e robot. Overall, DISF reduces CoM misalignment while maintaining geometric compatibility, translating into higher grasp success in both simulation and real-world execution compared to baselines. Additional videos and supplementary results are available on our project page: https://tomoya-yamanokuchi.github.io/disf-ras-project-page/

