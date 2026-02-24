---
layout: default
title: CountEx: Fine-Grained Counting via Exemplars and Exclusion
---

# CountEx: Fine-Grained Counting via Exemplars and Exclusion
**arXiv**：[2602.19432v1](https://arxiv.org/abs/2602.19432) · [PDF](https://arxiv.org/pdf/2602.19432.pdf)  
**作者**：Yifeng Huang, Gia Khanh Nguyen, Minh Hoai  

**一句话要点**：提出CountEx框架，通过包含与排除提示解决视觉计数中相似干扰物导致的过计数问题。

**关键词**：视觉计数, 多模态提示, 判别性查询细化, CoCount基准, 细粒度计数

## 3 点简述
- 核心问题：现有基于提示的计数方法无法明确排除视觉相似干扰物，在杂乱场景中易产生歧义和过计数。
- 方法要点：引入多模态提示（自然语言描述和可选视觉示例）表达包含与排除意图，采用判别性查询细化模块联合推理并抑制干扰特征。
- 实验或效果：在CoCount基准上优于现有方法，支持已知和新类别计数，数据和代码已开源。

## 摘要（原文）

> This paper presents CountEx, a discriminative visual counting framework designed to address a key limitation of existing prompt-based methods: the inability to explicitly exclude visually similar distractors. While current approaches allow users to specify what to count via inclusion prompts, they often struggle in cluttered scenes with confusable object categories, leading to ambiguity and overcounting. CountEx enables users to express both inclusion and exclusion intent, specifying what to count and what to ignore, through multimodal prompts including natural language descriptions and optional visual exemplars. At the core of CountEx is a novel Discriminative Query Refinement module, which jointly reasons over inclusion and exclusion cues by first identifying shared visual features, then isolating exclusion-specific patterns, and finally applying selective suppression to refine the counting query. To support systematic evaluation of fine-grained counting methods, we introduce CoCount, a benchmark comprising 1,780 videos and 10,086 annotated frames across 97 category pairs. Experiments show that CountEx achieves substantial improvements over state-of-the-art methods for counting objects from both known and novel categories. The data and code are available at https://github.com/bbvisual/CountEx.

