---
layout: default
title: FAIRT2V: Training-Free Debiasing for Text-to-Video Diffusion Models
---

# FAIRT2V: Training-Free Debiasing for Text-to-Video Diffusion Models
**arXiv**：[2601.20791v1](https://arxiv.org/abs/2601.20791) · [PDF](https://arxiv.org/pdf/2601.20791.pdf)  
**作者**：Haonan Zhong, Wei Song, Tingxu Han, Maurice Pagnucco, Jingling Xue, Yang Song  

**一句话要点**：提出FAIRT2V框架，通过训练无关方法减少文本到视频扩散模型中的性别偏见。

**关键词**：文本到视频生成, 去偏见方法, 训练无关框架, 性别偏见, 视频公平性评估, 扩散模型

## 3 点简述
- 核心问题：文本到视频模型存在性别偏见，主要源于预训练文本编码器。
- 方法要点：使用基于锚点的球面测地变换中和提示嵌入，保持语义并应用动态去噪计划。
- 实验或效果：在Open-Sora模型上显著减少职业相关偏见，视频质量影响最小。

## 摘要（原文）

> Text-to-video (T2V) diffusion models have achieved rapid progress, yet their demographic biases, particularly gender bias, remain largely unexplored. We present FairT2V, a training-free debiasing framework for text-to-video generation that mitigates encoder-induced bias without finetuning. We first analyze demographic bias in T2V models and show that it primarily originates from pretrained text encoders, which encode implicit gender associations even for neutral prompts. We quantify this effect with a gender-leaning score that correlates with bias in generated videos.
>   Based on this insight, FairT2V mitigates demographic bias by neutralizing prompt embeddings via anchor-based spherical geodesic transformations while preserving semantics. To maintain temporal coherence, we apply debiasing only during early identity-forming steps through a dynamic denoising schedule. We further propose a video-level fairness evaluation protocol combining VideoLLM-based reasoning with human verification. Experiments on the modern T2V model Open-Sora show that FairT2V substantially reduces demographic bias across occupations with minimal impact on video quality.

