---
layout: default
title: SAGE: Structure-Aware Generative Video Transitions between Diverse Clips
---

# SAGE: Structure-Aware Generative Video Transitions between Diverse Clips
**arXiv**：[2510.24667v1](https://arxiv.org/abs/2510.24667) · [PDF](https://arxiv.org/pdf/2510.24667.pdf)  
**作者**：Mia Kan, Yilin Liu, Niloy Mitra  

**一句话要点**：提出SAGE结构感知生成视频过渡方法，以解决多样片段间平滑过渡问题。

**关键词**：视频过渡, 结构感知生成, 零样本方法, 语义一致性, 运动流引导

## 3 点简述
- 核心问题：传统和生成方法难以处理大时间差或语义差异的多样视频片段过渡。
- 方法要点：结合结构引导和生成合成，无需微调实现结构保持和语义一致过渡。
- 实验或效果：在定量指标和用户研究中优于多种基线，代码待发布。

## 摘要（原文）

> Video transitions aim to synthesize intermediate frames between two clips,
> but naive approaches such as linear blending introduce artifacts that limit
> professional use or break temporal coherence. Traditional techniques
> (cross-fades, morphing, frame interpolation) and recent generative inbetweening
> methods can produce high-quality plausible intermediates, but they struggle
> with bridging diverse clips involving large temporal gaps or significant
> semantic differences, leaving a gap for content-aware and visually coherent
> transitions. We address this challenge by drawing on artistic workflows,
> distilling strategies such as aligning silhouettes and interpolating salient
> features to preserve structure and perceptual continuity. Building on this, we
> propose SAGE (Structure-Aware Generative vidEo transitions) as a zeroshot
> approach that combines structural guidance, provided via line maps and motion
> flow, with generative synthesis, enabling smooth, semantically consistent
> transitions without fine-tuning. Extensive experiments and comparison with
> current alternatives, namely [FILM, TVG, DiffMorpher, VACE, GI], demonstrate
> that SAGE outperforms both classical and generative baselines on quantitative
> metrics and user studies for producing transitions between diverse clips. Code
> to be released on acceptance.

