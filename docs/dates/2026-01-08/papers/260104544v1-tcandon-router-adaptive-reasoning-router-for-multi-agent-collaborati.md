---
layout: default
title: TCAndon-Router: Adaptive Reasoning Router for Multi-Agent Collaboration
---

# TCAndon-Router: Adaptive Reasoning Router for Multi-Agent Collaboration
**arXiv**：[2601.04544v1](https://arxiv.org/abs/2601.04544) · [PDF](https://arxiv.org/pdf/2601.04544.pdf)  
**作者**：Jiuzhou Zhao, Chunrong Chen, Chenqi Qiao, Lebin Zheng, Minqi Han, Yanchi Liu Yongzhou Xu Xiaochuan Xu Min Zhang  

**一句话要点**：提出TCAndon-Router以解决多智能体系统中动态集成与路由冲突问题

**关键词**：多智能体系统, 自适应路由, 协作推理, 动态集成, 任务路由

## 3 点简述
- 核心问题：现有任务路由依赖静态单标签决策，难以集成新智能体且易因能力重叠引发冲突
- 方法要点：支持动态智能体集成，通过自然语言推理链预测候选智能体集，并设计协作执行流程
- 实验或效果：在公共数据集和企业数据上显著提升路由准确性、减少冲突，并在模糊场景中保持鲁棒性

## 摘要（原文）

> Multi-Agent Systems(MAS) have become a powerful paradigm for building high performance intelligent applications. Within these systems, the router responsible for determining which expert agents should handle a given query plays a crucial role in overall performance. Existing routing strategies generally fall into two categories: performance routing, which balances latency and cost across models of different sizes, and task routing, which assigns queries to domain-specific experts to improve accuracy. In real-world enterprise applications, task routing is more suitable; however, most existing approaches rely on static single-label decisions, which introduce two major limitations: (i) difficulty in seamlessly integrating new agents as business domains expand, and (ii) routing conflicts caused by overlapping agent capabilities, ultimately degrading accuracy and robustness.To address these challenges, we propose TCAndon-Router(TCAR): an adaptive reasoning router for multi-agent collaboration. Unlike traditional routers, TCAR supports dynamic agent onboarding and first generates a natural-language reasoning chain before predicting a set of candidate agents capable of handling the query. In addition, we design a collaborative execution pipeline in which selected agents independently produce responses, which are then aggregated and refined into a single high-quality response by a dedicated Refining Agent.Experiments on public datasets and real enterprise data demonstrate that TCAR significantly improves routing accuracy, reduces routing conflicts, and remains robust in ambiguous scenarios. We have released TCAR at https://huggingface.co/tencent/TCAndon-Router to support future research on explainable and collaborative multi-agent routing.

