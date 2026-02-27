---
layout: default
title: A Holistic Framework for Robust Bangla ASR and Speaker Diarization with Optimized VAD and CTC Alignment
---

# A Holistic Framework for Robust Bangla ASR and Speaker Diarization with Optimized VAD and CTC Alignment
**arXiv**：[2602.22935v1](https://arxiv.org/abs/2602.22935) · [PDF](https://arxiv.org/pdf/2602.22935.pdf)  
**作者**：Zarif Ishmam, Zarif Mahir, Shafnan Wasif, Md. Ishtiak Moin  

**一句话要点**：提出鲁棒框架以解决孟加拉语长音频自动语音识别和说话人日志中的性能问题

**关键词**：孟加拉语自动语音识别, 说话人日志, 语音活动检测优化, 连接时序分类对齐, 长音频处理, 低资源语言处理

## 3 点简述
- 核心问题：孟加拉语作为低资源语言，长音频（超过3060秒）的自动语音识别和说话人日志性能受限。
- 方法要点：通过优化语音活动检测和连接时序分类对齐，结合微调与数据增强，提升长音频处理的准确性和鲁棒性。
- 实验或效果：在DL Sprint 4.0竞赛中应用，为复杂多说话人环境提供可扩展的解决方案，改善长音频转录完整性。

## 摘要（原文）

> Despite being one of the most widely spoken languages globally, Bangla remains a low-resource language in the field of Natural Language Processing (NLP). Mainstream Automatic Speech Recognition (ASR) and Speaker Diarization systems for Bangla struggles when processing longform audio exceeding 3060 seconds. This paper presents a robust framework specifically engineered for extended Bangla content by leveraging preexisting models enhanced with novel optimization pipelines for the DL Sprint 4.0 contest. Our approach utilizes Voice Activity Detection (VAD) optimization and Connectionist Temporal Classification (CTC) segmentation via forced word alignment to maintain temporal accuracy and transcription integrity over long durations. Additionally, we employed several finetuning techniques and preprocessed the data using augmentation techniques and noise removal. By bridging the performance gap in complex, multi-speaker environments, this work provides a scalable solution for real-world, longform Bangla speech applications.

