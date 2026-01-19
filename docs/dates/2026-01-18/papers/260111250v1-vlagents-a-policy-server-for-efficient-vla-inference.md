---
layout: default
title: VLAgents: A Policy Server for Efficient VLA Inference
---

# VLAgents: A Policy Server for Efficient VLA Inference
**arXiv**：[2601.11250v1](https://arxiv.org/abs/2601.11250) · [PDF](https://arxiv.org/pdf/2601.11250.pdf)  
**作者**：Tobias Jülg, Khaled Gamal, Nisarga Nilavadi, Pierre Krack, Seongjin Bien, Michael Krawez, Florian Walter, Wolfram Burgard  

**一句话要点**：提出VLAgents策略服务器以解决机器人中视觉-语言-动作模型部署的接口碎片化和通信延迟问题

**关键词**：视觉-语言-动作模型, 策略服务器, 机器人部署, 通信优化, 模块化架构, 基准测试

## 3 点简述
- 核心问题：VLA模型在机器人部署中面临接口碎片化和分布式通信延迟的挑战
- 方法要点：设计模块化策略服务器，通过统一Gymnasium协议抽象VLA推理，支持零拷贝共享内存和压缩流传输
- 实验或效果：集成七种策略，在本地和远程通信基准测试中优于OpenVLA等默认服务器

## 摘要（原文）

> The rapid emergence of Vision-Language-Action models (VLAs) has a significant impact on robotics. However, their deployment remains complex due to the fragmented interfaces and the inherent communication latency in distributed setups. To address this, we introduce VLAgents, a modular policy server that abstracts VLA inferencing behind a unified Gymnasium-style protocol. Crucially, its communication layer transparently adapts to the context by supporting both zero-copy shared memory for high-speed simulation and compressed streaming for remote hardware. In this work, we present the architecture of VLAgents and validate it by integrating seven policies -- including OpenVLA and Pi Zero. In a benchmark with both local and remote communication, we further demonstrate how it outperforms the default policy servers provided by OpenVLA, OpenPi, and LeRobot. VLAgents is available at https://github.com/RobotControlStack/vlagents

