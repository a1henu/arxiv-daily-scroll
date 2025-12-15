---
layout: default
title: Flowception: Temporally Expansive Flow Matching for Video Generation
---

# Flowception: Temporally Expansive Flow Matching for Video Generation
**arXiv**：[2512.11438v1](https://arxiv.org/abs/2512.11438) · [PDF](https://arxiv.org/pdf/2512.11438.pdf)  
**作者**：Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen  

**一句话要点**：提出Flowception框架，通过交织离散帧插入与连续帧去噪实现非自回归变长视频生成。

**关键词**：视频生成, 非自回归模型, 流匹配, 变长序列, 帧插入去噪

## 3 点简述
- 核心问题：解决自回归方法中的误差累积/漂移问题，以及全序列流方法的高计算成本。
- 方法要点：学习概率路径，结合离散帧插入作为压缩机制，减少训练FLOPs三倍，并支持联合学习视频长度与内容。
- 实验或效果：在FVD和VBench指标上优于基线，支持图像到视频生成和视频插值等任务。

## 摘要（原文）

> We present Flowception, a novel non-autoregressive and variable-length video generation framework. Flowception learns a probability path that interleaves discrete frame insertions with continuous frame denoising. Compared to autoregressive methods, Flowception alleviates error accumulation/drift as the frame insertion mechanism during sampling serves as an efficient compression mechanism to handle long-term context. Compared to full-sequence flows, our method reduces FLOPs for training three-fold, while also being more amenable to local attention variants, and allowing to learn the length of videos jointly with their content. Quantitative experimental results show improved FVD and VBench metrics over autoregressive and full-sequence baselines, which is further validated with qualitative results. Finally, by learning to insert and denoise frames in a sequence, Flowception seamlessly integrates different tasks such as image-to-video generation and video interpolation.

