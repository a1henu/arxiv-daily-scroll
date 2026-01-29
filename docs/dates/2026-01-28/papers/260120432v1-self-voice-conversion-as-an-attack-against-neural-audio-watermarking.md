---
layout: default
title: Self Voice Conversion as an Attack against Neural Audio Watermarking
---

# Self Voice Conversion as an Attack against Neural Audio Watermarking
**arXiv**：[2601.20432v1](https://arxiv.org/abs/2601.20432) · [PDF](https://arxiv.org/pdf/2601.20432.pdf)  
**作者**：Yigitcan Özer, Wanying Ge, Zhe Zhang, Xin Wang, Junichi Yamagishi  

**一句话要点**：提出自语音转换作为攻击方法，以评估神经音频水印的安全性。

**关键词**：音频水印, 自语音转换, 深度学习攻击, 水印安全性, 声学特征

## 3 点简述
- 核心问题：深度学习攻击对音频水印安全构成新威胁，现有评估主要针对传统失真。
- 方法要点：利用自语音转换模型，在保持说话人身份和内容下改变声学特征，作为通用攻击。
- 实验或效果：攻击显著降低先进水印方法的可靠性，突出现代技术安全风险。

## 摘要（原文）

> Audio watermarking embeds auxiliary information into speech while maintaining speaker identity, linguistic content, and perceptual quality. Although recent advances in neural and digital signal processing-based watermarking methods have improved imperceptibility and embedding capacity, robustness is still primarily assessed against conventional distortions such as compression, additive noise, and resampling. However, the rise of deep learning-based attacks introduces novel and significant threats to watermark security. In this work, we investigate self voice conversion as a universal, content-preserving attack against audio watermarking systems. Self voice conversion remaps a speaker's voice to the same identity while altering acoustic characteristics through a voice conversion model. We demonstrate that this attack severely degrades the reliability of state-of-the-art watermarking approaches and highlight its implications for the security of modern audio watermarking techniques.

