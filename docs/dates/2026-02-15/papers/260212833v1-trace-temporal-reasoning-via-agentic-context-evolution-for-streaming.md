---
layout: default
title: TRACE: Temporal Reasoning via Agentic Context Evolution for Streaming Electronic Health Records (EHRs)
---

# TRACE: Temporal Reasoning via Agentic Context Evolution for Streaming Electronic Health Records (EHRs)
**arXiv**：[2602.12833v1](https://arxiv.org/abs/2602.12833) · [PDF](https://arxiv.org/pdf/2602.12833.pdf)  
**作者**：Zhan Qu, Michael Färber  

**一句话要点**：提出TRACE框架，通过结构化上下文实现冻结大语言模型在流式电子健康记录中的时序推理。

**关键词**：时序推理, 电子健康记录, 大语言模型, 上下文管理, 临床决策支持, 代理架构

## 3 点简述
- 核心问题：大语言模型在纵向患者轨迹中因临床状态演变、不规则时序和异构事件而性能下降。
- 方法要点：采用双内存架构和四个代理组件，结构化维护上下文以支持时序推理和状态演化。
- 实验或效果：在MIMIC-IV数据集上显著提升预测准确性、协议依从性和临床安全性，并产生可解释推理痕迹。

## 摘要（原文）

> Large Language Models (LLMs) encode extensive medical knowledge but struggle to apply it reliably to longitudinal patient trajectories, where evolving clinical states, irregular timing, and heterogeneous events degrade performance over time. Existing adaptation strategies rely on fine-tuning or retrieval-based augmentation, which introduce computational overhead, privacy constraints, or instability under long contexts. We introduce TRACE (Temporal Reasoning via Agentic Context Evolution), a framework that enables temporal clinical reasoning with frozen LLMs by explicitly structuring and maintaining context rather than extending context windows or updating parameters. TRACE operates over a dual-memory architecture consisting of a static Global Protocol encoding institutional clinical rules and a dynamic Individual Protocol tracking patient-specific state. Four agentic components, Router, Reasoner, Auditor, and Steward, coordinate over this structured memory to support temporal inference and state evolution. The framework maintains bounded inference cost via structured state compression and selectively audits safety-critical clinical decisions. Evaluated on longitudinal clinical event streams from MIMIC-IV, TRACE significantly improves next-event prediction accuracy, protocol adherence, and clinical safety over long-context and retrieval-augmented baselines, while producing interpretable and auditable reasoning traces.

