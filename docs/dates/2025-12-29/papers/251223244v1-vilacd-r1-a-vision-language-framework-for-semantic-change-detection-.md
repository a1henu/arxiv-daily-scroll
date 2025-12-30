---
layout: default
title: ViLaCD-R1: A Vision-Language Framework for Semantic Change Detection in Remote Sensing
---

# ViLaCD-R1: A Vision-Language Framework for Semantic Change Detection in Remote Sensing
**arXiv**：[2512.23244v1](https://arxiv.org/abs/2512.23244) · [PDF](https://arxiv.org/pdf/2512.23244.pdf)  
**作者**：Xingwei Ma, Shiyang Feng, Bo Zhang, Bin Wang  

**一句话要点**：提出ViLaCD-R1视觉语言框架，以提升遥感语义变化检测的准确性与鲁棒性。

**关键词**：遥感变化检测, 视觉语言模型, 语义理解, 两阶段框架, 强化学习, 像素级定位

## 3 点简述
- 传统遥感变化检测方法难以捕获高层语义且易受非语义扰动影响。
- ViLaCD-R1采用两阶段框架，结合多图像推理器和掩码引导解码器进行精细变化检测。
- 在多个基准测试中，该方法显著提升语义变化识别与定位精度，达到先进水平。

## 摘要（原文）

> Remote sensing change detection (RSCD), a complex multi-image inference task, traditionally uses pixel-based operators or encoder-decoder networks that inadequately capture high-level semantics and are vulnerable to non-semantic perturbations. Although recent multimodal and vision-language model (VLM)-based approaches enhance semantic understanding of change regions by incorporating textual descriptions, they still suffer from challenges such as inaccurate spatial localization, imprecise pixel-level boundary delineation, and limited interpretability. To address these issues, we propose ViLaCD-R1, a two-stage framework comprising a Multi-Image Reasoner (MIR) and a Mask-Guided Decoder (MGD). Specifically, the VLM is trained through supervised fine-tuning (SFT) and reinforcement learning (RL) on block-level dual-temporal inference tasks, taking dual-temporal image patches as input and outputting a coarse change mask. Then, the decoder integrates dual-temporal image features with this coarse mask to predict a precise binary change map. Comprehensive evaluations on multiple RSCD benchmarks demonstrate that ViLaCD-R1 substantially improves true semantic change recognition and localization, robustly suppresses non-semantic variations, and achieves state-of-the-art accuracy in complex real-world scenarios.

