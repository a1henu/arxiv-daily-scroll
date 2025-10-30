---
layout: default
title: Learning to Plan & Schedule with Reinforcement-Learned Bimanual Robot Skills
---

# Learning to Plan & Schedule with Reinforcement-Learned Bimanual Robot Skills
**arXiv**：[2510.25634v1](https://arxiv.org/abs/2510.25634) · [PDF](https://arxiv.org/pdf/2510.25634.pdf)  
**作者**：Weikang Wan, Fabio Ramos, Xuning Yang, Caelan Garrett  

**一句话要点**：提出分层框架以解决长时程接触丰富的双手机器人操作问题

**关键词**：双手机器人操作, 分层规划, 强化学习技能, Transformer规划器, 接触丰富任务, 技能调度

## 3 点简述
- 核心问题：长时程接触丰富的双手机器人操作需要复杂协调，涉及并行执行与顺序协作。
- 方法要点：使用强化学习训练技能库，并基于Transformer的规划器预测技能调度与参数。
- 实验或效果：在复杂任务中比端到端强化学习和传统顺序规划器成功率更高、行为更高效。

## 摘要（原文）

> Long-horizon contact-rich bimanual manipulation presents a significant
> challenge, requiring complex coordination involving a mixture of parallel
> execution and sequential collaboration between arms. In this paper, we
> introduce a hierarchical framework that frames this challenge as an integrated
> skill planning & scheduling problem, going beyond purely sequential
> decision-making to support simultaneous skill invocation. Our approach is built
> upon a library of single-arm and bimanual primitive skills, each trained using
> Reinforcement Learning (RL) in GPU-accelerated simulation. We then train a
> Transformer-based planner on a dataset of skill compositions to act as a
> high-level scheduler, simultaneously predicting the discrete schedule of skills
> as well as their continuous parameters. We demonstrate that our method achieves
> higher success rates on complex, contact-rich tasks than end-to-end RL
> approaches and produces more efficient, coordinated behaviors than traditional
> sequential-only planners.

