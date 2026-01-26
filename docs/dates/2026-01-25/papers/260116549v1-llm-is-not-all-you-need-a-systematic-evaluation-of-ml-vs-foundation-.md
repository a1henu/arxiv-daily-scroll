---
layout: default
title: LLM is Not All You Need: A Systematic Evaluation of ML vs. Foundation Models for text and image based Medical Classification
---

# LLM is Not All You Need: A Systematic Evaluation of ML vs. Foundation Models for text and image based Medical Classification
**arXiv**：[2601.16549v1](https://arxiv.org/abs/2601.16549) · [PDF](https://arxiv.org/pdf/2601.16549.pdf)  
**作者**：Meet Raval, Tejul Pandit, Dhvani Upadhyay  

**一句话要点**：系统评估传统机器学习与基础模型在医学分类任务中的性能对比

**关键词**：医学分类, 机器学习基准, 多模态模型, 参数高效微调, Transformer模型

## 3 点简述
- 核心问题：比较传统机器学习与基于Transformer的基础模型在医学文本和图像分类任务中的效果
- 方法要点：使用统一基准，评估三类模型：传统ML、提示式LLM/VLM和微调PEFT模型
- 实验或效果：传统ML在多数任务中表现最佳，PEFT微调效果差，LLM/VLM在图像任务中具竞争力

## 摘要（原文）

> The combination of multimodal Vision-Language Models (VLMs) and Large Language Models (LLMs) opens up new possibilities for medical classification. This work offers a rigorous, unified benchmark by using four publicly available datasets covering text and image modalities (binary and multiclass complexity) that contrasts traditional Machine Learning (ML) with contemporary transformer-based techniques. We evaluated three model classes for each task: Classical ML (LR, LightGBM, ResNet-50), Prompt-Based LLMs/VLMs (Gemini 2.5), and Fine-Tuned PEFT Models (LoRA-adapted Gemma3 variants). All experiments used consistent data splits and aligned metrics. According to our results, traditional machine learning (ML) models set a high standard by consistently achieving the best overall performance across most medical categorization tasks. This was especially true for structured text-based datasets, where the classical models performed exceptionally well. In stark contrast, the LoRA-tuned Gemma variants consistently showed the worst performance across all text and image experiments, failing to generalize from the minimal fine-tuning provided. However, the zero-shot LLM/VLM pipelines (Gemini 2.5) had mixed results; they performed poorly on text-based tasks, but demonstrated competitive performance on the multiclass image task, matching the classical ResNet-50 baseline. These results demonstrate that in many medical categorization scenarios, established machine learning models continue to be the most reliable option. The experiment suggests that foundation models are not universally superior and that the effectiveness of Parameter-Efficient Fine-Tuning (PEFT) is highly dependent on the adaptation strategy, as minimal fine-tuning proved detrimental in this study.

