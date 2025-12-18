---
layout: default
title: On the Effectiveness of Textual Prompting with Lightweight Fine-Tuning for SAM3 Remote Sensing Segmentation
---

# On the Effectiveness of Textual Prompting with Lightweight Fine-Tuning for SAM3 Remote Sensing Segmentation
**arXiv**：[2512.15564v1](https://arxiv.org/abs/2512.15564) · [PDF](https://arxiv.org/pdf/2512.15564.pdf)  
**作者**：Roni Blushtein-Livnon, Osher Rafaeli, David Ioffe, Amir Boger, Karen Sandberg Esquenazi, Tal Svoray  

**一句话要点**：评估SAM3在遥感图像分割中基于文本提示与轻量微调的有效性，结合几何提示提升性能。

**关键词**：遥感图像分割, SAM3框架, 文本提示, 几何提示, 轻量微调, 零样本推理

## 3 点简述
- 遥感图像分割面临标注数据有限和基础模型训练图像差异的挑战，需在有限监督下有效适应。
- SAM3框架通过文本提示生成掩码，无需任务特定修改，评估了文本、几何和混合提示策略及轻量微调效果。
- 实验表明语义与几何提示结合性能最佳，文本提示对不规则目标效果较差，轻量微调在几何规则目标上提供实用权衡。

## 摘要（原文）

> Remote sensing (RS) image segmentation is constrained by the limited availability of annotated data and a gap between overhead imagery and natural images used to train foundational models. This motivates effective adaptation under limited supervision. SAM3 concept-driven framework generates masks from textual prompts without requiring task-specific modifications, which may enable this adaptation. We evaluate SAM3 for RS imagery across four target types, comparing textual, geometric, and hybrid prompting strategies, under lightweight fine-tuning scales with increasing supervision, alongside zero-shot inference. Results show that combining semantic and geometric cues yields the highest performance across targets and metrics. Text-only prompting exhibits the lowest performance, with marked score gaps for irregularly shaped targets, reflecting limited semantic alignment between SAM3 textual representations and their overhead appearances. Nevertheless, textual prompting with light fine-tuning offers a practical performance-effort trade-off for geometrically regular and visually salient targets. Across targets, performance improves between zero-shot inference and fine-tuning, followed by diminishing returns as the supervision scale increases. Namely, a modest geometric annotation effort is sufficient for effective adaptation. A persistent gap between Precision and IoU further indicates that under-segmentation and boundary inaccuracies remain prevalent error patterns in RS tasks, particularly for irregular and less prevalent targets.

