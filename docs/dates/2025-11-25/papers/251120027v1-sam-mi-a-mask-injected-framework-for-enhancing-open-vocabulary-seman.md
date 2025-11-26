---
layout: default
title: SAM-MI: A Mask-Injected Framework for Enhancing Open-Vocabulary Semantic Segmentation with SAM
---

# SAM-MI: A Mask-Injected Framework for Enhancing Open-Vocabulary Semantic Segmentation with SAM
**arXiv**：[2511.20027v1](https://arxiv.org/abs/2511.20027) · [PDF](https://arxiv.org/pdf/2511.20027.pdf)  
**作者**：Lin Chen, Yingjian Zhu, Qi Yang, Xin Niu, Kun Ding, Shiming Xiang  

**一句话要点**：提出SAM-MI框架以解决开放词汇语义分割中的过分割和硬组合问题

**关键词**：开放词汇语义分割, 掩码注入框架, 稀疏点提示, 浅层掩码聚合, 解耦掩码注入, SAM模型增强

## 3 点简述
- 核心问题：SAM模型在开放词汇语义分割中存在过分割和固定掩码与标签硬组合的挑战
- 方法要点：采用文本引导稀疏点提示、浅层掩码聚合和解耦掩码注入来优化分割过程
- 实验或效果：在MESS基准上mIoU相对提升16.7%，速度提升1.6倍

## 摘要（原文）

> Open-vocabulary semantic segmentation (OVSS) aims to segment and recognize objects universally. Trained on extensive high-quality segmentation data, the segment anything model (SAM) has demonstrated remarkable universal segmentation capabilities, offering valuable support for OVSS. Although previous methods have made progress in leveraging SAM for OVSS, there are still some challenges: (1) SAM's tendency to over-segment and (2) hard combinations between fixed masks and labels. This paper introduces a novel mask-injected framework, SAM-MI, which effectively integrates SAM with OVSS models to address these challenges. Initially, SAM-MI employs a Text-guided Sparse Point Prompter to sample sparse prompts for SAM instead of previous dense grid-like prompts, thus significantly accelerating the mask generation process. The framework then introduces Shallow Mask Aggregation (SMAgg) to merge partial masks to mitigate the SAM's over-segmentation issue. Finally, Decoupled Mask Injection (DMI) incorporates SAM-generated masks for guidance at low-frequency and high-frequency separately, rather than directly combining them with labels. Extensive experiments on multiple benchmarks validate the superiority of SAM-MI. Notably, the proposed method achieves a 16.7% relative improvement in mIoU over Grounded-SAM on the MESS benchmark, along with a 1.6$\times$ speedup. We hope SAM-MI can serve as an alternative methodology to effectively equip the OVSS model with SAM.

