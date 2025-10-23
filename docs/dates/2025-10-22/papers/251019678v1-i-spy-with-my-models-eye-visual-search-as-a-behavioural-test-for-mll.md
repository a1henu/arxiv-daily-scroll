---
layout: default
title: I Spy With My Model's Eye: Visual Search as a Behavioural Test for MLLMs
---

# I Spy With My Model's Eye: Visual Search as a Behavioural Test for MLLMs
**arXiv**：[2510.19678v1](https://arxiv.org/abs/2510.19678) · [PDF](https://arxiv.org/pdf/2510.19678.pdf)  
**作者**：John Burden, Jonathan Prunty, Ben Slater, Matthieu Tehenan, Greg Davis, Lucy Cheke  

**一句话要点**：提出视觉搜索作为行为测试，评估多模态大语言模型的感知机制。

**关键词**：多模态大语言模型, 视觉搜索, 弹出效应, 认知心理学, 机制评估, 场景先验

## 3 点简述
- 核心问题：多模态大语言模型的视觉处理机制不透明，现有评估难以揭示底层机制。
- 方法要点：借鉴认知心理学，采用经典视觉搜索范式测试模型是否表现出弹出效应。
- 实验或效果：模型在颜色或大小搜索中表现出人类类似弹出效应，并受场景先验影响。

## 摘要（原文）

> Multimodal large language models (MLLMs) achieve strong performance on
> vision-language tasks, yet their visual processing is opaque. Most black-box
> evaluations measure task accuracy, but reveal little about underlying
> mechanisms. Drawing on cognitive psychology, we adapt classic visual search
> paradigms -- originally developed to study human perception -- to test whether
> MLLMs exhibit the ``pop-out'' effect, where salient visual features are
> detected independently of distractor set size. Using controlled experiments
> targeting colour, size and lighting features, we find that advanced MLLMs
> exhibit human-like pop-out effects in colour or size-based disjunctive (single
> feature) search, as well as capacity limits for conjunctive (multiple feature)
> search. We also find evidence to suggest that MLLMs, like humans, incorporate
> natural scene priors such as lighting direction into object representations. We
> reinforce our findings using targeted fine-tuning and mechanistic
> interpretability analyses. Our work shows how visual search can serve as a
> cognitively grounded diagnostic tool for evaluating perceptual capabilities in
> MLLMs.

