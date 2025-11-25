---
layout: default
title: AuViRe: Audio-visual Speech Representation Reconstruction for Deepfake Temporal Localization
---

# AuViRe: Audio-visual Speech Representation Reconstruction for Deepfake Temporal Localization
**arXiv**：[2511.18993v1](https://arxiv.org/abs/2511.18993) · [PDF](https://arxiv.org/pdf/2511.18993.pdf)  
**作者**：Christos Koutlis, Symeon Papadopoulos  

**一句话要点**：提出AuViRe方法，通过音频-视觉语音表示重建实现深度伪造视频的时间定位

**关键词**：音频-视觉表示重建, 深度伪造定位, 跨模态学习, 时间定位, 语音表示

## 3 点简述
- 核心问题：深度伪造视频的精确时间定位，以应对恶意音频-视觉内容操纵。
- 方法要点：利用跨模态重建语音表示，从一模态预测另一模态，放大伪造段差异。
- 实验或效果：在多个数据集上优于现有方法，如LAV-DF上AP@0.95提升8.9。

## 摘要（原文）

> With the rapid advancement of sophisticated synthetic audio-visual content, e.g., for subtle malicious manipulations, ensuring the integrity of digital media has become paramount. This work presents a novel approach to temporal localization of deepfakes by leveraging Audio-Visual Speech Representation Reconstruction (AuViRe). Specifically, our approach reconstructs speech representations from one modality (e.g., lip movements) based on the other (e.g., audio waveform). Cross-modal reconstruction is significantly more challenging in manipulated video segments, leading to amplified discrepancies, thereby providing robust discriminative cues for precise temporal forgery localization. AuViRe outperforms the state of the art by +8.9 AP@0.95 on LAV-DF, +9.6 AP@0.5 on AV-Deepfake1M, and +5.1 AUC on an in-the-wild experiment. Code available at https://github.com/mever-team/auvire.

