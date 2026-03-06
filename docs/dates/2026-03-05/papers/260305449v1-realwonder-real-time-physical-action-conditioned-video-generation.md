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
- 核心问题：现有视频生成模型缺乏对3D动作物理后果（如力、机器人操作）的结构化理解，无法模拟其影响。
- 方法要点：使用物理模拟作为中间桥梁，将连续动作转换为光流和RGB表示，结合3D重建、物理模拟和蒸馏视频生成器。
- 实验或效果：系统在480x832分辨率下达到13.2 FPS，支持对刚性物体、可变形体、流体和颗粒材料的交互探索。

## 摘要（原文）

> Current video generation models cannot simulate physical consequences of 3D actions like forces and robotic manipulations, as they lack structural understanding of how actions affect 3D scenes. We present RealWonder, the first real-time system for action-conditioned video generation from a single image. Our key insight is using physics simulation as an intermediate bridge: instead of directly encoding continuous actions, we translate them through physics simulation into visual representations (optical flow and RGB) that video models can process. RealWonder integrates three components: 3D reconstruction from single images, physics simulation, and a distilled video generator requiring only 4 diffusion steps. Our system achieves 13.2 FPS at 480x832 resolution, enabling interactive exploration of forces, robot actions, and camera controls on rigid objects, deformable bodies, fluids, and granular materials. We envision RealWonder opens new opportunities to apply video models in immersive experiences, AR/VR, and robot learning. Our code and model weights are publicly available in our project website: https://liuwei283.github.io/RealWonder/

