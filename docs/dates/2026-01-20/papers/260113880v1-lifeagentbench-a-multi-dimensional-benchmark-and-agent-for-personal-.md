---
layout: default
title: LifeAgentBench: A Multi-dimensional Benchmark and Agent for Personal Health Assistants in Digital Health
---

# LifeAgentBench: A Multi-dimensional Benchmark and Agent for Personal Health Assistants in Digital Health
**arXiv**：[2601.13880v1](https://arxiv.org/abs/2601.13880) · [PDF](https://arxiv.org/pdf/2601.13880.pdf)  
**作者**：Ye Tian, Zihao Wang, Onat Gungor, Xiaoran Fan, Tajana Rosing  

**一句话要点**：提出LifeAgentBench基准与LifeAgent代理，以评估和提升数字健康中个人健康助手的多维度推理能力。

**关键词**：数字健康, 长时程推理, 跨维度推理, 基准评估, 健康助手代理, 多用户分析

## 3 点简述
- 核心问题：缺乏系统基准评估LLM在长时程、跨维度生活方式健康推理中的能力。
- 方法要点：构建大规模QA基准LifeAgentBench，并设计LifeAgent代理集成多步证据检索与确定性聚合。
- 实验或效果：评估11个LLM，LifeAgent相比基线有显著改进，案例展示实际应用潜力。

## 摘要（原文）

> Personalized digital health support requires long-horizon, cross-dimensional reasoning over heterogeneous lifestyle signals, and recent advances in mobile sensing and large language models (LLMs) make such support increasingly feasible. However, the capabilities of current LLMs in this setting remain unclear due to the lack of systematic benchmarks. In this paper, we introduce LifeAgentBench, a large-scale QA benchmark for long-horizon, cross-dimensional, and multi-user lifestyle health reasoning, containing 22,573 questions spanning from basic retrieval to complex reasoning. We release an extensible benchmark construction pipeline and a standardized evaluation protocol to enable reliable and scalable assessment of LLM-based health assistants. We then systematically evaluate 11 leading LLMs on LifeAgentBench and identify key bottlenecks in long-horizon aggregation and cross-dimensional reasoning. Motivated by these findings, we propose LifeAgent as a strong baseline agent for health assistant that integrates multi-step evidence retrieval with deterministic aggregation, achieving significant improvements compared with two widely used baselines. Case studies further demonstrate its potential in realistic daily-life scenarios. The benchmark is publicly available at https://anonymous.4open.science/r/LifeAgentBench-CE7B.

