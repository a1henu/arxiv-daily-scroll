---
layout: default
title: Interpreting Emergent Extreme Events in Multi-Agent Systems
---

# Interpreting Emergent Extreme Events in Multi-Agent Systems
**arXiv**：[2601.20538v1](https://arxiv.org/abs/2601.20538) · [PDF](https://arxiv.org/pdf/2601.20538.pdf)  
**作者**：Ling Tang, Jilin Mei, Dongrui Liu, Chen Qian, Dawei Cheng, Jing Shao, Xia Hu  

**一句话要点**：提出首个框架以解释多智能体系统中的涌现极端事件，基于Shapley值进行归因分析。

**关键词**：多智能体系统, 涌现现象, 极端事件解释, Shapley值, 风险归因, 系统安全

## 3 点简述
- 核心问题：多智能体系统中涌现极端事件的起源难以解释，影响系统安全。
- 方法要点：采用Shapley值将极端事件归因于智能体在不同时间步的动作，量化时间、智能体和行为的风险贡献。
- 实验或效果：在多种场景（经济、金融、社会）中验证框架有效性，提供对极端现象涌现的通用见解。

## 摘要（原文）

> Large language model-powered multi-agent systems have emerged as powerful tools for simulating complex human-like systems. The interactions within these systems often lead to extreme events whose origins remain obscured by the black box of emergence. Interpreting these events is critical for system safety. This paper proposes the first framework for explaining emergent extreme events in multi-agent systems, aiming to answer three fundamental questions: When does the event originate? Who drives it? And what behaviors contribute to it? Specifically, we adapt the Shapley value to faithfully attribute the occurrence of extreme events to each action taken by agents at different time steps, i.e., assigning an attribution score to the action to measure its influence on the event. We then aggregate the attribution scores along the dimensions of time, agent, and behavior to quantify the risk contribution of each dimension. Finally, we design a set of metrics based on these contribution scores to characterize the features of extreme events. Experiments across diverse multi-agent system scenarios (economic, financial, and social) demonstrate the effectiveness of our framework and provide general insights into the emergence of extreme phenomena.

