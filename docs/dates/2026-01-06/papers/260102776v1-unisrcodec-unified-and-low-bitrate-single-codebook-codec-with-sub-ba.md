---
layout: default
title: UniSRCodec: Unified and Low-Bitrate Single Codebook Codec with Sub-Band Reconstruction
---

# UniSRCodec: Unified and Low-Bitrate Single Codebook Codec with Sub-Band Reconstruction
**arXiv**：[2601.02776v1](https://arxiv.org/abs/2601.02776) · [PDF](https://arxiv.org/pdf/2601.02776.pdf)  
**作者**：Zhisheng Zhang, Xiang Li, Yixuan Zhou, Jing Peng, Shengbo Cai, Guoyang Zeng, Zhiyong Wu  

**一句话要点**：提出UniSRCodec以解决单码本音频编解码器在统一建模和高频音频支持上的不足。

**关键词**：神经音频编解码, 单码本编解码器, 子带重建, 梅尔频谱图压缩, 低比特率音频编码

## 3 点简述
- 核心问题：单码本音频编解码器存在低保真度、统一音频建模无效和高频音频建模能力差的问题。
- 方法要点：采用梅尔频谱图进行时频压缩，结合声码器恢复相位，并引入子带重建技术提升高低频压缩质量。
- 实验或效果：在40令牌率下实现跨域单码本编解码器的SOTA性能，重建质量可与某些多码本方法媲美。

## 摘要（原文）

> Neural Audio Codecs (NACs) can reduce transmission overhead by performing compact compression and reconstruction, which also aim to bridge the gap between continuous and discrete signals. Existing NACs can be divided into two categories: multi-codebook and single-codebook codecs. Multi-codebook codecs face challenges such as structural complexity and difficulty in adapting to downstream tasks, while single-codebook codecs, though structurally simpler, suffer from low-fidelity, ineffective modeling of unified audio, and an inability to support modeling of high-frequency audio. We propose the UniSRCodec, a single-codebook codec capable of supporting high sampling rate, low-bandwidth, high fidelity, and unified. We analyze the inefficiency of waveform-based compression and introduce the time and frequency compression method using the Mel-spectrogram, and cooperate with a Vocoder to recover the phase information of the original audio. Moreover, we propose a sub-band reconstruction technique to achieve high-quality compression across both low and high frequency bands. Subjective and objective experimental results demonstrate that UniSRCodec achieves state-of-the-art (SOTA) performance among cross-domain single-codebook codecs with only a token rate of 40, and its reconstruction quality is comparable to that of certain multi-codebook methods. Our demo page is available at https://wxzyd123.github.io/unisrcodec.

