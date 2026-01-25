---
layout: default
title: Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech
---

# Transfer Learning from ImageNet for MEG-Based Decoding of Imagined Speech
**arXiv**：[2601.15909v1](https://arxiv.org/abs/2601.15909) · [PDF](https://arxiv.org/pdf/2601.15909.pdf)  
**作者**：Soufiane Jhilal, Stéphanie Martin, Anne-Lise Giraud  

**一句话要点**：提出基于ImageNet预训练视觉模型的图像化MEG表示方法，以解码想象语音信号。

**关键词**：想象语音解码, MEG信号处理, 预训练视觉模型, 时频表示, 跨被试评估

## 3 点简述
- 核心问题：想象语音的非侵入式解码因信号弱、分布广和标记数据有限而具挑战性。
- 方法要点：将MEG信号通过可学习卷积转换为时频表示，作为图像输入预训练视觉模型。
- 实验或效果：模型在想象与静默、静默阅读及元音解码任务中达到最高90.4%、81.0%和60.6%的平衡准确率。

## 摘要（原文）

> Non-invasive decoding of imagined speech remains challenging due to weak, distributed signals and limited labeled data. Our paper introduces an image-based approach that transforms magnetoencephalography (MEG) signals into time-frequency representations compatible with pretrained vision models. MEG data from 21 participants performing imagined speech tasks were projected into three spatial scalogram mixtures via a learnable sensor-space convolution, producing compact image-like inputs for ImageNet-pretrained vision architectures. These models outperformed classical and non-pretrained models, achieving up to 90.4% balanced accuracy for imagery vs. silence, 81.0% vs. silent reading, and 60.6% for vowel decoding. Cross-subject evaluation confirmed that pretrained models capture shared neural representations, and temporal analyses localized discriminative information to imagery-locked intervals. These findings show that pretrained vision models applied to image-based MEG representations can effectively capture the structure of imagined speech in non-invasive neural signals.

