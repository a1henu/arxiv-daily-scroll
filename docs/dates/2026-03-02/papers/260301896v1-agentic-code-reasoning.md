---
layout: default
title: Agentic Code Reasoning
---

# Agentic Code Reasoning
**arXiv**：[2603.01896v1](https://arxiv.org/abs/2603.01896) · [PDF](https://arxiv.org/pdf/2603.01896.pdf)  
**作者**：Shubham Ugare, Satish Chandra  

**一句话要点**：提出半形式化推理方法，以提升LLM代理在不执行代码时的语义分析能力。

**关键词**：代码语义推理, LLM代理, 半形式化推理, 静态程序分析, 代码问答

## 3 点简述
- 研究LLM代理能否在不执行代码的情况下探索代码库并推理代码语义。
- 引入半形式化推理：一种结构化提示方法，要求代理构建明确前提、追踪执行路径并推导形式结论。
- 在补丁等价验证、故障定位和代码问答任务中，半形式化推理一致提高准确性，例如补丁等价验证准确率从78%提升至88%。

## 摘要（原文）

> Can LLM agents explore codebases and reason about code semantics without executing the code? We study this capability, which we call agentic code reasoning, and introduce semi-formal reasoning: a structured prompting methodology that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Unlike unstructured chain-of-thought, semi-formal reasoning acts as a certificate: the agent cannot skip cases or make unsupported claims. We evaluate across three tasks (patch equivalence verification, fault localization, and code question answering) and show that semi-formal reasoning consistently improves accuracy on all of them. For patch equivalence, accuracy improves from 78% to 88% on curated examples and reaches 93% on real-world agent-generated patches, approaching the reliability needed for execution-free RL reward signals. For code question answering on RubberDuckBench Mohammad et al. (2026), semi-formal reasoning achieves 87% accuracy. For fault localization on Defects4J Just et al. (2014), semi-formal reasoning improves Top-5 accuracy by 5 percentage points over standard reasoning. These results demonstrate that structured agentic reasoning enables meaningful semantic code analysis without execution, opening practical applications in RL training pipelines, code review, and static program analysis.

