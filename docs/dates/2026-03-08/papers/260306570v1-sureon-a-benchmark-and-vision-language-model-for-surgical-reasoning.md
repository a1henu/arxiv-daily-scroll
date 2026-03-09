---
layout: default
title: SUREON: A Benchmark and Vision-Language-Model for Surgical Reasoning
---

# SUREON: A Benchmark and Vision-Language-Model for Surgical Reasoning
**arXiv**：[2603.06570v1](https://arxiv.org/abs/2603.06570) · [PDF](https://arxiv.org/pdf/2603.06570.pdf)  
**作者**：Alejandra Perez, Anita Rau, Lee White, Busisiwe Mlambo, Chinedu Nwoye, Muhammad Abdullah Jamal, Omid Mohareri  

**一句话要点**：提出SUREON基准与视觉语言模型，利用手术视频讲座解决手术推理数据标注难题。

**关键词**：手术推理, 视觉语言模型, 视频问答数据集, 多智能体管道, 监督微调, 相对策略优化

## 3 点简述
- 核心问题：手术AI缺乏大规模标注的推理数据，无法理解手术意图、风险与预测。
- 方法要点：从手术学术视频中提取专家讲解，构建大规模视频问答数据集，涵盖12类问题。
- 实验或效果：模型在基准上准确率超84%，优于通用模型，并展示显式推理行为。

## 摘要（原文）

> Surgeons don't just see -- they interpret. When an expert observes a surgical scene, they understand not only what instrument is being used, but why it was chosen, what risk it poses, and what comes next. Current surgical AI cannot answer such questions, largely because training data that explicitly encodes surgical reasoning is immensely difficult to annotate at scale. Yet surgical video lectures already contain exactly this -- explanations of intent, rationale, and anticipation, narrated by experts for the purpose of teaching. Though inherently noisy and unstructured, these narrations encode the reasoning that surgical AI currently lacks. We introduce SUREON, a large-scale video QA dataset that systematically harvests this training signal from surgical academic videos. SUREON defines 12 question categories covering safety assessment, decision rationale, and forecasting, and uses a multi-agent pipeline to extract and structure supervision at scale. Across 134.7K clips and 170 procedure types, SUREON yields 206.8k QA pairs and an expert-validated benchmark of 354 examples. To evaluate the extent to which this supervision translates to surgical reasoning ability, we introduce two models: SureonVLM, a vision-language model adapted through supervised fine-tuning, and SureonVLM-R1, a reasoning model trained with Group Relative Policy Optimization. Both models can answer complex questions about surgery and substantially outperform larger general-domain models, exceeding 84% accuracy on the SUREON benchmark while outperforming general-domain models on standard surgical perception tasks. Qualitative analysis of SureonVLM-R1 reveals explicit reasoning behavior, such as inferring operative intent from visual context.

