---
layout: default
title: From Static Benchmarks to Dynamic Protocol: Agent-Centric Text Anomaly Detection for Evaluating LLM Reasoning
---

# From Static Benchmarks to Dynamic Protocol: Agent-Centric Text Anomaly Detection for Evaluating LLM Reasoning
**arXiv**：[2602.23729v1](https://arxiv.org/abs/2602.23729) · [PDF](https://arxiv.org/pdf/2602.23729.pdf)  
**作者**：Seungdong Yoa, Sanghyu Yoon, Suhee Yoon, Dongmin Kim, Ye Seul Sim, Junhyun Lee, Woohyung Lim  

**一句话要点**：提出基于智能体的动态协议以评估大语言模型推理能力，替代静态基准测试

**关键词**：智能体基准测试, 动态评估协议, 文本异常检测, 大语言模型推理, 自动难度扩展

## 3 点简述
- 核心问题：静态数据集评估大语言模型存在可扩展性限制，无法捕捉模型推理能力的动态演变
- 方法要点：引入教师、协调者和学生智能体，通过迭代生成、验证和解决问题实现动态基准测试
- 实验或效果：该协议能系统暴露传统基准测试未揭示的推理错误，支持难度自动扩展

## 摘要（原文）

> The evaluation of large language models (LLMs) has predominantly relied on static datasets, which offer limited scalability and fail to capture the evolving reasoning capabilities of recent models. To overcome these limitations, we propose an agent-centric benchmarking paradigm that moves beyond static datasets by introducing a dynamic protocol in which autonomous agents iteratively generate, validate, and solve problems. Within this protocol, a teacher agent generates candidate problems, an orchestrator agent rigorously verifies their validity and guards against adversarial attacks, and a student agent attempts to solve the validated problems. An invalid problem is revised by the teacher agent until it passes validation. If the student correctly solves the problem, the orchestrator prompts the teacher to generate more challenging variants. Consequently, the benchmark scales in difficulty automatically as more capable agents are substituted into any role, enabling progressive evaluation of large language models without manually curated datasets. Adopting text anomaly detection as our primary evaluation format, which demands cross-sentence logical inference and resists pattern-matching shortcuts, we demonstrate that this protocol systematically exposes corner-case reasoning errors that conventional benchmarks fail to reveal. We further advocate evaluating systems along several complementary axes including cross-model pairwise performance and progress between the initial and orchestrator-finalized problems. By shifting the focus from fixed datasets to dynamic protocols, our approach offers a sustainable direction for evaluating ever-evolving language models and introduces a research agenda centered on the co-evolution of agent-centric benchmarks.

