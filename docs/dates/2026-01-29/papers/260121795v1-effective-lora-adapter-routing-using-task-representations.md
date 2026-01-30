---
layout: default
title: Effective LoRA Adapter Routing using Task Representations
---

# Effective LoRA Adapter Routing using Task Representations
**arXiv**：[2601.21795v1](https://arxiv.org/abs/2601.21795) · [PDF](https://arxiv.org/pdf/2601.21795.pdf)  
**作者**：Akash Dhasade, Anne-Marie Kermarrec, Igor Pavlovic, Diana Petrescu, Rafael Pires, Mathis Randl, Martijn de Vos  

**一句话要点**：提出LORAUTER框架，基于任务表示路由LoRA适配器以高效利用公共适配器池

**关键词**：LoRA适配器路由, 任务表示学习, 参数高效微调, 大语言模型适配, 适配器池管理

## 3 点简述
- 核心问题：LoRA适配器池快速增长，需高效路由选择适配器以应对多样化任务
- 方法要点：通过任务嵌入而非适配器特征路由，利用小验证集生成任务表示，无需适配器训练数据
- 实验或效果：在多个任务上优于基线，任务对齐时接近Oracle性能，对未见任务提升5.2点

## 摘要（原文）

> Low-rank adaptation (LoRA) enables parameter efficient specialization of large language models (LLMs) through modular adapters, resulting in rapidly growing public adapter pools spanning diverse tasks. Effectively using these adapters requires routing: selecting and composing the appropriate adapters for a query. We introduce LORAUTER, a novel routing framework that selects and composes LoRA adapters using task representations rather than adapter characteristics. Unlike existing approaches that map queries directly to adapters, LORAUTER routes queries via task embeddings derived from small validation sets and does not require adapter training data. By operating at the task level, LORAUTER achieves efficient routing that scales with the number of tasks rather than the number of adapters. Experiments across multiple tasks show that LORAUTER consistently outperforms baseline routing approaches, matching Oracle performance (101.2%) when task-aligned adapters exist and achieving state-of-the-art results on unseen tasks (+5.2 points). We further demonstrate the robustness of LORAUTER to very large, noisy adapter pools by scaling it to over 1500 adapters.

