---
layout: default
title: Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation
---

# Uncertainty-Aware 3D Emotional Talking Face Synthesis with Emotion Prior Distillation
**arXiv**：[2601.19112v1](https://arxiv.org/abs/2601.19112) · [PDF](https://arxiv.org/pdf/2601.19112.pdf)  
**作者**：Nanhan Shen, Zhilei Liu  

**一句话要点**：提出UA-3DTalk以解决3D情感说话人脸合成中的音视频情感对齐与多视图融合不确定性挑战

**关键词**：3D情感说话人脸合成, 不确定性建模, 情感先验蒸馏, 多视图融合, 音频情感提取, 高斯编码

## 3 点简述
- 核心问题：现有3D方法存在音视频情感对齐差和多视图融合策略忽视不确定性，影响情感表达与渲染质量。
- 方法要点：通过先验提取模块解耦音频特征，情感蒸馏模块实现细粒度情感控制，不确定性变形模块自适应融合多视图。
- 实验或效果：在情感数据集上，UA-3DTalk在E-FID、SyncC和LPIPS指标上优于现有方法，提升情感对齐、唇同步和渲染质量。

## 摘要（原文）

> Emotional Talking Face synthesis is pivotal in multimedia and signal processing, yet existing 3D methods suffer from two critical challenges: poor audio-vision emotion alignment, manifested as difficult audio emotion extraction and inadequate control over emotional micro-expressions; and a one-size-fits-all multi-view fusion strategy that overlooks uncertainty and feature quality differences, undermining rendering quality. We propose UA-3DTalk, Uncertainty-Aware 3D Emotional Talking Face Synthesis with emotion prior distillation, which has three core modules: the Prior Extraction module disentangles audio into content-synchronized features for alignment and person-specific complementary features for individualization; the Emotion Distillation module introduces a multi-modal attention-weighted fusion mechanism and 4D Gaussian encoding with multi-resolution code-books, enabling fine-grained audio emotion extraction and precise control of emotional micro-expressions; the Uncertainty-based Deformation deploys uncertainty blocks to estimate view-specific aleatoric (input noise) and epistemic (model parameters) uncertainty, realizing adaptive multi-view fusion and incorporating a multi-head decoder for Gaussian primitive optimization to mitigate the limitations of uniform-weight fusion. Extensive experiments on regular and emotional datasets show UA-3DTalk outperforms state-of-the-art methods like DEGSTalk and EDTalk by 5.2% in E-FID for emotion alignment, 3.1% in SyncC for lip synchronization, and 0.015 in LPIPS for rendering quality. Project page: https://mrask999.github.io/UA-3DTalk

