---
layout: default
title: When Do Tools and Planning Help LLMs Think? A Cost- and Latency-Aware Benchmark
---

# When Do Tools and Planning Help LLMs Think? A Cost- and Latency-Aware Benchmark
**arXiv**：[2601.02663v1](https://arxiv.org/abs/2601.02663) · [PDF](https://arxiv.org/pdf/2601.02663.pdf)  
**作者**：Subha Ghoshal, Ali Al-Bustami  

**一句话要点**：提出成本与延迟感知基准，评估工具与规划在事件问答和说服生成中对LLM推理的效益

**关键词**：大型语言模型, 工具增强推理, 延迟成本基准, 事件问答, 说服生成, 代理规划

## 3 点简述
- 核心问题：工具与规划何时提升LLM推理，需权衡成本与延迟
- 方法要点：使用LangChain和LangGraph比较单次提示与规划-执行-重规划代理，配备任务特定工具
- 实验或效果：在Event-QA中工具提升准确率但延迟剧增，在CMV中单次提示最优，复杂工具导致小模型性能下降

## 摘要（原文）

> Modern large language models (LLMs) increasingly rely on inference-time planning and external tools to improve reasoning. We benchmark this behavior on two real-world settings: event-centric question answering over graph-structured knowledge (Event-QA) and persuasive response generation in Reddit ChangeMyView (CMV). Using LangChain and LangGraph, we compare a one-shot baseline against a plan--execute--replan agent equipped with task-specific tools (DBpedia SPARQL/lookup/schema exploration, Wikipedia-focused retrieval, and topical web search). We evaluate on 60 examples each from Event-QA and CMV (3 splits of 20), and report both mean end-to-end latency and per-example token cost estimates. We evaluate GPT-4o and GPT-4o-mini under identical workflows and report accuracy and end-to-end latency. On Event-QA, the best tool-augmented configuration improves accuracy (e.g., 47.5\% $\rightarrow$ 67.5\% for GPT-4o) while increasing latency by orders of magnitude ($\sim$8s $\rightarrow$ $\sim$317s per example). On CMV, one-shot prompting is strongest (e.g., GPT-4o-mini achieves 75\% at $\sim$6s), and planning+search increases latency substantially without consistent gains. However, complex multi-tool orchestration exposes failure modes where the smaller model degrades. Overall, the findings highlight the need for task-specific, cost-aware choices of both model size and agent/tooling complexity.

