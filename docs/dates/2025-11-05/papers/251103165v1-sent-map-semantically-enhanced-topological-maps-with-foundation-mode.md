---
layout: default
title: SENT Map - Semantically Enhanced Topological Maps with Foundation Models
---

# SENT Map - Semantically Enhanced Topological Maps with Foundation Models
**arXiv**：[2511.03165v1](https://arxiv.org/abs/2511.03165) · [PDF](https://arxiv.org/pdf/2511.03165.pdf)  
**作者**：Raj Surya Rajendran Kathirvel, Zach A Chavis, Stephen J. Guy, Karthik Desingh  

**一句话要点**：提出SENT-Map以支持室内自主导航与操作，利用基础模型增强语义表示。

**关键词**：语义地图, 基础模型, 自主导航, 室内环境, 自然语言规划

## 3 点简述
- 核心问题：室内环境语义表示不足，影响机器人导航与操作。
- 方法要点：采用两阶段框架，先视觉映射，再基于JSON文本进行自然语言规划。
- 实验或效果：语义增强使小型本地部署基础模型能成功规划室内环境。

## 摘要（原文）

> We introduce SENT-Map, a semantically enhanced topological map for
> representing indoor environments, designed to support autonomous navigation and
> manipulation by leveraging advancements in foundational models (FMs). Through
> representing the environment in a JSON text format, we enable semantic
> information to be added and edited in a format that both humans and FMs
> understand, while grounding the robot to existing nodes during planning to
> avoid infeasible states during deployment. Our proposed framework employs a two
> stage approach, first mapping the environment alongside an operator with a
> Vision-FM, then using the SENT-Map representation alongside a natural-language
> query within an FM for planning. Our experimental results show that
> semantic-enhancement enables even small locally-deployable FMs to successfully
> plan over indoor environments.

