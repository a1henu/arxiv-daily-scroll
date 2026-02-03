---
layout: default
title: DDP-WM: Disentangled Dynamics Prediction for Efficient World Models
---

# DDP-WM: Disentangled Dynamics Prediction for Efficient World Models
**arXiv**：[2602.01780v1](https://arxiv.org/abs/2602.01780) · [PDF](https://arxiv.org/pdf/2602.01780.pdf)  
**作者**：Shicheng Yin, Kaixuan Yin, Weixing Chen, Yang Liu, Guanbin Li, Liang Lin  

**一句话要点**：提出DDP-WM世界模型，通过解耦动态预测解决密集Transformer模型计算开销大问题，提升机器人规划效率。

**关键词**：世界模型, 解耦动态预测, 机器人规划, 高效推理, Transformer优化

## 3 点简述
- 核心问题：现有密集Transformer世界模型计算开销大，阻碍实时部署。
- 方法要点：基于解耦动态预测，分解为稀疏主动态和背景更新，优化资源分配。
- 实验或效果：在Push-T任务中实现约9倍推理加速，MPC成功率从90%提升至98%。

## 摘要（原文）

> World models are essential for autonomous robotic planning. However, the substantial computational overhead of existing dense Transformerbased models significantly hinders real-time deployment. To address this efficiency-performance bottleneck, we introduce DDP-WM, a novel world model centered on the principle of Disentangled Dynamics Prediction (DDP). We hypothesize that latent state evolution in observed scenes is heterogeneous and can be decomposed into sparse primary dynamics driven by physical interactions and secondary context-driven background updates. DDP-WM realizes this decomposition through an architecture that integrates efficient historical processing with dynamic localization to isolate primary dynamics. By employing a crossattention mechanism for background updates, the framework optimizes resource allocation and provides a smooth optimization landscape for planners. Extensive experiments demonstrate that DDP-WM achieves significant efficiency and performance across diverse tasks, including navigation, precise tabletop manipulation, and complex deformable or multi-body interactions. Specifically, on the challenging Push-T task, DDP-WM achieves an approximately 9 times inference speedup and improves the MPC success rate from 90% to98% compared to state-of-the-art dense models. The results establish a promising path for developing efficient, high-fidelity world models. Codes will be available at https://github.com/HCPLabSYSU/DDP-WM.

