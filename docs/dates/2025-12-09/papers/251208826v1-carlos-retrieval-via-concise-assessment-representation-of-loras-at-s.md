---
layout: default
title: CARLoS: Retrieval via Concise Assessment Representation of LoRAs at Scale
---

# CARLoS: Retrieval via Concise Assessment Representation of LoRAs at Scale
**arXiv**：[2512.08826v1](https://arxiv.org/abs/2512.08826) · [PDF](https://arxiv.org/pdf/2512.08826.pdf)  
**作者**：Shahar Sarfaty, Adi Haviv, Uri Hacohen, Niva Elkin-Koren, Roi Livni, Amit H. Bermano  

**一句话要点**：提出CARLoS框架，通过简洁评估表示实现大规模LoRA检索，解决依赖不可靠元数据的问题。

**关键词**：LoRA检索, 生成组件评估, CLIP嵌入, 语义匹配, 版权分析, 大规模框架

## 3 点简述
- 核心问题：LoRA生态系统庞大但无序，现有发现方法依赖不可靠用户描述或流行度指标，影响可用性。
- 方法要点：分析650多个LoRA，基于CLIP嵌入差异定义三部分表示：方向、强度和一致性，用于语义检索。
- 实验或效果：在自动和人工评估中优于文本基线，支持检索并链接到版权法律概念，提升LoRA分析实用性。

## 摘要（原文）

> The rapid proliferation of generative components, such as LoRAs, has created a vast but unstructured ecosystem. Existing discovery methods depend on unreliable user descriptions or biased popularity metrics, hindering usability. We present CARLoS, a large-scale framework for characterizing LoRAs without requiring additional metadata. Analyzing over 650 LoRAs, we employ them in image generation over a variety of prompts and seeds, as a credible way to assess their behavior. Using CLIP embeddings and their difference to a base-model generation, we concisely define a three-part representation: Directions, defining semantic shift; Strength, quantifying the significance of the effect; and Consistency, quantifying how stable the effect is. Using these representations, we develop an efficient retrieval framework that semantically matches textual queries to relevant LoRAs while filtering overly strong or unstable ones, outperforming textual baselines in automated and human evaluations. While retrieval is our primary focus, the same representation also supports analyses linking Strength and Consistency to legal notions of substantiality and volition, key considerations in copyright, positioning CARLoS as a practical system with broader relevance for LoRA analysis.

