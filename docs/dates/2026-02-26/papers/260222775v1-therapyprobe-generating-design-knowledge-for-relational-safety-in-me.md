---
layout: default
title: TherapyProbe: Generating Design Knowledge for Relational Safety in Mental Health Chatbots Through Adversarial Simulation
---

# TherapyProbe: Generating Design Knowledge for Relational Safety in Mental Health Chatbots Through Adversarial Simulation
**arXiv**：[2602.22775v1](https://arxiv.org/abs/2602.22775) · [PDF](https://arxiv.org/pdf/2602.22775.pdf)  
**作者**：Joydeep Chandra, Satyam Kumar Navneet, Yong Zhang  

**一句话要点**：提出TherapyProbe方法，通过对抗模拟生成心理健康聊天机器人关系安全设计知识

**关键词**：心理健康聊天机器人, 关系安全, 对抗模拟, 设计模式库, 多智能体系统

## 3 点简述
- 核心问题：现有安全评估忽视多轮对话中的治疗动态，无法确保聊天机器人长期关系安全。
- 方法要点：采用对抗多智能体模拟，系统探索聊天机器人对话轨迹，识别关系安全失败模式。
- 实验或效果：构建包含23种失败原型的模式库，提供可复现方法、临床分类和设计建议。

## 摘要（原文）

> As mental health chatbots proliferate to address the global treatment gap, a critical question emerges: How do we design for relational safety the quality of interaction patterns that unfold across conversations rather than the correctness of individual responses? Current safety evaluations assess single-turn crisis responses, missing the therapeutic dynamics that determine whether chatbots help or harm over time. We introduce TherapyProbe, a design probe methodology that generates actionable design knowledge by systematically exploring chatbot conversation trajectories through adversarial multi-agent simulation. Using open-source models, TherapyProbe surfaces relational safety failures interaction patterns like "validation spirals" where chatbots progressively reinforce hopelessness, or "empathy fatigue" where responses become mechanical over turns. Our contribution is translating these failures into a Safety Pattern Library of 23 failure archetypes with corresponding design recommendations. We contribute: (1) a replicable methodology requiring no API costs, (2) a clinically-grounded failure taxonomy, and (3) design implications for developers, clinicians, and policymakers.

