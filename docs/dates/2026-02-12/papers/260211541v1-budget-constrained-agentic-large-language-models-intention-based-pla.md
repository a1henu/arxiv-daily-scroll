---
layout: default
title: Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use
---

# Budget-Constrained Agentic Large Language Models: Intention-Based Planning for Costly Tool Use
**arXiv**：[2602.11541v1](https://arxiv.org/abs/2602.11541) · [PDF](https://arxiv.org/pdf/2602.11541.pdf)  
**作者**：Hanbing Liu, Chunhao Tian, Nan An, Ziyuan Wang, Pinyan Lu, Changyuan Yu, Qi Qi  

**一句话要点**：提出INTENT框架，通过意图感知分层世界模型解决预算约束下大语言模型工具调用的规划问题。

**关键词**：预算约束工具调用, 推理时规划, 意图感知世界模型, 大语言模型代理, 成本校准, 多步任务求解

## 3 点简述
- 核心问题：大语言模型在多步任务中需调用外部工具，面临严格预算约束、状态-动作空间巨大及执行随机性等挑战。
- 方法要点：基于意图感知分层世界模型进行推理时规划，预测未来工具使用和风险校准成本，在线指导决策。
- 实验或效果：在成本增强的StableToolBench上，INTENT严格保证预算可行性，显著提升任务成功率，对动态市场变化保持鲁棒性。

## 摘要（原文）

> We study budget-constrained tool-augmented agents, where a large language model must solve multi-step tasks by invoking external tools under a strict monetary budget. We formalize this setting as sequential decision making in context space with priced and stochastic tool executions, making direct planning intractable due to massive state-action spaces, high variance of outcomes and prohibitive exploration cost. To address these challenges, we propose INTENT, an inference-time planning framework that leverages an intention-aware hierarchical world model to anticipate future tool usage, risk-calibrated cost, and guide decisions online. Across cost-augmented StableToolBench, INTENT strictly enforces hard budget feasibility while substantially improving task success over baselines, and remains robust under dynamic market shifts such as tool price changes and varying budgets.

