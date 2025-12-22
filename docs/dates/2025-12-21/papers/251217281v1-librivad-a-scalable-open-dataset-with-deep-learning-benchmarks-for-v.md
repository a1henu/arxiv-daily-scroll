---
layout: default
title: LibriVAD: A Scalable Open Dataset with Deep Learning Benchmarks for Voice Activity Detection
---

# LibriVAD: A Scalable Open Dataset with Deep Learning Benchmarks for Voice Activity Detection
**arXiv**：[2512.17281v1](https://arxiv.org/abs/2512.17281) · [PDF](https://arxiv.org/pdf/2512.17281.pdf)  
**作者**：Ioannis Stylianou, Achintya kr. Sarkar, Nauman Dawalatabad, James Glass, Zheng-Hua Tan  

**一句话要点**：提出LibriVAD数据集以解决语音活动检测在噪声和未见条件下的挑战

**关键词**：语音活动检测, 开源数据集, Vision Transformer, 噪声鲁棒性, 泛化性能, 深度学习基准

## 3 点简述
- 核心问题：缺乏大规模、可控的公开数据集限制了语音活动检测研究进展
- 方法要点：基于LibriSpeech构建可扩展数据集，控制信噪比和静默比，引入Vision Transformer架构
- 实验或效果：ViT结合MFCC特征在多种条件下优于现有模型，数据集规模和平衡提升泛化性能

## 摘要（原文）

> Robust Voice Activity Detection (VAD) remains a challenging task, especially under noisy, diverse, and unseen acoustic conditions. Beyond algorithmic development, a key limitation in advancing VAD research is the lack of large-scale, systematically controlled, and publicly available datasets. To address this, we introduce LibriVAD - a scalable open-source dataset derived from LibriSpeech and augmented with diverse real-world and synthetic noise sources. LibriVAD enables systematic control over speech-to-noise ratio, silence-to-speech ratio (SSR), and noise diversity, and is released in three sizes (15 GB, 150 GB, and 1.5 TB) with two variants (LibriVAD-NonConcat and LibriVAD-Concat) to support different experimental setups. We benchmark multiple feature-model combinations, including waveform, Mel-Frequency Cepstral Coefficients (MFCC), and Gammatone filter bank cepstral coefficients, and introduce the Vision Transformer (ViT) architecture for VAD. Our experiments show that ViT with MFCC features consistently outperforms established VAD models such as boosted deep neural network and convolutional long short-term memory deep neural network across seen, unseen, and out-of-distribution (OOD) conditions, including evaluation on the real-world VOiCES dataset. We further analyze the impact of dataset size and SSR on model generalization, experimentally showing that scaling up dataset size and balancing SSR noticeably and consistently enhance VAD performance under OOD conditions. All datasets, trained models, and code are publicly released to foster reproducibility and accelerate progress in VAD research.

