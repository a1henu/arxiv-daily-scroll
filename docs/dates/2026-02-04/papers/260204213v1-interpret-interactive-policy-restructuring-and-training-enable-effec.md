---
layout: default
title: InterPReT: Interactive Policy Restructuring and Training Enable Effective Imitation Learning from Laypersons
---

# InterPReT: Interactive Policy Restructuring and Training Enable Effective Imitation Learning from Laypersons
**arXiv**：[2602.04213v1](https://arxiv.org/abs/2602.04213) · [PDF](https://arxiv.org/pdf/2602.04213.pdf)  
**作者**：Feiyu Gavin Zhu, Jean Oh, Reid Simmons  

**一句话要点**：提出InterPReT方法，通过交互式策略重构与训练，使非专业用户能有效进行模仿学习

**关键词**：模仿学习, 交互式学习, 策略重构, 用户研究, 非专业用户

## 3 点简述
- 核心问题：模仿学习依赖专家演示和训练监控，非专业用户难以有效教导AI代理
- 方法要点：基于用户指令动态更新策略结构并优化参数，支持交互式教学与决策审查
- 实验或效果：用户研究显示，在赛车游戏中，相比基线，InterPReT能生成更鲁棒策略且不损害可用性

## 摘要（原文）

> Imitation learning has shown success in many tasks by learning from expert demonstrations. However, most existing work relies on large-scale demonstrations from technical professionals and close monitoring of the training process. These are challenging for a layperson when they want to teach the agent new skills. To lower the barrier of teaching AI agents, we propose Interactive Policy Restructuring and Training (InterPReT), which takes user instructions to continually update the policy structure and optimize its parameters to fit user demonstrations. This enables end-users to interactively give instructions and demonstrations, monitor the agent's performance, and review the agent's decision-making strategies. A user study (N=34) on teaching an AI agent to drive in a racing game confirms that our approach yields more robust policies without impairing system usability, compared to a generic imitation learning baseline, when a layperson is responsible for both giving demonstrations and determining when to stop. This shows that our method is more suitable for end-users without much technical background in machine learning to train a dependable policy

