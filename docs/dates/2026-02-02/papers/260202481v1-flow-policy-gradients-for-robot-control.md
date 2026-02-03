---
layout: default
title: Flow Policy Gradients for Robot Control
---

# Flow Policy Gradients for Robot Control
**arXiv**：[2602.02481v1](https://arxiv.org/abs/2602.02481) · [PDF](https://arxiv.org/pdf/2602.02481.pdf)  
**作者**：Brent Yi, Hongsuk Choi, Himanshu Gaurav Singh, Xiaoyu Huang, Takara E. Truong, Carmelo Sferrazza, Yi Ma, Rocky Duan, Pieter Abbeel, Guanya Shi, Karen Liu, Angjoo Kanazawa  

**一句话要点**：提出流匹配策略梯度以训练和微调机器人控制中的表达性策略

**关键词**：机器人控制, 策略梯度, 流匹配, 仿真到现实迁移, 表达性策略

## 3 点简述
- 核心问题：基于似然的策略梯度方法依赖可微动作似然，限制策略输出为简单分布如高斯分布。
- 方法要点：引入流匹配策略梯度框架，绕过似然计算，改进目标函数以增强表达性和训练效果。
- 实验或效果：在腿式运动、人形运动跟踪和操作任务中有效，实现稳健的仿真到现实迁移。

## 摘要（原文）

> Likelihood-based policy gradient methods are the dominant approach for training robot control policies from rewards. These methods rely on differentiable action likelihoods, which constrain policy outputs to simple distributions like Gaussians. In this work, we show how flow matching policy gradients -- a recent framework that bypasses likelihood computation -- can be made effective for training and fine-tuning more expressive policies in challenging robot control settings. We introduce an improved objective that enables success in legged locomotion, humanoid motion tracking, and manipulation tasks, as well as robust sim-to-real transfer on two humanoid robots. We then present ablations and analysis on training dynamics. Results show how policies can exploit the flow representation for exploration when training from scratch, as well as improved fine-tuning robustness over baselines.

