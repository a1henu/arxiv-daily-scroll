---
layout: default
title: ChartM$^3$: A Multi-Stage Code-Driven Pipeline for Constructing Multi-Dimensional and Multi-Step Visual Reasoning Data in Chart Comprehension
---

# ChartM$^3$: A Multi-Stage Code-Driven Pipeline for Constructing Multi-Dimensional and Multi-Step Visual Reasoning Data in Chart Comprehension
**arXiv**：[2511.02415v1](https://arxiv.org/abs/2511.02415) · [PDF](https://arxiv.org/pdf/2511.02415.pdf)  
**作者**：Duo Xu, Hao Cheng, Xin Lin, Zhen Xie, Hao Wang  

**一句话要点**：提出ChartM³多阶段代码驱动管道，以解决复杂图表理解中数据不足问题。

**关键词**：图表理解, 多模态大语言模型, 检索增强生成, 思维链, 监督微调, 强化学习

## 3 点简述
- 核心问题：现有研究对复杂图表场景和计算密集型推理任务覆盖不足。
- 方法要点：使用检索增强生成和思维链策略，自动生成图表和推理数据。
- 实验或效果：数据集显著提升模型推理能力和跨域泛化性能。

## 摘要（原文）

> Complex chart understanding tasks demand advanced visual recognition and
> reasoning capabilities from multimodal large language models (MLLMs). However,
> current research provides limited coverage of complex chart scenarios and
> computation-intensive reasoning tasks prevalent in real-world applications.
> This study proposes an automated multi-stage code-driven pipeline for
> systematically generating visual reasoning datasets to address these
> limitations. The pipeline integrates retrieval-augmented generation (RAG) to
> retrieve professional chart templates and employs chain-of-thought (CoT)
> strategies to generate reasoning codes that simulate real data distributions,
> thereby driving chart rendering and question-related statistical computations.
> Through model-based evaluation, the pipeline enhances chart diversity and data
> quality. Using this framework, we construct ChartM$^3$, a multi-dimensional and
> multi-step dataset containing 38K charts and 142K Q&A pairs for training, along
> with 2,871 high-quality evaluation samples for enabling practical performance
> assessment. Supervised fine-tuning (SFT) and reinforcement learning (RL)
> experiments demonstrate that our dataset significantly improves reasoning
> capabilities and cross-domain generalization performance, enabling smaller
> models to achieve performance comparable to larger-scale models in complex
> chart comprehension.

