---
layout: default
title: Visual-Informed Speech Enhancement Using Attention-Based Beamforming
---

# Visual-Informed Speech Enhancement Using Attention-Based Beamforming
**arXiv**：[2603.05270v1](https://arxiv.org/abs/2603.05270) · [PDF](https://arxiv.org/pdf/2603.05270.pdf)  
**作者**：Chihyun Liu, Jiaxuan Fan, Mingtung Sun, Michael Anthony, Mingsian R. Bai, Yu Tsao  

**一句话要点**：提出视觉引导神经波束形成网络，以提升动态场景下语音增强性能

**关键词**：语音增强, 神经波束形成, 多模态融合, 视觉语音识别, 注意力机制

## 3 点简述
- 针对单通道方法在低信噪比、高混响及动态说话人场景中性能受限的问题
- 集成麦克风阵列信号处理与深度神经网络，利用预训练视觉模型提取唇动特征进行说话人识别
- 实验表明系统在静态和动态说话人场景下均优于基线方法，具有更好的鲁棒性

## 摘要（原文）

> Recent studies have demonstrated that incorporating auxiliary information, such as speaker voiceprint or visual cues, can substantially improve Speech Enhancement (SE) performance. However, single-channel methods often yield suboptimal results in low signal-to-noise ratio (SNR) conditions, when there is high reverberation, or in complex scenarios involving dynamic speakers, overlapping speech, or non-stationary noise. To address these issues, we propose a novel Visual-Informed Neural Beamforming Network (VI-NBFNet), which integrates microphone array signal processing and deep neural networks (DNNs) using multimodal input features. The proposed network leverages a pretrained visual speech recognition model to extract lip movements as input features, which serve for voice activity detection (VAD) and target speaker identification. The system is intended to handle both static and moving speakers by introducing a supervised end-to-end beamforming framework equipped with an attention mechanism. The experimental results demonstrated that the proposed audiovisual system has achieved better SE performance and robustness for both stationary and dynamic speaker scenarios, compared to several baseline methods.

