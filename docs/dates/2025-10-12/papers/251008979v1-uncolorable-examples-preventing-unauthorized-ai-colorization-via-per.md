---
layout: default
title: Uncolorable Examples: Preventing Unauthorized AI Colorization via Perception-Aware Chroma-Restrictive Perturbation
---

# Uncolorable Examples: Preventing Unauthorized AI Colorization via Perception-Aware Chroma-Restrictive Perturbation
**arXiv**：[2510.08979v1](https://arxiv.org/abs/2510.08979) · [PDF](https://arxiv.org/pdf/2510.08979.pdf)  
**作者**：Yuki Nii, Futa Waseda, Ching-Chun Chang, Isao Echizen  

**一句话要点**：提出PAChroma方法以防止未经授权的AI着色，保护灰度图像版权。

**关键词**：AI着色防御, 不可感知扰动, 版权保护, 图像处理, 鲁棒性优化

## 3 点简述
- 核心问题：AI着色技术可能导致版权侵犯，如未经授权为漫画和电影着色。
- 方法要点：通过优化不可感知扰动，结合拉普拉斯滤波保持视觉质量。
- 实验或效果：在ImageNet和Danbooru数据集上验证，有效降低着色质量。

## 摘要（原文）

> AI-based colorization has shown remarkable capability in generating realistic
> color images from grayscale inputs. However, it poses risks of copyright
> infringement -- for example, the unauthorized colorization and resale of
> monochrome manga and films. Despite these concerns, no effective method
> currently exists to prevent such misuse. To address this, we introduce the
> first defensive paradigm, Uncolorable Examples, which embed imperceptible
> perturbations into grayscale images to invalidate unauthorized colorization. To
> ensure real-world applicability, we establish four criteria: effectiveness,
> imperceptibility, transferability, and robustness. Our method, Perception-Aware
> Chroma-Restrictive Perturbation (PAChroma), generates Uncolorable Examples that
> meet these four criteria by optimizing imperceptible perturbations with a
> Laplacian filter to preserve perceptual quality, and applying diverse input
> transformations during optimization to enhance transferability across models
> and robustness against common post-processing (e.g., compression). Experiments
> on ImageNet and Danbooru datasets demonstrate that PAChroma effectively
> degrades colorization quality while maintaining the visual appearance. This
> work marks the first step toward protecting visual content from illegitimate AI
> colorization, paving the way for copyright-aware defenses in generative media.

