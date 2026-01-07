---
layout: default
title: Learning from Prompt itself: the Hierarchical Attribution Prompt Optimization
---

# Learning from Prompt itself: the Hierarchical Attribution Prompt Optimization
**arXiv**：[2601.02683v1](https://arxiv.org/abs/2601.02683) · [PDF](https://arxiv.org/pdf/2601.02683.pdf)  
**作者**：Dongyu Chen, Jian Ma, Xianpeng Zhang, Lei Zhang, Haonan Lu, Chen Chen, Chuangchuang Wang, Kai Tang  

**一句话要点**：提出分层归因提示优化框架以解决提示漂移和可解释性问题

**关键词**：提示优化, 分层归因, 语义单元编辑, 多模态工作流, 可解释性, 提示漂移

## 3 点简述
- 核心问题：现有提示优化方法易导致提示漂移，且从头生成提示损害可解释性
- 方法要点：引入动态归因机制、语义单元优化和多模态友好流程
- 实验或效果：在单/多图像问答和复杂任务分析中提升优化效率，优于可比方法

## 摘要（原文）

> Optimization is fundamental across numerous disciplines, typically following an iterative process of refining an initial solution to enhance performance. This principle is equally critical in prompt engineering, where designing effective prompts for large language models constitutes a complex optimization challenge. A structured optimization approach requires automated or semi-automated procedures to develop improved prompts, thereby reducing manual effort, improving performance, and yielding an interpretable process. However, current prompt optimization methods often induce prompt drift, where new prompts fix prior failures but impair performance on previously successful tasks. Additionally, generating prompts from scratch can compromise interpretability. To address these limitations, this study proposes the Hierarchical Attribution Prompt Optimization (HAPO) framework, which introduces three innovations: (1) a dynamic attribution mechanism targeting error patterns in training data and prompting history, (2) semantic-unit optimization for editing functional prompt segments, and (3) multimodal-friendly progression supporting both end-to-end LLM and LLM-MLLM workflows. Applied in contexts like single/multi-image QA (e.g., OCRV2) and complex task analysis (e.g., BBH), HAPO demonstrates enhanced optimization efficiency, outperforming comparable automated prompt optimization methods and establishing an extensible paradigm for scalable prompt engineering.

