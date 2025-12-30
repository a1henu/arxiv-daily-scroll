---
layout: default
title: UniHetero: Could Generation Enhance Understanding for Vision-Language-Model at Large Data Scale?
---

# UniHetero: Could Generation Enhance Understanding for Vision-Language-Model at Large Data Scale?
**arXiv**：[2512.23512v1](https://arxiv.org/abs/2512.23512) · [PDF](https://arxiv.org/pdf/2512.23512.pdf)  
**作者**：Fengjiao Chen, Minhao Jing, Weitao Lu, Yan Feng, Xiaoyu Li, Xuezhi Cao  

**一句话要点**：提出UniHetero模型，在大规模数据下探索生成任务对视觉语言模型理解能力的增强作用。

**关键词**：视觉语言模型, 生成增强理解, 大规模预训练, 语义生成, 数据缩放, 输入嵌入自回归

## 3 点简述
- 核心问题：生成任务是否能在大规模数据下增强视觉语言模型的理解能力。
- 方法要点：采用简洁结构UniHetero，在大规模预训练（>200M样本）中分析生成语义而非像素的效果。
- 实验或效果：发现生成语义能提升理解，展现优越的数据缩放趋势和更高数据利用率，输入嵌入自回归有效捕捉视觉细节。

## 摘要（原文）

> Vision-language large models are moving toward the unification of visual understanding and visual generation tasks. However, whether generation can enhance understanding is still under-explored on large data scale. In this work, we analysis the unified model with a concise structure, UniHetero, under large-scale pretraining (>200M samples). Our key observations are: (1) Generation can improve understanding, but Only if you generate Semantics, Not Pixels. (2) Generation reveals a superior Data Scaling trend and higher Data Utilization. (3) Autoregression on Input Embedding is effective to capture visual details.

