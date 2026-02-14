---
layout: default
title: Cross-Architecture Model Diffing with Crosscoders: Unsupervised Discovery of Differences Between LLMs
---

# Cross-Architecture Model Diffing with Crosscoders: Unsupervised Discovery of Differences Between LLMs
**arXiv**：[2602.11729v1](https://arxiv.org/abs/2602.11729) · [PDF](https://arxiv.org/pdf/2602.11729.pdf)  
**作者**：Thomas Jiralerspong, Trenton Bricken  

**一句话要点**：提出专用特征交叉编码器以解决跨架构模型差异检测问题

**关键词**：模型差异检测, 跨架构比较, 无监督学习, 特征隔离, LLM安全分析

## 3 点简述
- 核心问题：现有模型差异检测方法主要针对同架构模型，难以应用于新发布的跨架构LLM。
- 方法要点：引入专用特征交叉编码器，改进Crosscoders架构以更好隔离模型特有特征。
- 实验或效果：无监督发现Qwen3-8B的中共对齐、Llama3.1-8B-Instruct的美国例外论等行为差异。

## 摘要（原文）

> Model diffing, the process of comparing models' internal representations to identify their differences, is a promising approach for uncovering safety-critical behaviors in new models. However, its application has so far been primarily focused on comparing a base model with its finetune. Since new LLM releases are often novel architectures, cross-architecture methods are essential to make model diffing widely applicable. Crosscoders are one solution capable of cross-architecture model diffing but have only ever been applied to base vs finetune comparisons. We provide the first application of crosscoders to cross-architecture model diffing and introduce Dedicated Feature Crosscoders (DFCs), an architectural modification designed to better isolate features unique to one model. Using this technique, we find in an unsupervised fashion features including Chinese Communist Party alignment in Qwen3-8B and Deepseek-R1-0528-Qwen3-8B, American exceptionalism in Llama3.1-8B-Instruct, and a copyright refusal mechanism in GPT-OSS-20B. Together, our results work towards establishing cross-architecture crosscoder model diffing as an effective method for identifying meaningful behavioral differences between AI models.

