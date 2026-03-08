---
layout: default
title: GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins
---

# GaussTwin: Unified Simulation and Correction with Gaussian Splatting for Robotic Digital Twins
**arXiv**：[2603.05108v1](https://arxiv.org/abs/2603.05108) · [PDF](https://arxiv.org/pdf/2603.05108.pdf)  
**作者**：Yichen Cai, Paul Jansonnie, Cristiana de Farias, Oleg Arenz, Jan Peters  

**一句话要点**：提出GaussTwin以解决机器人数字孪生中统一模型缺失和真实-模拟差距问题。

**关键词**：数字孪生, 高斯泼溅, 机器人操作, 物理模拟, 视觉校正, 模型预测控制

## 3 点简述
- 核心问题：现有数字孪生系统缺乏统一模型，难以处理复杂动态交互和真实-模拟差距。
- 方法要点：结合基于位置的动力学和离散Cosserat杆公式进行物理模拟，使用高斯泼溅实现高效渲染和视觉校正。
- 实验或效果：在仿真和Franka Research 3平台上验证，相比基线方法提升跟踪精度和鲁棒性，支持下游任务如推式规划。

## 摘要（原文）

> Digital twins promise to enhance robotic manipulation by maintaining a consistent link between real-world perception and simulation. However, most existing systems struggle with the lack of a unified model, complex dynamic interactions, and the real-to-sim gap, which limits downstream applications such as model predictive control. Thus, we propose GaussTwin, a real-time digital twin that combines position-based dynamics with discrete Cosserat rod formulations for physically grounded simulation, and Gaussian splatting for efficient rendering and visual correction. By anchoring Gaussians to physical primitives and enforcing coherent SE(3) updates driven by photometric error and segmentation masks, GaussTwin achieves stable prediction-correction while preserving physical fidelity. Through experiments in both simulation and on a Franka Research 3 platform, we show that GaussTwin consistently improves tracking accuracy and robustness compared to shape-matching and rigid-only baselines, while also enabling downstream tasks such as push-based planning. These results highlight GaussTwin as a step toward unified, physically meaningful digital twins that can support closed-loop robotic interaction and learning.

