---
layout: default
title: IIR-VLM: In-Context Instance-level Recognition for Large Vision-Language Models
---

# IIR-VLM: In-Context Instance-level Recognition for Large Vision-Language Models
**arXiv**：[2601.14188v1](https://arxiv.org/abs/2601.14188) · [PDF](https://arxiv.org/pdf/2601.14188.pdf)  
**作者**：Liang Shi, Wei Li, Kevin M Beussman, Lin Chen, Yun Fu  

**一句话要点**：提出IIR-VLM以增强大视觉语言模型在上下文中的实例级识别能力

**关键词**：实例级识别, 视觉语言模型, 上下文学习, 单样本学习, 辅助视觉编码器

## 3 点简述
- 核心问题：大视觉语言模型在实例级识别任务中表现不佳，远逊于领域专用模型，限制了实际应用。
- 方法要点：集成预训练实例级识别专家模型作为辅助视觉编码器，提供专业特征，支持单样本上下文学习。
- 实验或效果：在现有基准上验证有效性，并在新挑战基准上展示优于其他方法的实例级识别性能。

## 摘要（原文）

> Instance-level recognition (ILR) concerns distinguishing individual instances from one another, with person re-identification as a prominent example. Despite the impressive visual perception capabilities of modern VLMs, we find their performance on ILR unsatisfactory, often dramatically underperforming domain-specific ILR models. This limitation hinders many practical application of VLMs, e.g. where recognizing familiar people and objects is crucial for effective visual understanding. Existing solutions typically learn to recognize instances one at a time using instance-specific datasets, which not only incur substantial data collection and training costs but also struggle with fine-grained discrimination. In this work, we propose IIR-VLM, a VLM enhanced for In-context Instance-level Recognition. We integrate pre-trained ILR expert models as auxiliary visual encoders to provide specialized features for learning diverse instances, which enables VLMs to learn new instances in-context in a one-shot manner. Further, IIR-VLM leverages this knowledge for instance-aware visual understanding. We validate IIR-VLM's efficacy on existing instance personalization benchmarks. Finally, we demonstrate its superior ILR performance on a challenging new benchmark, which assesses ILR capabilities across varying difficulty and diverse categories, with person, face, pet and general objects as the instances at task.

