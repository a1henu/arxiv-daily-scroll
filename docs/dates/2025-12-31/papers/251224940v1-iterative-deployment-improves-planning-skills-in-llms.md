---
layout: default
title: Iterative Deployment Improves Planning Skills in LLMs
---

# Iterative Deployment Improves Planning Skills in LLMs
**arXiv**：[2512.24940v1](https://arxiv.org/abs/2512.24940) · [PDF](https://arxiv.org/pdf/2512.24940.pdf)  
**作者**：Augusto B. Corrêa, Yoav Gelberg, Luckeciano C. Melo, Ilia Shumailov, André G. Pereira, Yarin Gal  

**一句话要点**：提出迭代部署方法以提升大语言模型的规划能力

**关键词**：迭代部署, 规划技能, 大语言模型, 强化学习, 数据策划, AI安全

## 3 点简述
- 核心问题：大语言模型在规划任务中技能有限，缺乏泛化能力。
- 方法要点：通过用户从先前模型部署中精心策划数据，迭代微调模型。
- 实验或效果：在多个规划领域显著提升规划技能，模型能发现更长计划并展现涌现泛化。

## 摘要（原文）

> We show that iterative deployment of large language models (LLMs), each fine-tuned on data carefully curated by users from the previous models' deployment, can significantly change the properties of the resultant models. By testing this mechanism on various planning domains, we observe substantial improvements in planning skills, with later models displaying emergent generalization by discovering much longer plans than the initial models. We then provide theoretical analysis showing that iterative deployment effectively implements reinforcement learning (RL) training in the outer-loop (i.e. not as part of intentional model training), with an implicit reward function. The connection to RL has two important implications: first, for the field of AI safety, as the reward function entailed by repeated deployment is not defined explicitly, and could have unexpected implications to the properties of future model deployments. Second, the mechanism highlighted here can be viewed as an alternative training regime to explicit RL, relying on data curation rather than explicit rewards.

