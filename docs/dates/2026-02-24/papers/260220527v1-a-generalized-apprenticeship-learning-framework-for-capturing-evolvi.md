---
layout: default
title: A Generalized Apprenticeship Learning Framework for Capturing Evolving Student Pedagogical Strategies
---

# A Generalized Apprenticeship Learning Framework for Capturing Evolving Student Pedagogical Strategies
**arXiv**：[2602.20527v1](https://arxiv.org/abs/2602.20527) · [PDF](https://arxiv.org/pdf/2602.20527.pdf)  
**作者**：Md Mirajul Islam, Xi Yang, Adittya Soukarjya Saha, Rajesh Debnath, Min Chi  

**一句话要点**：提出THEMES框架，利用广义学徒学习捕捉动态演化的学生教学策略以优化智能辅导系统。

**关键词**：学徒学习, 智能辅导系统, 奖励函数推断, 教学策略优化, 样本效率

## 3 点简述
- 核心问题：深度强化学习在教育技术中应用受限，因样本效率低和奖励函数设计难。
- 方法要点：采用广义学徒学习框架，从少量专家演示推断动态演化的奖励函数，生成泛化策略。
- 实验或效果：在六种基线对比中表现优异，仅用18条轨迹预测学生决策，AUC达0.899，Jaccard为0.653。

## 摘要（原文）

> Reinforcement Learning (RL) and Deep Reinforcement Learning (DRL) have advanced rapidly in recent years and have been successfully applied to e-learning environments like intelligent tutoring systems (ITSs). Despite great success, the broader application of DRL to educational technologies has been limited due to major challenges such as sample inefficiency and difficulty designing the reward function. In contrast, Apprenticeship Learning (AL) uses a few expert demonstrations to infer the expert's underlying reward functions and derive decision-making policies that generalize and replicate optimal behavior. In this work, we leverage a generalized AL framework, THEMES, to induce effective pedagogical policies by capturing the complexities of the expert student learning process, where multiple reward functions may dynamically evolve over time. We evaluate the effectiveness of THEMES against six state-of-the-art baselines, demonstrating its superior performance and highlighting its potential as a powerful alternative for inducing effective pedagogical policies and show that it can achieve high performance, with an AUC of 0.899 and a Jaccard of 0.653, using only 18 trajectories of a previous semester to predict student pedagogical decisions in a later semester.

