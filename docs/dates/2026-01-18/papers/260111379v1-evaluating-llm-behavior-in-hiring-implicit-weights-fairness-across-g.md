---
layout: default
title: Evaluating LLM Behavior in Hiring: Implicit Weights, Fairness Across Groups, and Alignment with Human Preferences
---

# Evaluating LLM Behavior in Hiring: Implicit Weights, Fairness Across Groups, and Alignment with Human Preferences
**arXiv**：[2601.11379v1](https://arxiv.org/abs/2601.11379) · [PDF](https://arxiv.org/pdf/2601.11379.pdf)  
**作者**：Morgane Hoffmann, Emma Jouffroy, Warren Jouanneau, Marc Palyart, Charles Pebereau  

**一句话要点**：提出评估框架以分析大语言模型在招聘中的决策逻辑与公平性

**关键词**：大语言模型评估, 招聘决策分析, 公平性研究, 全因子设计, 合成数据集

## 3 点简述
- 核心问题：大语言模型在招聘中如何权衡属性，是否符合经济原则或人类偏好
- 方法要点：基于经济方法构建合成数据集，应用全因子设计估计模型权重
- 实验或效果：模型优先核心生产力信号，但存在跨群体权重差异，平均歧视最小

## 摘要（原文）

> General-purpose Large Language Models (LLMs) show significant potential in recruitment applications, where decisions require reasoning over unstructured text, balancing multiple criteria, and inferring fit and competence from indirect productivity signals. Yet, it is still uncertain how LLMs assign importance to each attribute and whether such assignments are in line with economic principles, recruiter preferences or broader societal norms. We propose a framework to evaluate an LLM's decision logic in recruitment, by drawing on established economic methodologies for analyzing human hiring behavior. We build synthetic datasets from real freelancer profiles and project descriptions from a major European online freelance marketplace and apply a full factorial design to estimate how a LLM weighs different match-relevant criteria when evaluating freelancer-project fit. We identify which attributes the LLM prioritizes and analyze how these weights vary across project contexts and demographic subgroups. Finally, we explain how a comparable experimental setup could be implemented with human recruiters to assess alignment between model and human decisions. Our findings reveal that the LLM weighs core productivity signals, such as skills and experience, but interprets certain features beyond their explicit matching value. While showing minimal average discrimination against minority groups, intersectional effects reveal that productivity signals carry different weights between demographic groups.

