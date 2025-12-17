---
layout: default
title: TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs
---

# TimeLens: Rethinking Video Temporal Grounding with Multimodal LLMs
**arXiv**：[2512.14698v1](https://arxiv.org/abs/2512.14698) · [PDF](https://arxiv.org/pdf/2512.14698.pdf)  
**作者**：Jun Zhang, Teng Wang, Yuying Ge, Yixiao Ge, Xinhao Li, Ying Shan, Limin Wang  

**一句话要点**：提出TimeLens基准与模型，通过高质量数据和算法设计提升视频时序定位能力。

**关键词**：视频时序定位, 多模态大语言模型, 基准数据集, 强化学习训练, 视频理解

## 3 点简述
- 核心问题：现有视频时序定位基准存在质量缺陷，影响多模态大语言模型优化。
- 方法要点：构建高质量数据集TimeLens-Bench和TimeLens-100K，并探索时间表示和训练范式等算法设计。
- 实验或效果：TimeLens模型在开源模型中达到最优性能，超越部分专有模型如GPT-5。

## 摘要（原文）

> This paper does not introduce a novel method but instead establishes a straightforward, incremental, yet essential baseline for video temporal grounding (VTG), a core capability in video understanding. While multimodal large language models (MLLMs) excel at various video understanding tasks, the recipes for optimizing them for VTG remain under-explored. In this paper, we present TimeLens, a systematic investigation into building MLLMs with strong VTG ability, along two primary dimensions: data quality and algorithmic design. We first expose critical quality issues in existing VTG benchmarks and introduce TimeLens-Bench, comprising meticulously re-annotated versions of three popular benchmarks with strict quality criteria. Our analysis reveals dramatic model re-rankings compared to legacy benchmarks, confirming the unreliability of prior evaluation standards. We also address noisy training data through an automated re-annotation pipeline, yielding TimeLens-100K, a large-scale, high-quality training dataset. Building on our data foundation, we conduct in-depth explorations of algorithmic design principles, yielding a series of meaningful insights and effective yet efficient practices. These include interleaved textual encoding for time representation, a thinking-free reinforcement learning with verifiable rewards (RLVR) approach as the training paradigm, and carefully designed recipes for RLVR training. These efforts culminate in TimeLens models, a family of MLLMs with state-of-the-art VTG performance among open-source models and even surpass proprietary models such as GPT-5 and Gemini-2.5-Flash. All codes, data, and models will be released to facilitate future research.

