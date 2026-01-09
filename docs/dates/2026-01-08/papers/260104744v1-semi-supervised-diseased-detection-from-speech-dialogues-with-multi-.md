---
layout: default
title: Semi-Supervised Diseased Detection from Speech Dialogues with Multi-Level Data Modeling
---

# Semi-Supervised Diseased Detection from Speech Dialogues with Multi-Level Data Modeling
**arXiv**：[2601.04744v1](https://arxiv.org/abs/2601.04744) · [PDF](https://arxiv.org/pdf/2601.04744.pdf)  
**作者**：Xingyuan Li, Mengyue Wu  

**一句话要点**：提出多级数据建模的半监督框架，从语音对话中检测疾病，解决弱监督和病理特征不均匀表达问题。

**关键词**：半监督学习, 语音医学检测, 多级数据建模, 弱监督学习, 伪标签生成, 数据高效学习

## 3 点简述
- 核心问题：语音医学检测面临弱监督、数据稀缺和病理特征在对话中不均匀表达的挑战。
- 方法要点：通过联合学习帧级、段级和会话级表示，动态聚合多粒度特征并生成高质量伪标签。
- 实验或效果：框架模型无关，跨语言和条件鲁棒，数据高效，仅用11个标注样本达到全监督性能的90%。

## 摘要（原文）

> Detecting medical conditions from speech acoustics is fundamentally a weakly-supervised learning problem: a single, often noisy, session-level label must be linked to nuanced patterns within a long, complex audio recording. This task is further hampered by severe data scarcity and the subjective nature of clinical annotations. While semi-supervised learning (SSL) offers a viable path to leverage unlabeled data, existing audio methods often fail to address the core challenge that pathological traits are not uniformly expressed in a patient's speech. We propose a novel, audio-only SSL framework that explicitly models this hierarchy by jointly learning from frame-level, segment-level, and session-level representations within unsegmented clinical dialogues. Our end-to-end approach dynamically aggregates these multi-granularity features and generates high-quality pseudo-labels to efficiently utilize unlabeled data. Extensive experiments show the framework is model-agnostic, robust across languages and conditions, and highly data-efficient-achieving, for instance, 90\% of fully-supervised performance using only 11 labeled samples. This work provides a principled approach to learning from weak, far-end supervision in medical speech analysis.

