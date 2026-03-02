---
layout: default
title: Mode Seeking meets Mean Seeking for Fast Long Video Generation
---

# Mode Seeking meets Mean Seeking for Fast Long Video Generation
**arXiv**：[2602.24289v1](https://arxiv.org/abs/2602.24289) · [PDF](https://arxiv.org/pdf/2602.24289.pdf)  
**作者**：Shengqu Cai, Weili Nie, Chao Liu, Julius Berner, Lvmin Zhang, Nanye Ma, Hansheng Chen, Maneesh Agrawala, Leonidas Guibas, Gordon Wetzstein, Arash Vahdat  

**一句话要点**：提出模式寻求与均值寻求结合的训练范式，以解决长视频生成中局部保真度与长期一致性的平衡问题。

**关键词**：长视频生成, 解耦扩散变换器, 流匹配, 分布匹配, 模式寻求, 均值寻求

## 3 点简述
- 核心问题：长视频数据稀缺，导致生成视频在长期连贯性上受限，而短视频数据丰富但缺乏全局结构。
- 方法要点：通过解耦扩散变换器，使用全局流匹配头学习长期叙事结构，局部分布匹配头对齐滑动窗口到冻结短视频教师模型。
- 实验或效果：评估显示方法有效缩小保真度与时间跨度差距，提升局部锐度、运动连贯性和长期一致性。

## 摘要（原文）

> Scaling video generation from seconds to minutes faces a critical bottleneck: while short-video data is abundant and high-fidelity, coherent long-form data is scarce and limited to narrow domains. To address this, we propose a training paradigm where Mode Seeking meets Mean Seeking, decoupling local fidelity from long-term coherence based on a unified representation via a Decoupled Diffusion Transformer. Our approach utilizes a global Flow Matching head trained via supervised learning on long videos to capture narrative structure, while simultaneously employing a local Distribution Matching head that aligns sliding windows to a frozen short-video teacher via a mode-seeking reverse-KL divergence. This strategy enables the synthesis of minute-scale videos that learns long-range coherence and motions from limited long videos via supervised flow matching, while inheriting local realism by aligning every sliding-window segment of the student to a frozen short-video teacher, resulting in a few-step fast long video generator. Evaluations show that our method effectively closes the fidelity-horizon gap by jointly improving local sharpness, motion and long-range consistency. Project website: https://primecai.github.io/mmm/.

