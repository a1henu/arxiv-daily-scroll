---
layout: default
title: Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation
---

# Annealed Relaxation of Speculative Decoding for Faster Autoregressive Image Generation
**arXiv**：[2601.09212v1](https://arxiv.org/abs/2601.09212) · [PDF](https://arxiv.org/pdf/2601.09212.pdf)  
**作者**：Xingyao Li, Fengzhuo Zhang, Cunxiao Du, Hui Ji  

**一句话要点**：提出COOL-SD以加速自回归图像生成，通过退火松弛推测解码优化速度-质量权衡。

**关键词**：自回归图像生成, 推测解码, 退火松弛, 总变差距离, 扰动分析

## 3 点简述
- 核心问题：自回归图像生成推理慢，推测解码存在模糊性，松弛方法缺乏理论依据。
- 方法要点：基于总变差距离和扰动分析，设计退火松弛推测解码，优化重采样分布。
- 实验或效果：COOL-SD在实验中提升速度-质量权衡，优于先前方法。

## 摘要（原文）

> Despite significant progress in autoregressive image generation, inference remains slow due to the sequential nature of AR models and the ambiguity of image tokens, even when using speculative decoding. Recent works attempt to address this with relaxed speculative decoding but lack theoretical grounding. In this paper, we establish the theoretical basis of relaxed SD and propose COOL-SD, an annealed relaxation of speculative decoding built on two key insights. The first analyzes the total variation (TV) distance between the target model and relaxed speculative decoding and yields an optimal resampling distribution that minimizes an upper bound of the distance. The second uses perturbation analysis to reveal an annealing behaviour in relaxed speculative decoding, motivating our annealed design. Together, these insights enable COOL-SD to generate images faster with comparable quality, or achieve better quality at similar latency. Experiments validate the effectiveness of COOL-SD, showing consistent improvements over prior methods in speed-quality trade-offs.

