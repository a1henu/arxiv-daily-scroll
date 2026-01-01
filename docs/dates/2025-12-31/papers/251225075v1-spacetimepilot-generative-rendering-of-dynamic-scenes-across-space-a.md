---
layout: default
title: SpaceTimePilot: Generative Rendering of Dynamic Scenes Across Space and Time
---

# SpaceTimePilot: Generative Rendering of Dynamic Scenes Across Space and Time
**arXiv**：[2512.25075v1](https://arxiv.org/abs/2512.25075) · [PDF](https://arxiv.org/pdf/2512.25075.pdf)  
**作者**：Zhening Huang, Hyeonho Jeong, Xuelin Chen, Yulia Gryaditskaya, Tuanfeng Y. Wang, Joan Lasenby, Chun-Hao Huang  

**一句话要点**：提出SpaceTimePilot视频扩散模型，实现动态场景在空间和时间上的可控生成渲染

**关键词**：视频扩散模型, 时空解耦, 可控生成渲染, 相机视角控制, 运动序列编辑, 时域扭曲训练

## 3 点简述
- 核心问题：如何从单目视频中独立控制相机视角和运动序列进行生成渲染
- 方法要点：引入动画时间嵌入机制和时域扭曲训练方案，实现时空解耦
- 实验效果：在真实和合成数据上验证了清晰的时空解耦能力，优于先前工作

## 摘要（原文）

> We present SpaceTimePilot, a video diffusion model that disentangles space and time for controllable generative rendering. Given a monocular video, SpaceTimePilot can independently alter the camera viewpoint and the motion sequence within the generative process, re-rendering the scene for continuous and arbitrary exploration across space and time. To achieve this, we introduce an effective animation time-embedding mechanism in the diffusion process, allowing explicit control of the output video's motion sequence with respect to that of the source video. As no datasets provide paired videos of the same dynamic scene with continuous temporal variations, we propose a simple yet effective temporal-warping training scheme that repurposes existing multi-view datasets to mimic temporal differences. This strategy effectively supervises the model to learn temporal control and achieve robust space-time disentanglement. To further enhance the precision of dual control, we introduce two additional components: an improved camera-conditioning mechanism that allows altering the camera from the first frame, and CamxTime, the first synthetic space-and-time full-coverage rendering dataset that provides fully free space-time video trajectories within a scene. Joint training on the temporal-warping scheme and the CamxTime dataset yields more precise temporal control. We evaluate SpaceTimePilot on both real-world and synthetic data, demonstrating clear space-time disentanglement and strong results compared to prior work. Project page: https://zheninghuang.github.io/Space-Time-Pilot/ Code: https://github.com/ZheningHuang/spacetimepilot

