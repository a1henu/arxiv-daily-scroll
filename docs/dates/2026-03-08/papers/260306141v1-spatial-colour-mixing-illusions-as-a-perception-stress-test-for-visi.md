---
layout: default
title: Spatial Colour Mixing Illusions as a Perception Stress Test for Vision-Language Models
---

# Spatial Colour Mixing Illusions as a Perception Stress Test for Vision-Language Models
**arXiv**：[2603.06141v1](https://arxiv.org/abs/2603.06141) · [PDF](https://arxiv.org/pdf/2603.06141.pdf)  
**作者**：Nicoleta-Nina Basoc, Adrian Cosma, Emilian Radoi  

**一句话要点**：提出空间色彩混合幻觉作为视觉语言模型的感知压力测试，揭示其系统感知弱点。

**关键词**：视觉语言模型, 感知鲁棒性, 色彩失真, 压力测试, 预处理策略

## 3 点简述
- 核心问题：视觉语言模型在结构化色彩失真下易产生自信但荒谬的预测，与人类感知存在差距。
- 方法要点：设计八种空间色彩混合变体，在RGB和Ostwald色彩系统中叠加模式到自然图像上。
- 实验或效果：评估九个模型，准确率随失真增加急剧下降，人类表现显著优于模型，简单预处理可部分恢复性能。

## 摘要（原文）

> Vision-language models (VLMs) achieve strong benchmark results, yet can exhibit systematic perceptual weaknesses: structured, large changes to pixel values can cause confident yet nonsensical predictions, even when the underlying scene remains easily recognizable to humans. We study this gap using Spatial Colour Mixing, a programmatic family of colour distortions that overlays structured patterns (in both RGB and Ostwald colour systems) onto natural images. We introduce a framework of eight spatial colour mixing variants and evaluate nine VLMs across three model families on four datasets. Across models and datasets, accuracy degrades sharply with increasing distortion, and scaling the language model does not reliably mitigate the failure. In a human study with 61 participants on an animal recognition dataset, humans substantially outperform VLMs under the same distortions. Finally, we show that a simple human-inspired preprocessing step recovers a meaningful portion of performance for several distortion types, motivating perception-aware preprocessing and tool-use as practical strategies for improving VLM robustness.

