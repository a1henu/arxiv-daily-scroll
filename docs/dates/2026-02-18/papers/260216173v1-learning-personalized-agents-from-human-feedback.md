---
layout: default
title: Learning Personalized Agents from Human Feedback
---

# Learning Personalized Agents from Human Feedback
**arXiv**：[2602.16173v1](https://arxiv.org/abs/2602.16173) · [PDF](https://arxiv.org/pdf/2602.16173.pdf)  
**作者**：Kaiqu Liang, Julia Kruk, Shengyi Qian, Xianjun Yang, Shengjie Bi, Yuanshun Yao, Shaoliang Nie, Mingyang Zhang, Lijuan Liu, Jaime Fernández Fisac, Shuyan Zhou, Saghar Hosseini  

**一句话要点**：提出PAHF框架，通过显式记忆与双反馈通道实现持续个性化代理学习

**关键词**：个性化代理, 持续学习, 显式记忆, 人类反馈, 偏好漂移, 在线交互

## 3 点简述
- 核心问题：现有AI代理难以适应个体用户动态变化的偏好，依赖静态数据集导致新用户和偏好漂移问题
- 方法要点：PAHF采用三步循环，包括预行动澄清、基于记忆的行动基础和反馈驱动的记忆更新
- 实验或效果：在具身操作和在线购物基准上，PAHF显著减少初始个性化误差并快速适应偏好变化

## 摘要（原文）

> Modern AI agents are powerful but often fail to align with the idiosyncratic, evolving preferences of individual users. Prior approaches typically rely on static datasets, either training implicit preference models on interaction history or encoding user profiles in external memory. However, these approaches struggle with new users and with preferences that change over time. We introduce Personalized Agents from Human Feedback (PAHF), a framework for continual personalization in which agents learn online from live interaction using explicit per-user memory. PAHF operationalizes a three-step loop: (1) seeking pre-action clarification to resolve ambiguity, (2) grounding actions in preferences retrieved from memory, and (3) integrating post-action feedback to update memory when preferences drift. To evaluate this capability, we develop a four-phase protocol and two benchmarks in embodied manipulation and online shopping. These benchmarks quantify an agent's ability to learn initial preferences from scratch and subsequently adapt to persona shifts. Our theoretical analysis and empirical results show that integrating explicit memory with dual feedback channels is critical: PAHF learns substantially faster and consistently outperforms both no-memory and single-channel baselines, reducing initial personalization error and enabling rapid adaptation to preference shifts.

