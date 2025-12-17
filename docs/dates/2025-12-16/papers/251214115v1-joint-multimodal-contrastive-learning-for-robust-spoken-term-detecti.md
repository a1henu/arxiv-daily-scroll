---
layout: default
title: Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting
---

# Joint Multimodal Contrastive Learning for Robust Spoken Term Detection and Keyword Spotting
**arXiv**：[2512.14115v1](https://arxiv.org/abs/2512.14115) · [PDF](https://arxiv.org/pdf/2512.14115.pdf)  
**作者**：Ramesh Gundluru, Shubham Gupta, Sri Rama Murty K  

**一句话要点**：提出联合多模态对比学习框架，以增强口语词检测和关键词发现的鲁棒性。

**关键词**：多模态对比学习, 声学词嵌入, 口语词检测, 关键词发现, 音频-文本对齐

## 3 点简述
- 现有声学词嵌入方法存在单模态监督、音频-音频与音频-文本对齐分离优化等局限。
- 通过结合音频-文本对比学习（CLAP损失）和音频-音频对比学习（DWD损失），在共享嵌入空间中统一监督。
- 在词区分任务上优于基线，并灵活支持口语词检测和关键词发现应用。

## 摘要（原文）

> Acoustic Word Embeddings (AWEs) improve the efficiency of speech retrieval tasks such as Spoken Term Detection (STD) and Keyword Spotting (KWS). However, existing approaches suffer from limitations, including unimodal supervision, disjoint optimization of audio-audio and audio-text alignment, and the need for task-specific models. To address these shortcomings, we propose a joint multimodal contrastive learning framework that unifies both acoustic and cross-modal supervision in a shared embedding space. Our approach simultaneously optimizes: (i) audio-text contrastive learning, inspired by the CLAP loss, to align audio and text representations and (ii) audio-audio contrastive learning, via Deep Word Discrimination (DWD) loss, to enhance intra-class compactness and inter-class separation. The proposed method outperforms existing AWE baselines on word discrimination task while flexibly supporting both STD and KWS. To our knowledge, this is the first comprehensive approach of its kind.

