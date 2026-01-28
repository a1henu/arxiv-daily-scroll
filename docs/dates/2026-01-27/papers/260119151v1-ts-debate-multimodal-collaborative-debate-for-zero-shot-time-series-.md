---
layout: default
title: TS-Debate: Multimodal Collaborative Debate for Zero-Shot Time Series Reasoning
---

# TS-Debate: Multimodal Collaborative Debate for Zero-Shot Time Series Reasoning
**arXiv**：[2601.19151v1](https://arxiv.org/abs/2601.19151) · [PDF](https://arxiv.org/pdf/2601.19151.pdf)  
**作者**：Patara Trirat, Jin Myung Kwak, Jay Heo, Heejun Lee, Sung Ju Hwang  

**一句话要点**：提出TS-Debate多模态协作辩论框架以解决零样本时间序列推理中的模态干扰和数值幻觉问题

**关键词**：时间序列推理, 多模态协作, 零样本学习, 辩论框架, 数值幻觉缓解

## 3 点简述
- 核心问题：大语言模型在时间序列分析中面临数值保真度低、模态干扰和跨模态整合困难。
- 方法要点：采用模态专家代理分工协作，通过结构化辩论协议和验证-冲突-校准机制提升推理准确性。
- 实验或效果：在20个任务上超越基线，包括标准多模态辩论，无需任务特定微调。

## 摘要（原文）

> Recent progress at the intersection of large language models (LLMs) and time series (TS) analysis has revealed both promise and fragility. While LLMs can reason over temporal structure given carefully engineered context, they often struggle with numeric fidelity, modality interference, and principled cross-modal integration. We present TS-Debate, a modality-specialized, collaborative multi-agent debate framework for zero-shot time series reasoning. TS-Debate assigns dedicated expert agents to textual context, visual patterns, and numerical signals, preceded by explicit domain knowledge elicitation, and coordinates their interaction via a structured debate protocol. Reviewer agents evaluate agent claims using a verification-conflict-calibration mechanism, supported by lightweight code execution and numerical lookup for programmatic verification. This architecture preserves modality fidelity, exposes conflicting evidence, and mitigates numeric hallucinations without task-specific fine-tuning. Across 20 tasks spanning three public benchmarks, TS-Debate achieves consistent and significant performance improvements over strong baselines, including standard multimodal debate in which all agents observe all inputs.

