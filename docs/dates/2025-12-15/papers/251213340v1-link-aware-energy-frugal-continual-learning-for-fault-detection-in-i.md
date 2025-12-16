---
layout: default
title: Link-Aware Energy-Frugal Continual Learning for Fault Detection in IoT Networks
---

# Link-Aware Energy-Frugal Continual Learning for Fault Detection in IoT Networks
**arXiv**：[2512.13340v1](https://arxiv.org/abs/2512.13340) · [PDF](https://arxiv.org/pdf/2512.13340.pdf)  
**作者**：Henrik C. M. Frederiksen, Junya Shiraishi, Cedomir Stefanovic, Hei Victor Cheng, Shashi Raj Pandey  

**一句话要点**：提出事件驱动通信框架，集成持续学习以在物联网网络中实现节能故障检测。

**关键词**：物联网网络, 故障检测, 持续学习, 节能通信, 轻量级机器学习, 边缘计算

## 3 点简述
- 核心问题：物联网设备资源受限，环境非平稳导致模型推理精度下降，更新模型能耗高。
- 方法要点：基于无线链路条件和能量预算，设备与边缘服务器协作更新轻量级机器学习模型。
- 实验或效果：在真实数据集上，相比周期性采样和非自适应持续学习，推理召回率提升高达42.8%。

## 摘要（原文）

> The use of lightweight machine learning (ML) models in internet of things (IoT) networks enables resource constrained IoT devices to perform on-device inference for several critical applications. However, the inference accuracy deteriorates due to the non-stationarity in the IoT environment and limited initial training data. To counteract this, the deployed models can be updated occasionally with new observed data samples. However, this approach consumes additional energy, which is undesirable for energy constrained IoT devices. This letter introduces an event-driven communication framework that strategically integrates continual learning (CL) in IoT networks for energy-efficient fault detection. Our framework enables the IoT device and the edge server (ES) to collaboratively update the lightweight ML model by adapting to the wireless link conditions for communication and the available energy budget. Evaluation on real-world datasets show that the proposed approach can outperform both periodic sampling and non-adaptive CL in terms of inference recall; our proposed approach achieves up to a 42.8% improvement, even under tight energy and bandwidth constraint.

