---
layout: default
title: Hybrid guided variational autoencoder for visual place recognition
---

# Hybrid guided variational autoencoder for visual place recognition
**arXiv**：[2601.09248v1](https://arxiv.org/abs/2601.09248) · [PDF](https://arxiv.org/pdf/2601.09248.pdf)  
**作者**：Ni Wang, Zihan You, Emre Neftci, Thorben Schoepe  

**一句话要点**：提出混合引导变分自编码器，用于解决视觉地点识别在移动部署中的内存与泛化问题。

**关键词**：视觉地点识别, 变分自编码器, 事件视觉传感器, 脉冲神经网络, 移动机器人导航, 室内环境定位

## 3 点简述
- 核心问题：现有视觉地点识别模型内存需求高或泛化能力不足，限制移动机器人部署。
- 方法要点：结合事件视觉传感器与引导变分自编码器，编码器基于脉冲神经网络，兼容低功耗硬件。
- 实验或效果：在新室内数据集上实现16个地点的特征解耦，分类性能媲美先进方法，并在未知场景中展示高泛化能力。

## 摘要（原文）

> Autonomous agents such as cars, robots and drones need to precisely localize themselves in diverse environments, including in GPS-denied indoor environments. One approach for precise localization is visual place recognition (VPR), which estimates the place of an image based on previously seen places. State-of-the-art VPR models require high amounts of memory, making them unwieldy for mobile deployment, while more compact models lack robustness and generalization capabilities. This work overcomes these limitations for robotics using a combination of event-based vision sensors and an event-based novel guided variational autoencoder (VAE). The encoder part of our model is based on a spiking neural network model which is compatible with power-efficient low latency neuromorphic hardware. The VAE successfully disentangles the visual features of 16 distinct places in our new indoor VPR dataset with a classification performance comparable to other state-of-the-art approaches while, showing robust performance also under various illumination conditions. When tested with novel visual inputs from unknown scenes, our model can distinguish between these places, which demonstrates a high generalization capability by learning the essential features of location. Our compact and robust guided VAE with generalization capabilities poses a promising model for visual place recognition that can significantly enhance mobile robot navigation in known and unknown indoor environments.

