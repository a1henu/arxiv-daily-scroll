---
layout: default
title: Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization
---

# Don't Blind Your VLA: Aligning Visual Representations for OOD Generalization
**arXiv**：[2510.25616v1](https://arxiv.org/abs/2510.25616) · [PDF](https://arxiv.org/pdf/2510.25616.pdf)  
**作者**：Nikita Kachaev, Mikhail Kolosov, Daniil Zelezetsky, Alexey K. Kovalev, Aleksandr I. Panov  

**一句话要点**：提出视觉表示对齐方法以缓解VLA微调中的视觉表示退化问题

**关键词**：视觉语言动作模型, 表示对齐, 微调退化, OOD泛化, 视觉表示分析

## 3 点简述
- 核心问题：VLA模型在动作微调中视觉表示退化，影响泛化能力
- 方法要点：设计对齐策略，对比VLA与VLM，保留视觉语言能力
- 实验或效果：评估OOD泛化，方法有效缓解退化并提升性能

## 摘要（原文）

> The growing success of Vision-Language-Action (VLA) models stems from the
> promise that pretrained Vision-Language Models (VLMs) can endow agents with
> transferable world knowledge and vision-language (VL) grounding, laying a
> foundation for action models with broader generalization. Yet when these VLMs
> are adapted to the action modality, it remains unclear to what extent their
> original VL representations and knowledge are preserved. In this work, we
> conduct a systematic study of representation retention during VLA fine-tuning,
> showing that naive action fine-tuning leads to degradation of visual
> representations. To characterize and measure these effects, we probe VLA's
> hidden representations and analyze attention maps, further, we design a set of
> targeted tasks and methods that contrast VLA models with their counterpart
> VLMs, isolating changes in VL capabilities induced by action fine-tuning. We
> further evaluate a range of strategies for aligning visual representations and
> introduce a simple yet effective method that mitigates degradation and yields
> improved generalization to out-of-distribution (OOD) scenarios. Taken together,
> our analysis clarifies the trade-off between action fine-tuning and the
> degradation of VL representations and highlights practical approaches to
> recover inherited VL capabilities. Code is publicly available:
> https://blind-vla-paper.github.io

