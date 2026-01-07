---
layout: default
title: TA-Prompting: Enhancing Video Large Language Models for Dense Video Captioning via Temporal Anchors
---

# TA-Prompting: Enhancing Video Large Language Models for Dense Video Captioning via Temporal Anchors
**arXiv**：[2601.02908v1](https://arxiv.org/abs/2601.02908) · [PDF](https://arxiv.org/pdf/2601.02908.pdf)  
**作者**：Wei-Yuan Cheng, Kai-Po Chang, Chi-Pin Huang, Fu-En Yang, Yu-Chiang Frank Wang  

**一句话要点**：提出TA-Prompting以增强视频大语言模型在密集视频描述中的时间定位能力

**关键词**：密集视频描述, 视频大语言模型, 时间定位, 事件连贯采样, 时间感知理解

## 3 点简述
- 现有VideoLLMs在未剪辑视频中难以精确定位事件边界，导致描述不准确
- TA-Prompting通过时间锚点学习精确定位事件，并提示模型进行时间感知的视频事件理解
- 在基准数据集上实验显示，该方法在密集视频描述和时间理解任务中优于现有方法

## 摘要（原文）

> Dense video captioning aims to interpret and describe all temporally localized events throughout an input video. Recent state-of-the-art methods leverage large language models (LLMs) to provide detailed moment descriptions for video data. However, existing VideoLLMs remain challenging in identifying precise event boundaries in untrimmed videos, causing the generated captions to be not properly grounded. In this paper, we propose TA-Prompting, which enhances VideoLLMs via Temporal Anchors that learn to precisely localize events and prompt the VideoLLMs to perform temporal-aware video event understanding. During inference, in order to properly determine the output caption sequence from an arbitrary number of events presented within a video, we introduce an event coherent sampling strategy to select event captions with sufficient coherence across temporal events and cross-modal similarity with the given video. Through extensive experiments on benchmark datasets, we show that our TA-Prompting is favorable against state-of-the-art VideoLLMs, yielding superior performance on dense video captioning and temporal understanding tasks including moment retrieval and temporalQA.

