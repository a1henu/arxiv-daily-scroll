---
layout: default
title: Rules or Weights? Comparing User Understanding of Explainable AI Techniques with the Cognitive XAI-Adaptive Model
---

# Rules or Weights? Comparing User Understanding of Explainable AI Techniques with the Cognitive XAI-Adaptive Model
**arXiv**：[2602.19620v1](https://arxiv.org/abs/2602.19620) · [PDF](https://arxiv.org/pdf/2602.19620.pdf)  
**作者**：Louth Bin Rawshan, Zhuoyu Wang, Brian Y Lim  

**一句话要点**：提出CoXAM认知模型以比较规则与权重XAI技术的可解释性，基于用户研究验证其对齐人类决策。

**关键词**：可解释人工智能, 认知模型, 用户研究, 规则解释, 权重解释, 决策任务

## 3 点简述
- 核心问题：规则与权重XAI技术缺乏认知框架比较可解释性，影响选择与应用。
- 方法要点：提出CoXAM模型，编码属性、权重和规则，通过计算理性选择推理过程。
- 实验或效果：验证研究显示CoXAM比基线模型更对齐人类决策，解释关键实证发现如任务难度差异。

## 摘要（原文）

> Rules and Weights are popular XAI techniques for explaining AI decisions. Yet, it remains unclear how to choose between them, lacking a cognitive framework to compare their interpretability. In an elicitation user study on forward and counterfactual decision tasks, we identified 7 reasoning strategies of interpreting three XAI Schemas - weights, rules, and their hybrid. To analyze their capabilities, we propose CoXAM, a Cognitive XAI-Adaptive Model with shared memory representation to encode instance attributes, linear weights, and decision rules. CoXAM employs computational rationality to choose among reasoning processes based on the trade-off in utility and reasoning time, separately for forward or counterfactual decision tasks. In a validation study, CoXAM demonstrated a stronger alignment with human decision-making compared to baseline machine learning proxy models. The model successfully replicated and explained several key empirical findings, including that counterfactual tasks are inherently harder than forward tasks, decision tree rules are harder to recall and apply than linear weights, and the helpfulness of XAI depends on the application data context, alongside identifying which underlying reasoning strategies were most effective. With CoXAM, we contribute a cognitive basis to accelerate debugging and benchmarking disparate XAI techniques.

