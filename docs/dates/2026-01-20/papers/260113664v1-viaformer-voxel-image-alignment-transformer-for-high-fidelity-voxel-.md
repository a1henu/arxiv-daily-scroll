---
layout: default
title: VIAFormer: Voxel-Image Alignment Transformer for High-Fidelity Voxel Refinement
---

# VIAFormer: Voxel-Image Alignment Transformer for High-Fidelity Voxel Refinement
**arXiv**：[2601.13664v1](https://arxiv.org/abs/2601.13664) · [PDF](https://arxiv.org/pdf/2601.13664.pdf)  
**作者**：Tiancheng Fang, Bowen Pan, Lingxi Chen, Jiangjing Lyu, Chengfei Lyu, Chaoyue Niu, Fan Wu  

**一句话要点**：提出VIAFormer模型，通过多视图图像引导修复不完整噪声体素，实现高保真体素细化。

**关键词**：体素细化, 多视图引导, 跨模态融合, Transformer模型, 3D重建

## 3 点简述
- 核心问题：多视图条件下修复不完整噪声体素，提升体素质量。
- 方法要点：结合图像索引、校正流目标和混合流Transformer，实现跨模态融合与直接细化轨迹学习。
- 实验或效果：在合成和真实体素修复任务中达到新SOTA，并展示实际3D创建应用潜力。

## 摘要（原文）

> We propose VIAFormer, a Voxel-Image Alignment Transformer model designed for Multi-view Conditioned Voxel Refinement--the task of repairing incomplete noisy voxels using calibrated multi-view images as guidance. Its effectiveness stems from a synergistic design: an Image Index that provides explicit 3D spatial grounding for 2D image tokens, a Correctional Flow objective that learns a direct voxel-refinement trajectory, and a Hybrid Stream Transformer that enables robust cross-modal fusion. Experiments show that VIAFormer establishes a new state of the art in correcting both severe synthetic corruptions and realistic artifacts on the voxel shape obtained from powerful Vision Foundation Models. Beyond benchmarking, we demonstrate VIAFormer as a practical and reliable bridge in real-world 3D creation pipelines, paving the way for voxel-based methods to thrive in large-model, big-data wave.

