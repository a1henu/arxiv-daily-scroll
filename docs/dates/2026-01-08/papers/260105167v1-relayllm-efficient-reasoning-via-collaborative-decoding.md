---
layout: default
title: RelayLLM: Efficient Reasoning via Collaborative Decoding
---

# RelayLLM: Efficient Reasoning via Collaborative Decoding
**arXiv**：[2601.05167v1](https://arxiv.org/abs/2601.05167) · [PDF](https://arxiv.org/pdf/2601.05167.pdf)  
**作者**：Chengsong Huang, Tong Zheng, Langlin Huang, Jinyuan Li, Haolin Liu, Jiaxin Huang  

**一句话要点**：提出RelayLLM框架，通过令牌级协作解码实现高效推理，解决大模型成本高与小模型能力不足的问题。

**关键词**：协作解码, 令牌级推理, 成本优化, 两阶段训练, 大语言模型, 小语言模型

## 3 点简述
- 核心问题：大语言模型推理成本高、延迟大，小语言模型推理能力不足，现有协作方法粒度粗导致计算浪费。
- 方法要点：引入令牌级协作解码，让小模型作为主动控制器，动态调用大模型处理关键令牌，采用两阶段训练框架优化策略。
- 实验或效果：在六个基准测试中平均准确率达49.52%，仅调用大模型处理1.07%令牌，成本降低98.2%。

## 摘要（原文）

> Large Language Models (LLMs) for complex reasoning is often hindered by high computational costs and latency, while resource-efficient Small Language Models (SLMs) typically lack the necessary reasoning capacity. Existing collaborative approaches, such as cascading or routing, operate at a coarse granularity by offloading entire queries to LLMs, resulting in significant computational waste when the SLM is capable of handling the majority of reasoning steps. To address this, we propose RelayLLM, a novel framework for efficient reasoning via token-level collaborative decoding. Unlike routers, RelayLLM empowers the SLM to act as an active controller that dynamically invokes the LLM only for critical tokens via a special command, effectively "relaying" the generation process. We introduce a two-stage training framework, including warm-up and Group Relative Policy Optimization (GRPO) to teach the model to balance independence with strategic help-seeking. Empirical results across six benchmarks demonstrate that RelayLLM achieves an average accuracy of 49.52%, effectively bridging the performance gap between the two models. Notably, this is achieved by invoking the LLM for only 1.07% of the total generated tokens, offering a 98.2% cost reduction compared to performance-matched random routers.

