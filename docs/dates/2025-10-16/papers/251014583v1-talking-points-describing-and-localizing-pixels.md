---
layout: default
title: Talking Points: Describing and Localizing Pixels
---

# Talking Points: Describing and Localizing Pixels
**arXiv**：[2510.14583v1](https://arxiv.org/abs/2510.14583) · [PDF](https://arxiv.org/pdf/2510.14583.pdf)  
**作者**：Matan Rusanovsky, Shimon Malnick, Shai Avidan  

**一句话要点**：提出双向框架以解决像素级关键点描述与定位问题

**关键词**：像素级定位, 关键点描述, 视觉语言模型, 数据集合成, 双向框架

## 3 点简述
- 核心问题：视觉语言模型缺乏像素级关键点理解能力，仅支持对象或区域级定位。
- 方法要点：结合点描述器和点定位器，生成上下文描述并回归像素坐标。
- 实验或效果：在LlamaPointInPart数据集上优于基线，建立新评估协议。

## 摘要（原文）

> Vision-language models have achieved remarkable success in cross-modal
> understanding. Yet, these models remain limited to object-level or region-level
> grounding, lacking the capability for pixel-precise keypoint comprehension
> through natural language. We introduce a novel framework for pixel level
> grounding. The framework consists of two complementary components: a Point
> Descriptor that generates rich, contextual descriptions of individual
> keypoints, and a Point Localizer that regresses precise pixel coordinates from
> these descriptions. Unlike prior work that relies on templated prompts or
> keypoint names, our approach produces free-form, coarse-to-fine descriptions
> that situate keypoints within their visual context. Since there is no available
> dataset to train such a system, we introduce LlamaPointInPart, a carefully
> curated dataset of 20K+ image-keypoint-description triplets synthesized from
> multiple vision-language models, capturing multi-scale information from
> scene-level context to visual features around the keypoint. For cross-category
> generalization, we optimize the Point Descriptor on AP-10K via GRPO, using the
> frozen Point Localizer as a reward model to produce descriptions that maximize
> localization accuracy. To evaluate our results we establish a new evaluation
> protocol. Instead of comparing the text description produced by our method to
> the ground truth, we use the localizer to determine how close is the predicted
> point generated to the ground truth point. Experiments demonstrate superior
> performance compared to baseline models on LlamaPointInPart.The bidirectional
> nature of our framework should enable future applications in both
> keypoint-guided image understanding and language-guided precise localization.
> Our code and dataset are publicly available at
> https://github.com/matanr/Talking_Points.

