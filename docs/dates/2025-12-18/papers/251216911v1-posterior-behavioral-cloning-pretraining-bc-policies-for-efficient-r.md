---
layout: default
title: Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning
---

# Posterior Behavioral Cloning: Pretraining BC Policies for Efficient RL Finetuning
**arXiv**：[2512.16911v1](https://arxiv.org/abs/2512.16911) · [PDF](https://arxiv.org/pdf/2512.16911.pdf)  
**作者**：Andrew Wagenmaker, Perry Dong, Raymond Tsao, Chelsea Finn, Sergey Levine  

**一句话要点**：提出后验行为克隆以提升强化学习微调效率

**关键词**：行为克隆, 强化学习微调, 后验分布, 机器人控制, 预训练策略

## 3 点简述
- 标准行为克隆在预训练中可能无法覆盖演示者动作，影响微调效果
- 后验行为克隆通过建模演示者行为的后验分布，确保动作覆盖并保持性能
- 在机器人控制基准和真实任务中，后验行为克隆显著提升强化学习微调性能

## 摘要（原文）

> Standard practice across domains from robotics to language is to first pretrain a policy on a large-scale demonstration dataset, and then finetune this policy, typically with reinforcement learning (RL), in order to improve performance on deployment domains. This finetuning step has proved critical in achieving human or super-human performance, yet while much attention has been given to developing more effective finetuning algorithms, little attention has been given to ensuring the pretrained policy is an effective initialization for RL finetuning. In this work we seek to understand how the pretrained policy affects finetuning performance, and how to pretrain policies in order to ensure they are effective initializations for finetuning. We first show theoretically that standard behavioral cloning (BC) -- which trains a policy to directly match the actions played by the demonstrator -- can fail to ensure coverage over the demonstrator's actions, a minimal condition necessary for effective RL finetuning. We then show that if, instead of exactly fitting the observed demonstrations, we train a policy to model the posterior distribution of the demonstrator's behavior given the demonstration dataset, we do obtain a policy that ensures coverage over the demonstrator's actions, enabling more effective finetuning. Furthermore, this policy -- which we refer to as the posterior behavioral cloning (PostBC) policy -- achieves this while ensuring pretrained performance is no worse than that of the BC policy. We then show that PostBC is practically implementable with modern generative models in robotic control domains -- relying only on standard supervised learning -- and leads to significantly improved RL finetuning performance on both realistic robotic control benchmarks and real-world robotic manipulation tasks, as compared to standard behavioral cloning.

