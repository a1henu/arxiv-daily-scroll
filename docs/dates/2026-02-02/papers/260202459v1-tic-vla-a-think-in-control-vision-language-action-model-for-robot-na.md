---
layout: default
title: TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments
---

# TIC-VLA: A Think-in-Control Vision-Language-Action Model for Robot Navigation in Dynamic Environments
**arXiv**：[2602.02459v1](https://arxiv.org/abs/2602.02459) · [PDF](https://arxiv.org/pdf/2602.02459.pdf)  
**作者**：Zhiyu Huang, Yun Zhang, Johnson Liu, Rui Song, Chen Tang, Jiaqi Ma  

**一句话要点**：提出TIC-VLA框架以解决动态环境中机器人导航的语义推理延迟问题

**关键词**：机器人导航, 视觉-语言-动作模型, 延迟补偿, 动态环境, 异步推理, 仿真评估

## 3 点简述
- 核心问题：现有VLA模型假设语义推理与实时控制对齐，但推理延迟导致异步问题
- 方法要点：引入延迟感知框架，通过延迟语义-控制接口和延迟一致训练补偿异步推理
- 实验或效果：在仿真和真实机器人上优于现有VLA模型，支持多秒延迟下的鲁棒控制

## 摘要（原文）

> Robots in dynamic, human-centric environments must follow language instructions while maintaining real-time reactive control. Vision-language-action (VLA) models offer a promising framework, but they assume temporally aligned reasoning and control, despite semantic inference being inherently delayed relative to real-time action. We introduce Think-in-Control (TIC)-VLA, a latency-aware framework that explicitly models delayed semantic reasoning during action generation. TIC-VLA defines a delayed semantic-control interface that conditions action generation on delayed vision-language semantic states and explicit latency metadata, in addition to current observations, enabling policies to compensate for asynchronous reasoning. We further propose a latency-consistent training pipeline that injects reasoning inference delays during imitation learning and online reinforcement learning, aligning training with asynchronous deployment. To support realistic evaluation, we present DynaNav, a physics-accurate, photo-realistic simulation suite for language-guided navigation in dynamic environments. Extensive experiments in simulation and on a real robot show that TIC-VLA consistently outperforms prior VLA models while maintaining robust real-time control under multi-second reasoning latency. Project website: https://ucla-mobility.github.io/TIC-VLA/

