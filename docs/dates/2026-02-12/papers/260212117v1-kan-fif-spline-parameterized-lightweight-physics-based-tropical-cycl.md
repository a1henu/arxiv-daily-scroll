---
layout: default
title: KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite
---

# KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite
**arXiv**：[2602.12117v1](https://arxiv.org/abs/2602.12117) · [PDF](https://arxiv.org/pdf/2602.12117.pdf)  
**作者**：Jiakang Shen, Qinghui Chen, Runtong Wang, Chenrui Xu, Jinglin Zhang, Cong Bai, Feng Zhang  

**一句话要点**：提出KAN-FIF框架，通过样条参数化轻量网络解决热带气旋监测在边缘设备上的计算效率问题。

**关键词**：热带气旋监测, 轻量网络, 样条参数化, 边缘计算, 多模态架构, 物理引导模型

## 3 点简述
- 核心问题：现有物理引导模型参数多、计算慢，难以在资源受限边缘设备上高效监测热带气旋。
- 方法要点：结合MLP、CNN与样条参数化KAN层，构建轻量多模态架构以捕获高阶多项式关系。
- 实验或效果：相比基线模型，参数减少94.8%，推理速度提升68.7%，MAE降低32.5%，在卫星处理器上验证了边缘部署可行性。

## 摘要（原文）

> Tropical cyclones (TC) are among the most destructive natural disasters, causing catastrophic damage to coastal regions through extreme winds, heavy rainfall, and storm surges. Timely monitoring of tropical cyclones is crucial for reducing loss of life and property, yet it is hindered by the computational inefficiency and high parameter counts of existing methods on resource-constrained edge devices. Current physics-guided models suffer from linear feature interactions that fail to capture high-order polynomial relationships between TC attributes, leading to inflated model sizes and hardware incompatibility. To overcome these challenges, this study introduces the Kolmogorov-Arnold Network-based Feature Interaction Framework (KAN-FIF), a lightweight multimodal architecture that integrates MLP and CNN layers with spline-parameterized KAN layers. For Maximum Sustained Wind (MSW) prediction, experiments demonstrate that the KAN-FIF framework achieves a $94.8\%$ reduction in parameters (0.99MB vs 19MB) and $68.7\%$ faster inference per sample (2.3ms vs 7.35ms) compared to baseline model Phy-CoCo, while maintaining superior accuracy with $32.5\%$ lower MAE. The offline deployment experiment of the FY-4 series meteorological satellite processor on the Qingyun-1000 development board achieved a 14.41ms per-sample inference latency with the KAN-FIF framework, demonstrating promising feasibility for operational TC monitoring and extending deployability to edge-device AI applications. The code is released at https://github.com/Jinglin-Zhang/KAN-FIF.

