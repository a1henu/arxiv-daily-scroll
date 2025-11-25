---
layout: default
title: MonoMSK: Monocular 3D Musculoskeletal Dynamics Estimation
---

# MonoMSK: Monocular 3D Musculoskeletal Dynamics Estimation
**arXiv**：[2511.19326v1](https://arxiv.org/abs/2511.19326) · [PDF](https://arxiv.org/pdf/2511.19326.pdf)  
**作者**：Farnoosh Koleini, Hongfei Xue, Ahmed Helmy, Pu Wang  

**一句话要点**：提出MonoMSK框架，通过单目视频估计生物力学真实的3D人体运动与力。

**关键词**：单目3D估计, 生物力学建模, 物理模拟, 运动与力联合估计, 变换器逆动力学

## 3 点简述
- 核心问题：现有单目方法使用简化模型忽略物理，限制生物力学保真度。
- 方法要点：结合数据驱动与物理模拟，使用解剖准确模型联合估计运动与力。
- 实验效果：在多个数据集上显著提升运动精度，首次实现精确单目力估计。

## 摘要（原文）

> Reconstructing biomechanically realistic 3D human motion - recovering both kinematics (motion) and kinetics (forces) - is a critical challenge. While marker-based systems are lab-bound and slow, popular monocular methods use oversimplified, anatomically inaccurate models (e.g., SMPL) and ignore physics, fundamentally limiting their biomechanical fidelity. In this work, we introduce MonoMSK, a hybrid framework that bridges data-driven learning and physics-based simulation for biomechanically realistic 3D human motion estimation from monocular video. MonoMSK jointly recovers both kinematics (motions) and kinetics (forces and torques) through an anatomically accurate musculoskeletal model. By integrating transformer-based inverse dynamics with differentiable forward kinematics and dynamics layers governed by ODE-based simulation, MonoMSK establishes a physics-regulated inverse-forward loop that enforces biomechanical causality and physical plausibility. A novel forward-inverse consistency loss further aligns motion reconstruction with the underlying kinetic reasoning. Experiments on BML-MoVi, BEDLAM, and OpenCap show that MonoMSK significantly outperforms state-of-the-art methods in kinematic accuracy, while for the first time enabling precise monocular kinetics estimation.

