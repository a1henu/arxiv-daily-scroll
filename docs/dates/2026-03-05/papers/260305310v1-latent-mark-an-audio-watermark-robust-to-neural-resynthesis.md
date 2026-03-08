---
layout: default
title: Latent-Mark: An Audio Watermark Robust to Neural Resynthesis
---

# Latent-Mark: An Audio Watermark Robust to Neural Resynthesis
**arXiv**：[2603.05310v1](https://arxiv.org/abs/2603.05310) · [PDF](https://arxiv.org/pdf/2603.05310.pdf)  
**作者**：Yen-Shan Chen, Shih-Yu Lai, Ying-Jung Tsou, Yi-Cheng Lin, Bing-Yu Chen, Yun-Nung Chen, Hung-Yi Lee, Shang-Tse Chen  

**一句话要点**：提出Latent-Mark框架以解决音频水印在神经重合成攻击下的脆弱性问题

**关键词**：音频水印, 神经编解码器, 潜在空间优化, 跨编解码器鲁棒性, 零样本迁移

## 3 点简述
- 现有音频水印技术对传统DSP攻击鲁棒，但易受神经重合成攻击，因神经编解码器丢弃不可感知波形变化
- 方法核心是将水印嵌入编解码器不变潜在空间，通过优化波形诱导潜在表示方向性偏移，并约束扰动以保持不可感知性
- 引入跨编解码器优化，针对共享潜在不变量，实验显示对未见神经编解码器具有零样本迁移性和鲁棒性

## 摘要（原文）

> While existing audio watermarking techniques have achieved strong robustness against traditional digital signal processing (DSP) attacks, they remain vulnerable to neural resynthesis. This occurs because modern neural audio codecs act as semantic filters and discard the imperceptible waveform variations used in prior watermarking methods. To address this limitation, we propose Latent-Mark, the first zero-bit audio watermarking framework designed to survive semantic compression. Our key insight is that robustness to the encode-decode process requires embedding the watermark within the codec's invariant latent space. We achieve this by optimizing the audio waveform to induce a detectable directional shift in its encoded latent representation, while constraining perturbations to align with the natural audio manifold to ensure imperceptibility. To prevent overfitting to a single codec's quantization rules, we introduce Cross-Codec Optimization, jointly optimizing the waveform across multiple surrogate codecs to target shared latent invariants. Extensive evaluations demonstrate robust zero-shot transferability to unseen neural codecs, achieving state-of-the-art resilience against traditional DSP attacks while preserving perceptual imperceptibility. Our work inspires future research into universal watermarking frameworks capable of maintaining integrity across increasingly complex and diverse generative distortions.

