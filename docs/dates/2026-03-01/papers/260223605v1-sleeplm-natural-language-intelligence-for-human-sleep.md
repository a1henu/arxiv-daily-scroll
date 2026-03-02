---
layout: default
title: SleepLM: Natural-Language Intelligence for Human Sleep
---

# SleepLM: Natural-Language Intelligence for Human Sleep
**arXiv**：[2602.23605v1](https://arxiv.org/abs/2602.23605) · [PDF](https://arxiv.org/pdf/2602.23605.pdf)  
**作者**：Zongzhe Xu, Zitao Shuai, Eideen Mozaffari, Ravi S. Aysola, Rajesh Kumar, Yuzhe Yang  

**一句话要点**：提出SleepLM睡眠语言基础模型，通过自然语言实现多导睡眠图的对齐、解释与交互。

**关键词**：睡眠语言模型, 多导睡眠图对齐, 跨模态学习, 零样本泛化, 睡眠描述生成

## 3 点简述
- 核心问题：基于学习的睡眠分析系统受限于封闭标签空间，无法描述或泛化新现象。
- 方法要点：引入多级睡眠描述生成流程，构建首个大规模睡眠-文本数据集，并采用统一预训练目标。
- 实验或效果：在零样本和少样本学习、跨模态检索及睡眠描述任务中优于现有方法，展现语言引导定位等能力。

## 摘要（原文）

> We present SleepLM, a family of sleep-language foundation models that enable human sleep alignment, interpretation, and interaction with natural language. Despite the critical role of sleep, learning-based sleep analysis systems operate in closed label spaces (e.g., predefined stages or events) and fail to describe, query, or generalize to novel sleep phenomena. SleepLM bridges natural language and multimodal polysomnography, enabling language-grounded representations of sleep physiology. To support this alignment, we introduce a multilevel sleep caption generation pipeline that enables the curation of the first large-scale sleep-text dataset, comprising over 100K hours of data from more than 10,000 individuals. Furthermore, we present a unified pretraining objective that combines contrastive alignment, caption generation, and signal reconstruction to better capture physiological fidelity and cross-modal interactions. Extensive experiments on real-world sleep understanding tasks verify that SleepLM outperforms state-of-the-art in zero-shot and few-shot learning, cross-modal retrieval, and sleep captioning. Importantly, SleepLM also exhibits intriguing capabilities including language-guided event localization, targeted insight generation, and zero-shot generalization to unseen tasks. All code and data will be open-sourced.

