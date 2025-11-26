---
layout: default
title: Collaborate sim and real: Robot Bin Packing Learning in Real-world and Physical Engine
---

# Collaborate sim and real: Robot Bin Packing Learning in Real-world and Physical Engine
**arXiv**：[2511.19932v1](https://arxiv.org/abs/2511.19932) · [PDF](https://arxiv.org/pdf/2511.19932.pdf)  
**作者**：Lidi Zhang, Han Wu, Liyu Zhang, Ruofeng Liu, Haotian Wang, Chao Li, Desheng Zhang, Yunhuai Liu, Tian He  

**一句话要点**：提出混合强化学习框架以解决机器人三维装箱中的仿真与现实差距问题

**关键词**：三维装箱问题, 强化学习, 仿真到现实迁移, 领域随机化, 机器人部署

## 3 点简述
- 核心问题：现实装箱涉及连续重力交互，现有方法简化导致不稳定部署。
- 方法要点：结合物理仿真与真实数据反馈，使用领域随机化和微调。
- 实验或效果：实验显示倒塌率降低，物流部署中倒塌减少35%。

## 摘要（原文）

> The 3D bin packing problem, with its diverse industrial applications, has garnered significant research attention in recent years. Existing approaches typically model it as a discrete and static process, while real-world applications involve continuous gravity-driven interactions. This idealized simplification leads to infeasible deployments (e.g., unstable packing) in practice. Simulations with physical engine offer an opportunity to emulate continuous gravity effects, enabling the training of reinforcement learning (RL) agents to address such limitations and improve packing stability. However, a simulation-to-reality gap persists due to dynamic variations in physical properties of real-world objects, such as various friction coefficients, elasticity, and non-uniform weight distributions. To bridge this gap, we propose a hybrid RL framework that collaborates with physical simulation with real-world data feedback. Firstly, domain randomization is applied during simulation to expose agents to a spectrum of physical parameters, enhancing their generalization capability. Secondly, the RL agent is fine-tuned with real-world deployment feedback, further reducing collapse rates. Extensive experiments demonstrate that our method achieves lower collapse rates in both simulated and real-world scenarios. Large-scale deployments in logistics systems validate the practical effectiveness, with a 35\% reduction in packing collapse compared to baseline methods.

