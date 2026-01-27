---
layout: default
title: MindCine: Multimodal EEG-to-Video Reconstruction with Large-Scale Pretrained Models
---

# MindCine: Multimodal EEG-to-Video Reconstruction with Large-Scale Pretrained Models
**arXiv**：[2601.18192v1](https://arxiv.org/abs/2601.18192) · [PDF](https://arxiv.org/pdf/2601.18192.pdf)  
**作者**：Tian-Yi Zhou, Xuan-Hao Liu, Bao-Liang Lu, Wei-Long Zheng  

**一句话要点**：提出MindCine框架，通过多模态联合学习和预训练大模型，解决EEG到视频重建中的单模态和数据稀缺问题。

**关键词**：EEG到视频重建, 多模态学习, 预训练模型, 因果注意力, 数据稀缺缓解, Seq2Seq模型

## 3 点简述
- 核心问题：EEG到视频重建面临单模态对齐（仅文本）和数据稀缺导致的过拟合与收敛困难。
- 方法要点：采用多模态联合学习策略整合文本外模态，利用预训练大EEG模型解码语义信息，设计因果注意力Seq2Seq模型解码感知信息。
- 实验或效果：实验显示模型在质量和数量上优于现有方法，验证了多模态互补和大模型缓解数据稀缺的有效性。

## 摘要（原文）

> Reconstructing human dynamic visual perception from electroencephalography (EEG) signals is of great research significance since EEG's non-invasiveness and high temporal resolution. However, EEG-to-video reconstruction remains challenging due to: 1) Single Modality: existing studies solely align EEG signals with the text modality, which ignores other modalities and are prone to suffer from overfitting problems; 2) Data Scarcity: current methods often have difficulty training to converge with limited EEG-video data. To solve the above problems, we propose a novel framework MindCine to achieve high-fidelity video reconstructions on limited data. We employ a multimodal joint learning strategy to incorporate beyond-text modalities in the training stage and leverage a pre-trained large EEG model to relieve the data scarcity issue for decoding semantic information, while a Seq2Seq model with causal attention is specifically designed for decoding perceptual information. Extensive experiments demonstrate that our model outperforms state-of-the-art methods both qualitatively and quantitatively. Additionally, the results underscore the effectiveness of the complementary strengths of different modalities and demonstrate that leveraging a large-scale EEG model can further enhance reconstruction performance by alleviating the challenges associated with limited data.

