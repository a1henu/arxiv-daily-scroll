---
layout: default
title: Towards Governance-Oriented Low-Altitude Intelligence: A Management-Centric Multi-Modal Benchmark With Implicitly Coordinated Vision-Language Reasoning Framework
---

# Towards Governance-Oriented Low-Altitude Intelligence: A Management-Centric Multi-Modal Benchmark With Implicitly Coordinated Vision-Language Reasoning Framework
**arXiv**：[2601.19640v1](https://arxiv.org/abs/2601.19640) · [PDF](https://arxiv.org/pdf/2601.19640.pdf)  
**作者**：Hao Chang, Zhihui Wang, Lingxiang Wu, Peijin Wang, Wenhui Diao, Jinqiao Wang  

**一句话要点**：提出GovLA-10K基准与GovLA-Reasoner框架，以支持面向治理的低空智能视觉-语言推理。

**关键词**：低空智能, 多模态基准, 视觉-语言推理, 城市治理, 隐式协调

## 3 点简述
- 核心问题：现有低空视觉系统难以支持城市治理中的管理导向异常理解。
- 方法要点：引入管理导向多模态基准和隐式协调视觉-语言推理框架。
- 实验或效果：实验表明方法显著提升性能，无需微调任务特定组件。

## 摘要（原文）

> Low-altitude vision systems are becoming a critical infrastructure for smart city governance. However, existing object-centric perception paradigms and loosely coupled vision-language pipelines are still difficult to support management-oriented anomaly understanding required in real-world urban governance. To bridge this gap, we introduce GovLA-10K, the first management-oriented multi-modal benchmark for low-altitude intelligence, along with GovLA-Reasoner, a unified vision-language reasoning framework tailored for governance-aware aerial perception. Unlike existing studies that aim to exhaustively annotate all visible objects, GovLA-10K is deliberately designed around functionally salient targets that directly correspond to practical management needs, and further provides actionable management suggestions grounded in these observations. To effectively coordinate the fine-grained visual grounding with high-level contextual language reasoning, GovLA-Reasoner introduces an efficient feature adapter that implicitly coordinates discriminative representation sharing between the visual detector and the large language model (LLM). Extensive experiments show that our method significantly improves performance while avoiding the need of fine-tuning for any task-specific individual components. We believe our work offers a new perspective and foundation for future studies on management-aware low-altitude vision-language systems.

