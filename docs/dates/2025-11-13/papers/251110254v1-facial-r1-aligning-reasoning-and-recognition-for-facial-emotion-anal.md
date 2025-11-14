---
layout: default
title: Facial-R1: Aligning Reasoning and Recognition for Facial Emotion Analysis
---

# Facial-R1: Aligning Reasoning and Recognition for Facial Emotion Analysis
**arXiv**：[2511.10254v1](https://arxiv.org/abs/2511.10254) · [PDF](https://arxiv.org/pdf/2511.10254.pdf)  
**作者**：Jiulong Wu, Yucheng Shen, Lingyong Yan, Haixin Sun, Deguo Xia, Jizhou Huang, Min Cao  

**一句话要点**：提出Facial-R1框架以解决面部情感分析中的幻觉推理和识别不对齐问题

**关键词**：面部情感分析, 视觉语言模型, 对齐框架, 强化训练, 数据合成, 基准数据集

## 3 点简述
- 核心问题：视觉语言模型在面部情感分析中产生幻觉推理和识别不对齐
- 方法要点：采用三阶段对齐框架，包括指令微调、强化训练和数据合成
- 实验或效果：在八个基准测试中实现最先进性能，并引入FEA-20K数据集

## 摘要（原文）

> Facial Emotion Analysis (FEA) extends traditional facial emotion recognition by incorporating explainable, fine-grained reasoning. The task integrates three subtasks: emotion recognition, facial Action Unit (AU) recognition, and AU-based emotion reasoning to model affective states jointly. While recent approaches leverage Vision-Language Models (VLMs) and achieve promising results, they face two critical limitations: (1) hallucinated reasoning, where VLMs generate plausible but inaccurate explanations due to insufficient emotion-specific knowledge; and (2) misalignment between emotion reasoning and recognition, caused by fragmented connections between observed facial features and final labels. We propose Facial-R1, a three-stage alignment framework that effectively addresses both challenges with minimal supervision. First, we employ instruction fine-tuning to establish basic emotional reasoning capability. Second, we introduce reinforcement training guided by emotion and AU labels as reward signals, which explicitly aligns the generated reasoning process with the predicted emotion. Third, we design a data synthesis pipeline that iteratively leverages the prior stages to expand the training dataset, enabling scalable self-improvement of the model. Built upon this framework, we introduce FEA-20K, a benchmark dataset comprising 17,737 training and 1,688 test samples with fine-grained emotion analysis annotations. Extensive experiments across eight standard benchmarks demonstrate that Facial-R1 achieves state-of-the-art performance in FEA, with strong generalization and robust interpretability.

