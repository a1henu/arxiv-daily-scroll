---
layout: default
title: MultiPriv: Benchmarking Individual-Level Privacy Reasoning in Vision-Language Models
---

# MultiPriv: Benchmarking Individual-Level Privacy Reasoning in Vision-Language Models
**arXiv**：[2511.16940v1](https://arxiv.org/abs/2511.16940) · [PDF](https://arxiv.org/pdf/2511.16940.pdf)  
**作者**：Xiongtao Sun, Hui Li, Jiaming Zhang, Yujie Yang, Kaili Liu, Ruxin Feng, Wen Jun Tan, Wei Yang Bryan Lim  

**一句话要点**：提出MultiPriv基准以评估视觉语言模型中的个体级隐私推理风险

**关键词**：视觉语言模型, 隐私推理基准, 个体档案构建, 多模态数据集, 安全对齐评估, 隐私风险分析

## 3 点简述
- 核心问题：现有隐私基准无法评估VLMs从分布式信息推断个体档案的推理风险
- 方法要点：构建双语多模态数据集，包含合成个体档案，支持九项隐私推理任务
- 实验或效果：评估50多个VLMs，揭示推理风险高、感知指标预测差、安全对齐无效

## 摘要（原文）

> Modern Vision-Language Models (VLMs) demonstrate sophisticated reasoning, escalating privacy risks beyond simple attribute perception to individual-level linkage. Current privacy benchmarks are structurally insufficient for this new threat, as they primarily evaluate privacy perception while failing to address the more critical risk of privacy reasoning: a VLM's ability to infer and link distributed information to construct individual profiles. To address this critical gap, we propose \textbf{MultiPriv}, the first benchmark designed to systematically evaluate individual-level privacy reasoning in VLMs. We introduce the \textbf{Privacy Perception and Reasoning (PPR)} framework and construct a novel, bilingual multimodal dataset to support it. The dataset uniquely features a core component of synthetic individual profiles where identifiers (e.g., faces, names) are meticulously linked to sensitive attributes. This design enables nine challenging tasks evaluating the full PPR spectrum, from attribute detection to cross-image re-identification and chained inference. We conduct a large-scale evaluation of over 50 foundational and commercial VLMs. Our analysis reveals: (1) Many VLMs possess significant, unmeasured reasoning-based privacy risks. (2) Perception-level metrics are poor predictors of these reasoning risks, revealing a critical evaluation gap. (3) Existing safety alignments are inconsistent and ineffective against such reasoning-based attacks. MultiPriv exposes systemic vulnerabilities and provides the necessary framework for developing robust, privacy-preserving VLMs.

