---
layout: default
title: Breaking the accuracy-resource dilemma: a lightweight adaptive video inference enhancement
---

# Breaking the accuracy-resource dilemma: a lightweight adaptive video inference enhancement
**arXiv**：[2601.14568v1](https://arxiv.org/abs/2601.14568) · [PDF](https://arxiv.org/pdf/2601.14568.pdf)  
**作者**：Wei Ma, Shaowu Chen, Junjie Ye, Peichang Zhang, Lei Huang  

**一句话要点**：提出基于模糊控制器的自适应视频推理增强框架，以平衡资源利用与推理性能。

**关键词**：视频推理增强, 模糊控制器, 自适应模型切换, 资源效率, 时空相关性

## 3 点简述
- 核心问题：现有视频推理增强方法忽视资源效率与推理效果的权衡，导致资源利用低效和性能不佳。
- 方法要点：开发模糊控制器，利用相邻帧的时空相关性，根据设备实时资源动态切换不同规模模型。
- 实验或效果：实验结果表明，该方法有效实现了资源利用与推理性能之间的平衡。

## 摘要（原文）

> Existing video inference (VI) enhancement methods typically aim to improve performance by scaling up model sizes and employing sophisticated network architectures. While these approaches demonstrated state-of-the-art performance, they often overlooked the trade-off of resource efficiency and inference effectiveness, leading to inefficient resource utilization and suboptimal inference performance. To address this problem, a fuzzy controller (FC-r) is developed based on key system parameters and inference-related metrics. Guided by the FC-r, a VI enhancement framework is proposed, where the spatiotemporal correlation of targets across adjacent video frames is leveraged. Given the real-time resource conditions of the target device, the framework can dynamically switch between models of varying scales during VI. Experimental results demonstrate that the proposed method effectively achieves a balance between resource utilization and inference performance.

