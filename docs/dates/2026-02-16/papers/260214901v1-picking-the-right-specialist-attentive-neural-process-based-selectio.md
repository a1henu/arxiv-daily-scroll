---
layout: default
title: Picking the Right Specialist: Attentive Neural Process-based Selection of Task-Specialized Models as Tools for Agentic Healthcare Systems
---

# Picking the Right Specialist: Attentive Neural Process-based Selection of Task-Specialized Models as Tools for Agentic Healthcare Systems
**arXiv**：[2602.14901v1](https://arxiv.org/abs/2602.14901) · [PDF](https://arxiv.org/pdf/2602.14901.pdf)  
**作者**：Pramit Saha, Joshua Strong, Mohammad Alsharid, Divyanshu Mishra, J. Alison Noble  

**一句话要点**：提出ToolSelect以解决医疗代理系统中任务专用模型选择问题

**关键词**：医疗代理系统, 模型选择, Attentive Neural Process, 胸部X光环境, 任务专用模型, 基准测试

## 3 点简述
- 核心问题：医疗代理系统中，任务专用模型多样，需为查询选择最优模型，但缺乏标准测试环境。
- 方法要点：基于Attentive Neural Process，通过最小化任务条件选择损失的代理风险，自适应学习模型选择。
- 实验或效果：在ToolSelectBench基准上，ToolSelect在四种任务家族中优于10种SOTA方法。

## 摘要（原文）

> Task-specialized models form the backbone of agentic healthcare systems, enabling the agents to answer clinical queries across tasks such as disease diagnosis, localization, and report generation. Yet, for a given task, a single "best" model rarely exists. In practice, each task is better served by multiple competing specialist models where different models excel on different data samples. As a result, for any given query, agents must reliably select the right specialist model from a heterogeneous pool of tool candidates. To this end, we introduce ToolSelect, which adaptively learns model selection for tools by minimizing a population risk over sampled specialist tool candidates using a consistent surrogate of the task-conditional selection loss. Concretely, we propose an Attentive Neural Process-based selector conditioned on the query and per-model behavioral summaries to choose among the specialist models. Motivated by the absence of any established testbed, we, for the first time, introduce an agentic Chest X-ray environment equipped with a diverse suite of task-specialized models (17 disease detection, 19 report generation, 6 visual grounding, and 13 VQA) and develop ToolSelectBench, a benchmark of 1448 queries. Our results demonstrate that ToolSelect consistently outperforms 10 SOTA methods across four different task families.

