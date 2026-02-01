---
layout: default
title: Understanding Multimodal Complementarity for Single-Frame Action Anticipation
---

# Understanding Multimodal Complementarity for Single-Frame Action Anticipation
**arXiv**：[2601.22039v1](https://arxiv.org/abs/2601.22039) · [PDF](https://arxiv.org/pdf/2601.22039.pdf)  
**作者**：Manuel Benavent-Lledo, Konstantinos Bacharidis, Konstantinos Papoutsakis, Antonis Argyros, Jose Garcia-Rodriguez  

**一句话要点**：提出AAG+框架，通过单帧多模态融合实现动作预测，性能媲美视频方法。

**关键词**：单帧动作预测, 多模态融合, 动作历史建模, 关键帧选择, 时序建模分析

## 3 点简述
- 研究单帧动作预测的信息潜力，挑战密集时序建模的必要性。
- 系统分析RGB、深度和语义历史等多模态信息融合策略。
- 在IKEA-ASM等基准上，AAG+超越原AAG，性能接近或优于视频方法。

## 摘要（原文）

> Human action anticipation is commonly treated as a video understanding problem, implicitly assuming that dense temporal information is required to reason about future actions. In this work, we challenge this assumption by investigating what can be achieved when action anticipation is constrained to a single visual observation. We ask a fundamental question: how much information about the future is already encoded in a single frame, and how can it be effectively exploited? Building on our prior work on Action Anticipation at a Glimpse (AAG), we conduct a systematic investigation of single-frame action anticipation enriched with complementary sources of information. We analyze the contribution of RGB appearance, depth-based geometric cues, and semantic representations of past actions, and investigate how different multimodal fusion strategies, keyframe selection policies and past-action history sources influence anticipation performance. Guided by these findings, we consolidate the most effective design choices into AAG+, a refined single-frame anticipation framework. Despite operating on a single frame, AAG+ consistently improves upon the original AAG and achieves performance comparable to, or exceeding, that of state-of-the-art video-based methods on challenging anticipation benchmarks including IKEA-ASM, Meccano and Assembly101. Our results offer new insights into the limits and potential of single-frame action anticipation, and clarify when dense temporal modeling is necessary and when a carefully selected glimpse is sufficient.

