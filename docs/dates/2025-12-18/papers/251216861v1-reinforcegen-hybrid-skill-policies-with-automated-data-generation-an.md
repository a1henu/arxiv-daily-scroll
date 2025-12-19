---
layout: default
title: ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning
---

# ReinforceGen: Hybrid Skill Policies with Automated Data Generation and Reinforcement Learning
**arXiv**：[2512.16861v1](https://arxiv.org/abs/2512.16861) · [PDF](https://arxiv.org/pdf/2512.16861.pdf)  
**作者**：Zihan Zhou, Animesh Garg, Ajay Mandlekar, Caelan Garrett  

**一句话要点**：提出ReinforceGen系统，结合任务分解与强化学习微调，以解决机器人长时程操作挑战。

**关键词**：长时程操作, 任务分解, 模仿学习, 强化学习微调, 机器人控制, 运动规划

## 3 点简述
- 核心问题：机器人长时程操作是长期挑战，需处理复杂任务分解与技能协调。
- 方法要点：系统集成任务分解、数据生成、模仿学习和运动规划，并通过强化学习微调各组件。
- 实验或效果：在Robosuite数据集上，最高重置范围设置下达到80%成功率，微调贡献平均性能提升89%。

## 摘要（原文）

> Long-horizon manipulation has been a long-standing challenge in the robotics community. We propose ReinforceGen, a system that combines task decomposition, data generation, imitation learning, and motion planning to form an initial solution, and improves each component through reinforcement-learning-based fine-tuning. ReinforceGen first segments the task into multiple localized skills, which are connected through motion planning. The skills and motion planning targets are trained with imitation learning on a dataset generated from 10 human demonstrations, and then fine-tuned through online adaptation and reinforcement learning. When benchmarked on the Robosuite dataset, ReinforceGen reaches 80% success rate on all tasks with visuomotor controls in the highest reset range setting. Additional ablation studies show that our fine-tuning approaches contributes to an 89% average performance increase. More results and videos available in https://reinforcegen.github.io/

