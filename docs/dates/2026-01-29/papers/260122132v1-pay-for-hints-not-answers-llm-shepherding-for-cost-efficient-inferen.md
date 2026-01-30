---
layout: default
title: Pay for Hints, Not Answers: LLM Shepherding for Cost-Efficient Inference
---

# Pay for Hints, Not Answers: LLM Shepherding for Cost-Efficient Inference
**arXiv**：[2601.22132v1](https://arxiv.org/abs/2601.22132) · [PDF](https://arxiv.org/pdf/2601.22132.pdf)  
**作者**：Ziming Dong, Hardik Sharma, Evan O'Toole, Jaya Prakash Champati, Kui Wu  

**一句话要点**：提出LLM Shepherding框架，通过LLM生成提示前缀以低成本提升SLM推理性能

**关键词**：LLM-SLM协作, 成本高效推理, 提示前缀生成, 两阶段预测, 数学推理, 代码生成

## 3 点简述
- 核心问题：LLM推理成本高，SLM成本低但准确性不足，现有方法如路由和级联处理LLM为全有或全无资源
- 方法要点：引入LLM Shepherding，仅从LLM请求短前缀（提示）提供给SLM，结合两阶段预测器决定是否需要提示及请求令牌数
- 实验或效果：在数学推理和代码生成基准测试中，成本降低42-94%，相比基线最多减少2.8倍成本，同时保持准确性

## 摘要（原文）

> Large Language Models (LLMs) deliver state-of-the-art performance on complex reasoning tasks, but their inference costs limit deployment at scale. Small Language Models (SLMs) offer dramatic cost savings yet lag substantially in accuracy. Existing approaches - routing and cascading - treat the LLM as an all-or-nothing resource: either the query bypasses the LLM entirely, or the LLM generates a complete response at full cost. We introduce LLM Shepherding, a framework that requests only a short prefix (a hint) from the LLM and provides it to SLM. This simple mechanism is surprisingly effective for math and coding tasks: even hints comprising 10-30% of the full LLM response improve SLM accuracy significantly. Shepherding generalizes both routing and cascading, and it achieves lower cost under oracle decision-making. We develop a two-stage predictor that jointly determines whether a hint is needed and how many tokens to request. On the widely-used mathematical reasoning (GSM8K, CNK12) and code generation (HumanEval, MBPP) benchmarks, Shepherding reduces costs by 42-94% relative to LLM-only inference. Compared to state-of-the-art routing and cascading baselines, shepherding delivers up to 2.8x cost reduction while matching accuracy. To our knowledge, this is the first work to exploit token-level budget control for SLM-LLM collaboration.

