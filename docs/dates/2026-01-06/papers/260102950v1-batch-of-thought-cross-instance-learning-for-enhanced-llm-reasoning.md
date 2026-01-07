---
layout: default
title: Batch-of-Thought: Cross-Instance Learning for Enhanced LLM Reasoning
---

# Batch-of-Thought: Cross-Instance Learning for Enhanced LLM Reasoning
**arXiv**：[2601.02950v1](https://arxiv.org/abs/2601.02950) · [PDF](https://arxiv.org/pdf/2601.02950.pdf)  
**作者**：Xuan Yang, Furong Jia, Roy Xie, Xiong Xi, Hengwei Bian, Jian Li, Monica Agrawal  

**一句话要点**：提出Batch-of-Thought方法，通过跨实例学习提升大语言模型推理能力

**关键词**：大语言模型推理, 跨实例学习, 批量处理, 多代理系统, 推理优化

## 3 点简述
- 当前大语言模型推理系统独立处理查询，忽略跨实例信号如共享推理模式和一致性约束。
- Batch-of-Thought是一种无需训练的方法，联合处理相关查询以启用跨实例学习，包括识别高质量推理模板和错误检测。
- 实验表明，在多代理反射架构中，该方法能提高准确性和置信度校准，并降低推理成本达61%。

## 摘要（原文）

> Current Large Language Model reasoning systems process queries independently, discarding valuable cross-instance signals such as shared reasoning patterns and consistency constraints. We introduce Batch-of-Thought (BoT), a training-free method that processes related queries jointly to enable cross-instance learning. By performing comparative analysis across batches, BoT identifies high-quality reasoning templates, detects errors through consistency checks, and amortizes computational costs. We instantiate BoT within a multi-agent reflection architecture (BoT-R), where a Reflector performs joint evaluation to unlock mutual information gain unavailable in isolated processing. Experiments across three model families and six benchmarks demonstrate that BoT-R consistently improves accuracy and confidence calibration while reducing inference costs by up to 61%. Our theoretical and experimental analysis reveals when and why batch-aware reasoning benefits LLM systems.

