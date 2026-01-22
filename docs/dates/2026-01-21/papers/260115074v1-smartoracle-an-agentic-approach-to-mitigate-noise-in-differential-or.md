---
layout: default
title: SmartOracle -- An Agentic Approach to Mitigate Noise in Differential Oracles
---

# SmartOracle -- An Agentic Approach to Mitigate Noise in Differential Oracles
**arXiv**：[2601.15074v1](https://arxiv.org/abs/2601.15074) · [PDF](https://arxiv.org/pdf/2601.15074.pdf)  
**作者**：Srinath Srinivasan, Tim Menzies, Marcelo D'Amorim  

**一句话要点**：提出SmartOracle，通过代理架构缓解JavaScript差分测试中的噪声问题

**关键词**：差分测试, JavaScript引擎, 代理系统, LLM应用, 噪声缓解, 软件测试

## 3 点简述
- 差分测试JavaScript时，手动构建预言机成本高且易产生误报
- SmartOracle使用LLM子代理分解工作流，综合终端运行和规范查询证据
- 在历史基准测试中，召回率达0.84，误报率18%，分析时间减少4倍

## 摘要（原文）

> Differential fuzzers detect bugs by executing identical inputs across distinct implementations of the same specification, such as JavaScript interpreters. Validating the outputs requires an oracle and for differential testing of JavaScript, these are constructed manually, making them expensive, time-consuming, and prone to false positives. Worse, when the specification evolves, this manual effort must be repeated.
>   Inspired by the success of agentic systems in other SE domains, this paper introduces SmartOracle. SmartOracle decomposes the manual triage workflow into specialized Large Language Model (LLM) sub-agents. These agents synthesize independently gathered evidence from terminal runs and targeted specification queries to reach a final verdict.
>   For historical benchmarks, SmartOracle achieves 0.84 recall with an 18% false positive rate. Compared to a sequential Gemini 2.5 Pro baseline, it improves triage accuracy while reducing analysis time by 4$\times$ and API costs by 10$\times$. In active fuzzing campaigns, SmartOracle successfully identified and reported previously unknown specification-level issues across major engines, including bugs in V8, JavaScriptCore, and GraalJS.
>   The success of SmartOracle's agentic architecture on Javascript suggests it might be useful other software systems- a research direction we will explore in future work.

