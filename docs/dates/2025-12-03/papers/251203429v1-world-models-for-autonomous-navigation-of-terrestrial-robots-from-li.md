---
layout: default
title: World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations
---

# World Models for Autonomous Navigation of Terrestrial Robots from LIDAR Observations
**arXiv**：[2512.03429v1](https://arxiv.org/abs/2512.03429) · [PDF](https://arxiv.org/pdf/2512.03429.pdf)  
**作者**：Raul Steinmetz, Fabio Demo Rosa, Victor Augusto Kich, Jair Augusto Bottega, Ricardo Bedin Grando, Daniel Fernando Tello Gamarra  

**一句话要点**：提出基于DreamerV3和MLP-VAE的世界模型框架，以解决地面机器人从高维LIDAR观测中自主导航的挑战。

**关键词**：自主导航, 强化学习, 世界模型, LIDAR编码, 潜在表示, 机器人仿真

## 3 点简述
- 核心问题：模型无关强化学习处理全分辨率LIDAR数据时样本效率低，导致导航鲁棒性不足。
- 方法要点：集成MLP-VAE编码LIDAR观测为紧凑潜在表示，结合动态预测器实现基于想象的策略优化。
- 实验或效果：在模拟TurtleBot3任务中，相比SAC等基线，实现更快收敛和100%成功率。

## 摘要（原文）

> Autonomous navigation of terrestrial robots using Reinforcement Learning (RL) from LIDAR observations remains challenging due to the high dimensionality of sensor data and the sample inefficiency of model-free approaches. Conventional policy networks struggle to process full-resolution LIDAR inputs, forcing prior works to rely on simplified observations that reduce spatial awareness and navigation robustness. This paper presents a novel model-based RL framework built on top of the DreamerV3 algorithm, integrating a Multi-Layer Perceptron Variational Autoencoder (MLP-VAE) within a world model to encode high-dimensional LIDAR readings into compact latent representations. These latent features, combined with a learned dynamics predictor, enable efficient imagination-based policy optimization. Experiments on simulated TurtleBot3 navigation tasks demonstrate that the proposed architecture achieves faster convergence and higher success rate compared to model-free baselines such as SAC, DDPG, and TD3. It is worth emphasizing that the DreamerV3-based agent attains a 100% success rate across all evaluated environments when using the full dataset of the Turtlebot3 LIDAR (360 readings), while model-free methods plateaued below 85%. These findings demonstrate that integrating predictive world models with learned latent representations enables more efficient and robust navigation from high-dimensional sensory data.

