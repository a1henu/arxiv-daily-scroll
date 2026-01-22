---
layout: default
title: HumanDiffusion: A Vision-Based Diffusion Trajectory Planner with Human-Conditioned Goals for Search and Rescue UAV
---

# HumanDiffusion: A Vision-Based Diffusion Trajectory Planner with Human-Conditioned Goals for Search and Rescue UAV
**arXiv**：[2601.14973v1](https://arxiv.org/abs/2601.14973) · [PDF](https://arxiv.org/pdf/2601.14973.pdf)  
**作者**：Faryal Batool, Iana Zhura, Valerii Serpiva, Roohan Ahmed Khan, Ivan Valuev, Issatay Tokmurziyev, Dzmitry Tsetserukou  

**一句话要点**：提出HumanDiffusion，一种基于视觉的扩散轨迹规划器，用于搜救无人机在紧急场景中实现人机协作导航。

**关键词**：无人机导航, 扩散模型, 人类检测, 轨迹规划, 搜救应用, 图像条件生成

## 3 点简述
- 核心问题：紧急场景中无人机需自主检测人类、推断导航目标并安全操作，传统方法依赖地图或计算密集型规划。
- 方法要点：结合YOLO-11人类检测与图像条件扩散模型，直接从RGB图像生成像素空间轨迹，确保平滑运动和安全距离。
- 实验或效果：在模拟和真实室内灾难场景测试，像素轨迹重建均方误差0.02，真实任务成功率80%，支持部分遮挡。

## 摘要（原文）

> Reliable human--robot collaboration in emergency scenarios requires autonomous systems that can detect humans, infer navigation goals, and operate safely in dynamic environments. This paper presents HumanDiffusion, a lightweight image-conditioned diffusion planner that generates human-aware navigation trajectories directly from RGB imagery. The system combines YOLO-11--based human detection with diffusion-driven trajectory generation, enabling a quadrotor to approach a target person and deliver medical assistance without relying on prior maps or computationally intensive planning pipelines. Trajectories are predicted in pixel space, ensuring smooth motion and a consistent safety margin around humans. We evaluate HumanDiffusion in simulation and real-world indoor mock-disaster scenarios. On a 300-sample test set, the model achieves a mean squared error of 0.02 in pixel-space trajectory reconstruction. Real-world experiments demonstrate an overall mission success rate of 80% across accident-response and search-and-locate tasks with partial occlusions. These results indicate that human-conditioned diffusion planning offers a practical and robust solution for human-aware UAV navigation in time-critical assistance settings.

