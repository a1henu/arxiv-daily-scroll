---
layout: default
title: KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite
---

# KAN-FIF: Spline-Parameterized Lightweight Physics-based Tropical Cyclone Estimation on Meteorological Satellite
**arXiv**：[2602.12117v1](https://arxiv.org/abs/2602.12117) · [PDF](https://arxiv.org/pdf/2602.12117.pdf)  
**作者**：Jiakang Shen, Qinghui Chen, Runtong Wang, Chenrui Xu, Jinglin Zhang, Cong Bai, Feng Zhang  

**一句话要点**：提出KAN-FIF框架以解决热带气旋监测中模型计算效率低和参数多的问题

**关键词**：热带气旋估计, 轻量级模型, 样条参数化, 边缘计算, 气象卫星, 特征交互

## 3 点简述
- 现有物理引导模型因线性特征交互导致参数多、硬件不兼容，阻碍边缘设备部署
- KAN-FIF集成MLP、CNN与样条参数化KAN层，实现轻量级多模态架构
- 实验显示参数减少94.8%，推理加速68.7%，MAE降低32.5%，边缘部署可行

## 摘要（原文）

> Tropical cyclones (TC) are among the most destructive natural disasters, causing catastrophic damage to coastal regions through extreme winds, heavy rainfall, and storm surges. Timely monitoring of tropical cyclones is crucial for reducing loss of life and property, yet it is hindered by the computational inefficiency and high parameter counts of existing methods on resource-constrained edge devices. Current physics-guided models suffer from linear feature interactions that fail to capture high-order polynomial relationships between TC attributes, leading to inflated model sizes and hardware incompatibility. To overcome these challenges, this study introduces the Kolmogorov-Arnold Network-based Feature Interaction Framework (KAN-FIF), a lightweight multimodal architecture that integrates MLP and CNN layers with spline-parameterized KAN layers. For Maximum Sustained Wind (MSW) prediction, experiments demonstrate that the KAN-FIF framework achieves a $94.8\%$ reduction in parameters (0.99MB vs 19MB) and $68.7\%$ faster inference per sample (2.3ms vs 7.35ms) compared to baseline model Phy-CoCo, while maintaining superior accuracy with $32.5\%$ lower MAE. The offline deployment experiment of the FY-4 series meteorological satellite processor on the Qingyun-1000 development board achieved a 14.41ms per-sample inference latency with the KAN-FIF framework, demonstrating promising feasibility for operational TC monitoring and extending deployability to edge-device AI applications. The code is released at https://github.com/Jinglin-Zhang/KAN-FIF.

