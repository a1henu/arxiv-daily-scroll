---
layout: default
title: 4D Gaussian Splatting as a Learned Dynamical System
---

# 4D Gaussian Splatting as a Learned Dynamical System
**arXiv**：[2512.19648v1](https://arxiv.org/abs/2512.19648) · [PDF](https://arxiv.org/pdf/2512.19648.pdf)  
**作者**：Arnold Caleb Asiimwe, Carl Vondrick  

**一句话要点**：提出EvoGS将4D高斯溅射重构为连续时间动力系统，以提升动态场景建模的效率和一致性

**关键词**：4D高斯溅射, 连续时间动力系统, 神经动力场, 动态场景建模, 时间一致性, 实时渲染

## 3 点简述
- 核心问题：传统基于变形的4D高斯溅射方法在动态场景建模中可能缺乏运动连贯性和时间一致性
- 方法要点：将高斯表示视为演化物理系统，通过学习的神经动力场连续积分生成场景运动，而非逐帧变形
- 实验或效果：在动态场景基准测试中，EvoGS相比变形场基线实现了更好的运动连贯性和时间一致性，同时保持实时渲染

## 摘要（原文）

> We reinterpret 4D Gaussian Splatting as a continuous-time dynamical system, where scene motion arises from integrating a learned neural dynamical field rather than applying per-frame deformations. This formulation, which we call EvoGS, treats the Gaussian representation as an evolving physical system whose state evolves continuously under a learned motion law. This unlocks capabilities absent in deformation-based approaches:(1) sample-efficient learning from sparse temporal supervision by modeling the underlying motion law; (2) temporal extrapolation enabling forward and backward prediction beyond observed time ranges; and (3) compositional dynamics that allow localized dynamics injection for controllable scene synthesis. Experiments on dynamic scene benchmarks show that EvoGS achieves better motion coherence and temporal consistency compared to deformation-field baselines while maintaining real-time rendering

