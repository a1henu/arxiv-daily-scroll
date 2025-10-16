---
layout: default
title: AVAR-Net: A Lightweight Audio-Visual Anomaly Recognition Framework with a Benchmark Dataset
---

# AVAR-Net: A Lightweight Audio-Visual Anomaly Recognition Framework with a Benchmark Dataset
**arXiv**：[2510.13630v1](https://arxiv.org/abs/2510.13630) · [PDF](https://arxiv.org/pdf/2510.13630.pdf)  
**作者**：Amjid Ali, Zulfiqar Ahmad Khan, Altaf Hussain, Muhammad Munsif, Adnan Hussain, Sung Wook Baik  

**一句话要点**：提出AVAR-Net轻量级音视频异常识别框架，解决视觉单模态在恶劣条件下的不可靠问题。

**关键词**：音视频异常识别, 轻量级框架, 多模态融合, 时序卷积网络, 基准数据集

## 3 点简述
- 核心问题：现有方法依赖视觉数据，在遮挡、低光照等条件下不可靠，且缺乏大规模音视频数据集。
- 方法要点：使用Wav2Vec2和MobileViT提取音视频特征，早期融合后通过MTCN学习时空依赖。
- 实验效果：在VAAR数据集准确率达89.29%，XD-Violence数据集平均精度提升2.8%。

## 摘要（原文）

> Anomaly recognition plays a vital role in surveillance, transportation,
> healthcare, and public safety. However, most existing approaches rely solely on
> visual data, making them unreliable under challenging conditions such as
> occlusion, low illumination, and adverse weather. Moreover, the absence of
> large-scale synchronized audio-visual datasets has hindered progress in
> multimodal anomaly recognition. To address these limitations, this study
> presents AVAR-Net, a lightweight and efficient audio-visual anomaly recognition
> framework designed for real-world environments. AVAR-Net consists of four main
> modules: an audio feature extractor, a video feature extractor, fusion
> strategy, and a sequential pattern learning network that models cross-modal
> relationships for anomaly recognition. Specifically, the Wav2Vec2 model
> extracts robust temporal features from raw audio, while MobileViT captures both
> local and global visual representations from video frames. An early fusion
> mechanism combines these modalities, and a Multi-Stage Temporal Convolutional
> Network (MTCN) model that learns long-range temporal dependencies within the
> fused representation, enabling robust spatiotemporal reasoning. A novel
> Visual-Audio Anomaly Recognition (VAAR) dataset, is also introduced, serving as
> a medium-scale benchmark containing 3,000 real-world videos with synchronized
> audio across ten diverse anomaly classes. Experimental evaluations demonstrate
> that AVAR-Net achieves 89.29% accuracy on VAAR and 88.56% Average Precision on
> the XD-Violence dataset, improving Average Precision by 2.8% over existing
> state-of-the-art methods. These results highlight the effectiveness,
> efficiency, and generalization capability of the proposed framework, as well as
> the utility of VAAR as a benchmark for advancing multimodal anomaly recognition
> research.

