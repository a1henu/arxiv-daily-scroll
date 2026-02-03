---
layout: default
title: MentisOculi: Revealing the Limits of Reasoning with Mental Imagery
---

# MentisOculi: Revealing the Limits of Reasoning with Mental Imagery
**arXiv**：[2602.02465v1](https://arxiv.org/abs/2602.02465) · [PDF](https://arxiv.org/pdf/2602.02465.pdf)  
**作者**：Jana Zeller, Thaddäus Wiedemer, Fanfei Li, Thomas Klein, Prasanna Mayilvahanan, Matthias Bethge, Felix Wichmann, Ryan Cotterell, Wieland Brendel  

**一句话要点**：提出MentisOculi以评估统一多模态模型在视觉辅助推理中的局限性

**关键词**：统一多模态模型, 视觉推理, 多步问题解决, 生成错误分析, 模型评估基准

## 3 点简述
- 核心问题：评估统一多模态模型利用视觉化进行多步推理的能力
- 方法要点：开发分层多步推理问题套件，测试从潜在标记到显式生成图像的视觉策略
- 实验或效果：发现视觉策略通常无法提升性能，模型存在生成错误累积和无法利用真实视觉化的问题

## 摘要（原文）

> Frontier models are transitioning from multimodal large language models (MLLMs) that merely ingest visual information to unified multimodal models (UMMs) capable of native interleaved generation. This shift has sparked interest in using intermediate visualizations as a reasoning aid, akin to human mental imagery. Central to this idea is the ability to form, maintain, and manipulate visual representations in a goal-oriented manner. To evaluate and probe this capability, we develop MentisOculi, a procedural, stratified suite of multi-step reasoning problems amenable to visual solution, tuned to challenge frontier models. Evaluating visual strategies ranging from latent tokens to explicit generated imagery, we find they generally fail to improve performance. Analysis of UMMs specifically exposes a critical limitation: While they possess the textual reasoning capacity to solve a task and can sometimes generate correct visuals, they suffer from compounding generation errors and fail to leverage even ground-truth visualizations. Our findings suggest that despite their inherent appeal, visual thoughts do not yet benefit model reasoning. MentisOculi establishes the necessary foundation to analyze and close this gap across diverse model families.

