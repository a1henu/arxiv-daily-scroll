---
layout: default
title: Learning Terrain Aware Bipedal Locomotion via Reduced Dimensional Perceptual Representations
---

# Learning Terrain Aware Bipedal Locomotion via Reduced Dimensional Perceptual Representations
**arXiv**：[2512.12993v1](https://arxiv.org/abs/2512.12993) · [PDF](https://arxiv.org/pdf/2512.12993.pdf)  
**作者**：Guillermo A. Castillo, Himanshu Lodha, Ayonga Hereid  

**一句话要点**：提出基于降维感知表示的分层策略，以增强地形感知双足机器人强化学习步态生成。

**关键词**：双足机器人步态生成, 地形感知强化学习, 降维感知表示, CNN-VAE, 分层控制策略, 硬件部署验证

## 3 点简述
- 核心问题：传统端到端方法在地形感知双足步态生成中效率低、鲁棒性差。
- 方法要点：使用CNN-VAE提取地形潜在编码，结合降阶动力学和历史感知，优化决策状态。
- 实验或效果：通过高保真模拟和硬件验证，确认方法在噪声和动态环境下的鲁棒性与适应性。

## 摘要（原文）

> This work introduces a hierarchical strategy for terrain-aware bipedal locomotion that integrates reduced-dimensional perceptual representations to enhance reinforcement learning (RL)-based high-level (HL) policies for real-time gait generation. Unlike end-to-end approaches, our framework leverages latent terrain encodings via a Convolutional Variational Autoencoder (CNN-VAE) alongside reduced-order robot dynamics, optimizing the locomotion decision process with a compact state. We systematically analyze the impact of latent space dimensionality on learning efficiency and policy robustness. Additionally, we extend our method to be history-aware, incorporating sequences of recent terrain observations into the latent representation to improve robustness. To address real-world feasibility, we introduce a distillation method to learn the latent representation directly from depth camera images and provide preliminary hardware validation by comparing simulated and real sensor data. We further validate our framework using the high-fidelity Agility Robotics (AR) simulator, incorporating realistic sensor noise, state estimation, and actuator dynamics. The results confirm the robustness and adaptability of our method, underscoring its potential for hardware deployment.

