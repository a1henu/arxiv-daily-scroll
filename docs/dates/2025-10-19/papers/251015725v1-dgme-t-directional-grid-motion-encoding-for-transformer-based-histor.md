---
layout: default
title: DGME-T: Directional Grid Motion Encoding for Transformer-Based Historical Camera Movement Classification
---

# DGME-T: Directional Grid Motion Encoding for Transformer-Based Historical Camera Movement Classification
**arXiv**：[2510.15725v1](https://arxiv.org/abs/2510.15725) · [PDF](https://arxiv.org/pdf/2510.15725.pdf)  
**作者**：Tingyu Lin, Armin Dadras, Florian Kleber, Robert Sablatnig  

**一句话要点**：提出DGME-T方法，通过方向性网格运动编码增强Transformer，提升历史影片相机运动分类鲁棒性

**关键词**：相机运动分类, Transformer模型, 光流编码, 历史影片分析, 跨域学习, 鲁棒性增强

## 3 点简述
- 核心问题：当代相机运动分类模型在噪声、低对比度历史影片上性能下降
- 方法要点：基于光流提取方向性网格运动编码，通过可学习归一化融合层集成到Video Swin Transformer
- 实验效果：在现代和历史数据集上准确率和宏F1分数均显著提升，跨域微调进一步改善性能

## 摘要（原文）

> Camera movement classification (CMC) models trained on contemporary,
> high-quality footage often degrade when applied to archival film, where noise,
> missing frames, and low contrast obscure motion cues. We bridge this gap by
> assembling a unified benchmark that consolidates two modern corpora into four
> canonical classes and restructures the HISTORIAN collection into five balanced
> categories. Building on this benchmark, we introduce DGME-T, a lightweight
> extension to the Video Swin Transformer that injects directional grid motion
> encoding, derived from optical flow, via a learnable and normalised late-fusion
> layer. DGME-T raises the backbone's top-1 accuracy from 81.78% to 86.14% and
> its macro F1 from 82.08% to 87.81% on modern clips, while still improving the
> demanding World-War-II footage from 83.43% to 84.62% accuracy and from 81.72%
> to 82.63% macro F1. A cross-domain study further shows that an intermediate
> fine-tuning stage on modern data increases historical performance by more than
> five percentage points. These results demonstrate that structured motion priors
> and transformer representations are complementary and that even a small,
> carefully calibrated motion head can substantially enhance robustness in
> degraded film analysis. Related resources are available at
> https://github.com/linty5/DGME-T.

