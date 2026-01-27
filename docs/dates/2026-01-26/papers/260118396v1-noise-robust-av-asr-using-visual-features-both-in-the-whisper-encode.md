---
layout: default
title: Noise-Robust AV-ASR Using Visual Features Both in the Whisper Encoder and Decoder
---

# Noise-Robust AV-ASR Using Visual Features Both in the Whisper Encoder and Decoder
**arXiv**：[2601.18396v1](https://arxiv.org/abs/2601.18396) · [PDF](https://arxiv.org/pdf/2601.18396.pdf)  
**作者**：Zhengyang Li, Thomas Graave, Björn Möller, Zehang Wu, Matthias Franz, Tim Fingscheidt  

**一句话要点**：提出在Whisper编码器和解码器中双重使用视觉特征的噪声鲁棒视听语音识别方法

**关键词**：视听语音识别, 噪声鲁棒性, 视觉特征融合, Whisper模型, 编码器-解码器架构, LRS3基准

## 3 点简述
- 核心问题：在噪声环境下，传统视听语音识别系统融合视觉信息不足，影响鲁棒性。
- 方法要点：基于Whisper模型，在编码器学习视听交互，在解码器加权模态，实现简单有效的双重视觉融合。
- 实验或效果：在LRS3基准上，双重使用法在多种信噪比下达到4.08%-4.43%平均词错误率，优于典型中间融合。

## 摘要（原文）

> In audiovisual automatic speech recognition (AV-ASR) systems, information fusion of visual features in a pre-trained ASR has been proven as a promising method to improve noise robustness. In this work, based on the prominent Whisper ASR, first, we propose a simple and effective visual fusion method -- use of visual features both in encoder and decoder (dual-use) -- to learn the audiovisual interactions in the encoder and to weigh modalities in the decoder. Second, we compare visual fusion methods in Whisper models of various sizes. Our proposed dual-use method shows consistent noise robustness improvement, e.g., a 35% relative improvement (WER: 4.41% vs. 6.83%) based on Whisper small, and a 57% relative improvement (WER: 4.07% vs. 9.53%) based on Whisper medium, compared to typical reference middle fusion in babble noise with a signal-to-noise ratio (SNR) of 0dB. Third, we conduct ablation studies examining the impact of various module designs and fusion options. Fine-tuned on 1929 hours of audiovisual data, our dual-use method using Whisper medium achieves 4.08% (MUSAN babble noise) and 4.43% (NoiseX babble noise) average WER across various SNRs, thereby establishing a new state-of-the-art in noisy conditions on the LRS3 AV-ASR benchmark. Our code is at https://github.com/ifnspaml/Dual-Use-AVASR

