---
layout: default
title: Monocular Reconstruction of Neural Tactile Fields
---

# Monocular Reconstruction of Neural Tactile Fields
**arXiv**：[2602.12508v1](https://arxiv.org/abs/2602.12508) · [PDF](https://arxiv.org/pdf/2602.12508.pdf)  
**作者**：Pavan Mantripragada, Siddhanth Deshmukh, Eadom Dessalene, Manas Desai, Yiannis Aloimonos  

**一句话要点**：提出神经触觉场以从单目图像预测交互感知的3D表示，用于机器人路径规划。

**关键词**：神经触觉场, 单目3D重建, 机器人路径规划, 交互感知表示, 触觉预测

## 3 点简述
- 核心问题：机器人需在可变形环境中规划路径，现有静态几何表示无法处理交互感知。
- 方法要点：引入神经触觉场，从单目RGB图像预测空间位置到预期触觉响应的映射。
- 实验或效果：相比先进方法，体积重建提升85.8%，表面重建提升26.7%，支持路径规划避开高阻力区域。

## 摘要（原文）

> Robots operating in the real world must plan through environments that deform, yield, and reconfigure under contact, requiring interaction-aware 3D representations that extend beyond static geometric occupancy. To address this, we introduce neural tactile fields, a novel 3D representation that maps spatial locations to the expected tactile response upon contact. Our model predicts these neural tactile fields from a single monocular RGB image -- the first method to do so. When integrated with off-the-shelf path planners, neural tactile fields enable robots to generate paths that avoid high-resistance objects while deliberately routing through low-resistance regions (e.g. foliage), rather than treating all occupied space as equally impassable. Empirically, our learning framework improves volumetric 3D reconstruction by $85.8\%$ and surface reconstruction by $26.7\%$ compared to state-of-the-art monocular 3D reconstruction methods (LRM and Direct3D).

