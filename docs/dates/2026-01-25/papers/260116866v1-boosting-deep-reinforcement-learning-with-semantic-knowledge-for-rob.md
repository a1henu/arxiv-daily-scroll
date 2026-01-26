---
layout: default
title: Boosting Deep Reinforcement Learning with Semantic Knowledge for Robotic Manipulators
---

# Boosting Deep Reinforcement Learning with Semantic Knowledge for Robotic Manipulators
**arXiv**：[2601.16866v1](https://arxiv.org/abs/2601.16866) · [PDF](https://arxiv.org/pdf/2601.16866.pdf)  
**作者**：Lucía Güitta-López, Vincenzo Suriani, Jaime Boal, Álvaro J. López-López, Daniele Nardi  

**一句话要点**：提出结合知识图谱嵌入与深度强化学习的方法，以提升机器人操作器的学习效率与准确性。

**关键词**：深度强化学习, 知识图谱嵌入, 机器人操作器, 语义知识, 学习效率提升

## 3 点简述
- 核心问题：深度强化学习在机器人控制中面临高样本复杂度，导致学习成本高。
- 方法要点：集成知识图谱嵌入提供语义知识，结合视觉观察增强环境理解。
- 实验或效果：在固定和随机目标属性环境中，学习时间减少达60%，任务准确率提升约15个百分点。

## 摘要（原文）

> Deep Reinforcement Learning (DRL) is a powerful framework for solving complex sequential decision-making problems, particularly in robotic control. However, its practical deployment is often hindered by the substantial amount of experience required for learning, which results in high computational and time costs. In this work, we propose a novel integration of DRL with semantic knowledge in the form of Knowledge Graph Embeddings (KGEs), aiming to enhance learning efficiency by providing contextual information to the agent. Our architecture combines KGEs with visual observations, enabling the agent to exploit environmental knowledge during training. Experimental validation with robotic manipulators in environments featuring both fixed and randomized target attributes demonstrates that our method achieves up to {60}{\%} reduction in learning time and improves task accuracy by approximately 15 percentage points, without increasing training time or computational complexity. These results highlight the potential of semantic knowledge to reduce sample complexity and improve the effectiveness of DRL in robotic applications.

