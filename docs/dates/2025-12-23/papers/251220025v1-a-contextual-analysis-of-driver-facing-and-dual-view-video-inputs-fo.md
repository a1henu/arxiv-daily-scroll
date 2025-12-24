---
layout: default
title: A Contextual Analysis of Driver-Facing and Dual-View Video Inputs for Distraction Detection in Naturalistic Driving Environments
---

# A Contextual Analysis of Driver-Facing and Dual-View Video Inputs for Distraction Detection in Naturalistic Driving Environments
**arXiv**：[2512.20025v1](https://arxiv.org/abs/2512.20025) · [PDF](https://arxiv.org/pdf/2512.20025.pdf)  
**作者**：Anthony Dontoh, Stephanie Ivey, Armstrong Aboah  

**一句话要点**：提出双视图输入方法以提升自然驾驶环境中分心驾驶检测的准确性

**关键词**：分心驾驶检测, 双视图输入, 时空动作识别, 自然驾驶环境, 多模态融合

## 3 点简述
- 核心问题：现有分心驾驶检测模型依赖驾驶员面部视图，忽略环境上下文影响。
- 方法要点：使用同步双摄像头数据，评估三种时空动作识别架构在单视图和双视图配置下的性能。
- 实验或效果：双视图输入在某些模型中提升性能，但效果取决于架构设计，如SlowOnly提升9.8%，SlowFast下降7.2%。

## 摘要（原文）

> Despite increasing interest in computer vision-based distracted driving detection, most existing models rely exclusively on driver-facing views and overlook crucial environmental context that influences driving behavior. This study investigates whether incorporating road-facing views alongside driver-facing footage improves distraction detection accuracy in naturalistic driving conditions. Using synchronized dual-camera recordings from real-world driving, we benchmark three leading spatiotemporal action recognition architectures: SlowFast-R50, X3D-M, and SlowOnly-R50. Each model is evaluated under two input configurations: driver-only and stacked dual-view. Results show that while contextual inputs can improve detection in certain models, performance gains depend strongly on the underlying architecture. The single-pathway SlowOnly model achieved a 9.8 percent improvement with dual-view inputs, while the dual-pathway SlowFast model experienced a 7.2 percent drop in accuracy due to representational conflicts. These findings suggest that simply adding visual context is not sufficient and may lead to interference unless the architecture is specifically designed to support multi-view integration. This study presents one of the first systematic comparisons of single- and dual-view distraction detection models using naturalistic driving data and underscores the importance of fusion-aware design for future multimodal driver monitoring systems.

