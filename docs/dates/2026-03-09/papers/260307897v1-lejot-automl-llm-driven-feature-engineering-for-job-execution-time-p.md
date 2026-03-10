---
layout: default
title: LeJOT-AutoML: LLM-Driven Feature Engineering for Job Execution Time Prediction in Databricks Cost Optimization
---

# LeJOT-AutoML: LLM-Driven Feature Engineering for Job Execution Time Prediction in Databricks Cost Optimization
**arXiv**：[2603.07897v1](https://arxiv.org/abs/2603.07897) · [PDF](https://arxiv.org/pdf/2603.07897.pdf)  
**作者**：Lizhi Ma, Yi-Xiang Hu, Yihui Ren, Feng Wu, Xiang-Yang Li  

**一句话要点**：提出LeJOT-AutoML框架，利用LLM代理自动化特征工程以优化Databricks作业执行时间预测与成本。

**关键词**：作业执行时间预测, 自动化特征工程, 大语言模型代理, 成本优化, Databricks

## 3 点简述
- 核心问题：现有方法依赖静态手动特征，难以捕捉运行时效应，导致预测不准确和工程开销大。
- 方法要点：结合检索增强生成与工具链，分析作业工件，自动合成和验证特征提取代码。
- 实验或效果：在企业负载上，特征工程循环从数周缩短至20-30分钟，部署中实现19.01%的成本节省。

## 摘要（原文）

> Databricks job orchestration systems (e.g., LeJOT) reduce cloud costs by selecting low-priced compute configurations while meeting latency and dependency constraints. Accurate execution-time prediction under heterogeneous instance types and non-stationary runtime conditions is therefore critical. Existing pipelines rely on static, manually engineered features that under-capture runtime effects (e.g., partition pruning, data skew, and shuffle amplification), and predictive signals are scattered across logs, metadata, and job scripts-lengthening update cycles and increasing engineering overhead. We present LeJOT-AutoML, an agent-driven AutoML framework that embeds large language model agents throughout the ML lifecycle. LeJOT-AutoML combines retrieval-augmented generation over a domain knowledge base with a Model Context Protocol toolchain (log parsers, metadata queries, and a read-only SQL sandbox) to analyze job artifacts, synthesize and validate feature-extraction code via safety gates, and train/select predictors. This design materializes runtime-derived features that are difficult to obtain through static analysis alone. On enterprise Databricks workloads, LeJOT-AutoML generates over 200 features and reduces the feature-engineering and evaluation loop from weeks to 20-30 minutes, while maintaining competitive prediction accuracy. Integrated into the LeJOT pipeline, it enables automated continuous model updates and achieves 19.01% cost savings in our deployment setting through improved orchestration.

