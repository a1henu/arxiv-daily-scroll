---
layout: default
title: Neural NMPC through Signed Distance Field Encoding for Collision Avoidance
---

# Neural NMPC through Signed Distance Field Encoding for Collision Avoidance
**arXiv**：[2511.21312v1](https://arxiv.org/abs/2511.21312) · [PDF](https://arxiv.org/pdf/2511.21312.pdf)  
**作者**：Martin Jacquet, Marvin Harms, Kostas Alexis  

**一句话要点**：提出神经非线性模型预测控制框架，用于未知环境中空中机器人的无地图避障。

**关键词**：神经非线性模型预测控制, 符号距离函数编码, 避障导航, 空中机器人, 距离图像处理

## 3 点简述
- 核心问题：未知环境中空中机器人基于机载距离感知的无地图避障导航。
- 方法要点：使用卷积编码器和多层感知器从距离图像编码符号距离函数，嵌入NMPC约束。
- 实验或效果：在模拟和真实森林环境中验证避障性能，包括对抗性输入和漂移估计。

## 摘要（原文）

> This paper introduces a neural Nonlinear Model Predictive Control (NMPC) framework for mapless, collision-free navigation in unknown environments with Aerial Robots, using onboard range sensing. We leverage deep neural networks to encode a single range image, capturing all the available information about the environment, into a Signed Distance Function (SDF). The proposed neural architecture consists of two cascaded networks: a convolutional encoder that compresses the input image into a low-dimensional latent vector, and a Multi-Layer Perceptron that approximates the corresponding spatial SDF. This latter network parametrizes an explicit position constraint used for collision avoidance, which is embedded in a velocity-tracking NMPC that outputs thrust and attitude commands to the robot. First, a theoretical analysis of the contributed NMPC is conducted, verifying recursive feasibility and stability properties under fixed observations. Subsequently, we evaluate the open-loop performance of the learning-based components as well as the closed-loop performance of the controller in simulations and experiments. The simulation study includes an ablation study, comparisons with two state-of-the-art local navigation methods, and an assessment of the resilience to drifting odometry. The real-world experiments are conducted in forest environments, demonstrating that the neural NMPC effectively performs collision avoidance in cluttered settings against an adversarial reference velocity input and drifting position estimates.

