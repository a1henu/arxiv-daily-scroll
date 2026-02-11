---
layout: default
title: Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference
---

# Decoupled Reasoning with Implicit Fact Tokens (DRIFT): A Dual-Model Framework for Efficient Long-Context Inference
**arXiv**：[2602.10021v1](https://arxiv.org/abs/2602.10021) · [PDF](https://arxiv.org/pdf/2602.10021.pdf)  
**作者**：Wenxuan Xie, Yujia Wang, Xin Tan, Chaochao Lu, Xia Hu, Xuhong Wang  

**一句话要点**：提出DRIFT双模型框架，通过隐式事实令牌解耦知识提取与推理，以高效处理长上下文任务。

**关键词**：长上下文推理, 知识解耦, 隐式事实令牌, 双模型架构, 动态压缩, 大语言模型优化

## 3 点简述
- 核心问题：大语言模型中事实数据与推理模式纠缠，导致长上下文处理受限，现有方法如RAG和知识编辑存在窗口限制或遗忘风险。
- 方法要点：采用轻量知识模型动态压缩文档块为隐式事实令牌，基于查询条件化，并投影到推理模型嵌入空间，替代冗余文本。
- 实验或效果：在长上下文任务中显著提升性能，优于同规模基线，提供可扩展的高效范式扩展LLM上下文窗口和推理能力。

## 摘要（原文）

> The integration of extensive, dynamic knowledge into Large Language Models (LLMs) remains a significant challenge due to the inherent entanglement of factual data and reasoning patterns. Existing solutions, ranging from non-parametric Retrieval-Augmented Generation (RAG) to parametric knowledge editing, are often constrained in practice by finite context windows, retriever noise, or the risk of catastrophic forgetting. In this paper, we propose DRIFT, a novel dual-model architecture designed to explicitly decouple knowledge extraction from the reasoning process. Unlike static prompt compression, DRIFT employs a lightweight knowledge model to dynamically compress document chunks into implicit fact tokens conditioned on the query. These dense representations are projected into the reasoning model's embedding space, replacing raw, redundant text while maintaining inference accuracy. Extensive experiments show that DRIFT significantly improves performance on long-context tasks, outperforming strong baselines among comparably sized models. Our approach provides a scalable and efficient paradigm for extending the effective context window and reasoning capabilities of LLMs. Our code is available at https://github.com/Lancelot-Xie/DRIFT.

