---
layout: default
title: Vehicle Dynamics Embedded World Models for Autonomous Driving
---

# Vehicle Dynamics Embedded World Models for Autonomous Driving
**arXiv**：[2512.02417v1](https://arxiv.org/abs/2512.02417) · [PDF](https://arxiv.org/pdf/2512.02417.pdf)  
**作者**：Huiqian Li, Wei Pan, Haodong Zhang, Jin Huang, Zhihua Zhong  

**一句话要点**：提出VDD方法，通过解耦自车动力学与环境动力学建模，提升自动驾驶世界模型的泛化性与鲁棒性。

**关键词**：自动驾驶世界模型, 车辆动力学建模, 解耦学习, 策略鲁棒性, 模拟环境实验

## 3 点简述
- 核心问题：现有方法从图像输入联合学习自车动力学与环境动力学，导致效率低且对车辆参数变化鲁棒性差。
- 方法要点：VDD方法分离自车动力学与环境动力学建模，并引入PAD和PAT策略增强策略鲁棒性。
- 实验或效果：在模拟环境中验证，VDD显著提升驾驶性能和对车辆动力学变化的鲁棒性，优于现有方法。

## 摘要（原文）

> World models have gained significant attention as a promising approach for autonomous driving. By emulating human-like perception and decision-making processes, these models can predict and adapt to dynamic environments. Existing methods typically map high-dimensional observations into compact latent spaces and learn optimal policies within these latent representations. However, prior work usually jointly learns ego-vehicle dynamics and environmental transition dynamics from the image input, leading to inefficiencies and a lack of robustness to variations in vehicle dynamics. To address these issues, we propose the Vehicle Dynamics embedded Dreamer (VDD) method, which decouples the modeling of ego-vehicle dynamics from environmental transition dynamics. This separation allows the world model to generalize effectively across vehicles with diverse parameters. Additionally, we introduce two strategies to further enhance the robustness of the learned policy: Policy Adjustment during Deployment (PAD) and Policy Augmentation during Training (PAT). Comprehensive experiments in simulated environments demonstrate that the proposed model significantly improves both driving performance and robustness to variations in vehicle dynamics, outperforming existing approaches.

