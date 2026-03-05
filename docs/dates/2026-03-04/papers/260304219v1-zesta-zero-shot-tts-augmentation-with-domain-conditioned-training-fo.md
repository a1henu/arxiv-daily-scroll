---
layout: default
title: ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis
---

# ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis
**arXiv**：[2603.04219v1](https://arxiv.org/abs/2603.04219) · [PDF](https://arxiv.org/pdf/2603.04219.pdf)  
**作者**：Youngwon Choi, Jinwoo Oh, Hwayeon Kim, Hyeonyu Kim  

**一句话要点**：提出ZeSTA框架，通过域条件训练解决低资源个性化语音合成中合成增强导致的说话人相似度下降问题。

**关键词**：零样本语音合成, 数据增强, 个性化语音合成, 域条件训练, 低资源学习

## 3 点简述
- 核心问题：在低资源个性化语音合成中，直接混合大量合成语音与有限真实录音会降低说话人相似度。
- 方法要点：采用轻量级域嵌入区分真实与合成语音，结合真实数据过采样，无需修改基础架构。
- 实验或效果：在LibriTTS和内部数据集上验证，提升说话人相似度，同时保持可懂度和感知质量。

## 摘要（原文）

> We investigate the use of zero-shot text-to-speech (ZS-TTS) as a data augmentation source for low-resource personalized speech synthesis. While synthetic augmentation can provide linguistically rich and phonetically diverse speech, naively mixing large amounts of synthetic speech with limited real recordings often leads to speaker similarity degradation during fine-tuning. To address this issue, we propose ZeSTA, a simple domain-conditioned training framework that distinguishes real and synthetic speech via a lightweight domain embedding, combined with real-data oversampling to stabilize adaptation under extremely limited target data, without modifying the base architecture. Experiments on LibriTTS and an in-house dataset with two ZS-TTS sources demonstrate that our approach improves speaker similarity over naive synthetic augmentation while preserving intelligibility and perceptual quality.

