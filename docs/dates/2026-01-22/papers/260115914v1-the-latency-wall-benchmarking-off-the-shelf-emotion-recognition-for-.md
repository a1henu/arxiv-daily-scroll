---
layout: default
title: The Latency Wall: Benchmarking Off-the-Shelf Emotion Recognition for Real-Time Virtual Avatars
---

# The Latency Wall: Benchmarking Off-the-Shelf Emotion Recognition for Real-Time Virtual Avatars
**arXiv**：[2601.15914v1](https://arxiv.org/abs/2601.15914) · [PDF](https://arxiv.org/pdf/2601.15914.pdf)  
**作者**：Yarin Benyamin  

**一句话要点**：基准测试现成模型在虚拟角色上的零样本表情识别，揭示实时VR治疗中的延迟瓶颈

**关键词**：实时表情识别, 虚拟现实治疗, 延迟-精度权衡, 零样本学习, 基准测试, 轻量级架构

## 3 点简述
- 核心问题：实时VR治疗需严格延迟-精度权衡，但现成DL模型常忽视硬件约束。
- 方法要点：在UIBVFED数据集上评估YOLO变体和通用ViT，包括CLIP、SigLIP和ViT-FER。
- 实验或效果：YOLOv11n检测最优，但通用Transformer在分类阶段存在延迟墙，精度和速度不足。

## 摘要（原文）

> In the realm of Virtual Reality (VR) and Human-Computer Interaction (HCI), real-time emotion recognition shows promise for supporting individuals with Autism Spectrum Disorder (ASD) in improving social skills. This task requires a strict latency-accuracy trade-off, with motion-to-photon (MTP) latency kept below 140 ms to maintain contingency. However, most off-the-shelf Deep Learning models prioritize accuracy over the strict timing constraints of commodity hardware. As a first step toward accessible VR therapy, we benchmark State-of-the-Art (SOTA) models for Zero-Shot Facial Expression Recognition (FER) on virtual characters using the UIBVFED dataset. We evaluate Medium and Nano variants of YOLO (v8, v11, and v12) for face detection, alongside general-purpose Vision Transformers including CLIP, SigLIP, and ViT-FER.Our results on CPU-only inference demonstrate that while face detection on stylized avatars is robust (100% accuracy), a "Latency Wall" exists in the classification stage. The YOLOv11n architecture offers the optimal balance for detection (~54 ms). However, general-purpose Transformers like CLIP and SigLIP fail to achieve viable accuracy (<23%) or speed (>150 ms) for real-time loops. This study highlights the necessity for lightweight, domain-specific architectures to enable accessible, real-time AI in therapeutic settings.

