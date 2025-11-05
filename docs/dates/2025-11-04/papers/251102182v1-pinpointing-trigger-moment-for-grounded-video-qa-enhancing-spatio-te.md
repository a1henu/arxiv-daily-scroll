---
layout: default
title: Pinpointing Trigger Moment for Grounded Video QA: Enhancing Spatio-temporal Grounding in Multimodal Large Language Models
---

# Pinpointing Trigger Moment for Grounded Video QA: Enhancing Spatio-temporal Grounding in Multimodal Large Language Models
**arXiv**：[2511.02182v1](https://arxiv.org/abs/2511.02182) · [PDF](https://arxiv.org/pdf/2511.02182.pdf)  
**作者**：Jinhwan Seo, Yoonki Cho, Junhyug Noh, Sung-eui Yoon  

**一句话要点**：提出触发时刻框架以增强多模态大语言模型在视频问答中的时空定位能力

**关键词**：视频问答, 时空定位, 多模态大语言模型, 触发时刻, 目标跟踪

## 3 点简述
- 核心问题：视频问答任务需模型进行复杂推理、视觉定位和时间跟踪。
- 方法要点：采用三阶段流水线，引入触发时刻作为目标对象最可见帧的锚点。
- 实验或效果：在GVQA任务中HOTA得分0.4968，显著优于去年获胜分数0.2704。

## 摘要（原文）

> In this technical report, we introduce a framework to address Grounded Video
> Question Answering (GVQA) task for the ICCV 2025 Perception Test Challenge. The
> GVQA task demands robust multimodal models capable of complex reasoning over
> video content, grounding the resulting answers visually, and tracking the
> referenced objects temporally. To achieve this capability, our proposed
> approach decomposes the GVQA task into a three-stage pipeline: (1) Video
> Reasoning \& QA, (2) Spatio-temporal Grounding and (3) Tracking. Our key
> contribution is the introduction of a trigger moment, derived from our proposed
> CORTEX prompt, which pinpoints the single most visible frame of a target object
> to serve as a robust anchor for grounding and tracking. To this end, we achieve
> the HOTA score of 0.4968, which marks a significant improvement over the
> previous year's winning score of 0.2704 on GVQA task.

