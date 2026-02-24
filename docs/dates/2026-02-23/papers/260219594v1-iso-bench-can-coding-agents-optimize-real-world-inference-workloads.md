---
layout: default
title: ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads?
---

# ISO-Bench: Can Coding Agents Optimize Real-World Inference Workloads?
**arXiv**：[2602.19594v1](https://arxiv.org/abs/2602.19594) · [PDF](https://arxiv.org/pdf/2602.19594.pdf)  
**作者**：Ayush Nangia, Shikhar Mishra, Aman Gokrani, Paras Chopra  

**一句话要点**：提出ISO-Bench基准，评估编码代理在真实推理优化任务中的能力。

**关键词**：编码代理评估, 推理优化基准, 硬软指标结合, vLLM框架, SGLang框架, 性能改进任务

## 3 点简述
- 核心问题：现有基准依赖运行时指标，易被操纵，无法全面评估编码代理的优化能力。
- 方法要点：结合硬性（执行）和软性（LLM）指标，从vLLM和SGLang框架选取54个任务。
- 实验或效果：代理常识别正确瓶颈但执行失败，不同代理表现差异大，支架设计至关重要。

## 摘要（原文）

> We introduce ISO-Bench, a benchmark for coding agents to test their capabilities on real-world inference optimization tasks. These tasks were taken from vLLM and SGLang, two of the most popular LLM serving frameworks. Each task provides an agent with a codebase and bottleneck description, whereby the agent must produce an optimization patch evaluated against expert human solutions. We curated 54 tasks from merged pull requests with measurable performance improvements. While existing benchmarks heavily use runtime-based metrics, such approaches can be gamed to pass tests without capturing the actual intent of the code changes. Therefore, we combine both hard (execution-based) and soft (LLM-based) metrics to show that both are necessary for complete evaluation. While evaluating both closed and open-source coding agents, we find no single agent dominates across codebases. Surprisingly, agents often identify correct bottlenecks but fail to execute working solutions. We also show that agents with identical underlying models differ substantially, suggesting scaffolding is as important as the model.

