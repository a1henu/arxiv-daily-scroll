---
layout: default
title: GTA: Generative Traffic Agents for Simulating Realistic Mobility Behavior
---

# GTA: Generative Traffic Agents for Simulating Realistic Mobility Behavior
**arXiv**：[2601.16778v1](https://arxiv.org/abs/2601.16778) · [PDF](https://arxiv.org/pdf/2601.16778.pdf)  
**作者**：Simon Lämmer, Mark Colley, Patrick Ebel  

**一句话要点**：提出生成式交通代理GTA，利用LLM驱动的基于人物代理模拟大规模、上下文敏感的交通选择行为。

**关键词**：交通行为模拟, 生成式代理, 大语言模型应用, 城市交通规划, 基于人物建模

## 3 点简述
- 核心问题：传统交通行为预测方法依赖手工假设和数据收集，难以大规模模拟复杂个人偏好和社会因素。
- 方法要点：基于人口普查数据生成人工群体，使用LLM驱动的基于人物代理模拟活动安排和交通方式选择，无需手工规则。
- 实验或效果：在柏林规模实验中评估，代理能复制社会经济地位相关的交通方式分布模式，但在行程长度和偏好上存在系统性偏差。

## 摘要（原文）

> People's transportation choices reflect complex trade-offs shaped by personal preferences, social norms, and technology acceptance. Predicting such behavior at scale is a critical challenge with major implications for urban planning and sustainable transport. Traditional methods use handcrafted assumptions and costly data collection, making them impractical for early-stage evaluations of new technologies or policies. We introduce Generative Traffic Agents (GTA) for simulating large-scale, context-sensitive transportation choices using LLM-powered, persona-based agents. GTA generates artificial populations from census-based sociodemographic data. It simulates activity schedules and mode choices, enabling scalable, human-like simulations without handcrafted rules. We evaluate GTA in Berlin-scale experiments, comparing simulation results against empirical data. While agents replicate patterns, such as modal split by socioeconomic status, they show systematic biases in trip length and mode preference. GTA offers new opportunities for modeling how future innovations, from bike lanes to transit apps, shape mobility decisions.

