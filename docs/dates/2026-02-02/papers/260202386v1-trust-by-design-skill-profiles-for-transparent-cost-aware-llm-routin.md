---
layout: default
title: Trust by Design: Skill Profiles for Transparent, Cost-Aware LLM Routing
---

# Trust by Design: Skill Profiles for Transparent, Cost-Aware LLM Routing
**arXiv**：[2602.02386v1](https://arxiv.org/abs/2602.02386) · [PDF](https://arxiv.org/pdf/2602.02386.pdf)  
**作者**：Mika Okamoto, Ansel Kaplan Erol, Glenn Matlin  

**一句话要点**：提出BELLA框架，通过技能剖析实现透明、预算感知的LLM路由选择

**关键词**：LLM路由, 技能剖析, 预算优化, 透明性, 多目标优化, 金融推理

## 3 点简述
- 核心问题：标准基准测试的聚合指标难以揭示任务所需具体能力，导致模型选择浪费预算
- 方法要点：基于批评者剖析分解LLM输出，聚类技能为结构化矩阵，进行多目标优化选择模型
- 实验或效果：应用于金融推理领域，提供自然语言理由，增强透明性并优化成本性能权衡

## 摘要（原文）

> How should Large Language Model (LLM) practitioners select the right model for a task without wasting money? We introduce BELLA (Budget-Efficient LLM Selection via Automated skill-profiling), a framework that recommends optimal LLM selection for tasks through interpretable skill-based model selection. Standard benchmarks report aggregate metrics that obscure which specific capabilities a task requires and whether a cheaper model could suffice. BELLA addresses this gap through three stages: (1) decomposing LLM outputs and extract the granular skills required by using critic-based profiling, (2) clustering skills into structured capability matrices, and (3) multi-objective optimization to select the right models to maximize performance while respecting budget constraints. BELLA provides natural-language rationale for recommendations, providing transparency that current black-box routing systems lack. We describe the framework architecture, situate it within the landscape of LLM routing and evaluation, and discuss its application to financial reasoning as a representative domain exhibiting diverse skill requirements and cost-variation across models. Our framework enables practitioners to make principled and cost-performance trade-offs for deploying LLMs.

