---
layout: default
title: Using Vision Language Models as Closed-Loop Symbolic Planners for Robotic Applications: A Control-Theoretic Perspective
---

# Using Vision Language Models as Closed-Loop Symbolic Planners for Robotic Applications: A Control-Theoretic Perspective
**arXiv**：[2511.07410v1](https://arxiv.org/abs/2511.07410) · [PDF](https://arxiv.org/pdf/2511.07410.pdf)  
**作者**：Hao Wang, Sathwik Karnik, Bea Lim, Somil Bansal  

**一句话要点**：从控制理论视角研究视觉语言模型作为机器人闭环符号规划器

**关键词**：视觉语言模型, 闭环符号规划, 机器人应用, 控制理论, 规划性能优化

## 3 点简述
- 核心问题：视觉语言模型在机器人闭环符号规划中易产生不可预测错误
- 方法要点：分析控制视野和热启动对规划性能的影响
- 实验或效果：通过受控实验提出改进VLM规划器性能的建议

## 摘要（原文）

> Large Language Models (LLMs) and Vision Language Models (VLMs) have been
> widely used for embodied symbolic planning. Yet, how to effectively use these
> models for closed-loop symbolic planning remains largely unexplored. Because
> they operate as black boxes, LLMs and VLMs can produce unpredictable or costly
> errors, making their use in high-level robotic planning especially challenging.
> In this work, we investigate how to use VLMs as closed-loop symbolic planners
> for robotic applications from a control-theoretic perspective. Concretely, we
> study how the control horizon and warm-starting impact the performance of VLM
> symbolic planners. We design and conduct controlled experiments to gain
> insights that are broadly applicable to utilizing VLMs as closed-loop symbolic
> planners, and we discuss recommendations that can help improve the performance
> of VLM symbolic planners.

