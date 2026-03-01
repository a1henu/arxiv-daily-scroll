---
layout: default
title: Make It Hard to Hear, Easy to Learn: Long-Form Bengali ASR and Speaker Diarization via Extreme Augmentation and Perfect Alignment
---

# Make It Hard to Hear, Easy to Learn: Long-Form Bengali ASR and Speaker Diarization via Extreme Augmentation and Perfect Alignment
**arXiv**：[2602.23070v1](https://arxiv.org/abs/2602.23070) · [PDF](https://arxiv.org/pdf/2602.23070.pdf)  
**作者**：Sanjid Hasan, Risalat Labib, A H M Fuad, Bayazid Hasan  

**一句话要点**：提出Lipi-Ghor-882数据集与优化双管道，解决孟加拉语长音频ASR与说话人日志的资源稀缺与性能挑战。

**关键词**：孟加拉语语音识别, 说话人日志, 长音频处理, 数据增强, 后处理优化, 低资源语音

## 3 点简述
- 核心问题：孟加拉语长音频ASR与说话人日志资源严重不足，现有模型在复杂数据上表现不佳。
- 方法要点：ASR采用完美对齐标注与合成声学退化进行微调；说话人日志通过启发式后处理提升基线模型输出。
- 实验或效果：构建882小时多说话人数据集，优化管道实现约0.019实时因子，为低资源长音频处理提供基准。

## 摘要（原文）

> Although Automatic Speech Recognition (ASR) in Bengali has seen significant progress, processing long-duration audio and performing robust speaker diarization remain critical research gaps. To address the severe scarcity of joint ASR and diarization resources for this language, we introduce Lipi-Ghor-882, a comprehensive 882-hour multi-speaker Bengali dataset. In this paper, detailing our submission to the DL Sprint 4.0 competition, we systematically evaluate various architectures and approaches for long-form Bengali speech. For ASR, we demonstrate that raw data scaling is ineffective; instead, targeted fine-tuning utilizing perfectly aligned annotations paired with synthetic acoustic degradation (noise and reverberation) emerges as the singular most effective approach. Conversely, for speaker diarization, we observed that global open-source state-of-the-art models (such as Diarizen) performed surprisingly poorly on this complex dataset. Extensive model retraining yielded negligible improvements; instead, strategic, heuristic post-processing of baseline model outputs proved to be the primary driver for increasing accuracy. Ultimately, this work outlines a highly optimized dual pipeline achieving a $\sim$0.019 Real-Time Factor (RTF), establishing a practical, empirically backed benchmark for low-resource, long-form speech processing.

