---
layout: default
title: Multi-Task Learning for Visually Grounded Reasoning in Gastrointestinal VQA
---

# Multi-Task Learning for Visually Grounded Reasoning in Gastrointestinal VQA
**arXiv**：[2511.04384v1](https://arxiv.org/abs/2511.04384) · [PDF](https://arxiv.org/pdf/2511.04384.pdf)  
**作者**：Itbaan Safwan, Muhammad Annas Shaikh, Muhammad Haaris, Ramail Khan, Muhammad Atif Tahir  

**一句话要点**：提出多任务框架以提升胃肠道视觉问答的准确性和可解释性

**关键词**：多任务学习, 视觉问答, 医学图像分析, 视觉定位, 解释生成

## 3 点简述
- 核心问题：医学视觉问答中视觉推理和解释生成不足
- 方法要点：使用LoRA微调Florence-2模型，集成多任务学习
- 实验或效果：多任务方法在答案准确性和视觉定位上优于单任务基线

## 摘要（原文）

> We present a multi-task framework for the MediaEval Medico 2025 challenge,
> leveraging a LoRA-tuned Florence-2 model for simultaneous visual question
> answering (VQA), explanation generation, and visual grounding. The proposed
> system integrates three curated datasets: (1) Kvasir-VQA-x1 for question-answer
> learning, (2) a synthetically enriched explanation dataset offering structured
> medical reasoning, and (3) text-to-region pairs linking visual features with
> segmentation masks. This multi-task setup enables the model to jointly learn
> visual grounding, reasoning, and interpretation, producing responses that are
> both accurate and interpretable. Extensive evaluation demonstrates that our
> approach substantially improves over single-task baselines in both answer
> accuracy and visual localization, highlighting the effectiveness of grounded
> multi-task learning for medical VQA applications.

