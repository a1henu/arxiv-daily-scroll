---
layout: default
title: Real-World Adverse Weather Image Restoration via Dual-Level Reinforcement Learning with High-Quality Cold Start
---

# Real-World Adverse Weather Image Restoration via Dual-Level Reinforcement Learning with High-Quality Cold Start
**arXiv**：[2511.05095v1](https://arxiv.org/abs/2511.05095) · [PDF](https://arxiv.org/pdf/2511.05095.pdf)  
**作者**：Fuyang Liu, Jiaqi Xu, Xiaowei Hu  

**一句话要点**：提出双层次强化学习框架以解决恶劣天气图像恢复问题

**关键词**：恶劣天气图像恢复, 双层次强化学习, 高保真数据集, 冷启动训练, 无配对监督学习, 动态模型选择

## 3 点简述
- 核心问题：恶劣天气导致视觉感知受损，现有模型泛化能力不足
- 方法要点：构建高保真数据集，并设计双层次强化学习框架进行冷启动训练
- 实验或效果：在多种恶劣天气场景中实现先进性能，代码已开源

## 摘要（原文）

> Adverse weather severely impairs real-world visual perception, while existing
> vision models trained on synthetic data with fixed parameters struggle to
> generalize to complex degradations. To address this, we first construct
> HFLS-Weather, a physics-driven, high-fidelity dataset that simulates diverse
> weather phenomena, and then design a dual-level reinforcement learning
> framework initialized with HFLS-Weather for cold-start training. Within this
> framework, at the local level, weather-specific restoration models are refined
> through perturbation-driven image quality optimization, enabling reward-based
> learning without paired supervision; at the global level, a meta-controller
> dynamically orchestrates model selection and execution order according to scene
> degradation. This framework enables continuous adaptation to real-world
> conditions and achieves state-of-the-art performance across a wide range of
> adverse weather scenarios. Code is available at
> https://github.com/xxclfy/AgentRL-Real-Weather

