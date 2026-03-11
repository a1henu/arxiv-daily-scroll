---
layout: default
title: GSStream: 3D Gaussian Splatting based Volumetric Scene Streaming System
---

# GSStream: 3D Gaussian Splatting based Volumetric Scene Streaming System
**arXiv**：[2603.09718v1](https://arxiv.org/abs/2603.09718) · [PDF](https://arxiv.org/pdf/2603.09718.pdf)  
**作者**：Zhiye Tang, Qiudan Zhang, Lei Zhang, Junhui Hou, You Yang, Xu Wang  

**一句话要点**：提出GSStream系统以解决3D高斯泼溅场景实时流式传输的带宽挑战

**关键词**：3D高斯泼溅, 场景流式传输, 视口预测, 深度强化学习, 码率自适应, 体积场景

## 3 点简述
- 核心问题：3D高斯泼溅技术产生大量数据，带宽需求高，实时分发困难
- 方法要点：集成协作视口预测和基于深度强化学习的码率自适应模块，优化场景传输
- 实验或效果：在视觉质量和网络使用上优于现有系统，并构建用户视口轨迹数据集

## 摘要（原文）

> Recently, the 3D Gaussian splatting (3DGS) technique for real-time radiance field rendering has revolutionized the field of volumetric scene representation, providing users with an immersive experience. But in return, it also poses a large amount of data volume, which is extremely bandwidth-intensive. Cutting-edge researchers have tried to introduce different approaches and construct multiple variants for 3DGS to obtain a more compact scene representation, but it is still challenging for real-time distribution. In this paper, we propose GSStream, a novel volumetric scene streaming system to support 3DGS data format. Specifically, GSStream integrates a collaborative viewport prediction module to better predict users' future behaviors by learning collaborative priors and historical priors from multiple users and users' viewport sequences and a deep reinforcement learning (DRL)-based bitrate adaptation module to tackle the state and action space variability challenge of the bitrate adaptation problem, achieving efficient volumetric scene delivery. Besides, we first build a user viewport trajectory dataset for volumetric scenes to support the training and streaming simulation. Extensive experiments prove that our proposed GSStream system outperforms existing representative volumetric scene streaming systems in visual quality and network usage. Demo video: https://youtu.be/3WEe8PN8yvA.

