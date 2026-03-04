---
layout: default
title: Watch Your Step: Learning Semantically-Guided Locomotion in Cluttered Environment
---

# Watch Your Step: Learning Semantically-Guided Locomotion in Cluttered Environment
**arXiv**：[2603.02657v1](https://arxiv.org/abs/2603.02657) · [PDF](https://arxiv.org/pdf/2603.02657.pdf)  
**作者**：Denan Liang, Yuan Zhu, Ruimeng Liu, Thien-Minh Nguyen, Shenghai Yuan, Lihua Xie  

**一句话要点**：提出SemLoco强化学习框架，以解决足式机器人在杂乱环境中避障的挑战。

**关键词**：足式机器人, 强化学习, 语义导航, 避障控制, 杂乱环境

## 3 点简述
- 核心问题：足式机器人因高层语义理解与底层控制脱节，难以避免踩踏低矮物体。
- 方法要点：采用两阶段强化学习，结合软硬约束和像素级立足点安全推断，集成语义图分配可通行成本。
- 实验或效果：显著减少碰撞，提升敏感物体周围安全性，适用于复杂非结构化真实环境。

## 摘要（原文）

> Although legged robots demonstrate impressive mobility on rough terrain, using them safely in cluttered environments remains a challenge. A key issue is their inability to avoid stepping on low-lying objects, such as high-cost small devices or cables on flat ground. This limitation arises from a disconnection between high-level semantic understanding and low-level control, combined with errors in elevation maps during real-world operation. To address this, we introduce SemLoco, a Reinforcement Learning (RL) framework designed to avoid obstacles precisely in densely cluttered environments. SemLoco uses a two-stage RL approach that combines both soft and hard constraints and performs pixel-wise foothold safety inference, enabling more accurate foot placement. Additionally, SemLoco integrates a semantic map to assign traversability costs rather than relying solely on geometric data. SemLoco significantly reduces collisions and improves safety around sensitive objects, enabling reliable navigation in situations where traditional controllers would likely cause damage. Experimental results further demonstrate that SemLoco can be effectively applied to more complex, unstructured real-world environments.

