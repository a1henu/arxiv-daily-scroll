---
layout: default
title: A Unified Evaluation-Instructed Framework for Query-Dependent Prompt Optimization
---

# A Unified Evaluation-Instructed Framework for Query-Dependent Prompt Optimization
**arXiv**：[2511.19829v1](https://arxiv.org/abs/2511.19829) · [PDF](https://arxiv.org/pdf/2511.19829.pdf)  
**作者**：Ke Chen, Yifeng Wang, Hassan Almosapeeh, Haohan Wang  

**一句话要点**：提出统一评估指导框架以优化查询依赖提示，解决动态场景中提示质量评估与优化问题。

**关键词**：提示优化, 查询依赖优化, 评估框架, 免执行评估器, 可解释AI, 模型无关改进

## 3 点简述
- 核心问题：提示质量缺乏统一系统定义，现有方法依赖不稳定反馈，导致优化信号弱且不可解释。
- 方法要点：建立性能导向的评估框架，开发免执行评估器预测多维质量分数，指导可解释的查询依赖优化。
- 实验或效果：在八个数据集和三个骨干模型上，评估器预测准确率最高，优化方法超越静态和查询依赖基线。

## 摘要（原文）

> Most prompt-optimization methods refine a single static template, making them ineffective in complex and dynamic user scenarios. Existing query-dependent approaches rely on unstable textual feedback or black-box reward models, providing weak and uninterpretable optimization signals. More fundamentally, prompt quality itself lacks a unified, systematic definition, resulting in fragmented and unreliable evaluation signals. Our approach first establishes a performance-oriented, systematic, and comprehensive prompt evaluation framework. Furthermore, we develop and finetune an execution-free evaluator that predicts multi-dimensional quality scores directly from text. The evaluator then instructs a metric-aware optimizer that diagnoses failure modes and rewrites prompts in an interpretable, query-dependent manner. Our evaluator achieves the strongest accuracy in predicting prompt performance, and the evaluation-instructed optimization consistently surpass both static-template and query-dependent baselines across eight datasets and on three backbone models. Overall, we propose a unified, metric-grounded perspective on prompt quality, and demonstrated that our evaluation-instructed optimization pipeline delivers stable, interpretable, and model-agnostic improvements across diverse tasks.

