---
layout: default
title: AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation
---

# AdaWorldPolicy: World-Model-Driven Diffusion Policy with Online Adaptive Learning for Robotic Manipulation
**arXiv**：[2602.20057v1](https://arxiv.org/abs/2602.20057) · [PDF](https://arxiv.org/pdf/2602.20057.pdf)  
**作者**：Ge Yuan, Qiyuan Qiao, Jing Zhang, Dong Xu  

**一句话要点**：提出AdaWorldPolicy框架，通过世界模型驱动扩散策略与在线自适应学习增强动态环境下的机器人操作

**关键词**：机器人操作, 世界模型, 扩散策略, 在线自适应学习, Flow Matching, Transformer

## 3 点简述
- 核心问题：机器人操作需预测物理结果并适应动态环境，传统方法可能依赖大量人工干预或难以处理分布外场景
- 方法要点：集成世界模型、动作专家和力预测器，基于Flow Matching扩散Transformer实现模块化联合学习，并引入在线自适应学习策略动态切换模式
- 实验或效果：在模拟和真实机器人基准测试中达到先进性能，展示对视觉和物理域偏移的动态适应能力

## 摘要（原文）

> Effective robotic manipulation requires policies that can anticipate physical outcomes and adapt to real-world environments. Effective robotic manipulation requires policies that can anticipate physical outcomes and adapt to real-world environments. In this work, we introduce a unified framework, World-Model-Driven Diffusion Policy with Online Adaptive Learning (AdaWorldPolicy) to enhance robotic manipulation under dynamic conditions with minimal human involvement. Our core insight is that world models provide strong supervision signals, enabling online adaptive learning in dynamic environments, which can be complemented by force-torque feedback to mitigate dynamic force shifts. Our AdaWorldPolicy integrates a world model, an action expert, and a force predictor-all implemented as interconnected Flow Matching Diffusion Transformers (DiT). They are interconnected via the multi-modal self-attention layers, enabling deep feature exchange for joint learning while preserving their distinct modularity characteristics. We further propose a novel Online Adaptive Learning (AdaOL) strategy that dynamically switches between an Action Generation mode and a Future Imagination mode to drive reactive updates across all three modules. This creates a powerful closed-loop mechanism that adapts to both visual and physical domain shifts with minimal overhead. Across a suite of simulated and real-robot benchmarks, our AdaWorldPolicy achieves state-of-the-art performance, with dynamical adaptive capacity to out-of-distribution scenarios.

