---
layout: default
title: DyQ-VLA: Temporal-Dynamic-Aware Quantization for Embodied Vision-Language-Action Models
---

# DyQ-VLA: Temporal-Dynamic-Aware Quantization for Embodied Vision-Language-Action Models
**arXiv**：[2603.07904v1](https://arxiv.org/abs/2603.07904) · [PDF](https://arxiv.org/pdf/2603.07904.pdf)  
**作者**：Zihao Zheng, Hangyu Cao, Sicheng Tian, Jiayu Chen, Maoliang Li, Xinhao Sun, Hailong Zou, Zhaobo Zhang, Xuanzhe Liu, Donggang Cao, Hong Mei, Xiang Chen  

**一句话要点**：提出DyQ-VLA动态量化框架，以解决具身视觉-语言-动作模型中的时态动态敏感性和实时分配问题。

**关键词**：具身智能, 模型量化, 动态位宽分配, 视觉-语言-动作模型, 实时优化

## 3 点简述
- 核心问题：静态量化在VLA模型中因时态动态敏感性和实时分配不足而效果不佳。
- 方法要点：基于实时运动学代理触发位宽切换，并动态分配最优位宽。
- 实验或效果：内存占用降至30.9%，性能保持99.5%，仿真和现实速度提升达1.49倍和1.43倍。

## 摘要（原文）

> Vision-Language-Action (VLA) models are dominant in embodied intelligence but are constrained by inference overheads. While model quantization alleviates these bottlenecks for edge deployment, static quantization approaches remain suboptimal for VLAs due to two critical challenges: (1) Temporal-dynamic sensitivity, where fixed precision wastes resources by ignoring stage-varying error tolerances; and (2) Real-time allocation, where identifying real-time sensitivity to guide bit allocation remains unsolved. To address these challenges, we propose DyQ-VLA, a dynamic quantization framework for VLAs. Specifically, a sensitivity-aware switching strategy leverages real-time kinematic proxies to trigger the bit-width switch, while a kinematic-guided module dynamically allocates the optimal bit-width. Experiments show that DyQ-VLA requires only 30.9% of the original memory footprint while maintaining 99.5% of its original performance, achieving 1.49x simulation and up to 1.43x real-world speedups.

