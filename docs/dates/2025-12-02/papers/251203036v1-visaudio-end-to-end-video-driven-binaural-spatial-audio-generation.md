---
layout: default
title: ViSAudio: End-to-End Video-Driven Binaural Spatial Audio Generation
---

# ViSAudio: End-to-End Video-Driven Binaural Spatial Audio Generation
**arXiv**：[2512.03036v1](https://arxiv.org/abs/2512.03036) · [PDF](https://arxiv.org/pdf/2512.03036.pdf)  
**作者**：Mengchen Zhang, Qi Chen, Tong Wu, Zihan Liu, Dahua Lin  

**一句话要点**：提出ViSAudio端到端框架，从无声视频直接生成双耳空间音频以解决现有方法误差累积问题。

**关键词**：视频到音频生成, 双耳空间音频, 端到端框架, 条件流匹配, 时空对齐

## 3 点简述
- 核心问题：现有视频到音频生成方法多输出单声道，双耳音频生成依赖两阶段流程导致误差累积和时空不一致。
- 方法要点：采用条件流匹配与双分支音频生成架构，结合条件时空模块平衡声道一致性与空间特性。
- 实验或效果：在BiAudio数据集上验证，ViSAudio在客观指标和主观评估中优于现有方法，生成高质量空间音频。

## 摘要（原文）

> Despite progress in video-to-audio generation, the field focuses predominantly on mono output, lacking spatial immersion. Existing binaural approaches remain constrained by a two-stage pipeline that first generates mono audio and then performs spatialization, often resulting in error accumulation and spatio-temporal inconsistencies. To address this limitation, we introduce the task of end-to-end binaural spatial audio generation directly from silent video. To support this task, we present the BiAudio dataset, comprising approximately 97K video-binaural audio pairs spanning diverse real-world scenes and camera rotation trajectories, constructed through a semi-automated pipeline. Furthermore, we propose ViSAudio, an end-to-end framework that employs conditional flow matching with a dual-branch audio generation architecture, where two dedicated branches model the audio latent flows. Integrated with a conditional spacetime module, it balances consistency between channels while preserving distinctive spatial characteristics, ensuring precise spatio-temporal alignment between audio and the input video. Comprehensive experiments demonstrate that ViSAudio outperforms existing state-of-the-art methods across both objective metrics and subjective evaluations, generating high-quality binaural audio with spatial immersion that adapts effectively to viewpoint changes, sound-source motion, and diverse acoustic environments. Project website: https://kszpxxzmc.github.io/ViSAudio-project.

