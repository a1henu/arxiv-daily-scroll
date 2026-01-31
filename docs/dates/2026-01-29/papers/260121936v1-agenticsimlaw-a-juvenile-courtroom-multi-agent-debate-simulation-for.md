---
layout: default
title: AgenticSimLaw: A Juvenile Courtroom Multi-Agent Debate Simulation for Explainable High-Stakes Tabular Decision Making
---

# AgenticSimLaw: A Juvenile Courtroom Multi-Agent Debate Simulation for Explainable High-Stakes Tabular Decision Making
**arXiv**：[2601.21936v1](https://arxiv.org/abs/2601.21936) · [PDF](https://arxiv.org/pdf/2601.21936.pdf)  
**作者**：Jon Chun, Kathrine Elkins, Yong Suk Lee  

**一句话要点**：提出AgenticSimLaw多智能体辩论框架，用于高风险表格决策的透明推理

**关键词**：多智能体系统, 高风险决策, 可解释人工智能, 表格数据, 结构化辩论, 透明推理

## 3 点简述
- 核心问题：高风险表格决策任务中黑盒方法缺乏透明度和可控性，需可审计推理过程
- 方法要点：基于法庭辩论结构，定义角色、协议和策略，实现多智能体结构化辩论
- 实验或效果：在年轻成人再犯预测上，相比单智能体推理，表现更稳定且可解释性更强

## 摘要（原文）

> We introduce AgenticSimLaw, a role-structured, multi-agent debate framework that provides transparent and controllable test-time reasoning for high-stakes tabular decision-making tasks. Unlike black-box approaches, our courtroom-style orchestration explicitly defines agent roles (prosecutor, defense, judge), interaction protocols (7-turn structured debate), and private reasoning strategies, creating a fully auditable decision-making process. We benchmark this framework on young adult recidivism prediction using the NLSY97 dataset, comparing it against traditional chain-of-thought (CoT) prompting across almost 90 unique combinations of models and strategies. Our results demonstrate that structured multi-agent debate provides more stable and generalizable performance compared to single-agent reasoning, with stronger correlation between accuracy and F1-score metrics. Beyond performance improvements, AgenticSimLaw offers fine-grained control over reasoning steps, generates complete interaction transcripts for explainability, and enables systematic profiling of agent behaviors. While we instantiate this framework in the criminal justice domain to stress-test reasoning under ethical complexity, the approach generalizes to any deliberative, high-stakes decision task requiring transparency and human oversight. This work addresses key LLM-based multi-agent system challenges: organization through structured roles, observability through logged interactions, and responsibility through explicit non-deployment constraints for sensitive domains. Data, results, and code will be available on github.com under the MIT license.

