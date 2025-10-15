---
layout: default
title: VISaGE: Understanding Visual Generics and Exceptions
---

# VISaGE: Understanding Visual Generics and Exceptions
**arXiv**：[2510.12548v1](https://arxiv.org/abs/2510.12548) · [PDF](https://arxiv.org/pdf/2510.12548.pdf)  
**作者**：Stella Frank, Emily Allaway  

**一句话要点**：提出VISaGE数据集以评估视觉语言模型在典型与异常图像上的概念理解

**关键词**：视觉语言模型, 概念理解, 语用先验, 语义先验, 异常图像, 评估数据集

## 3 点简述
- 核心问题：视觉语言模型在异常实例上存在语用先验与语义先验的冲突
- 方法要点：构建平衡数据集，包含典型和异常图像，用于系统实验
- 实验或效果：语用先验违反时概念理解退化，影响强于语义先验

## 摘要（原文）

> While Vision Language Models (VLMs) learn conceptual representations, in the
> form of generalized knowledge, during training, they are typically used to
> analyze individual instances. When evaluation instances are atypical, this
> paradigm results in tension between two priors in the model. The first is a
> pragmatic prior that the textual and visual input are both relevant, arising
> from VLM finetuning on congruent inputs; the second is a semantic prior that
> the conceptual representation is generally true for instances of the category.
> In order to understand how VLMs trade off these priors, we introduce a new
> evaluation dataset, VISaGE, consisting of both typical and exceptional images.
> In carefully balanced experiments, we show that conceptual understanding
> degrades when the assumption of congruency underlying the pragmatic prior is
> violated with incongruent images. This effect is stronger than the effect of
> the semantic prior when querying about individual instances.

