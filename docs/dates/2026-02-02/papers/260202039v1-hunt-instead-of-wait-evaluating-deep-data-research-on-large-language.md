---
layout: default
title: Hunt Instead of Wait: Evaluating Deep Data Research on Large Language Models
---

# Hunt Instead of Wait: Evaluating Deep Data Research on Large Language Models
**arXiv**：[2602.02039v1](https://arxiv.org/abs/2602.02039) · [PDF](https://arxiv.org/pdf/2602.02039.pdf)  
**作者**：Wei Liu, Peijie Yu, Michele Orini, Yali Du, Yulan He  

**一句话要点**：提出Deep Data Research任务与DDR-Bench基准，评估大语言模型在数据科学中的自主探索能力。

**关键词**：大语言模型, 自主探索, 数据科学, 调查智能, 基准评估, 开放任务

## 3 点简述
- 核心问题：现有基准缺乏对大语言模型在数据科学中自主探索能力的评估，需区分调查智能与执行智能。
- 方法要点：引入Deep Data Research开放任务，让模型从数据库自主提取关键洞察，并开发基于检查表的DDR-Bench基准进行可验证评估。
- 实验或效果：前沿模型显示出初步自主性，但长期探索仍具挑战，有效调查智能依赖内在策略而非仅靠代理框架或规模扩展。

## 摘要（原文）

> The agency expected of Agentic Large Language Models goes beyond answering correctly, requiring autonomy to set goals and decide what to explore. We term this investigatory intelligence, distinguishing it from executional intelligence, which merely completes assigned tasks. Data Science provides a natural testbed, as real-world analysis starts from raw data rather than explicit queries, yet few benchmarks focus on it. To address this, we introduce Deep Data Research (DDR), an open-ended task where LLMs autonomously extract key insights from databases, and DDR-Bench, a large-scale, checklist-based benchmark that enables verifiable evaluation. Results show that while frontier models display emerging agency, long-horizon exploration remains challenging. Our analysis highlights that effective investigatory intelligence depends not only on agent scaffolding or merely scaling, but also on intrinsic strategies of agentic models.

