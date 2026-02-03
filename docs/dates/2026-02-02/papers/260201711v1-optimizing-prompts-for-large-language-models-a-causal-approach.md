---
layout: default
title: Optimizing Prompts for Large Language Models: A Causal Approach
---

# Optimizing Prompts for Large Language Models: A Causal Approach
**arXiv**：[2602.01711v1](https://arxiv.org/abs/2602.01711) · [PDF](https://arxiv.org/pdf/2602.01711.pdf)  
**作者**：Wei Chen, Yanbin Fang, Shuran Fu, Fasheng Xu, Xuan Wei  

**一句话要点**：提出因果提示优化框架，以解决企业大语言模型中提示设计不稳定和成本高的问题。

**关键词**：因果推断, 提示优化, 大语言模型, 双重机器学习, 企业部署

## 3 点简述
- 核心问题：现有提示优化方法难以适应异构查询，且依赖离线奖励模型存在混淆偏差。
- 方法要点：采用双重机器学习学习因果奖励模型，隔离提示变化与查询属性的因果效应。
- 实验或效果：在数学推理等基准测试中超越人工和自动优化方法，提升硬查询鲁棒性并降低推理成本。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly embedded in enterprise workflows, yet their performance remains highly sensitive to prompt design. Automatic Prompt Optimization (APO) seeks to mitigate this instability, but existing approaches face two persistent challenges. First, commonly used prompt strategies rely on static instructions that perform well on average but fail to adapt to heterogeneous queries. Second, more dynamic approaches depend on offline reward models that are fundamentally correlational, confounding prompt effectiveness with query characteristics. We propose Causal Prompt Optimization (CPO), a framework that reframes prompt design as a problem of causal estimation. CPO operates in two stages. First, it learns an offline causal reward model by applying Double Machine Learning (DML) to semantic embeddings of prompts and queries, isolating the causal effect of prompt variations from confounding query attributes. Second, it utilizes this unbiased reward signal to guide a resource-efficient search for query-specific prompts without relying on costly online evaluation. We evaluate CPO across benchmarks in mathematical reasoning, visualization, and data analytics. CPO consistently outperforms human-engineered prompts and state-of-the-art automated optimizers. The gains are driven primarily by improved robustness on hard queries, where existing methods tend to deteriorate. Beyond performance, CPO fundamentally reshapes the economics of prompt optimization: by shifting evaluation from real-time model execution to an offline causal model, it enables high-precision, per-query customization at a fraction of the inference cost required by online methods. Together, these results establish causal inference as a scalable foundation for reliable and cost-efficient prompt optimization in enterprise LLM deployments.

