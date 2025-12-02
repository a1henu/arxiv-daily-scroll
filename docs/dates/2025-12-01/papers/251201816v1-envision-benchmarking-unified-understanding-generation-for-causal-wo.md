---
layout: default
title: Envision: Benchmarking Unified Understanding & Generation for Causal World Process Insights
---

# Envision: Benchmarking Unified Understanding & Generation for Causal World Process Insights
**arXiv**：[2512.01816v1](https://arxiv.org/abs/2512.01816) · [PDF](https://arxiv.org/pdf/2512.01816.pdf)  
**作者**：Juanxi Tian, Siyuan Li, Conghui He, Lijun Wu, Cheng Tan  

**一句话要点**：提出Envision因果事件进展基准，以解决多模态模型在动态过程建模中的局限性。

**关键词**：因果事件建模, 文本到多图像生成, 时空一致性评估, 世界知识内部化, 多模态基准测试

## 3 点简述
- 核心问题：现有模型依赖静态单图像生成，导致过拟合静态模式匹配，难以建模动态世界过程。
- 方法要点：基于世界知识和时空因果性，构建链式文本到多图像生成基准，包含1000个四阶段提示和Envision-Score评估指标。
- 实验或效果：评估15个模型，发现统一模型在因果叙事连贯性上优于专业模型，但仍落后于闭源模型且面临时空一致性挑战。

## 摘要（原文）

> Current multimodal models aim to transcend the limitations of single-modality representations by unifying understanding and generation, often using text-to-image (T2I) tasks to calibrate semantic consistency. However, their reliance on static, single-image generation in training and evaluation leads to overfitting to static pattern matching and semantic fusion, while fundamentally hindering their ability to model dynamic processes that unfold over time. To address these constraints, we propose Envision-a causal event progression benchmark for chained text-to-multi-image generation. Grounded in world knowledge and structured by spatiotemporal causality, it reorganizes existing evaluation dimensions and includes 1,000 four-stage prompts spanning six scientific and humanities domains. To transition evaluation from single images to sequential frames and assess whether models truly internalize world knowledge while adhering to causal-temporal constraints, we introduce Envision-Score, a holistic metric integrating multi-dimensional consistency, physicality, and aesthetics. Comprehensive evaluation of 15 models (10 specialized T2I models, 5 unified models) uncovers: specialized T2I models demonstrate proficiency in aesthetic rendering yet lack intrinsic world knowledge. Unified multimodal models bridge this gap, consistently outperforming specialized counterparts in causal narrative coherence. However, even these unified architectures remain subordinate to closed-source models and struggle to overcome the core challenge of spatiotemporal consistency. This demonstrates that a focus on causally-isolated single images impedes multi-frame reasoning and generation, promoting static pattern matching over dynamic world modeling-ultimately limiting world knowledge internalization, generation.

