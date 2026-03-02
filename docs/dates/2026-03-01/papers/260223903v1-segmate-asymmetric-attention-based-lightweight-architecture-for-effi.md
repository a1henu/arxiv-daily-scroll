---
layout: default
title: SegMate: Asymmetric Attention-Based Lightweight Architecture for Efficient Multi-Organ Segmentation
---

# SegMate: Asymmetric Attention-Based Lightweight Architecture for Efficient Multi-Organ Segmentation
**arXiv**：[2602.23903v1](https://arxiv.org/abs/2602.23903) · [PDF](https://arxiv.org/pdf/2602.23903.pdf)  
**作者**：Andrei-Alexandru Bunea, Dan-Matei Popovici, Radu Tudor Ionescu  

**一句话要点**：提出SegMate轻量架构，通过非对称注意力机制高效解决医学图像多器官分割问题。

**关键词**：医学图像分割, 轻量架构, 注意力机制, 多器官分割, 计算效率

## 3 点简述
- 核心问题：医学图像分割模型计算资源需求高，限制临床部署。
- 方法要点：集成非对称架构、注意力机制、多尺度特征融合和切片位置条件。
- 实验效果：在多个数据集上减少计算和内存，性能提升约1%，泛化能力强。

## 摘要（原文）

> State-of-the-art models for medical image segmentation achieve excellent accuracy but require substantial computational resources, limiting deployment in resource-constrained clinical settings. We present SegMate, an efficient 2.5D framework that achieves state-of-the-art accuracy, while considerably reducing computational requirements. Our efficient design is the result of meticulously integrating asymmetric architectures, attention mechanisms, multi-scale feature fusion, slice-based positional conditioning, and multi-task optimization. We demonstrate the efficiency-accuracy trade-off of our framework across three modern backbones (EfficientNetV2-M, MambaOut-Tiny, FastViT-T12). We perform experiments on three datasets: TotalSegmentator, SegTHOR and AMOS22. Compared with the vanilla models, SegMate reduces computation (GFLOPs) by up to 2.5x and memory footprint (VRAM) by up to 2.1x, while generally registering performance gains of around 1%. On TotalSegmentator, we achieve a Dice score of 93.51% with only 295MB peak GPU memory. Zero-shot cross-dataset evaluations on SegTHOR and AMOS22 demonstrate strong generalization, with Dice scores of up to 86.85% and 89.35%, respectively. We release our open-source code at https://github.com/andreibunea99/SegMate.

