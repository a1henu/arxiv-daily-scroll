---
layout: default
title: WildCross: A Cross-Modal Large Scale Benchmark for Place Recognition and Metric Depth Estimation in Natural Environments
---

# WildCross: A Cross-Modal Large Scale Benchmark for Place Recognition and Metric Depth Estimation in Natural Environments
**arXiv**：[2603.01475v1](https://arxiv.org/abs/2603.01475) · [PDF](https://arxiv.org/pdf/2603.01475.pdf)  
**作者**：Joshua Knights, Joseph Reid, Kaushik Roy, David Hall, Mark Cox, Peyman Moghadam  

**一句话要点**：提出WildCross跨模态基准，以解决自然环境中位置识别和度量深度估计的挑战。

**关键词**：跨模态基准, 位置识别, 度量深度估计, 自然场景, 机器人感知, 数据集构建

## 3 点简述
- 核心问题：现有数据集主要针对结构化城市环境，难以应对复杂自然场景的机器人感知需求。
- 方法要点：构建包含大量RGB帧、半稠密深度和表面法线标注，并与6DoF位姿和激光雷达子图对齐的跨模态数据集。
- 实验或效果：在视觉、激光雷达和跨模态位置识别及度量深度估计任务上进行全面实验，验证其作为挑战性基准的价值。

## 摘要（原文）

> Recent years have seen a significant increase in demand for robotic solutions in unstructured natural environments, alongside growing interest in bridging 2D and 3D scene understanding. However, existing robotics datasets are predominantly captured in structured urban environments, making them inadequate for addressing the challenges posed by complex, unstructured natural settings. To address this gap, we propose WildCross, a cross-modal benchmark for place recognition and metric depth estimation in large-scale natural environments. WildCross comprises over 476K sequential RGB frames with semi-dense depth and surface normal annotations, each aligned with accurate 6DoF poses and synchronized dense lidar submaps. We conduct comprehensive experiments on visual, lidar, and cross-modal place recognition, as well as metric depth estimation, demonstrating the value of WildCross as a challenging benchmark for multi-modal robotic perception tasks. We provide access to the code repository and dataset at https://csiro-robotics.github.io/WildCross.

