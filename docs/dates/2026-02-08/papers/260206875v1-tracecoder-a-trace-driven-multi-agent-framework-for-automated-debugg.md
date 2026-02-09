---
layout: default
title: TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code
---

# TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code
**arXiv**：[2602.06875v1](https://arxiv.org/abs/2602.06875) · [PDF](https://arxiv.org/pdf/2602.06875.pdf)  
**作者**：Jiangping Huang, Wenguang Ye, Weisong Sun, Jian Zhang, Mingyue Zhang, Yang Liu  

**一句话要点**：提出TraceCoder框架，通过运行时追踪与历史学习机制，提升LLM生成代码的自动调试精度与效率。

**关键词**：代码调试, 多代理系统, 运行时追踪, 历史学习机制, LLM生成代码, 自动修复

## 3 点简述
- 核心问题：LLM生成代码常含细微错误，现有修复方法依赖浅层测试信号，难以精确定位根因且易陷入低效循环。
- 方法要点：采用多代理协作框架，结合运行时追踪、因果分析和历史教训学习机制，模拟专家观察-分析-修复过程。
- 实验或效果：在多个基准测试中，Pass@1准确率相对提升达34.43%，迭代修复过程贡献65.61%的相对增益。

## 摘要（原文）

> Large Language Models (LLMs) often generate code with subtle but critical bugs, especially for complex tasks. Existing automated repair methods typically rely on superficial pass/fail signals, offering limited visibility into program behavior and hindering precise error localization. In addition, without a way to learn from prior failures, repair processes often fall into repetitive and inefficient cycles. To overcome these challenges, we present TraceCoder, a collaborative multi-agent framework that emulates the observe-analyze-repair process of human experts. The framework first instruments the code with diagnostic probes to capture fine-grained runtime traces, enabling deep insight into its internal execution. It then conducts causal analysis on these traces to accurately identify the root cause of the failure. This process is further enhanced by a novel Historical Lesson Learning Mechanism (HLLM), which distills insights from prior failed repair attempts to inform subsequent correction strategies and prevent recurrence of similar mistakes. To ensure stable convergence, a Rollback Mechanism enforces that each repair iteration constitutes a strict improvement toward the correct solution. Comprehensive experiments across multiple benchmarks show that TraceCoder achieves up to a 34.43\% relative improvement in Pass@1 accuracy over existing advanced baselines. Ablation studies verify the significance of each system component, with the iterative repair process alone contributing a 65.61\% relative gain in accuracy. Furthermore, TraceCoder significantly outperforms leading iterative methods in terms of both accuracy and cost-efficiency.

