---
layout: default
title: Towards Metric-Aware Multi-Person Mesh Recovery by Jointly Optimizing Human Crowd in Camera Space
---

# Towards Metric-Aware Multi-Person Mesh Recovery by Jointly Optimizing Human Crowd in Camera Space
**arXiv**：[2511.13282v1](https://arxiv.org/abs/2511.13282) · [PDF](https://arxiv.org/pdf/2511.13282.pdf)  
**作者**：Kaiwen Wang, Kaili Zheng, Yiming Shi, Chenyi Guo, Ji Wu  

**一句话要点**：提出DTO和Metric-Aware HMR以解决多人网格恢复中的场景一致性和度量尺度问题

**关键词**：多人网格恢复, 场景一致性优化, 度量尺度估计, 深度条件优化, 伪真值数据集

## 3 点简述
- 核心问题：单中心伪真值生成导致多人场景深度和尺度不一致
- 方法要点：DTO联合优化相机空间平移，Metric-Aware HMR直接估计度量尺度网格
- 实验或效果：在相对深度推理和网格恢复上达到先进水平，构建DTO-Humans数据集

## 摘要（原文）

> Multi-person human mesh recovery from a single image is a challenging task, hindered by the scarcity of in-the-wild training data. Prevailing in-the-wild human mesh pseudo-ground-truth (pGT) generation pipelines are single-person-centric, where each human is processed individually without joint optimization. This oversight leads to a lack of scene-level consistency, producing individuals with conflicting depths and scales within the same image. To address this, we introduce Depth-conditioned Translation Optimization (DTO), a novel optimization-based method that jointly refines the camera-space translations of all individuals in a crowd. By leveraging anthropometric priors on human height and depth cues from a monocular depth estimator, DTO solves for a scene-consistent placement of all subjects within a principled Maximum a posteriori (MAP) framework. Applying DTO to the 4D-Humans dataset, we construct DTO-Humans, a new large-scale pGT dataset of 0.56M high-quality, scene-consistent multi-person images, featuring dense crowds with an average of 4.8 persons per image. Furthermore, we propose Metric-Aware HMR, an end-to-end network that directly estimates human mesh and camera parameters in metric scale. This is enabled by a camera branch and a novel relative metric loss that enforces plausible relative scales. Extensive experiments demonstrate that our method achieves state-of-the-art performance on relative depth reasoning and human mesh recovery. Code and data will be released publicly.

