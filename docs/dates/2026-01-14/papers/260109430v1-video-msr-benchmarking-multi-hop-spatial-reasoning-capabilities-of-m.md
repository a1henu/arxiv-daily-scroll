---
layout: default
title: Video-MSR: Benchmarking Multi-hop Spatial Reasoning Capabilities of MLLMs
---

# Video-MSR: Benchmarking Multi-hop Spatial Reasoning Capabilities of MLLMs
**arXiv**：[2601.09430v1](https://arxiv.org/abs/2601.09430) · [PDF](https://arxiv.org/pdf/2601.09430.pdf)  
**作者**：Rui Zhu, Xin Shen, Shuchen Wu, Chenxi Miao, Xin Yu, Yang Li, Weikang Li, Deguo Xia, Jizhou Huang  

**一句话要点**：提出Video-MSR基准以评估动态视频中的多跳空间推理能力

**关键词**：多跳空间推理, 视频基准, 指令调优, 多模态大语言模型, 动态场景

## 3 点简述
- 现有基准缺乏对复杂视觉空间逻辑链的评估，聚焦单步感知任务
- Video-MSR包含四个任务和高质量视频实例，通过模型生成与人工验证构建
- 评估显示模型在多跳推理中表现下降，指令调优数据集MSR-9K提升性能

## 摘要（原文）

> Spatial reasoning has emerged as a critical capability for Multimodal Large Language Models (MLLMs), drawing increasing attention and rapid advancement. However, existing benchmarks primarily focus on single-step perception-to-judgment tasks, leaving scenarios requiring complex visual-spatial logical chains significantly underexplored. To bridge this gap, we introduce Video-MSR, the first benchmark specifically designed to evaluate Multi-hop Spatial Reasoning (MSR) in dynamic video scenarios. Video-MSR systematically probes MSR capabilities through four distinct tasks: Constrained Localization, Chain-based Reference Retrieval, Route Planning, and Counterfactual Physical Deduction. Our benchmark comprises 3,052 high-quality video instances with 4,993 question-answer pairs, constructed via a scalable, visually-grounded pipeline combining advanced model generation with rigorous human verification. Through a comprehensive evaluation of 20 state-of-the-art MLLMs, we uncover significant limitations, revealing that while models demonstrate proficiency in surface-level perception, they exhibit distinct performance drops in MSR tasks, frequently suffering from spatial disorientation and hallucination during multi-step deductions. To mitigate these shortcomings and empower models with stronger MSR capabilities, we further curate MSR-9K, a specialized instruction-tuning dataset, and fine-tune Qwen-VL, achieving a +7.82% absolute improvement on Video-MSR. Our results underscore the efficacy of multi-hop spatial instruction data and establish Video-MSR as a vital foundation for future research. The code and data will be available at https://github.com/ruiz-nju/Video-MSR.

