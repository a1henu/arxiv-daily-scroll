---
layout: default
title: A Vision-and-Knowledge Enhanced Large Language Model for Generalizable Pedestrian Crossing Behavior Inference
---

# A Vision-and-Knowledge Enhanced Large Language Model for Generalizable Pedestrian Crossing Behavior Inference
**arXiv**：[2601.00694v1](https://arxiv.org/abs/2601.00694) · [PDF](https://arxiv.org/pdf/2601.00694.pdf)  
**作者**：Qingwen Pu, Kun Xie, Hong Yang, Guocong Zhai  

**一句话要点**：提出PedX-LLM框架，通过视觉与知识增强提升行人过街行为推理的泛化能力

**关键词**：行人过街行为推理, 视觉增强大语言模型, 领域知识集成, 低秩适应微调, 跨站点泛化

## 3 点简述
- 现有方法泛化性差，LLMs缺乏领域适应和视觉上下文
- 集成LLaVA视觉特征、文本数据和交通知识，基于LoRA微调LLaMA-2-7B
- 在未见场景中，零-shot配置准确率66.9%，few-shot学习提升至72.2%

## 摘要（原文）

> Existing paradigms for inferring pedestrian crossing behavior, ranging from statistical models to supervised learning methods, demonstrate limited generalizability and perform inadequately on new sites. Recent advances in Large Language Models (LLMs) offer a shift from numerical pattern fitting to semantic, context-aware behavioral reasoning, yet existing LLM applications lack domain-specific adaptation and visual context. This study introduces Pedestrian Crossing LLM (PedX-LLM), a vision-and-knowledge enhanced framework designed to transform pedestrian crossing inference from site-specific pattern recognition to generalizable behavioral reasoning. By integrating LLaVA-extracted visual features with textual data and transportation domain knowledge, PedX-LLM fine-tunes a LLaMA-2-7B foundation model via Low-Rank Adaptation (LoRA) to infer crossing decisions. PedX-LLM achieves 82.0% balanced accuracy, outperforming the best statistical and supervised learning methods. Results demonstrate that the vision-augmented module contributes a 2.9% performance gain by capturing the built environment and integrating domain knowledge yields an additional 4.1% improvement. To evaluate generalizability across unseen environments, cross-site validation was conducted using site-based partitioning. The zero-shot PedX-LLM configuration achieves 66.9% balanced accuracy on five unseen test sites, outperforming the baseline data-driven methods by at least 18 percentage points. Incorporating just five validation examples via few-shot learning to PedX-LLM further elevates the balanced accuracy to 72.2%. PedX-LLM demonstrates strong generalizability to unseen scenarios, confirming that vision-and-knowledge-enhanced reasoning enables the model to mimic human-like decision logic and overcome the limitations of purely data-driven methods.

