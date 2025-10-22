---
layout: default
title: AV-Master: Dual-Path Comprehensive Perception Makes Better Audio-Visual Question Answering
---

# AV-Master: Dual-Path Comprehensive Perception Makes Better Audio-Visual Question Answering
**arXiv**：[2510.18346v1](https://arxiv.org/abs/2510.18346) · [PDF](https://arxiv.org/pdf/2510.18346.pdf)  
**作者**：Jiayu Zhang, Qilang Ye, Shuo Ye, Xun Lin, Zihan Song, Zitong Yu  

**一句话要点**：提出AV-Master框架以解决音频视觉问答中的冗余和模态偏好问题

**关键词**：音频视觉问答, 动态采样, 模态偏好, 对比学习, 多模态融合

## 3 点简述
- 核心问题：现有方法在时间采样和模态偏好上缺乏灵活性，难以聚焦关键信息。
- 方法要点：引入动态自适应焦点采样和偏好感知策略，增强关键信息提取。
- 实验或效果：在四个大规模基准测试中显著优于现有方法，尤其在复杂推理任务。

## 摘要（原文）

> Audio-Visual Question Answering (AVQA) requires models to effectively utilize
> both visual and auditory modalities to answer complex and diverse questions
> about audio-visual scenes. However, existing methods lack sufficient
> flexibility and dynamic adaptability in temporal sampling and modality
> preference awareness, making it difficult to focus on key information based on
> the question. This limits their reasoning capability in complex scenarios. To
> address these challenges, we propose a novel framework named AV-Master. It
> enhances the model's ability to extract key information from complex
> audio-visual scenes with substantial redundant content by dynamically modeling
> both temporal and modality dimensions. In the temporal dimension, we introduce
> a dynamic adaptive focus sampling mechanism that progressively focuses on
> audio-visual segments most relevant to the question, effectively mitigating
> redundancy and segment fragmentation in traditional sampling methods. In the
> modality dimension, we propose a preference-aware strategy that models each
> modality's contribution independently, enabling selective activation of
> critical features. Furthermore, we introduce a dual-path contrastive loss to
> reinforce consistency and complementarity across temporal and modality
> dimensions, guiding the model to learn question-specific cross-modal
> collaborative representations. Experiments on four large-scale benchmarks show
> that AV-Master significantly outperforms existing methods, especially in
> complex reasoning tasks.

