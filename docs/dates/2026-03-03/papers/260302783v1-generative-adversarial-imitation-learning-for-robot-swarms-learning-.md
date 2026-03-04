---
layout: default
title: Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies
---

# Generative adversarial imitation learning for robot swarms: Learning from human demonstrations and trained policies
**arXiv**：[2603.02783v1](https://arxiv.org/abs/2603.02783) · [PDF](https://arxiv.org/pdf/2603.02783.pdf)  
**作者**：Mattes Kraus, Jonas Kuckling  

**一句话要点**：提出基于生成对抗模仿学习的框架，使机器人群体能从人类演示中学习集体行为

**关键词**：生成对抗模仿学习, 机器人群体, 集体行为学习, 人类演示, 模仿学习框架, 真实机器人实验

## 3 点简述
- 核心问题：模仿学习中，机器人群体通常依赖现有策略演示，缺乏从人类演示直接学习集体行为的方法
- 方法要点：采用生成对抗模仿学习框架，支持从人类手动演示和PPO训练策略演示中学习
- 实验或效果：在六个任务中评估，学习到的行为性能与演示相当，并在真实TurtleBot 4机器人上部署验证

## 摘要（原文）

> In imitation learning, robots are supposed to learn from demonstrations of the desired behavior. Most of the work in imitation learning for swarm robotics provides the demonstrations as rollouts of an existing policy. In this work, we provide a framework based on generative adversarial imitation learning that aims to learn collective behaviors from human demonstrations. Our framework is evaluated across six different missions, learning both from manual demonstrations and demonstrations derived from a PPO-trained policy. Results show that the imitation learning process is able to learn qualitatively meaningful behaviors that perform similarly well as the provided demonstrations. Additionally, we deploy the learned policies on a swarm of TurtleBot 4 robots in real-robot experiments. The exhibited behaviors preserved their visually recognizable character and their performance is comparable to the one achieved in simulation.

