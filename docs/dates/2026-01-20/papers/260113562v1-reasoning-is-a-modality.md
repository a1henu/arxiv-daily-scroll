---
layout: default
title: Reasoning is a Modality
---

# Reasoning is a Modality
**arXiv**：[2601.13562v1](https://arxiv.org/abs/2601.13562) · [PDF](https://arxiv.org/pdf/2601.13562.pdf)  
**作者**：Zhiguang Liu, Yi Shang  

**一句话要点**：提出角色分离Transformer块，在视觉推理任务中实现超越人类平均性能

**关键词**：抽象推理, 视觉推理, Transformer架构, 角色分离, ARC任务, 可解释AI

## 3 点简述
- 核心问题：AI系统缺乏可解释的内部状态，与人类推理存在差距
- 方法要点：设计角色分离Transformer块，分离全局控制器与网格工作空间令牌
- 实验或效果：在ARC-1任务上达到62.6%准确率，优于人类平均和基线方法

## 摘要（原文）

> The Abstraction and Reasoning Corpus (ARC) provides a compact laboratory for studying abstract reasoning, an ability central to human intelligence. Modern AI systems, including LLMs and ViTs, largely operate as sequence-of-behavior prediction machines: they match observable behaviors by modeling token statistics without a persistent, readable mental state. This creates a gap with human-like behavior: humans can explain an action by decoding internal state, while AI systems can produce fluent post-hoc rationalizations that are not grounded in such a state. We hypothesize that reasoning is a modality: reasoning should exist as a distinct channel separate from the low-level workspace on which rules are applied. To test this hypothesis, on solving ARC tasks as a visual reasoning problem, we designed a novel role-separated transformer block that splits global controller tokens from grid workspace tokens, enabling iterative rule execution. Trained and evaluated within the VARC vision-centric protocol, our method achieved 62.6% accuracy on ARC-1, surpassing average human performance (60.2%) and outperforming prior methods significantly. Qualitatively, our models exhibit more coherent rule-application structure than the dense ViT baseline, consistent with a shift away from plausible probability blobs toward controller-driven reasoning.

