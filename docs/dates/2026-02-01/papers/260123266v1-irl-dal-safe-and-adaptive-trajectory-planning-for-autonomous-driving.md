---
layout: default
title: IRL-DAL: Safe and Adaptive Trajectory Planning for Autonomous Driving via Energy-Guided Diffusion Models
---

# IRL-DAL: Safe and Adaptive Trajectory Planning for Autonomous Driving via Energy-Guided Diffusion Models
**arXiv**：[2601.23266v1](https://arxiv.org/abs/2601.23266) · [PDF](https://arxiv.org/pdf/2601.23266.pdf)  
**作者**：Seyed Ahmad Hosseini Miangoleh, Amin Jalal Aghdasian, Farzaneh Abdollahi  

**一句话要点**：提出基于能量引导扩散模型的逆强化学习框架，用于自动驾驶的安全自适应轨迹规划。

**关键词**：自动驾驶轨迹规划, 逆强化学习, 扩散模型, 安全监督, 自适应感知, 模仿学习

## 3 点简述
- 核心问题：自动驾驶中安全轨迹规划与专家目标对齐的挑战。
- 方法要点：结合模仿学习、逆强化学习和扩散模型，通过自适应掩码提升感知。
- 实验或效果：在Webots模拟器中达到96%成功率，碰撞率降至每千步0.05次。

## 摘要（原文）

> This paper proposes a novel inverse reinforcement learning framework using a diffusion-based adaptive lookahead planner (IRL-DAL) for autonomous vehicles. Training begins with imitation from an expert finite state machine (FSM) controller to provide a stable initialization. Environment terms are combined with an IRL discriminator signal to align with expert goals. Reinforcement learning (RL) is then performed with a hybrid reward that combines diffuse environmental feedback and targeted IRL rewards. A conditional diffusion model, which acts as a safety supervisor, plans safe paths. It stays in its lane, avoids obstacles, and moves smoothly. Then, a learnable adaptive mask (LAM) improves perception. It shifts visual attention based on vehicle speed and nearby hazards. After FSM-based imitation, the policy is fine-tuned with Proximal Policy Optimization (PPO). Training is run in the Webots simulator with a two-stage curriculum. A 96\% success rate is reached, and collisions are reduced to 0.05 per 1k steps, marking a new benchmark for safe navigation. By applying the proposed approach, the agent not only drives in lane but also handles unsafe conditions at an expert level, increasing robustness.We make our code publicly available.

