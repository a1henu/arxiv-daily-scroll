---
layout: default
title: 3D-DRES: Detailed 3D Referring Expression Segmentation
---

# 3D-DRES: Detailed 3D Referring Expression Segmentation
**arXiv**：[2603.02896v1](https://arxiv.org/abs/2603.02896) · [PDF](https://arxiv.org/pdf/2603.02896.pdf)  
**作者**：Qi Chen, Changli Wu, Jiayi Ji, Yiwei Ma, Liujuan Cao  

**一句话要点**：提出3D-DRES任务与DetailRefer数据集，以增强细粒度3D视觉语言理解。

**关键词**：3D视觉语言理解, 短语级分割, 数据集构建, 双模分割架构, 细粒度标注

## 3 点简述
- 核心问题：现有3D视觉定位任务仅处理句子级检测或分割，未能利用自然语言表达中的丰富组合上下文推理。
- 方法要点：引入DetailRefer数据集，采用短语-实例标注范式，并设计DetailBase基线架构支持句子和短语级双模分割。
- 实验或效果：在DetailRefer上训练的模型在短语级分割表现出色，并在传统3D-RES基准上带来意外提升。

## 摘要（原文）

> Current 3D visual grounding tasks only process sentence level detection or segmentation, which critically fails to leverage the rich compositional contextual reasonings within natural language expressions. To address this challenge, we introduce Detailed 3D Referring Expression Segmentation (3D-DRES), a new task that provides a phrase to 3D instance mapping, aiming at enhancing fine-grained 3D vision language understanding. To support 3D-DRES, we present DetailRefer, a new dataset comprising 54,432 descriptions spanning 11,054 distinct objects. Unlike previous datasets, DetailRefer implements a pioneering phrase-instance annotation paradigm where each referenced noun phrase is explicitly mapped to its corresponding 3D elements. Additionally, we introduce DetailBase, a purposefully streamlined yet effective baseline architecture that supports dual-mode segmentation at both sentence and phrase levels. Our experimental results demonstrate that models trained on DetailRefer not only excel at phrase-level segmentation but also show surprising improvements on traditional 3D-RES benchmarks.

