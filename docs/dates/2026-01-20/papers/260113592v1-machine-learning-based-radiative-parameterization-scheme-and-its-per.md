---
layout: default
title: Machine learning based radiative parameterization scheme and its performance in operational reforecast experiments
---

# Machine learning based radiative parameterization scheme and its performance in operational reforecast experiments
**arXiv**：[2601.13592v1](https://arxiv.org/abs/2601.13592) · [PDF](https://arxiv.org/pdf/2601.13592.pdf)  
**作者**：Hao Jing, Sa Xiao, Haoyu Li, Huadong Xiao, Wei Xue  

**一句话要点**：提出基于残差卷积神经网络的辐射参数化方案，以提升数值天气预报的计算效率与稳定性

**关键词**：辐射参数化, 机器学习仿真, 残差卷积神经网络, 混合预报框架, 计算加速, 业务天气预报

## 3 点简述
- 研究聚焦于混合预报框架中深度神经网络与数值模型的耦合兼容性和长期积分稳定性问题
- 采用离线训练与在线耦合方法，通过经验回放和物理约束增强数据集，利用LibTorch实现实时计算
- 两月业务回算实验显示，方案精度与传统物理方案相当，计算速度提升约八倍

## 摘要（原文）

> Radiation is typically the most time-consuming physical process in numerical models. One solution is to use machine learning methods to simulate the radiation process to improve computational efficiency. From an operational standpoint, this study investigates critical limitations inherent to hybrid forecasting frameworks that embed deep neural networks into numerical prediction models, with a specific focus on two fundamental bottlenecks: coupling compatibility and long-term integration stability. A residual convolutional neural network is employed to approximate the Rapid Radiative Transfer Model for General Circulation Models (RRTMG) within the global operational system of China Meteorological Administration. We adopted an offline training and online coupling approach. First, a comprehensive dataset is generated through model simulations, encompassing all atmospheric columns both with and without cloud cover. To ensure the stability of the hybrid model, the dataset is enhanced via experience replay, and additional output constraints based on physical significance are imposed. Meanwhile, a LibTorch-based coupling method is utilized, which is more suitable for real-time operational computations. The hybrid model is capable of performing ten-day integrated forecasts as required. A two-month operational reforecast experiment demonstrates that the machine learning emulator achieves accuracy comparable to that of the traditional physical scheme, while accelerating the computation speed by approximately eightfold.

