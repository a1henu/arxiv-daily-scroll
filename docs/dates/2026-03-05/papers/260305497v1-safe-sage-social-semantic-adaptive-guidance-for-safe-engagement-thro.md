---
layout: default
title: Safe-SAGE: Social-Semantic Adaptive Guidance for Safe Engagement through Laplace-Modulated Poisson Safety Functions
---

# Safe-SAGE: Social-Semantic Adaptive Guidance for Safe Engagement through Laplace-Modulated Poisson Safety Functions
**arXiv**：[2603.05497v1](https://arxiv.org/abs/2603.05497) · [PDF](https://arxiv.org/pdf/2603.05497.pdf)  
**作者**：Lizhi Yang, Ryan M. Bena, Meg Wilkinson, Gilbert Bahati, Andy Navarro Brenes, Ryan K. Cosner, Aaron D. Ames  

**一句话要点**：提出Safe-SAGE框架，通过拉普拉斯调制泊松安全函数实现语义感知的安全导航

**关键词**：安全关键控制, 语义感知导航, 泊松安全函数, 拉普拉斯引导场, 腿部机器人, 多传感器融合

## 3 点简述
- 传统安全控制方法存在语义盲区，对所有障碍物一视同仁，缺乏上下文感知
- 融合多传感器点云与视觉实例分割，结合泊松安全函数和拉普拉斯引导场进行安全调制
- 在动态环境中实现腿部机器人安全导航，保持严格安全保证和上下文依赖的安全边界

## 摘要（原文）

> Traditional safety-critical control methods, such as control barrier functions, suffer from semantic blindness, exhibiting the same behavior around obstacles regardless of contextual significance. This limitation leads to the uniform treatment of all obstacles, despite their differing semantic meanings. We present Safe-SAGE (Social-Semantic Adaptive Guidance for Safe Engagement), a unified framework that bridges the gap between high-level semantic understanding and low-level safety-critical control through a Poisson safety function (PSF) modulated using a Laplace guidance field. Our approach perceives the environment by fusing multi-sensor point clouds with vision-based instance segmentation and persistent object tracking to maintain up-to-date semantics beyond the camera's field of view. A multi-layer safety filter is then used to modulate system inputs to achieve safe navigation using this semantic understanding of the environment. This safety filter consists of both a model predictive control layer and a control barrier function layer. Both layers utilize the PSF and flux modulation of the guidance field to introduce varying levels of conservatism and multi-agent passing norms for different obstacles in the environment. Our framework enables legged robots to navigate semantically rich, dynamic environments with context-dependent safety margins while maintaining rigorous safety guarantees.

