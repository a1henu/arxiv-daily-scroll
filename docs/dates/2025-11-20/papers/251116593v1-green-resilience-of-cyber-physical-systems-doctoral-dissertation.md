---
layout: default
title: Green Resilience of Cyber-Physical Systems: Doctoral Dissertation
---

# Green Resilience of Cyber-Physical Systems: Doctoral Dissertation
**arXiv**：[2511.16593v1](https://arxiv.org/abs/2511.16593) · [PDF](https://arxiv.org/pdf/2511.16593.pdf)  
**作者**：Diaeddin Rimawi  

**一句话要点**：提出GResilience框架以优化在线协作AI系统的绿色性与韧性平衡

**关键词**：网络物理系统, 在线协作AI, 绿色韧性, 多目标优化, 强化学习, 灾难性遗忘

## 3 点简述
- 核心问题：在线协作AI系统在干扰事件中需平衡韧性恢复与能源影响。
- 方法要点：通过多目标优化、博弈论和强化学习开发恢复策略。
- 实验效果：GResilience策略缩短恢复时间、稳定性能并减少碳排放。

## 摘要（原文）

> Cyber-physical systems (CPS) combine computational and physical components. Online Collaborative AI System (OL-CAIS) is a type of CPS that learn online in collaboration with humans to achieve a common goal, which makes it vulnerable to disruptive events that degrade performance. Decision-makers must therefore restore performance while limiting energy impact, creating a trade-off between resilience and greenness. This research addresses how to balance these two properties in OL-CAIS. It aims to model resilience for automatic state detection, develop agent-based policies that optimize the greenness-resilience trade-off, and understand catastrophic forgetting to maintain performance consistency. We model OL-CAIS behavior through three operational states: steady, disruptive, and final. To support recovery during disruptions, we introduce the GResilience framework, which provides recovery strategies through multi-objective optimization (one-agent), game-theoretic decision-making (two-agent), and reinforcement learning (RL-agent). We also design a measurement framework to quantify resilience and greenness. Empirical evaluation uses real and simulated experiments with a collaborative robot learning object classification from human demonstrations. Results show that the resilience model captures performance transitions during disruptions, and that GResilience policies improve green recovery by shortening recovery time, stabilizing performance, and reducing human dependency. RL-agent policies achieve the strongest results, although with a marginal increase in CO2 emissions. We also observe catastrophic forgetting after repeated disruptions, while our policies help maintain steadiness. A comparison with containerized execution shows that containerization cuts CO2 emissions by half. Overall, this research provides models, metrics, and policies that ensure the green recovery of OL-CAIS.

