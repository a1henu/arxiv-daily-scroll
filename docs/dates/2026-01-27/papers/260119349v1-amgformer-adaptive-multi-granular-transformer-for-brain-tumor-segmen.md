---
layout: default
title: AMGFormer: Adaptive Multi-Granular Transformer for Brain Tumor Segmentation with Missing Modalities
---

# AMGFormer: Adaptive Multi-Granular Transformer for Brain Tumor Segmentation with Missing Modalities
**arXiv**：[2601.19349v1](https://arxiv.org/abs/2601.19349) · [PDF](https://arxiv.org/pdf/2601.19349.pdf)  
**作者**：Chengxiang Guo, Jian Wang, Junhua Fei, Xiao Li, Chunling Chen, Yun Jin  

**一句话要点**：提出AMGFormer自适应多粒度Transformer，解决脑肿瘤分割中模态缺失导致的性能不稳定问题。

**关键词**：脑肿瘤分割, 多模态MRI, 缺失模态, Transformer, 自适应融合, 临床部署

## 3 点简述
- 核心问题：多模态MRI脑肿瘤分割中，模态缺失导致现有方法性能方差>40%，临床不可靠。
- 方法要点：通过QuadIntegrator Bridge、Multi-Granular Attention Orchestrator和Modality Quality-Aware Enhancement模块，实现自适应融合与稳定性提升。
- 实验或效果：在BraTS 2018上，Dice分数方差<0.5%，单模态ET分割相对改进40-81%，推理时间1.2秒。

## 摘要（原文）

> Multimodal MRI is essential for brain tumor segmentation, yet missing modalities in clinical practice cause existing methods to exhibit >40% performance variance across modality combinations, rendering them clinically unreliable. We propose AMGFormer, achieving significantly improved stability through three synergistic modules: (1) QuadIntegrator Bridge (QIB) enabling spatially adaptive fusion maintaining consistent predictions regardless of available modalities, (2) Multi-Granular Attention Orchestrator (MGAO) focusing on pathological regions to reduce background sensitivity, and (3) Modality Quality-Aware Enhancement (MQAE) preventing error propagation from corrupted sequences. On BraTS 2018, our method achieves 89.33% WT, 82.70% TC, 67.23% ET Dice scores with <0.5% variance across 15 modality combinations, solving the stability crisis. Single-modality ET segmentation shows 40-81% relative improvements over state-of-the-art methods. The method generalizes to BraTS 2020/2021, achieving up to 92.44% WT, 89.91% TC, 84.57% ET. The model demonstrates potential for clinical deployment with 1.2s inference. Code: https://github.com/guochengxiangives/AMGFormer.

