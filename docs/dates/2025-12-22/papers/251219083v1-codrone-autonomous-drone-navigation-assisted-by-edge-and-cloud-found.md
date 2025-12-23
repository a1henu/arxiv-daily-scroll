---
layout: default
title: CoDrone: Autonomous Drone Navigation Assisted by Edge and Cloud Foundation Models
---

# CoDrone: Autonomous Drone Navigation Assisted by Edge and Cloud Foundation Models
**arXiv**：[2512.19083v1](https://arxiv.org/abs/2512.19083) · [PDF](https://arxiv.org/pdf/2512.19083.pdf)  
**作者**：Pengyu Chen, Tao Ouyang, Ke Luo, Weijie Hong, Xu Chen  

**一句话要点**：提出CoDrone云边端协同框架，集成基础模型以增强资源受限无人机自主导航性能。

**关键词**：无人机自主导航, 云边端协同计算, 基础模型集成, 深度估计, 强化学习调度, 视觉语言交互

## 3 点简述
- 核心问题：无人机机载计算资源有限，导致导航模型能力不足，而卸载任务到边缘服务器则引入高延迟。
- 方法要点：采用灰度图像减少计算开销，利用边缘辅助基础模型进行深度估计，并引入基于一维占用网格的导航方法。
- 实验或效果：在多种飞行速度和网络条件下优于基线方法，平均飞行距离提升40%，导航质量提高5%。

## 摘要（原文）

> Autonomous navigation for Unmanned Aerial Vehicles faces key challenges from limited onboard computational resources, which restrict deployed deep neural networks to shallow architectures incapable of handling complex environments. Offloading tasks to remote edge servers introduces high latency, creating an inherent trade-off in system design. To address these limitations, we propose CoDrone - the first cloud-edge-end collaborative computing framework integrating foundation models into autonomous UAV cruising scenarios - effectively leveraging foundation models to enhance performance of resource-constrained unmanned aerial vehicle platforms. To reduce onboard computation and data transmission overhead, CoDrone employs grayscale imagery for the navigation model. When enhanced environmental perception is required, CoDrone leverages the edge-assisted foundation model Depth Anything V2 for depth estimation and introduces a novel one-dimensional occupancy grid-based navigation method - enabling fine-grained scene understanding while advancing efficiency and representational simplicity of autonomous navigation. A key component of CoDrone is a Deep Reinforcement Learning-based neural scheduler that seamlessly integrates depth estimation with autonomous navigation decisions, enabling real-time adaptation to dynamic environments. Furthermore, the framework introduces a UAV-specific vision language interaction module incorporating domain-tailored low-level flight primitives to enable effective interaction between the cloud foundation model and the UAV. The introduction of VLM enhances open-set reasoning capabilities in complex unseen scenarios. Experimental results show CoDrone outperforms baseline methods under varying flight speeds and network conditions, achieving a 40% increase in average flight distance and a 5% improvement in average Quality of Navigation.

