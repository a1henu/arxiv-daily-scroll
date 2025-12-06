---
layout: default
title: GovBench: Benchmarking LLM Agents for Real-World Data Governance Workflows
---

# GovBench: Benchmarking LLM Agents for Real-World Data Governance Workflows
**arXiv**：[2512.04416v1](https://arxiv.org/abs/2512.04416) · [PDF](https://arxiv.org/pdf/2512.04416.pdf)  
**作者**：Zhou Liu, Zhaoyang Han, Guochen Yan, Hao Liang, Bohan Zeng, Xing Chen, Yuanfeng Song, Wentao Zhang  

**一句话要点**：提出GovBench基准与DataGovAgent框架以解决LLM在真实数据治理工作流中的自动化挑战

**关键词**：数据治理基准, LLM代理, 工作流自动化, 反向目标方法, 规划-执行-评估架构, 错误纠正机制

## 3 点简述
- 核心问题：现有基准未覆盖数据治理的独特挑战，如确保数据正确性与质量。
- 方法要点：引入GovBench基准，采用反向目标方法合成噪声，并设计DataGovAgent框架集成规划与调试。
- 实验或效果：DataGovAgent显著提升复杂任务平均分，并减少调试迭代超过77.9%。

## 摘要（原文）

> Data governance ensures data quality, security, and compliance through policies and standards, a critical foundation for scaling modern AI development. Recently, large language models (LLMs) have emerged as a promising solution for automating data governance by translating user intent into executable transformation code. However, existing benchmarks for automated data science often emphasize snippet-level coding or high-level analytics, failing to capture the unique challenge of data governance: ensuring the correctness and quality of the data itself. To bridge this gap, we introduce GovBench, a benchmark featuring 150 diverse tasks grounded in real-world scenarios, built on data from actual cases. GovBench employs a novel "reversed-objective" methodology to synthesize realistic noise and utilizes rigorous metrics to assess end-to-end pipeline reliability. Our analysis on GovBench reveals that current models struggle with complex, multi-step workflows and lack robust error-correction mechanisms. Consequently, we propose DataGovAgent, a framework utilizing a Planner-Executor-Evaluator architecture that integrates constraint-based planning, retrieval-augmented generation, and sandboxed feedback-driven debugging. Experimental results show that DataGovAgent significantly boosts the Average Task Score (ATS) on complex tasks from 39.7 to 54.9 and reduces debugging iterations by over 77.9 percent compared to general-purpose baselines.

