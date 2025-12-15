---
layout: default
title: Pace: Physics-Aware Attentive Temporal Convolutional Network for Battery Health Estimation
---

# Pace: Physics-Aware Attentive Temporal Convolutional Network for Battery Health Estimation
**arXiv**：[2512.11332v1](https://arxiv.org/abs/2512.11332) · [PDF](https://arxiv.org/pdf/2512.11332.pdf)  
**作者**：Sara Sameer, Wei Zhang, Kannan Dhivya Dharshini, Xin Lou, Yulin Gao, Terence Goh, Qingyu Yan  

**一句话要点**：提出Pace物理感知注意力时序卷积网络，用于电池健康估计

**关键词**：电池健康估计, 物理感知模型, 时序卷积网络, 注意力机制, 边缘计算

## 3 点简述
- 核心问题：电池健康管理对现代能源系统安全与效率至关重要
- 方法要点：结合原始传感器数据与等效电路模型物理特征，设计电池专用模块
- 实验或效果：在公开数据集上优于基线模型，并在树莓派上实现实时边缘部署

## 摘要（原文）

> Batteries are critical components in modern energy systems such as electric vehicles and power grid energy storage. Effective battery health management is essential for battery system safety, cost-efficiency, and sustainability. In this paper, we propose Pace, a physics-aware attentive temporal convolutional network for battery health estimation. Pace integrates raw sensor measurements with battery physics features derived from the equivalent circuit model. We develop three battery-specific modules, including dilated temporal blocks for efficient temporal encoding, chunked attention blocks for context modeling, and a dual-head output block for fusing short- and long-term battery degradation patterns. Together, the modules enable Pace to predict battery health accurately and efficiently in various battery usage conditions. In a large public dataset, Pace performs much better than existing models, achieving an average performance improvement of 6.5 and 2.0x compared to two best-performing baseline models. We further demonstrate its practical viability with a real-time edge deployment on a Raspberry Pi. These results establish Pace as a practical and high-performance solution for battery health analytics.

