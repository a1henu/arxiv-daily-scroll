---
layout: default
title: From Synthetic Scenes to Real Performance: Enhancing Spatial Reasoning in VLMs
---

# From Synthetic Scenes to Real Performance: Enhancing Spatial Reasoning in VLMs
**arXiv**：[2511.11440v1](https://arxiv.org/abs/2511.11440) · [PDF](https://arxiv.org/pdf/2511.11440.pdf)  
**作者**：Massimo Rizzoli, Simone Alghisi, Seyed Mahed Mousavi, Giuseppe Riccardi  

**一句话要点**：提出基于合成数据的VLM微调方法以增强空间推理性能

**关键词**：视觉语言模型, 合成数据生成, 空间推理, 微调优化, 分布平衡

## 3 点简述
- 核心问题：真实数据微调易产生偏差、分布不均和过拟合
- 方法要点：控制合成数据生成，确保属性多样和标注无偏
- 实验或效果：合成微调提升真实数据性能，优于匹配设置

## 摘要（原文）

> Fine-tuning Vision-Language Models (VLMs) is a common strategy to improve performance following an ad-hoc data collection and annotation of real-world scenes. However, this process is often prone to biases, errors, and distribution imbalance, resulting in overfitting and imbalanced performance. Although a few studies have tried to address this problem by generating synthetic data, they lacked control over distribution bias and annotation quality. To address these challenges, we redesign the fine-tuning process in two ways. First, we control the generation of data and its annotations, ensuring it is free from bias, distribution imbalance, and annotation errors. We automatically construct the dataset by comprehensively sampling objects' attributes, including color, shape, size, and position within the scene. Secondly, using this annotated dataset, we fine-tune state-of-the-art VLMs and assess performance transferability to real-world data on the absolute position task. We conduct exhaustive evaluations on both synthetic and real-world benchmarks. Our experiments reveal two key findings: 1) fine-tuning on balanced synthetic data yields uniform performance across the visual scene and mitigates common biases; and 2) fine-tuning on synthetic stimuli significantly improves performance on real-world data (COCO), outperforming models fine-tuned in the matched setting.

