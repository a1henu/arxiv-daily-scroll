---
layout: default
title: Disentangling Deception and Hallucination Failures in LLMs
---

# Disentangling Deception and Hallucination Failures in LLMs
**arXiv**：[2602.14529v1](https://arxiv.org/abs/2602.14529) · [PDF](https://arxiv.org/pdf/2602.14529.pdf)  
**作者**：Haolang Lu, Hongrui Peng, WeiYe Fu, Guoshun Nan, Xinye Cao, Xingrui Li, Hongcan Guo, Kun Wang  

**一句话要点**：提出知识存在与行为表达分离框架，以区分大语言模型中的幻觉与欺骗失败模式

**关键词**：大语言模型失败分析, 幻觉与欺骗分离, 实体事实查询, 机制导向视角, 表示可分性, 推理时激活引导

## 3 点简述
- 核心问题：大语言模型在实体事实查询中的失败常被归因于知识缺失，可能混淆不同机制
- 方法要点：构建受控环境，通过表示可分性、稀疏可解释性和推理时激活引导分析失败模式
- 实验或效果：系统分析四种行为案例，区分幻觉和欺骗的底层机制差异

## 摘要（原文）

> Failures in large language models (LLMs) are often analyzed from a behavioral perspective, where incorrect outputs in factual question answering are commonly associated with missing knowledge. In this work, focusing on entity-based factual queries, we suggest that such a view may conflate different failure mechanisms, and propose an internal, mechanism-oriented perspective that separates Knowledge Existence from Behavior Expression. Under this formulation, hallucination and deception correspond to two qualitatively different failure modes that may appear similar at the output level but differ in their underlying mechanisms. To study this distinction, we construct a controlled environment for entity-centric factual questions in which knowledge is preserved while behavioral expression is selectively altered, enabling systematic analysis of four behavioral cases. We analyze these failure modes through representation separability, sparse interpretability, and inference-time activation steering.

