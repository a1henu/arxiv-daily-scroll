---
layout: default
title: World-Gymnast: Training Robots with Reinforcement Learning in a World Model
---

# World-Gymnast: Training Robots with Reinforcement Learning in a World Model
**arXiv**：[2602.02454v1](https://arxiv.org/abs/2602.02454) · [PDF](https://arxiv.org/pdf/2602.02454.pdf)  
**作者**：Ansh Kumar Sharma, Yixiang Sun, Ninghao Lu, Yunzhe Zhang, Jiarao Liu, Sherry Yang  

**一句话要点**：提出World-Gymnast，通过世界模型中的强化学习训练机器人策略以提升真实机器人性能。

**关键词**：世界模型, 强化学习, 机器人学习, 视觉语言动作策略, 仿真到真实迁移, 云训练

## 3 点简述
- 核心问题：物理交互成本高，监督微调和软件模拟存在数据限制和仿真到真实差距。
- 方法要点：在动作条件视频世界模型中执行强化学习微调，使用视觉语言模型奖励策略展开。
- 实验或效果：在Bridge机器人设置中，性能优于监督微调达18倍，优于软件模拟达2倍。

## 摘要（原文）

> Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world model can be more effective than supervised learning or software simulation in achieving better real-robot performance. We propose World-Gymnast, which performs RL finetuning of a vision-language-action (VLA) policy by rolling out the policy in an action-conditioned video world model and rewarding the rollouts with a vision-language model (VLM). On the Bridge robot setup, World-Gymnast outperforms SFT by as much as 18x and outperforms software simulator by as much as 2x. More importantly, World-Gymnast demonstrates intriguing capabilities of RL with a world model, including training on diverse language instructions and novel scenes from the world model, test-time training in a novel scene, and online iterative world model and policy improvement. Our results suggest learning a world model and training robot policies in the cloud could be the key to bridging the gap between robots that work in demonstrations and robots that can work in anyone's household.

