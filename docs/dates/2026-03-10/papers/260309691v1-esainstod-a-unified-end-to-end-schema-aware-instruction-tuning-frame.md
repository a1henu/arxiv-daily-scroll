---
layout: default
title: ESAinsTOD: A Unified End-to-End Schema-Aware Instruction-Tuning Framework for Task-Oriented Dialog Modeling
---

# ESAinsTOD: A Unified End-to-End Schema-Aware Instruction-Tuning Framework for Task-Oriented Dialog Modeling
**arXiv**：[2603.09691v1](https://arxiv.org/abs/2603.09691) · [PDF](https://arxiv.org/pdf/2603.09691.pdf)  
**作者**：Dechuan Teng, Chunlin Lu, Libo Qin, Wanxiang Che  

**一句话要点**：提出ESAinsTOD框架，通过指令与模式对齐增强任务导向对话建模的泛化能力。

**关键词**：任务导向对话, 端到端建模, 指令微调, 模式对齐, 泛化能力, 大语言模型

## 3 点简述
- 现有端到端方法难以适应新对话场景，需统一框架提升泛化性。
- 采用全参数微调，引入指令对齐和模式对齐机制，确保任务遵循与模式一致性。
- 实验显示在多个基准上显著优于现有模型，尤其在低资源设置下泛化能力突出。

## 摘要（原文）

> Existing end-to-end modeling methods for modular task-oriented dialog systems are typically tailored to specific datasets, making it challenging to adapt to new dialog scenarios. In this work, we propose ESAinsTOD, a unified End-to-end Schema-Aware Instruction-tuning framework for general Task-Oriented Dialog modeling. This framework introduces a structured methodology to go beyond simply fine-tuning Large Language Models (LLMs), enabling flexible adaptation to various dialogue task flows and schemas. Specifically, we leverage full-parameter fine-tuning of LLMs and introduce two alignment mechanisms to make the resulting system both instruction-aware and schema-aware: (i) instruction alignment, which ensures that the system faithfully follows task instructions to complete various task flows from heterogeneous TOD datasets; and (ii) schema alignment, which encourages the system to make predictions adhering to the specified schema. In addition, we employ session-level end-to-end modeling, which allows the system to access the results of previously executed task flows within the dialogue history, to bridge the gap between the instruction-tuning paradigm and the real-world application of TOD systems. Empirical results show that while a fine-tuned LLM serves as a strong baseline, our structured approach provides significant additional benefits. In particular, our findings indicate that: (i) ESAinsTOD outperforms state-of-the-art models by a significant margin on end-to-end task-oriented dialog modeling benchmarks: CamRest676, In-Car and MultiWOZ; (ii) more importantly, it exhibits superior generalization capabilities across various low-resource settings, with the proposed alignment mechanisms significantly enhancing zero-shot performance; and (iii) our instruction-tuning paradigm substantially improves the model's robustness against data noise and cascading errors.

