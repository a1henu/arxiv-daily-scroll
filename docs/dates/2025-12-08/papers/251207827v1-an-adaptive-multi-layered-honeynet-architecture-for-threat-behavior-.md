---
layout: default
title: An Adaptive Multi-Layered Honeynet Architecture for Threat Behavior Analysis via Deep Learning
---

# An Adaptive Multi-Layered Honeynet Architecture for Threat Behavior Analysis via Deep Learning
**arXiv**：[2512.07827v1](https://arxiv.org/abs/2512.07827) · [PDF](https://arxiv.org/pdf/2512.07827.pdf)  
**作者**：Lukas Johannes Möller  

**一句话要点**：提出自适应深度学习蜜网ADLAH，通过强化学习实时升级会话以高效捕获威胁行为。

**关键词**：蜜网架构, 深度学习异常检测, 强化学习决策, 威胁行为分析, 自动化攻击链提取

## 3 点简述
- 核心问题：静态蜜罐无法应对复杂网络威胁，需自适应智能欺骗。
- 方法要点：基于强化学习的决策机制，动态升级会话至高交互蜜罐。
- 实验或效果：原型验证可行性，但缺乏大规模现场数据，提供详细设计权衡与评估路线图。

## 摘要（原文）

> The escalating sophistication and variety of cyber threats have rendered static honeypots inadequate, necessitating adaptive, intelligence-driven deception. In this work, ADLAH is introduced: an Adaptive Deep Learning Anomaly Detection Honeynet designed to maximize high-fidelity threat intelligence while minimizing cost through autonomous orchestration of infrastructure. The principal contribution is offered as an end-to-end architectural blueprint and vision for an AI-driven deception platform. Feasibility is evidenced by a functional prototype of the central decision mechanism, in which a reinforcement learning (RL) agent determines, in real time, when sessions should be escalated from low-interaction sensor nodes to dynamically provisioned, high-interaction honeypots. Because sufficient live data were unavailable, field-scale validation is not claimed; instead, design trade-offs and limitations are detailed, and a rigorous roadmap toward empirical evaluation at scale is provided. Beyond selective escalation and anomaly detection, the architecture pursues automated extraction, clustering, and versioning of bot attack chains, a core capability motivated by the empirical observation that exposed services are dominated by automated traffic. Together, these elements delineate a practical path toward cost-efficient capture of high-value adversary behavior, systematic bot versioning, and the production of actionable threat intelligence.

