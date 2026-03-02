---
layout: default
title: Actor-Critic Pretraining for Proximal Policy Optimization
---

# Actor-Critic Pretraining for Proximal Policy Optimization
**arXiv**：[2602.23804v1](https://arxiv.org/abs/2602.23804) · [PDF](https://arxiv.org/pdf/2602.23804.pdf)  
**作者**：Andreas Kernbach, Amr Elsheikh, Nicolas Grupp, René Nagel, Marco F. Huber  

**一句话要点**：提出基于专家演示的Actor-Critic预训练方法，以提升PPO在机器人任务中的样本效率。

**关键词**：强化学习, Actor-Critic算法, 预训练, 样本效率, 机器人任务, 专家演示

## 3 点简述
- 核心问题：强化学习Actor-Critic算法在机器人应用中样本效率低，专家数据利用不足。
- 方法要点：通过行为克隆预训练Actor，利用预训练策略的回报预训练Critic，实现双网络初始化。
- 实验或效果：在15个模拟机器人任务中，相比无预训练平均提升86.1%样本效率，优于仅Actor预训练。

## 摘要（原文）

> Reinforcement learning (RL) actor-critic algorithms enable autonomous learning but often require a large number of environment interactions, which limits their applicability in robotics. Leveraging expert data can reduce the number of required environment interactions. A common approach is actor pretraining, where the actor network is initialized via behavioral cloning on expert demonstrations and subsequently fine-tuned with RL. In contrast, the initialization of the critic network has received little attention, despite its central role in policy optimization. This paper proposes a pretraining approach for actor-critic algorithms like Proximal Policy Optimization (PPO) that uses expert demonstrations to initialize both networks. The actor is pretrained via behavioral cloning, while the critic is pretrained using returns obtained from rollouts of the pretrained policy. The approach is evaluated on 15 simulated robotic manipulation and locomotion tasks. Experimental results show that actor-critic pretraining improves sample efficiency by 86.1% on average compared to no pretraining and by 30.9% to actor-only pretraining.

