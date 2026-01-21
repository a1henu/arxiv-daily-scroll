---
layout: default
title: Diffusion-Guided Backdoor Attacks in Real-World Reinforcement Learning
---

# Diffusion-Guided Backdoor Attacks in Real-World Reinforcement Learning
**arXiv**：[2601.14104v1](https://arxiv.org/abs/2601.14104) · [PDF](https://arxiv.org/pdf/2601.14104.pdf)  
**作者**：Tairan Huang, Qingqing Ye, Yulin Jin, Jiawei Lian, Yi Wang, Haibo Hu  

**一句话要点**：提出扩散引导后门攻击框架，以解决真实世界强化学习中安全约束对传统攻击的衰减问题。

**关键词**：后门攻击, 强化学习, 真实世界机器人, 扩散模型, 安全约束, 视觉触发器

## 3 点简述
- 核心问题：真实世界机器人系统的安全约束（如速度限制）会抑制传统后门攻击，导致其有效性未知。
- 方法要点：使用条件扩散模型生成多样化的视觉补丁触发器，并基于优势的投毒策略在关键训练状态注入。
- 实验或效果：在TurtleBot3移动机器人上评估，实现可靠的目标攻击激活，同时保持正常任务性能。

## 摘要（原文）

> Backdoor attacks embed hidden malicious behaviors in reinforcement learning (RL) policies and activate them using triggers at test time. Most existing attacks are validated only in simulation, while their effectiveness in real-world robotic systems remains unclear. In physical deployment, safety-constrained control pipelines such as velocity limiting, action smoothing, and collision avoidance suppress abnormal actions, causing strong attenuation of conventional backdoor attacks. We study this previously overlooked problem and propose a diffusion-guided backdoor attack framework (DGBA) for real-world RL. We design small printable visual patch triggers placed on the floor and generate them using a conditional diffusion model that produces diverse patch appearances under real-world visual variations. We treat the robot control stack as a black-box system. We further introduce an advantage-based poisoning strategy that injects triggers only at decision-critical training states. We evaluate our method on a TurtleBot3 mobile robot and demonstrate reliable activation of targeted attacks while preserving normal task performance. Demo videos and code are available in the supplementary material.

