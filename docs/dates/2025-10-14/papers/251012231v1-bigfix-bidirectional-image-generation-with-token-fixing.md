---
layout: default
title: BIGFix: Bidirectional Image Generation with Token Fixing
---

# BIGFix: Bidirectional Image Generation with Token Fixing
**arXiv**：[2510.12231v1](https://arxiv.org/abs/2510.12231) · [PDF](https://arxiv.org/pdf/2510.12231.pdf)  
**作者**：Victor Besnier, David Hurych, Andrei Bursuc, Eduardo Valle  

**一句话要点**：提出BIGFix方法，通过迭代修复令牌解决并行令牌预测中的结构不一致问题。

**关键词**：图像生成, 视频生成, 并行令牌预测, 令牌修复, 推理效率

## 3 点简述
- 核心问题：并行令牌预测导致结构不一致，缺乏回溯机制。
- 方法要点：使用新颖训练方案注入随机令牌，实现迭代令牌修复。
- 实验或效果：在图像和视频生成数据集上显著提升生成质量。

## 摘要（原文）

> Recent advances in image and video generation have raised significant
> interest from both academia and industry. A key challenge in this field is
> improving inference efficiency, as model size and the number of inference steps
> directly impact the commercial viability of generative models while also posing
> fundamental scientific challenges. A promising direction involves combining
> auto-regressive sequential token modeling with multi-token prediction per step,
> reducing inference time by up to an order of magnitude. However, predicting
> multiple tokens in parallel can introduce structural inconsistencies due to
> token incompatibilities, as capturing complex joint dependencies during
> training remains challenging. Traditionally, once tokens are sampled, there is
> no mechanism to backtrack and refine erroneous predictions. We propose a method
> for self-correcting image generation by iteratively refining sampled tokens. We
> achieve this with a novel training scheme that injects random tokens in the
> context, improving robustness and enabling token fixing during sampling. Our
> method preserves the efficiency benefits of parallel token prediction while
> significantly enhancing generation quality. We evaluate our approach on image
> generation using the ImageNet-256 and CIFAR-10 datasets, as well as on video
> generation with UCF-101 and NuScenes, demonstrating substantial improvements
> across both modalities.

