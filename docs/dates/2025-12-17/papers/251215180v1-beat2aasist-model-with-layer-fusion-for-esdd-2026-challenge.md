---
layout: default
title: BEAT2AASIST model with layer fusion for ESDD 2026 Challenge
---

# BEAT2AASIST model with layer fusion for ESDD 2026 Challenge
**arXiv**：[2512.15180v1](https://arxiv.org/abs/2512.15180) · [PDF](https://arxiv.org/pdf/2512.15180.pdf)  
**作者**：Sanghyeok Chung, Eujin Kim, Donggun Kim, Gaeun Heo, Jeongbin You, Nahyun Lee, Sunmook Choi, Soyul Han, Seungsang Oh, Il-Youp Kwak  

**一句话要点**：提出BEAT2AASIST模型，通过层融合增强特征表示，用于环境声音深度伪造检测挑战

**关键词**：环境声音深度伪造检测, 层融合策略, 双分支处理, 数据增强, Transformer模型

## 3 点简述
- 针对环境声音深度伪造检测挑战，扩展BEATs-AASIST模型，分割频率或通道维度特征并采用双分支处理
- 引入top-k Transformer层融合策略，包括拼接、CNN门控和SE门控方法，以丰富特征表示
- 应用基于声码器的数据增强提升模型鲁棒性，在官方测试集上取得竞争性性能

## 摘要（原文）

> Recent advances in audio generation have increased the risk of realistic environmental sound manipulation, motivating the ESDD 2026 Challenge as the first large-scale benchmark for Environmental Sound Deepfake Detection (ESDD). We propose BEAT2AASIST which extends BEATs-AASIST by splitting BEATs-derived representations along frequency or channel dimension and processing them with dual AASIST branches. To enrich feature representations, we incorporate top-k transformer layer fusion using concatenation, CNN-gated, and SE-gated strategies. In addition, vocoder-based data augmentation is applied to improve robustness against unseen spoofing methods. Experimental results on the official test sets demonstrate that the proposed approach achieves competitive performance across the challenge tracks.

