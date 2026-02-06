---
layout: default
title: Ethology of Latent Spaces
---

# Ethology of Latent Spaces
**arXiv**：[2602.05710v1](https://arxiv.org/abs/2602.05710) · [PDF](https://arxiv.org/pdf/2602.05710.pdf)  
**作者**：Philippe Boisnard  

**一句话要点**：提出计算潜在政治化等概念，揭示视觉语言模型潜在空间非中性，应用于数字艺术史分析。

**关键词**：潜在空间分析, 视觉语言模型, 计算民族志, 算法偏见, 数字艺术史, 模型比较

## 3 点简述
- 核心问题：挑战视觉语言模型潜在空间的中性假设，探究其算法行为中的模型特异性敏感度。
- 方法要点：采用民族志视角，通过向量类比分析比较三个模型在艺术作品上的政治和文化分类差异。
- 实验或效果：发现模型间政治分类差异显著，如SigLIP将59.4%作品归类为政治参与，而OpenCLIP仅4%。

## 摘要（原文）

> This study challenges the presumed neutrality of latent spaces in vision language models (VLMs) by adopting an ethological perspective on their algorithmic behaviors. Rather than constituting spaces of homogeneous indeterminacy, latent spaces exhibit model-specific algorithmic sensitivities, understood as differential regimes of perceptual salience shaped by training data and architectural choices.
>   Through a comparative analysis of three models (OpenAI CLIP, OpenCLIP LAION, SigLIP) applied to a corpus of 301 artworks (15th to 20th), we reveal substantial divergences in the attribution of political and cultural categories. Using bipolar semantic axes derived from vector analogies (Mikolov et al., 2013), we show that SigLIP classifies 59.4% of the artworks as politically engaged, compared to only 4% for OpenCLIP. African masks receive the highest political scores in SigLIP while remaining apolitical in OpenAI CLIP. On an aesthetic colonial axis, inter-model discrepancies reach 72.6 percentage points.
>   We introduce three operational concepts: computational latent politicization, describing the emergence of political categories without intentional encoding; emergent bias, irreducible to statistical or normative bias and detectable only through contrastive analysis; and three algorithmic scopic regimes: entropic (LAION), institutional (OpenAI), and semiotic (SigLIP), which structure distinct modes of visibility. Drawing on Foucault's notion of the archive, Jameson's ideologeme, and Simondon's theory of individuation, we argue that training datasets function as quasi-archives whose discursive formations crystallize within latent space. This work contributes to a critical reassessment of the conditions under which VLMs are applied to digital art history and calls for methodologies that integrate learning architectures into any delegation of cultural interpretation to algorithmic agents.

