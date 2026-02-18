---
layout: default
title: The Equalizer: Introducing Shape-Gain Decomposition in Neural Audio Codecs
---

# The Equalizer: Introducing Shape-Gain Decomposition in Neural Audio Codecs
**arXiv**：[2602.15491v1](https://arxiv.org/abs/2602.15491) · [PDF](https://arxiv.org/pdf/2602.15491.pdf)  
**作者**：Samir Sadok, Laurent Girin, Xavier Alameda-Pineda  

**一句话要点**：提出Equalizer方法，通过形状-增益分解提升神经音频编解码器的比特率-失真性能与鲁棒性。

**关键词**：神经音频编解码, 形状-增益分解, 比特率-失真优化, 信号鲁棒性, 量化效率

## 3 点简述
- 神经音频编解码器将能量与结构联合编码，导致对输入信号电平变化鲁棒性差和码本冗余。
- 在编码前将信号分解为增益和归一化形状，增益单独量化，形状由神经编解码器处理。
- 实验表明该方法显著提升比特率-失真性能，并大幅降低复杂度，适用于语音信号。

## 摘要（原文）

> Neural audio codecs (NACs) typically encode the short-term energy (gain) and normalized structure (shape) of speech/audio signals jointly within the same latent space. As a result, they are poorly robust to a global variation of the input signal level in the sense that such variation has strong influence on the embedding vectors at the output of the encoder and their quantization. This methodology is inherently inefficient, leading to codebook redundancy and suboptimal bitrate-distortion performance. To address these limitations, we propose to introduce shape-gain decomposition, widely used in classical speech/audio coding, into the NAC framework. The principle of the proposed Equalizer methodology is to decompose the input signal -- before the NAC encoder -- into gain and normalized shape vector on a short-term basis. The shape vector is processed by the NAC, while the gain is quantized with scalar quantization and transmitted separately. The output (decoded) signal is reconstructed from the normalized output of the NAC and the quantized gain. Our experiments conducted on speech signals show that this general methodology, easily applicable to any NAC, enables a substantial gain in bitrate-distortion performance, as well as a massive reduction in complexity.

