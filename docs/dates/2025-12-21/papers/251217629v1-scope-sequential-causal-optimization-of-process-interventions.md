---
layout: default
title: SCOPE: Sequential Causal Optimization of Process Interventions
---

# SCOPE: Sequential Causal Optimization of Process Interventions
**arXiv**：[2512.17629v1](https://arxiv.org/abs/2512.17629) · [PDF](https://arxiv.org/pdf/2512.17629.pdf)  
**作者**：Jakob De Moor, Hans Weytjens, Johannes De Smedt, Jochen De Weerdt  

**一句话要点**：提出SCOPE方法以解决业务流程中序列干预的因果优化问题

**关键词**：预测性流程监控, 序列干预, 因果学习, 反向归纳, 关键绩效指标优化

## 3 点简述
- 核心问题：现有预测性流程监控方法难以处理序列干预的依赖关系，常依赖模拟或数据增强导致偏差
- 方法要点：SCOPE利用因果学习和反向归纳，直接从观测数据估计干预效果，避免现实差距
- 实验或效果：在合成和半合成数据集上，SCOPE在优化关键绩效指标方面优于现有技术

## 摘要（原文）

> Prescriptive Process Monitoring (PresPM) recommends interventions during business processes to optimize key performance indicators (KPIs). In realistic settings, interventions are rarely isolated: organizations need to align sequences of interventions to jointly steer the outcome of a case. Existing PresPM approaches fall short in this respect. Many focus on a single intervention decision, while others treat multiple interventions independently, ignoring how they interact over time. Methods that do address these dependencies depend either on simulation or data augmentation to approximate the process to train a Reinforcement Learning (RL) agent, which can create a reality gap and introduce bias. We introduce SCOPE, a PresPM approach that learns aligned sequential intervention recommendations. SCOPE employs backward induction to estimate the effect of each candidate intervention action, propagating its impact from the final decision point back to the first. By leveraging causal learners, our method can utilize observational data directly, unlike methods that require constructing process approximations for reinforcement learning. Experiments on both an existing synthetic dataset and a new semi-synthetic dataset show that SCOPE consistently outperforms state-of-the-art PresPM techniques in optimizing the KPI. The novel semi-synthetic setup, based on a real-life event log, is provided as a reusable benchmark for future work on sequential PresPM.

