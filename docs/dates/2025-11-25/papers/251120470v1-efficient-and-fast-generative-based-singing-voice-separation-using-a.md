---
layout: default
title: Efficient and Fast Generative-Based Singing Voice Separation using a Latent Diffusion Model
---

# Efficient and Fast Generative-Based Singing Voice Separation using a Latent Diffusion Model
**arXiv**：[2511.20470v1](https://arxiv.org/abs/2511.20470) · [PDF](https://arxiv.org/pdf/2511.20470.pdf)  
**作者**：Genís Plaja-Roglans, Yun-Ning Hung, Xavier Serra, Igor Pereira  

**一句话要点**：提出基于潜在扩散模型的生成式歌声分离方法，以高效解决音乐源分离问题。

**关键词**：歌声分离, 潜在扩散模型, 生成式方法, 音乐源分离, 高效推理

## 3 点简述
- 核心问题：音乐信号中源重叠和相关性导致分离困难，且训练需所有源数据。
- 方法要点：使用潜在扩散模型，在紧凑潜在空间生成样本后解码为音频，提升效率。
- 实验或效果：在信号质量和干扰去除上优于现有生成系统，与非生成系统相当。

## 摘要（原文）

> Extracting individual elements from music mixtures is a valuable tool for music production and practice. While neural networks optimized to mask or transform mixture spectrograms into the individual source(s) have been the leading approach, the source overlap and correlation in music signals poses an inherent challenge. Also, accessing all sources in the mixture is crucial to train these systems, while complicated. Attempts to address these challenges in a generative fashion exist, however, the separation performance and inference efficiency remain limited. In this work, we study the potential of diffusion models to advance toward bridging this gap, focusing on generative singing voice separation relying only on corresponding pairs of isolated vocals and mixtures for training. To align with creative workflows, we leverage latent diffusion: the system generates samples encoded in a compact latent space, and subsequently decodes these into audio. This enables efficient optimization and faster inference. Our system is trained using only open data. We outperform existing generative separation systems, and level the compared non-generative systems on a list of signal quality measures and on interference removal. We provide a noise robustness study on the latent encoder, providing insights on its potential for the task. We release a modular toolkit for further research on the topic.

