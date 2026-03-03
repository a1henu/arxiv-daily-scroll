---
layout: default
title: TCG CREST System Description for the DISPLACE-M Challenge
---

# TCG CREST System Description for the DISPLACE-M Challenge
**arXiv**：[2603.02030v1](https://arxiv.org/abs/2603.02030) · [PDF](https://arxiv.org/pdf/2603.02030.pdf)  
**作者**：Nikhil Raghav, Md Sahidullah  

**一句话要点**：提出TCG CREST系统，评估VAD与聚类算法在嘈杂医疗对话中的说话人日志性能

**关键词**：说话人日志, 语音活动检测, 端到端神经网络, 聚类算法, 医疗对话分析

## 3 点简述
- 研究在嘈杂农村医疗场景下，说话人日志的VAD方法和聚类算法影响
- 比较模块化SpeechBrain框架与端到端Diarizen系统，探索AHC和谱聚类变体
- Diarizen系统在Phase I后评估中相对SpeechBrain基线降低DER约39%

## 摘要（原文）

> This report presents the TCG CREST system description for Track 1 (Speaker Diarization) of the DISPLACE-M challenge, focusing on naturalistic medical conversations in noisy rural-healthcare scenarios. Our study evaluates the impact of various voice activity detection (VAD) methods and advanced clustering algorithms on overall speaker diarization (SD) performance. We compare and analyze two SD frameworks: a modular pipeline utilizing SpeechBrain with ECAPA-TDNN embeddings, and a state-of-the-art (SOTA) hybrid end-to-end neural diarization system, Diarizen, built on top of a pre-trained WavLM. With these frameworks, we explore diverse clustering techniques, including agglomerative hierarchical clustering (AHC), and multiple novel variants of spectral clustering, such as SC-adapt, SC-PNA, and SC-MK. Experimental results demonstrate that the Diarizen system provides an approximate $39\%$ relative improvement in the diarization error rate (DER) on the post-evaluation analysis of Phase~I compared to the SpeechBrain baseline. Our best-performing submitted system employing the Diarizen baseline with AHC employing a median filtering with a larger context window of $29$ achieved a DER of 10.37\% on the development and 9.21\% on the evaluation sets, respectively. Our team ranked sixth out of the 11 participating teams after the Phase~I evaluation.

