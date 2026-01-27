---
layout: default
title: ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection
---

# ExoGS: A 4D Real-to-Sim-to-Real Framework for Scalable Manipulation Data Collection
**arXiv**：[2601.18629v1](https://arxiv.org/abs/2601.18629) · [PDF](https://arxiv.org/pdf/2601.18629.pdf)  
**作者**：Yiming Wang, Ruogu Zhang, Minyang Li, Hao Shi, Junbo Wang, Deyi Li, Jieji Ren, Wenhai Liu, Weiming Wang, Hao-Shu Fang  

**一句话要点**：提出ExoGS框架，通过4D真实-仿真-真实转换实现可扩展的机器人操作数据收集

**关键词**：机器人操作, 真实-仿真-真实, 4D重建, 高斯溅射, 数据增强, 策略学习

## 3 点简述
- 核心问题：现有方法忽略交互转移，难以高效获取接触丰富任务的仿真数据
- 方法要点：使用被动外骨骼捕获真实交互，重建为可编辑3D高斯溅射资产进行仿真回放
- 实验或效果：相比遥操作基线，显著提升数据效率和策略泛化能力

## 摘要（原文）

> Real-to-Sim-to-Real technique is gaining increasing interest for robotic manipulation, as it can generate scalable data in simulation while having narrower sim-to-real gap. However, previous methods mainly focused on environment-level visual real-to-sim transfer, ignoring the transfer of interactions, which could be challenging and inefficient to obtain purely in simulation especially for contact-rich tasks. We propose ExoGS, a robot-free 4D Real-to-Sim-to-Real framework that captures both static environments and dynamic interactions in the real world and transfers them seamlessly to a simulated environment. It provides a new solution for scalable manipulation data collection and policy learning. ExoGS employs a self-designed robot-isomorphic passive exoskeleton AirExo-3 to capture kinematically consistent trajectories with millimeter-level accuracy and synchronized RGB observations during direct human demonstrations. The robot, objects, and environment are reconstructed as editable 3D Gaussian Splatting assets, enabling geometry-consistent replay and large-scale data augmentation. Additionally, a lightweight Mask Adapter injects instance-level semantics into the policy to enhance robustness under visual domain shifts. Real-world experiments demonstrate that ExoGS significantly improves data efficiency and policy generalization compared to teleoperation-based baselines. Code and hardware files have been released on https://github.com/zaixiabalala/ExoGS.

