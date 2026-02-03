---
layout: default
title: Masked Autoencoders as Universal Speech Enhancer
---

# Masked Autoencoders as Universal Speech Enhancer
**arXiv**：[2602.02413v1](https://arxiv.org/abs/2602.02413) · [PDF](https://arxiv.org/pdf/2602.02413.pdf)  
**作者**：Rajalaxmi Rajagopalan, Ritwik Giri, Zhiqiang Tang, Kyu Han  

**一句话要点**：提出基于掩码自编码器的通用语音增强方法，以解决缺乏干净语音数据时的自监督学习问题。

**关键词**：语音增强, 自监督学习, 掩码自编码器, 去噪, 去混响, 预训练微调

## 3 点简述
- 核心问题：实际场景中缺乏干净语音，需自监督学习方法来提升语音增强性能并适用于下游任务。
- 方法要点：使用掩码自编码器预训练，通过添加失真学习去除噪声和重构频谱图，再微调于少量配对数据。
- 实验或效果：在去噪和去混响任务中超越基线，达到最先进性能，包括域内和域外数据集评估。

## 摘要（原文）

> Supervised speech enhancement methods have been very successful. However, in practical scenarios, there is a lack of clean speech, and self-supervised learning-based (SSL) speech enhancement methods that offer comparable enhancement performance and can be applied to other speech-related downstream applications are desired. In this work, we develop a masked autoencoder based universal speech enhancer that is agnostic to the type of distortion affecting speech, can handle multiple distortions simultaneously, and is trained in a self-supervised manner. An augmentation stack adds further distortions to the noisy input data. The masked autoencoder model learns to remove the added distortions along with reconstructing the masked regions of the spectrogram during pre-training. The pre-trained embeddings are then used by fine-tuning models trained on a small amount of paired data for specific downstream tasks. We evaluate the pre-trained features for denoising and dereverberation downstream tasks. We explore different augmentations (like single or multi-speaker) in the pre-training augmentation stack and the effect of different noisy input feature representations (like $log1p$ compression) on pre-trained embeddings and downstream fine-tuning enhancement performance. We show that the proposed method not only outperforms the baseline but also achieves state-of-the-art performance for both in-domain and out-of-domain evaluation datasets.

