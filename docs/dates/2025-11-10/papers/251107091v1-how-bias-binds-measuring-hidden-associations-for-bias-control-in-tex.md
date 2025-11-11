---
layout: default
title: How Bias Binds: Measuring Hidden Associations for Bias Control in Text-to-Image Compositions
---

# How Bias Binds: Measuring Hidden Associations for Bias Control in Text-to-Image Compositions
**arXiv**：[2511.07091v1](https://arxiv.org/abs/2511.07091) · [PDF](https://arxiv.org/pdf/2511.07091.pdf)  
**作者**：Jeng-Lin Li, Ming-Ching Chang, Wei-Chao Chen  

**一句话要点**：提出偏差依从分数与上下文偏差控制框架以解决文本到图像生成中的语义绑定偏差问题

**关键词**：文本到图像生成, 偏差测量, 语义绑定, 去偏控制, 组合生成, 上下文关联

## 3 点简述
- 核心问题：文本到图像模型在语义绑定中偏差被放大，现有方法忽略对象与属性的联合效应。
- 方法要点：引入偏差依从分数量化偏差，开发无需训练的上下文偏差控制框架。
- 实验或效果：在组合生成任务中偏差减少超过10%，揭示去偏与语义保持的挑战。

## 摘要（原文）

> Text-to-image generative models often exhibit bias related to sensitive
> attributes. However, current research tends to focus narrowly on single-object
> prompts with limited contextual diversity. In reality, each object or attribute
> within a prompt can contribute to bias. For example, the prompt "an assistant
> wearing a pink hat" may reflect female-inclined biases associated with a pink
> hat. The neglected joint effects of the semantic binding in the prompts cause
> significant failures in current debiasing approaches. This work initiates a
> preliminary investigation on how bias manifests under semantic binding, where
> contextual associations between objects and attributes influence generative
> outcomes. We demonstrate that the underlying bias distribution can be amplified
> based on these associations. Therefore, we introduce a bias adherence score
> that quantifies how specific object-attribute bindings activate bias. To delve
> deeper, we develop a training-free context-bias control framework to explore
> how token decoupling can facilitate the debiasing of semantic bindings. This
> framework achieves over 10% debiasing improvement in compositional generation
> tasks. Our analysis of bias scores across various attribute-object bindings and
> token decorrelation highlights a fundamental challenge: reducing bias without
> disrupting essential semantic relationships. These findings expose critical
> limitations in current debiasing approaches when applied to semantically bound
> contexts, underscoring the need to reassess prevailing bias mitigation
> strategies.

