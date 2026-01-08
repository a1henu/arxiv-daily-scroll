---
layout: default
title: Interleaved Tool-Call Reasoning for Protein Function Understanding
---

# Interleaved Tool-Call Reasoning for Protein Function Understanding
**arXiv**：[2601.03604v1](https://arxiv.org/abs/2601.03604) · [PDF](https://arxiv.org/pdf/2601.03604.pdf)  
**作者**：Chuanliu Fan, Zicheng Ma, Huanran Meng, Aijia Zhang, Wenjie Du, Jun Zhang, Yi Qin Gao, Ziqiang Cao, Guohong Fu  

**一句话要点**：提出PFUA工具增强蛋白质推理代理，以解决蛋白质功能理解中文本推理泛化有限的问题。

**关键词**：蛋白质功能理解, 工具增强推理, 链式思维, 生物信息学, 知识密集型任务, 泛化性能

## 3 点简述
- 核心问题：蛋白质功能预测依赖外部生物先验和计算工具，而非纯文本推理，现有方法泛化能力不足。
- 方法要点：PFUA统一问题分解、工具调用和基于证据的答案生成，集成领域特定工具产生可验证中间证据。
- 实验或效果：在四个基准测试中，PFUA平均性能提升103%，优于纯文本推理模型。

## 摘要（原文）

> Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

