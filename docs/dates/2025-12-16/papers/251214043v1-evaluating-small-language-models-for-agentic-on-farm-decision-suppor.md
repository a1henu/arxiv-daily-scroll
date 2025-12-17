---
layout: default
title: Evaluating Small Language Models for Agentic On-Farm Decision Support Systems
---

# Evaluating Small Language Models for Agentic On-Farm Decision Support Systems
**arXiv**：[2512.14043v1](https://arxiv.org/abs/2512.14043) · [PDF](https://arxiv.org/pdf/2512.14043.pdf)  
**作者**：Enhong Liu, Haiyu Yang, Miel Hostens  

**一句话要点**：评估小型语言模型用于乳业农场决策支持系统的可行性，强调隐私与计算效率。

**关键词**：小型语言模型, 乳业决策支持, 本地部署, 隐私保护, 计算效率, 代理系统

## 3 点简述
- 核心问题：大型语言模型计算需求高，难以在农场本地部署，限制了乳业决策支持工具的实际应用。
- 方法要点：在农场现实计算约束下，对20个开源小型语言模型进行基准测试，并构建集成五个任务特定代理的AI系统。
- 实验或效果：通过两阶段评估，Qwen-4B在多数任务中表现优异，但NoSQL数据库交互稳定性未知，显示小型语言模型在乳业部署的潜力与挑战。

## 摘要（原文）

> Large Language Models (LLM) hold potential to support dairy scholars and farmers by supporting decision-making and broadening access to knowledge for stakeholders with limited technical expertise. However, the substantial computational demand restricts access to LLM almost exclusively through cloud-based service, which makes LLM-based decision support tools impractical for dairy farming. To address this gap, lightweight alternatives capable of running locally on farm hardware are required. In this work, we benchmarked 20 open-source Small Language Models (SLM) available on HuggingFace under farm-realistic computing constraints. Building on our prior work, we developed an agentic AI system that integrates five task-specific agents: literature search, web search, SQL database interaction, NoSQL database interaction, and graph generation following predictive models. Evaluation was conducted in two phases. In the first phase, five test questions were used for the initial screening to identify models capable of following basic dairy-related instructions and performing reliably in a compute-constrained environment. Models that passed this preliminary stage were then evaluated using 30 questions (five per task category mentioned above, plus one category addressing integrity and misconduct) in phase two. In results, Qwen-4B achieved superior performance across most of task categories, although showed unstable effectiveness in NoSQL database interactions through PySpark. To our knowledge, this is the first work explicitly evaluating the feasibility of SLM as engines for dairy farming decision-making, with central emphases on privacy and computational efficiency. While results highlight the promise of SLM-assisted tools for practical deployment in dairy farming, challenges remain, and fine-tuning is still needed to refine SLM performance in dairy-specific questions.

