---
layout: default
title: Towards Intelligible Human-Robot Interaction: An Active Inference Approach to Occluded Pedestrian Scenarios
---

# Towards Intelligible Human-Robot Interaction: An Active Inference Approach to Occluded Pedestrian Scenarios
**arXiv**：[2602.23109v1](https://arxiv.org/abs/2602.23109) · [PDF](https://arxiv.org/pdf/2602.23109.pdf)  
**作者**：Kai Chen, Yuyao Huang, Guang Chen  

**一句话要点**：提出基于主动推理的框架以解决自动驾驶中遮挡行人场景的安全挑战

**关键词**：主动推理, 行人状态估计, 模型预测控制, 遮挡场景, 自动驾驶安全

## 3 点简述
- 核心问题：遮挡行人的突然出现带来高不确定性，传统方法难以处理。
- 方法要点：采用主动推理和RBPF估计行人状态，引入条件信念重置和假设注入模拟人类认知。
- 实验或效果：仿真实验显示碰撞率显著降低，并展现出可解释、类人的驾驶行为。

## 摘要（原文）

> The sudden appearance of occluded pedestrians presents a critical safety challenge in autonomous driving. Conventional rule-based or purely data-driven approaches struggle with the inherent high uncertainty of these long-tail scenarios. To tackle this challenge, we propose a novel framework grounded in Active Inference, which endows the agent with a human-like, belief-driven mechanism. Our framework leverages a Rao-Blackwellized Particle Filter (RBPF) to efficiently estimate the pedestrian's hybrid state. To emulate human-like cognitive processes under uncertainty, we introduce a Conditional Belief Reset mechanism and a Hypothesis Injection technique to explicitly model beliefs about the pedestrian's multiple latent intentions. Planning is achieved via a Cross-Entropy Method (CEM) enhanced Model Predictive Path Integral (MPPI) controller, which synergizes the efficient, iterative search of CEM with the inherent robustness of MPPI. Simulation experiments demonstrate that our approach significantly reduces the collision rate compared to reactive, rule-based, and reinforcement learning (RL) baselines, while also exhibiting explainable and human-like driving behavior that reflects the agent's internal belief state.

