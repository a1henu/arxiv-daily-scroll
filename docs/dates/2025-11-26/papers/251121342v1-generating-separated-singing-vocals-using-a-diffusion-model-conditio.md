---
layout: default
title: Generating Separated Singing Vocals Using a Diffusion Model Conditioned on Music Mixtures
---

# Generating Separated Singing Vocals Using a Diffusion Model Conditioned on Music Mixtures
**arXiv**：[2511.21342v1](https://arxiv.org/abs/2511.21342) · [PDF](https://arxiv.org/pdf/2511.21342.pdf)  
**作者**：Genís Plaja-Roglans, Yun-Ning Hung, Xavier Serra, Igor Pereira  

**一句话要点**：提出基于扩散模型的歌声分离方法，以从音乐混合中生成纯净人声。

**关键词**：歌声分离, 扩散模型, 条件生成, 音乐分析, 迭代采样

## 3 点简述
- 核心问题：从真实音乐录音中分离人声，支持音乐分析和实践。
- 方法要点：使用扩散模型，以音乐混合为条件生成独唱人声，提升灵活性和泛化能力。
- 实验或效果：在补充数据训练下，达到与非生成基线竞争的目标分数，支持质量-效率权衡控制。

## 摘要（原文）

> Separating the individual elements in a musical mixture is an essential process for music analysis and practice. While this is generally addressed using neural networks optimized to mask or transform the time-frequency representation of a mixture to extract the target sources, the flexibility and generalization capabilities of generative diffusion models are giving rise to a novel class of solutions for this complicated task. In this work, we explore singing voice separation from real music recordings using a diffusion model which is trained to generate the solo vocals conditioned on the corresponding mixture. Our approach improves upon prior generative systems and achieves competitive objective scores against non-generative baselines when trained with supplementary data. The iterative nature of diffusion sampling enables the user to control the quality-efficiency trade-off, and also refine the output when needed. We present an ablation study of the sampling algorithm, highlighting the effects of the user-configurable parameters.

