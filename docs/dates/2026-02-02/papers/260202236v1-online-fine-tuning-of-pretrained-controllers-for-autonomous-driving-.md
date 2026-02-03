---
layout: default
title: Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL
---

# Online Fine-Tuning of Pretrained Controllers for Autonomous Driving via Real-Time Recurrent RL
**arXiv**：[2602.02236v1](https://arxiv.org/abs/2602.02236) · [PDF](https://arxiv.org/pdf/2602.02236.pdf)  
**作者**：Julian Lemmel, Felix Resch, Mónika Farsang, Ramin Hasani, Daniela Rus, Radu Grosu  

**一句话要点**：提出基于实时循环强化学习的在线微调方法，以提升自动驾驶策略在环境变化下的适应性。

**关键词**：自动驾驶, 在线微调, 实时循环强化学习, 液体电阻-电容循环神经网络, 策略适应

## 3 点简述
- 核心问题：预训练策略在环境动态变化、传感器漂移或任务目标改变时性能迅速下降。
- 方法要点：采用实时循环强化学习在线微调预训练策略，结合液体电阻-电容循环神经网络模型。
- 实验或效果：在模拟CarRacing环境和真实RoboRacer汽车线跟随任务中验证了闭环方法的有效性。

## 摘要（原文）

> Deploying pretrained policies in real-world applications presents substantial challenges that fundamentally limit the practical applicability of learning-based control systems. When autonomous systems encounter environmental changes in system dynamics, sensor drift, or task objectives, fixed policies rapidly degrade in performance. We show that employing Real-Time Recurrent Reinforcement Learning (RTRRL), a biologically plausible algorithm for online adaptation, can effectively fine-tune a pretrained policy to improve autonomous agents' performance on driving tasks. We further show that RTRRL synergizes with a recent biologically inspired recurrent network model, the Liquid-Resistance Liquid-Capacitance RNN. We demonstrate the effectiveness of this closed-loop approach in a simulated CarRacing environment and in a real-world line-following task with a RoboRacer car equipped with an event camera.

