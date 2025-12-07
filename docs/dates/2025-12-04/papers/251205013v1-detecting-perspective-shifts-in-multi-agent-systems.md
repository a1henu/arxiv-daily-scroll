---
layout: default
title: Detecting Perspective Shifts in Multi-agent Systems
---

# Detecting Perspective Shifts in Multi-agent Systems
**arXiv**：[2512.05013v1](https://arxiv.org/abs/2512.05013) · [PDF](https://arxiv.org/pdf/2512.05013.pdf)  
**作者**：Eric Bridgeford, Hayden Helm  

**一句话要点**：提出TDKPS框架以检测黑盒多智能体系统中的行为动态变化

**关键词**：多智能体系统, 行为动态监测, 时间嵌入, 假设检验, 黑盒系统, 数字角色演化

## 3 点简述
- 核心问题：现有方法仅基于单时间点低维表示，难以监测多智能体系统随时间的行为变化
- 方法要点：引入TDKPS联合嵌入跨时间智能体，并设计新颖假设检验检测个体和群体级行为变化
- 实验或效果：通过模拟和自然实验验证测试敏感性，检测到与真实外生事件显著相关的行为变化

## 摘要（原文）

> Generative models augmented with external tools and update mechanisms (or \textit{agents}) have demonstrated capabilities beyond intelligent prompting of base models. As agent use proliferates, dynamic multi-agent systems have naturally emerged. Recent work has investigated the theoretical and empirical properties of low-dimensional representations of agents based on query responses at a single time point. This paper introduces the Temporal Data Kernel Perspective Space (TDKPS), which jointly embeds agents across time, and proposes several novel hypothesis tests for detecting behavioral change at the agent- and group-level in black-box multi-agent systems. We characterize the empirical properties of our proposed tests, including their sensitivity to key hyperparameters, in simulations motivated by a multi-agent system of evolving digital personas. Finally, we demonstrate via natural experiment that our proposed tests detect changes that correlate sensitively, specifically, and significantly with a real exogenous event. As far as we are aware, TDKPS is the first principled framework for monitoring behavioral dynamics in black-box multi-agent systems -- a critical capability as generative agent deployment continues to scale.

