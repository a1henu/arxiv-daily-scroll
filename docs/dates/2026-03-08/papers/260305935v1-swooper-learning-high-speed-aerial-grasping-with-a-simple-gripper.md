---
layout: default
title: Swooper: Learning High-Speed Aerial Grasping With a Simple Gripper
---

# Swooper: Learning High-Speed Aerial Grasping With a Simple Gripper
**arXiv**：[2603.05935v1](https://arxiv.org/abs/2603.05935) · [PDF](https://arxiv.org/pdf/2603.05935.pdf)  
**作者**：Ziken Huang, Xinze Niu, Bowen Chai, Renbiao Jin, Danping Zou  

**一句话要点**：提出Swooper方法，通过深度强化学习实现高速无人机抓取，使用简单夹爪完成精确飞行与抓取控制。

**关键词**：高速无人机抓取, 深度强化学习, 两阶段学习, 轻量神经网络, 实时控制, 零样本部署

## 3 点简述
- 核心问题：高速无人机抓取需精确飞行与夹爪协调，传统方法复杂且依赖高级硬件。
- 方法要点：采用两阶段学习策略，先预训练飞行控制，再微调抓取技能，使用轻量神经网络策略。
- 实验或效果：在真实世界部署，抓取成功率84%，速度达1.5 m/s，无需微调，训练时间短于60分钟。

## 摘要（原文）

> High-speed aerial grasping presents significant challenges due to the high demands on precise, responsive flight control and coordinated gripper manipulation. In this work, we propose Swooper, a deep reinforcement learning (DRL) based approach that achieves both precise flight control and active gripper control using a single lightweight neural network policy. Training such a policy directly via DRL is nontrivial due to the complexity of coordinating flight and grasping. To address this, we adopt a two-stage learning strategy: we first pre-train a flight control policy, and then fine-tune it to acquire grasping skills. With the carefully designed reward functions and training framework, the entire training process completes in under 60 minutes on a standard desktop with an Nvidia RTX 3060 GPU. To validate the trained policy in the real world, we develop a lightweight quadrotor grasping platform equipped with a simple off-the-shelf gripper, and deploy the policy in a zero-shot manner on the onboard Raspberry Pi 4B computer, where each inference takes only about 1.0 ms. In 25 real-world trials, our policy achieves an 84% grasp success rate and grasping speeds of up to 1.5 m/s without any fine-tuning. This matches the robustness and agility of state-of-the-art classical systems with sophisticated grippers, highlighting the capability of DRL for learning a robust control policy that seamlessly integrates high-speed flight and grasping. The supplementary video is available for more results.
>   Video: https://zikenhuang.github.io/Swooper/.

