---
layout: default
title: Action Hallucination in Generative Visual-Language-Action Models
---

# Action Hallucination in Generative Visual-Language-Action Models
**arXiv**：[2602.06339v1](https://arxiv.org/abs/2602.06339) · [PDF](https://arxiv.org/pdf/2602.06339.pdf)  
**作者**：Harold Soh, Eugene Lim  

**一句话要点**：分析视觉-语言-动作模型中违反物理约束的动作幻觉及其扩展至计划级失败

**关键词**：动作幻觉, 视觉-语言-动作模型, 机器人基础模型, 生成式策略, 物理约束, 可靠性改进

## 3 点简述
- 核心问题：生成式视觉-语言-动作模型在机器人策略中产生违反物理约束的动作幻觉，导致计划级失败
- 方法要点：聚焦于潜在变量生成策略，识别拓扑、精度和时域三个结构不匹配障碍
- 实验或效果：为生成式机器人策略的实证失败提供机制解释，并提出改进可靠性的原则方向

## 摘要（原文）

> Robot Foundation Models such as Vision-Language-Action models are rapidly reshaping how robot policies are trained and deployed, replacing hand-designed planners with end-to-end generative action models. While these systems demonstrate impressive generalization, it remains unclear whether they fundamentally resolve the long-standing challenges of robotics. We address this question by analyzing action hallucinations that violate physical constraints and their extension to plan-level failures. Focusing on latent-variable generative policies, we show that hallucinations often arise from structural mismatches between feasible robot behavior and common model architectures. We study three such barriers -- topological, precision, and horizon -- and show how they impose unavoidable tradeoffs. Our analysis provides mechanistic explanations for reported empirical failures of generative robot policies and suggests principled directions for improving reliability and trustworthiness, without abandoning their expressive power.

