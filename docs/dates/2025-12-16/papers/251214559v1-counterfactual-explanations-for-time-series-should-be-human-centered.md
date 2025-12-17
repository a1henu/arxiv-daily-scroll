---
layout: default
title: Counterfactual Explanations for Time Series Should be Human-Centered and Temporally Coherent in Interventions
---

# Counterfactual Explanations for Time Series Should be Human-Centered and Temporally Coherent in Interventions
**arXiv**：[2512.14559v1](https://arxiv.org/abs/2512.14559) · [PDF](https://arxiv.org/pdf/2512.14559.pdf)  
**作者**：Emmanuel C. Chukwu, Rianne M. Schouten, Monique Tabak, Mykola Pechenizkiy  

**一句话要点**：提出面向临床的时间序列反事实解释方法，强调干预的因果合理性与时间连贯性

**关键词**：反事实解释, 时间序列分类, 临床推荐系统, 干预可行性, 时间连贯性, 鲁棒性分析

## 3 点简述
- 核心问题：现有时间序列反事实解释方法基于静态假设，忽略临床干预的持续性与可行性
- 方法要点：倡导生成目标导向、因果合理且时间连贯的反事实，以匹配临床推理和患者动态
- 实验或效果：通过鲁棒性分析显示现有方法对随机噪声敏感，可靠性有限

## 摘要（原文）

> Counterfactual explanations are increasingly proposed as interpretable mechanisms to achieve algorithmic recourse. However, current counterfactual techniques for time series classification are predominantly designed with static data assumptions and focus on generating minimal input perturbations to flip model predictions. This paper argues that such approaches are fundamentally insufficient in clinical recommendation settings, where interventions unfold over time and must be causally plausible and temporally coherent. We advocate for a shift towards counterfactuals that reflect sustained, goal-directed interventions aligned with clinical reasoning and patient-specific dynamics. We identify critical gaps in existing methods that limit their practical applicability, specifically, temporal blind spots and the lack of user-centered considerations in both method design and evaluation metrics. To support our position, we conduct a robustness analysis of several state-of-the-art methods for time series and show that the generated counterfactuals are highly sensitive to stochastic noise. This finding highlights their limited reliability in real-world clinical settings, where minor measurement variations are inevitable. We conclude by calling for methods and evaluation frameworks that go beyond mere prediction changes without considering feasibility or actionability. We emphasize the need for actionable, purpose-driven interventions that are feasible in real-world contexts for the users of such applications.

