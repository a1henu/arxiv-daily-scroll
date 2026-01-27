---
layout: default
title: Self-Refining Video Sampling
---

# Self-Refining Video Sampling
**arXiv**：[2601.18577v1](https://arxiv.org/abs/2601.18577) · [PDF](https://arxiv.org/pdf/2601.18577.pdf)  
**作者**：Sangwon Jang, Taekyung Ki, Jaehyeong Jo, Saining Xie, Jaehong Yoon, Sung Ju Hwang  

**一句话要点**：提出自精炼视频采样方法，通过迭代内循环优化提升视频生成的物理真实感。

**关键词**：视频生成, 自精炼采样, 物理动态, 去噪自编码器, 不确定性感知

## 3 点简述
- 现代视频生成器在复杂物理动态上表现不足，缺乏物理真实感。
- 将预训练生成器解释为去噪自编码器，实现无需外部验证或额外训练的推理时迭代精炼。
- 实验显示在运动连贯性和物理对齐方面显著改进，人类偏好率超过70%。

## 摘要（原文）

> Modern video generators still struggle with complex physical dynamics, often falling short of physical realism. Existing approaches address this using external verifiers or additional training on augmented data, which is computationally expensive and still limited in capturing fine-grained motion. In this work, we present self-refining video sampling, a simple method that uses a pre-trained video generator trained on large-scale datasets as its own self-refiner. By interpreting the generator as a denoising autoencoder, we enable iterative inner-loop refinement at inference time without any external verifier or additional training. We further introduce an uncertainty-aware refinement strategy that selectively refines regions based on self-consistency, which prevents artifacts caused by over-refinement. Experiments on state-of-the-art video generators demonstrate significant improvements in motion coherence and physics alignment, achieving over 70\% human preference compared to the default sampler and guidance-based sampler.

