---
layout: default
title: Uni-FinLLM: A Unified Multimodal Large Language Model with Modular Task Heads for Micro-Level Stock Prediction and Macro-Level Systemic Risk Assessment
---

# Uni-FinLLM: A Unified Multimodal Large Language Model with Modular Task Heads for Micro-Level Stock Prediction and Macro-Level Systemic Risk Assessment
**arXiv**：[2601.02677v1](https://arxiv.org/abs/2601.02677) · [PDF](https://arxiv.org/pdf/2601.02677.pdf)  
**作者**：Gongao Zhang, Haijiang Zeng, Lu Jiang  

**一句话要点**：提出Uni-FinLLM统一多模态大语言模型，通过模块化任务头联合处理金融数据，以解决股票预测与系统性风险评估的跨尺度依赖问题。

**关键词**：多模态大语言模型, 金融预测, 系统性风险评估, 跨模态注意力, 模块化任务头, 多任务优化

## 3 点简述
- 核心问题：现有方法孤立处理金融任务，难以捕捉从股票波动到系统性风险的跨尺度依赖关系。
- 方法要点：采用共享Transformer骨干和模块化任务头，结合跨模态注意力与多任务优化，统一处理文本、时序、基本面和视觉数据。
- 实验或效果：在股票方向预测、信用风险评估和系统性风险检测上显著超越基线，准确率分别提升至67.4%、84.1%和82.3%。

## 摘要（原文）

> Financial institutions and regulators require systems that integrate heterogeneous data to assess risks from stock fluctuations to systemic vulnerabilities. Existing approaches often treat these tasks in isolation, failing to capture cross-scale dependencies. We propose Uni-FinLLM, a unified multimodal large language model that uses a shared Transformer backbone and modular task heads to jointly process financial text, numerical time series, fundamentals, and visual data. Through cross-modal attention and multi-task optimization, it learns a coherent representation for micro-, meso-, and macro-level predictions. Evaluated on stock forecasting, credit-risk assessment, and systemic-risk detection, Uni-FinLLM significantly outperforms baselines. It raises stock directional accuracy to 67.4% (from 61.7%), credit-risk accuracy to 84.1% (from 79.6%), and macro early-warning accuracy to 82.3%. Results validate that a unified multimodal LLM can jointly model asset behavior and systemic vulnerabilities, offering a scalable decision-support engine for finance.

