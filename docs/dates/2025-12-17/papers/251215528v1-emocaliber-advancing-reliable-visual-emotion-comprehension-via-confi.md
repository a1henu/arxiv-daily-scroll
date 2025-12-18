---
layout: default
title: EmoCaliber: Advancing Reliable Visual Emotion Comprehension via Confidence Verbalization and Calibration
---

# EmoCaliber: Advancing Reliable Visual Emotion Comprehension via Confidence Verbalization and Calibration
**arXiv**：[2512.15528v1](https://arxiv.org/abs/2512.15528) · [PDF](https://arxiv.org/pdf/2512.15528.pdf)  
**作者**：Daiqing Wu, Dongbao Yang, Can Ma. Yu Zhou  

**一句话要点**：提出EmoCaliber，通过置信度表达与校准提升视觉情感理解的可靠性。

**关键词**：视觉情感理解, 多模态大语言模型, 置信度校准, 情感感知主观性, 结构化推理

## 3 点简述
- 核心问题：现有MLLMs在视觉情感理解中忽略情感感知的主观性，缺乏对替代解释的考虑。
- 方法要点：引入三阶段训练框架，使MLLMs具备结构化推理、置信度表达和校准能力。
- 实验或效果：在VECBench基准上，EmoCaliber在情感预测和置信度估计方面优于现有方法。

## 摘要（原文）

> Visual Emotion Comprehension (VEC) aims to infer sentiment polarities or emotion categories from affective cues embedded in images. In recent years, Multimodal Large Language Models (MLLMs) have established a popular paradigm in VEC, leveraging their generalizability to unify VEC tasks defined under diverse emotion taxonomies. While this paradigm achieves notable success, it typically formulates VEC as a deterministic task, requiring the model to output a single, definitive emotion label for each image. Such a formulation insufficiently accounts for the inherent subjectivity of emotion perception, overlooking alternative interpretations that may be equally plausible to different viewers. To address this limitation, we propose equipping MLLMs with capabilities to verbalize their confidence in emotion predictions. This additional signal provides users with an estimate of both the plausibility of alternative interpretations and the MLLMs' self-assessed competence, thereby enhancing reliability in practice. Building on this insight, we introduce a three-stage training framework that progressively endows with structured reasoning, teaches to verbalize confidence, and calibrates confidence expression, culminating in EmoCaliber, a confidence-aware MLLM for VEC. Through fair and comprehensive evaluations on the unified benchmark VECBench, EmoCaliber demonstrates overall superiority against existing methods in both emotion prediction and confidence estimation. These results validate the effectiveness of our approach and mark a feasible step toward more reliable VEC systems. Project page: https://github.com/wdqqdw/EmoCaliber.

