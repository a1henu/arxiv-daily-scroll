---
layout: default
title: CausalReasoningBenchmark: A Real-World Benchmark for Disentangled Evaluation of Causal Identification and Estimation
---

# CausalReasoningBenchmark: A Real-World Benchmark for Disentangled Evaluation of Causal Identification and Estimation
**arXiv**：[2602.20571v1](https://arxiv.org/abs/2602.20571) · [PDF](https://arxiv.org/pdf/2602.20571.pdf)  
**作者**：Ayush Sawarni, Jiyuan Tan, Vasilis Syrgkanis  

**一句话要点**：提出CausalReasoningBenchmark以分离评估因果推理中的识别与估计步骤

**关键词**：因果推理基准, 识别与估计分离, 真实世界数据集, 结构化评估, 自动化因果推断

## 3 点简述
- 核心问题：现有基准混淆因果识别与估计，难以诊断系统失败原因
- 方法要点：基于173个真实世界查询，要求系统输出结构化识别规范和点估计
- 实验或效果：基线LLM在高级策略识别正确率84%，但完整识别规范正确率仅30%

## 摘要（原文）

> Many benchmarks for automated causal inference evaluate a system's performance based on a single numerical output, such as an Average Treatment Effect (ATE). This approach conflates two distinct steps in causal analysis: identification-formulating a valid research design under stated assumptions-and estimation-implementing that design numerically on finite data. We introduce CausalReasoningBenchmark, a benchmark of 173 queries across 138 real-world datasets, curated from 85 peer-reviewed research papers and four widely-used causal-inference textbooks. For each query a system must produce (i) a structured identification specification that names the strategy, the treatment, outcome, and control variables, and all design-specific elements, and (ii) a point estimate with a standard error. By scoring these two components separately, our benchmark enables granular diagnosis: it distinguishes failures in causal reasoning from errors in numerical execution. Baseline results with a state-of-the-art LLM show that, while the model correctly identifies the high-level strategy in 84 % of cases, full identification-specification correctness drops to only 30 %, revealing that the bottleneck lies in the nuanced details of research design rather than in computation. CausalReasoningBenchmark is publicly available on Hugging Face and is designed to foster the development of more robust automated causal-inference systems.

