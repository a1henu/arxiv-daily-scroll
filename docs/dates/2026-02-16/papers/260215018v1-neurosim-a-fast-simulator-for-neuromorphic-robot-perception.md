---
layout: default
title: Neurosim: A Fast Simulator for Neuromorphic Robot Perception
---

# Neurosim: A Fast Simulator for Neuromorphic Robot Perception
**arXiv**：[2602.15018v1](https://arxiv.org/abs/2602.15018) · [PDF](https://arxiv.org/pdf/2602.15018.pdf)  
**作者**：Richeek Das, Pratik Chaudhari  

**一句话要点**：提出Neurosim与Cortex库，用于快速模拟神经形态机器人感知传感器与动态环境，支持实时算法训练与测试。

**关键词**：神经形态感知, 传感器模拟, 实时仿真, 机器人控制, 自监督学习, 多模态数据

## 3 点简述
- 核心问题：需要高效模拟神经形态传感器（如动态视觉传感器）和多旋翼车辆动态，以支持机器人感知与控制算法的开发。
- 方法要点：Neurosim提供GPU加速的传感器模拟，Cortex基于ZeroMQ实现低延迟通信，集成Python/C++支持NumPy和PyTorch。
- 实验或效果：在桌面GPU上达到约2700 FPS的帧率，演示了自监督学习训练和闭环实时测试的应用。

## 摘要（原文）

> Neurosim is a fast, real-time, high-performance library for simulating sensors such as dynamic vision sensors, RGB cameras, depth sensors, and inertial sensors. It can also simulate agile dynamics of multi-rotor vehicles in complex and dynamic environments. Neurosim can achieve frame rates as high as ~2700 FPS on a desktop GPU. Neurosim integrates with a ZeroMQ-based communication library called Cortex to facilitate seamless integration with machine learning and robotics workflows. Cortex provides a high-throughput, low-latency message-passing system for Python and C++ applications, with native support for NumPy arrays and PyTorch tensors. This paper discusses the design philosophy behind Neurosim and Cortex. It demonstrates how they can be used to (i) train neuromorphic perception and control algorithms, e.g., using self-supervised learning on time-synchronized multi-modal data, and (ii) test real-time implementations of these algorithms in closed-loop. Neurosim and Cortex are available at https://github.com/grasp-lyrl/neurosim .

