---
layout: default
title: RealWonder: Real-Time Physical Action-Conditioned Video Generation
---

# RealWonder: Real-Time Physical Action-Conditioned Video Generation
**arXiv**：[2603.05449v1](https://arxiv.org/abs/2603.05449) · [PDF](https://arxiv.org/pdf/2603.05449.pdf)  
**作者**：Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  

**一句话要点**：提出RealWonder系统，通过物理模拟桥接动作与视频生成，实现实时交互式视频生成。

**关键词**：实时视频生成, 物理模拟, 动作条件生成, 3D重建, 蒸馏扩散模型

## 3 点简述
- 当前视频生成模型缺乏3D动作物理后果模拟能力，因缺少结构理解。
- 核心方法是将连续动作通过物理模拟转换为光流和RGB表示，供视频模型处理。
- 系统集成3D重建、物理模拟和蒸馏视频生成器，在480x832分辨率下达到13.2 FPS。

## 摘要（原文）

> Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (optical flow and RGB) that video models can process. RealWonder integrates three components: 3D reconstruction from single images, physics simulation, and a distilled video generator requiring only 4 diffusion steps. Our system achieves 13.2 FPS at 480x832 resolution, enabling interactive exploration of forces, robot actions, and camera controls on rigid objects, deformable bodies, fluids, and granular materials. We envision RealWonder opens new opportunities to apply video models in immersive experiences, AR/VR, and robot learning. Our code and model weights are publicly available in our project website: https://liuwei283.github.io/RealWonder/

