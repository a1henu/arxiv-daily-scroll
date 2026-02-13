---
layout: default
title: How to Sample High Quality 3D Fractals for Action Recognition Pre-Training?
---

# How to Sample High Quality 3D Fractals for Action Recognition Pre-Training?
**arXiv**：[2602.11810v1](https://arxiv.org/abs/2602.11810) · [PDF](https://arxiv.org/pdf/2602.11810.pdf)  
**作者**：Marko Putak, Thomas B. Moeslund, Joakim Bruslund Haurum  

**一句话要点**：提出Targeted Smart Filtering方法，以高效生成高质量3D分形用于动作识别预训练。

**关键词**：3D分形生成, 动作识别预训练, 合成数据集, 迭代函数系统, Targeted Smart Filtering

## 3 点简述
- 核心问题：传统3D分形生成方法速度慢且易产生退化分形，影响预训练效果。
- 方法要点：采用Targeted Smart Filtering，平衡生成速度与分形多样性，避免过度限制。
- 实验或效果：采样速度提升约100倍，下游任务性能优于其他3D分形过滤方法。

## 摘要（原文）

> Synthetic datasets are being recognized in the deep learning realm as a valuable alternative to exhaustively labeled real data. One such synthetic data generation method is Formula Driven Supervised Learning (FDSL), which can provide an infinite number of perfectly labeled data through a formula driven approach, such as fractals or contours. FDSL does not have common drawbacks like manual labor, privacy and other ethical concerns. In this work we generate 3D fractals using 3D Iterated Function Systems (IFS) for pre-training an action recognition model. The fractals are temporally transformed to form a video that is used as a pre-training dataset for downstream task of action recognition. We find that standard methods of generating fractals are slow and produce degenerate 3D fractals. Therefore, we systematically explore alternative ways of generating fractals and finds that overly-restrictive approaches, while generating aesthetically pleasing fractals, are detrimental for downstream task performance. We propose a novel method, Targeted Smart Filtering, to address both the generation speed and fractal diversity issue. The method reports roughly 100 times faster sampling speed and achieves superior downstream performance against other 3D fractal filtering methods.

