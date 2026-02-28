---
layout: default
title: Same Words, Different Judgments: Modality Effects on Preference Alignment
---

# Same Words, Different Judgments: Modality Effects on Preference Alignment
**arXiv**：[2602.22710v1](https://arxiv.org/abs/2602.22710) · [PDF](https://arxiv.org/pdf/2602.22710.pdf)  
**作者**：Aaron Broukhim, Nadir Weibel, Eshin Jolly  

**一句话要点**：比较文本与音频模态下偏好对齐的可靠性，揭示模态对判断的影响并验证合成评分的有效性。

**关键词**：偏好强化学习, 跨模态对齐, 音频偏好评估, 合成评分, 人类判断可靠性, 模态效应

## 3 点简述
- 核心问题：偏好强化学习在语音模态中的应用不足，模态如何影响人类偏好判断。
- 方法要点：通过100个提示的跨模态实验，对比人类与合成偏好注释的可靠性。
- 实验或效果：音频偏好可靠性高，模态改变判断标准，合成评分与人类对齐且可预测一致性。

## 摘要（原文）

> Preference-based reinforcement learning (PbRL) is the dominant framework for aligning AI systems to human preferences, but its application to speech remains underexplored. We present a controlled cross-modal study of human and synthetic preference annotations, comparing text and audio evaluations of identical semantic content across 100 prompts. Audio preferences prove as reliable as text, with inter-rater agreement reaching good levels (ICC(2,k) $\approx$ .80) at $\sim$9 raters -- the first ICC-based reliability characterization in the preference annotation literature for either modality. However, modality reshapes how people judge: audio raters exhibit narrower decision thresholds, reduced length bias, and more user-oriented evaluation criteria, with near-chance cross-modality agreement. Synthetic ratings further align with human judgments and predict inter-rater agreement, supporting their use both for triaging ambiguous pairs and as full replacements for human annotations.

