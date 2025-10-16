---
layout: default
title: Adaptive Visual Conditioning for Semantic Consistency in Diffusion-Based Story Continuation
---

# Adaptive Visual Conditioning for Semantic Consistency in Diffusion-Based Story Continuation
**arXiv**：[2510.13787v1](https://arxiv.org/abs/2510.13787) · [PDF](https://arxiv.org/pdf/2510.13787.pdf)  
**作者**：Seyed Mohammad Mousavi, Morteza Analoui  

**一句话要点**：提出自适应视觉条件框架以解决扩散故事延续中的语义一致性问题

**关键词**：故事延续, 扩散模型, 语义对齐, 视觉条件, CLIP检索, 数据增强

## 3 点简述
- 核心问题：故事延续中如何有效利用视觉上下文并确保与文本输入的语义对齐
- 方法要点：使用CLIP检索相关图像，无相关时限制视觉影响于扩散早期阶段
- 实验或效果：通过定量和人工评估，在冲突场景下实现更优一致性和视觉保真度

## 摘要（原文）

> Story continuation focuses on generating the next image in a narrative
> sequence so that it remains coherent with both the ongoing text description and
> the previously observed images. A central challenge in this setting lies in
> utilizing prior visual context effectively, while ensuring semantic alignment
> with the current textual input. In this work, we introduce AVC (Adaptive Visual
> Conditioning), a framework for diffusion-based story continuation. AVC employs
> the CLIP model to retrieve the most semantically aligned image from previous
> frames. Crucially, when no sufficiently relevant image is found, AVC adaptively
> restricts the influence of prior visuals to only the early stages of the
> diffusion process. This enables the model to exploit visual context when
> beneficial, while avoiding the injection of misleading or irrelevant
> information. Furthermore, we improve data quality by re-captioning a noisy
> dataset using large language models, thereby strengthening textual supervision
> and semantic alignment. Quantitative results and human evaluations demonstrate
> that AVC achieves superior coherence, semantic consistency, and visual fidelity
> compared to strong baselines, particularly in challenging cases where prior
> visuals conflict with the current input.

