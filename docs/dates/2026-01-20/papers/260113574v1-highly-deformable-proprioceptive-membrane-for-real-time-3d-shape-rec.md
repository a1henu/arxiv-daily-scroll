---
layout: default
title: Highly Deformable Proprioceptive Membrane for Real-Time 3D Shape Reconstruction
---

# Highly Deformable Proprioceptive Membrane for Real-Time 3D Shape Reconstruction
**arXiv**：[2601.13574v1](https://arxiv.org/abs/2601.13574) · [PDF](https://arxiv.org/pdf/2601.13574.pdf)  
**作者**：Guanyu Xu, Jiaqi Wang, Dezhong Tong, Xiaonan Huang  

**一句话要点**：提出基于光学波导传感的可变形本体感知膜，用于机器人实时三维形状重建。

**关键词**：三维形状重建, 本体感知膜, 光学波导传感, 可变形机器人, 实时感知, 数据驱动模型

## 3 点简述
- 核心问题：视觉方法在低光照或遮挡下不可靠，现有形状感知膜存在结构复杂、变形受限和电磁干扰问题。
- 方法要点：采用软性硅胶膜集成LED和光电二极管，通过液态金属迹线解码光强信号，数据驱动模型重建三维点云。
- 实验或效果：在140毫米方形膜上实现90Hz实时重建，平均误差1.3毫米，支持高达25毫米的凹陷变形。

## 摘要（原文）

> Reconstructing the three-dimensional (3D) geometry of object surfaces is essential for robot perception, yet vision-based approaches are generally unreliable under low illumination or occlusion. This limitation motivates the design of a proprioceptive membrane that conforms to the surface of interest and infers 3D geometry by reconstructing its own deformation. Conventional shape-aware membranes typically rely on resistive, capacitive, or magneto-sensitive mechanisms. However, these methods often encounter challenges such as structural complexity, limited compliance during large-scale deformation, and susceptibility to electromagnetic interference. This work presents a soft, flexible, and stretchable proprioceptive silicone membrane based on optical waveguide sensing. The membrane sensor integrates edge-mounted LEDs and centrally distributed photodiodes (PDs), interconnected via liquid-metal traces embedded within a multilayer elastomeric composite. Rich deformation-dependent light intensity signals are decoded by a data-driven model to recover the membrane geometry as a 3D point cloud. On a customized 140 mm square membrane, real-time reconstruction of large-scale out-of-plane deformation is achieved at 90 Hz with an average reconstruction error of 1.3 mm, measured by Chamfer distance, while maintaining accuracy for indentations up to 25 mm. The proposed framework provides a scalable, robust, and low-profile solution for global shape perception in deformable robotic systems.

