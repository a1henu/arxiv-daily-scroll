---
layout: default
title: Terrain-Adaptive Mobile 3D Printing with Hierarchical Control
---

# Terrain-Adaptive Mobile 3D Printing with Hierarchical Control
**arXiv**：[2601.10208v1](https://arxiv.org/abs/2601.10208) · [PDF](https://arxiv.org/pdf/2601.10208.pdf)  
**作者**：Shuangshan Nors Li, J. Nathan Kutz  

**一句话要点**：提出AI驱动分层控制框架，实现非结构化地形上的移动3D打印高精度与高机动性

**关键词**：移动3D打印, 非结构化地形, AI扰动预测, 多模态传感器融合, 分层控制, 自主建造

## 3 点简述
- 核心问题：移动3D打印在非结构化地形上存在平台机动性与沉积精度冲突，现有系统难以兼顾。
- 方法要点：集成AI扰动预测与多模态传感器融合，采用三层控制架构实现闭环感知-学习-执行。
- 实验或效果：户外实验在斜坡和不规则地形上实现亚厘米级打印精度，同时保持平台全机动性。

## 摘要（原文）

> Mobile 3D printing on unstructured terrain remains challenging due to the conflict between platform mobility and deposition precision. Existing gantry-based systems achieve high accuracy but lack mobility, while mobile platforms struggle to maintain print quality on uneven ground. We present a framework that tightly integrates AI-driven disturbance prediction with multi-modal sensor fusion and hierarchical hardware control, forming a closed-loop perception-learning-actuation system. The AI module learns terrain-to-perturbation mappings from IMU, vision, and depth sensors, enabling proactive compensation rather than reactive correction. This intelligence is embedded into a three-layer control architecture: path planning, predictive chassis-manipulator coordination, and precision hardware execution. Through outdoor experiments on terrain with slopes and surface irregularities, we demonstrate sub-centimeter printing accuracy while maintaining full platform mobility. This AI-hardware integration establishes a practical foundation for autonomous construction in unstructured environments.

