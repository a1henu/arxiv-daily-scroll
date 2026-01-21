---
layout: default
title: PREFAB: PREFerence-based Affective Modeling for Low-Budget Self-Annotation
---

# PREFAB: PREFerence-based Affective Modeling for Low-Budget Self-Annotation
**arXiv**：[2601.13904v1](https://arxiv.org/abs/2601.13904) · [PDF](https://arxiv.org/pdf/2601.13904.pdf)  
**作者**：Jaeyoung Moon, Youjin Choi, Yucheon Park, David Melhart, Georgios N. Yannakakis, Kyung-Joong Kim  

**一句话要点**：提出PREFAB方法，基于偏好学习建模情感变化，实现低预算自标注以减轻标注负担。

**关键词**：情感计算, 自标注方法, 偏好学习, 低预算标注, 情感建模

## 3 点简述
- 核心问题：传统全标注方法耗时且易疲劳，影响情感计算数据收集效率。
- 方法要点：结合峰值-终值规则和序数情感表示，通过偏好学习检测情感变化区域，仅标注关键片段。
- 实验或效果：技术性能与用户研究显示，PREFAB在建模情感变化上优于基线，减轻工作负担并提升标注信心。

## 摘要（原文）

> Self-annotation is the gold standard for collecting affective state labels in affective computing. Existing methods typically rely on full annotation, requiring users to continuously label affective states across entire sessions. While this process yields fine-grained data, it is time-consuming, cognitively demanding, and prone to fatigue and errors. To address these issues, we present PREFAB, a low-budget retrospective self-annotation method that targets affective inflection regions rather than full annotation. Grounded in the peak-end rule and ordinal representations of emotion, PREFAB employs a preference-learning model to detect relative affective changes, directing annotators to label only selected segments while interpolating the remainder of the stimulus. We further introduce a preview mechanism that provides brief contextual cues to assist annotation. We evaluate PREFAB through a technical performance study and a 25-participant user study. Results show that PREFAB outperforms baselines in modeling affective inflections while mitigating workload (and conditionally mitigating temporal burden). Importantly PREFAB improves annotator confidence without degrading annotation quality.

