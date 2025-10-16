---
layout: default
title: What "Not" to Detect: Negation-Aware VLMs via Structured Reasoning and Token Merging
---

# What "Not" to Detect: Negation-Aware VLMs via Structured Reasoning and Token Merging
**arXiv**：[2510.13232v1](https://arxiv.org/abs/2510.13232) · [PDF](https://arxiv.org/pdf/2510.13232.pdf)  
**作者**：Inha Kang, Youngsun Lim, Seonho Lee, Jiho Choi, Junsuk Choe, Hyunjung Shim  

**一句话要点**：提出NegToMe和CoVAND以解决视觉语言模型在否定理解中的肯定偏见问题

**关键词**：否定理解, 视觉语言模型, 令牌合并, 描述对象检测, 参数高效微调, 数据集构建

## 3 点简述
- 核心问题：视觉语言模型存在肯定偏见，难以理解否定，影响描述对象检测任务。
- 方法要点：引入NegToMe模块，通过令牌合并保留否定语义；构建CoVAND数据集生成高质量否定数据。
- 实验或效果：在否定基准测试中显著提升性能，NMS-AP最高增加10.8点，降低误报率。

## 摘要（原文）

> State-of-the-art vision-language models (VLMs) suffer from a critical failure
> in understanding negation, often referred to as affirmative bias. This
> limitation is particularly severe in described object detection (DOD) tasks. To
> address this, we propose two primary contributions: (1) a new dataset pipeline
> and (2) a novel, lightweight adaptation recipe. First, we introduce CoVAND, a
> dataset constructed with a systematic chain-of-thought (CoT) and VQA-based
> pipeline to generate high-quality, instance-grounded negation data. Second, we
> propose NegToMe, a novel text token merging module that directly tackles the
> architectural cause of affirmative bias. NegToMe fundamentally addresses the
> structural loss of negation cues in tokenization, grouping them with attributes
> into coherent semantic phrases. It maintains correct polarity at the input
> level, enabling robust negation understanding even with limited data. For
> instance, to prevent a model from treating the fragmented tokens "not" and
> "girl" as simply "girl", NegToMe binds them into a single token whose meaning
> is correctly distinguished from that of "girl" alone. This module is integrated
> with a parameter-efficient and strategic LoRA fine-tuning approach. Our method
> significantly improves performance on challenging negation benchmarks with a
> lowered false positive rate, boosting NMS-AP by up to +10.8 points on OVDEval
> and demonstrating generalization to SoTA VLMs. This work marks a crucial step
> forward in addressing negation understanding for real-world detection
> applications.

