---
layout: default
title: Clinically-aligned ischemic stroke segmentation and ASPECTS scoring on NCCT imaging using a slice-gated loss on foundation representations
---

# Clinically-aligned ischemic stroke segmentation and ASPECTS scoring on NCCT imaging using a slice-gated loss on foundation representations
**arXiv**：[2602.23961v1](https://arxiv.org/abs/2602.23961) · [PDF](https://arxiv.org/pdf/2602.23961.pdf)  
**作者**：Hiba Azeem, Behraj Khan, Tahir Qasim Syed  

**一句话要点**：提出基于基础表示和区域感知门控损失的临床对齐框架，用于NCCT缺血性卒中分割和ASPECTS评分。

**关键词**：缺血性卒中分割, ASPECTS评分, 非对比CT成像, 基础模型表示, 解剖结构一致性, 门控损失函数

## 3 点简述
- 核心问题：现有深度学习方法在NCCT卒中分割中缺乏对ASPECTS评分所需解剖结构一致性的建模。
- 方法要点：结合冻结DINOv3骨干和轻量解码器，引入TAGL损失在训练中强制基底节与上节段一致性。
- 实验或效果：在AISD数据集上Dice分数达0.6385，优于基线；在专有ASPECTS数据集上平均Dice从0.698提升至0.767。

## 摘要（原文）

> Rapid infarct assessment on non-contrast CT (NCCT) is essential for acute ischemic stroke management. Most deep learning methods perform pixel-wise segmentation without modeling the structured anatomical reasoning underlying ASPECTS scoring, where basal ganglia (BG) and supraganglionic (SG) levels are clinically interpreted in a coupled manner. We propose a clinically aligned framework that combines a frozen DINOv3 backbone with a lightweight decoder and introduce a Territory-Aware Gated Loss (TAGL) to enforce BG-SG consistency during training. This anatomically informed supervision adds no inference-time complexity. Our method achieves a Dice score of 0.6385 on AISD, outperforming prior CNN and foundation-model baselines. On a proprietary ASPECTS dataset, TAGL improves mean Dice from 0.698 to 0.767. These results demonstrate that integrating foundation representations with structured clinical priors improves NCCT stroke segmentation and ASPECTS delineation.

