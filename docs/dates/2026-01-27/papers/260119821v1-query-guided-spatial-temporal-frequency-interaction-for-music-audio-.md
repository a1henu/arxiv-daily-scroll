---
layout: default
title: Query-Guided Spatial-Temporal-Frequency Interaction for Music Audio-Visual Question Answering
---

# Query-Guided Spatial-Temporal-Frequency Interaction for Music Audio-Visual Question Answering
**arXiv**：[2601.19821v1](https://arxiv.org/abs/2601.19821) · [PDF](https://arxiv.org/pdf/2601.19821.pdf)  
**作者**：Kun Li, Michael Ying Yang, Sami Sebastian Brandt  

**一句话要点**：提出QSTar方法以增强音乐音频-视觉问答中的多模态交互

**关键词**：音频-视觉问答, 多模态交互, 查询引导, 频域特征, 空间-时间-频率, 提示式推理

## 3 点简述
- 核心问题：现有AVQA方法音频处理不足，文本问题信息利用有限，影响多模态推理。
- 方法要点：引入查询引导的空间-时间-频率交互，结合音频频域特性和提示式查询上下文推理。
- 实验或效果：在多个AVQA基准测试中表现优异，超越现有音频、视觉、视频及AVQA方法。

## 摘要（原文）

> Audio--Visual Question Answering (AVQA) is a challenging multimodal task that requires jointly reasoning over audio, visual, and textual information in a given video to answer natural language questions. Inspired by recent advances in Video QA, many existing AVQA approaches primarily focus on visual information processing, leveraging pre-trained models to extract object-level and motion-level representations. However, in those methods, the audio input is primarily treated as complementary to video analysis, and the textual question information contributes minimally to audio--visual understanding, as it is typically integrated only in the final stages of reasoning. To address these limitations, we propose a novel Query-guided Spatial--Temporal--Frequency (QSTar) interaction method, which effectively incorporates question-guided clues and exploits the distinctive frequency-domain characteristics of audio signals, alongside spatial and temporal perception, to enhance audio--visual understanding. Furthermore, we introduce a Query Context Reasoning (QCR) block inspired by prompting, which guides the model to focus more precisely on semantically relevant audio and visual features. Extensive experiments conducted on several AVQA benchmarks demonstrate the effectiveness of our proposed method, achieving significant performance improvements over existing Audio QA, Visual QA, Video QA, and AVQA approaches. The code and pretrained models will be released after publication.

