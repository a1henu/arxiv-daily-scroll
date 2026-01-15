---
layout: default
title: SSVP: Synergistic Semantic-Visual Prompting for Industrial Zero-Shot Anomaly Detection
---

# SSVP: Synergistic Semantic-Visual Prompting for Industrial Zero-Shot Anomaly Detection
**arXiv**：[2601.09147v1](https://arxiv.org/abs/2601.09147) · [PDF](https://arxiv.org/pdf/2601.09147.pdf)  
**作者**：Chenhao Fu, Han Fang, Xiuzheng Zheng, Wenbo Wei, Yonghua Li, Hao Sun, Xuelong Li  

**一句话要点**：提出SSVP方法，通过语义-视觉协同提示解决工业零样本异常检测中全局语义与细粒度结构平衡问题。

**关键词**：零样本异常检测, 视觉语言模型, 语义-视觉协同, 工业检测, 多尺度融合, 动态提示生成

## 3 点简述
- 现有零样本异常检测方法依赖单一视觉骨干，难以兼顾全局语义泛化与细粒度结构判别。
- SSVP引入HSVS机制融合DINOv3多尺度结构先验到CLIP语义空间，并利用VCPG和VTAM实现动态提示生成与异常映射校准。
- 在七个工业基准测试中，SSVP在MVTec-AD上达到93.0%图像AUROC和92.2%像素AUROC，性能领先。

## 摘要（原文）

> Zero-Shot Anomaly Detection (ZSAD) leverages Vision-Language Models (VLMs) to enable supervision-free industrial inspection. However, existing ZSAD paradigms are constrained by single visual backbones, which struggle to balance global semantic generalization with fine-grained structural discriminability. To bridge this gap, we propose Synergistic Semantic-Visual Prompting (SSVP), that efficiently fuses diverse visual encodings to elevate model's fine-grained perception. Specifically, SSVP introduces the Hierarchical Semantic-Visual Synergy (HSVS) mechanism, which deeply integrates DINOv3's multi-scale structural priors into the CLIP semantic space. Subsequently, the Vision-Conditioned Prompt Generator (VCPG) employs cross-modal attention to guide dynamic prompt generation, enabling linguistic queries to precisely anchor to specific anomaly patterns. Furthermore, to address the discrepancy between global scoring and local evidence, the Visual-Text Anomaly Mapper (VTAM) establishes a dual-gated calibration paradigm. Extensive evaluations on seven industrial benchmarks validate the robustness of our method; SSVP achieves state-of-the-art performance with 93.0\% Image-AUROC and 92.2\% Pixel-AUROC on MVTec-AD, significantly outperforming existing zero-shot approaches.

