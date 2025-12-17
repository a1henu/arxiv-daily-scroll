---
layout: default
title: Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in
---

# Zoom-Zero: Reinforced Coarse-to-Fine Video Understanding via Temporal Zoom-in
**arXiv**：[2512.14273v1](https://arxiv.org/abs/2512.14273) · [PDF](https://arxiv.org/pdf/2512.14273.pdf)  
**作者**：Xiaoqian Shen, Min-Hung Chen, Yu-Chiang Frank Wang, Mohamed Elhoseiny, Ryo Hachiuma  

**一句话要点**：提出Zoom-Zero框架，通过粗到细的时序放大解决视频问答中的时序定位不准确问题。

**关键词**：视频问答, 时序定位, 强化学习, 粗到细框架, 长视频理解

## 3 点简述
- 核心问题：大型视频语言模型在时序感知上有限，导致时序错位和幻觉。
- 方法要点：采用粗到细框架，先定位相关片段，再放大关键帧进行细粒度视觉验证。
- 实验或效果：在NExT-GQA和ReXTime上时序定位提升5.2%和4.6%，答案准确率平均提高2.4%。

## 摘要（原文）

> Grounded video question answering (GVQA) aims to localize relevant temporal segments in videos and generate accurate answers to a given question; however, large video-language models (LVLMs) exhibit limited temporal awareness. Although existing approaches based on Group Relative Policy Optimization (GRPO) attempt to improve temporal grounding, they still struggle to faithfully ground their answers in the relevant video evidence, leading to temporal mislocalization and hallucinations. In this work, we present Zoom-Zero, a coarse-to-fine framework that first localizes query-relevant segments and then temporally zooms into the most salient frames for finer-grained visual verification. Our method addresses the limits of GRPO for the GVQA task with two key innovations: (i) a zoom-in accuracy reward that validates the fidelity of temporal grounding prediction and facilitates fine-grained visual verification on grounded frames; (ii) token-selective credit assignment, which attributes rewards to the tokens responsible for temporal localization or answer generation, mitigating GRPO's issue in handling multi-faceted reward signals. Our proposed method advances grounded video question answering, improving temporal grounding by 5.2\% on NExT-GQA and 4.6\% on ReXTime, while also enhancing average answer accuracy by 2.4\%. Additionally, the coarse-to-fine zoom-in during inference further benefits long-form video understanding by preserving critical visual details without compromising global context, yielding an average improvement of 6.4\% on long-video benchmarks.

