---
layout: default
title: Zero-shot image privacy classification with Vision-Language Models
---

# Zero-shot image privacy classification with Vision-Language Models
**arXiv**：[2510.09253v1](https://arxiv.org/abs/2510.09253) · [PDF](https://arxiv.org/pdf/2510.09253.pdf)  
**作者**：Alina Elena Baia, Alessio Xompero, Andrea Cavallaro  
**一句话要点**：建立零样本基准以公平比较视觉语言模型在图像隐私分类中的性能。
**关键词**：图像隐私分类, 视觉语言模型, 零样本基准, 模型鲁棒性, 公平比较

## 3 点简述
- 核心问题：缺乏系统评估，视觉语言模型在图像隐私预测中可能被高估。
- 方法要点：使用任务对齐提示评估开源视觉语言模型，对比专业模型。
- 实验或效果：视觉语言模型精度较低但鲁棒性更高，资源消耗大。

## 摘要（原文）

> While specialized learning-based models have historically dominated image
> privacy prediction, the current literature increasingly favours adopting large
> Vision-Language Models (VLMs) designed for generic tasks. This trend risks
> overlooking the performance ceiling set by purpose-built models due to a lack
> of systematic evaluation. To address this problem, we establish a zero-shot
> benchmark for image privacy classification, enabling a fair comparison. We
> evaluate the top-3 open-source VLMs, according to a privacy benchmark, using
> task-aligned prompts and we contrast their performance, efficiency, and
> robustness against established vision-only and multi-modal methods.
> Counter-intuitively, our results show that VLMs, despite their
> resource-intensive nature in terms of high parameter count and slower
> inference, currently lag behind specialized, smaller models in privacy
> prediction accuracy. We also find that VLMs exhibit higher robustness to image
> perturbations.

