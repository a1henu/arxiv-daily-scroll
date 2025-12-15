---
layout: default
title: Evaluating Foundation Models' 3D Understanding Through Multi-View Correspondence Analysis
---

# Evaluating Foundation Models' 3D Understanding Through Multi-View Correspondence Analysis
**arXiv**：[2512.11574v1](https://arxiv.org/abs/2512.11574) · [PDF](https://arxiv.org/pdf/2512.11574.pdf)  
**作者**：Valentina Lilova, Toyesh Chakravorty, Julian I. Bibo, Emma Boccaletti, Brandon Li, Lívia Baxová, Cees G. M. Snoek, Mohammadreza Salehi  

**一句话要点**：提出无需微调的基准以评估基础模型在3D多视角对应中的内在理解能力

**关键词**：3D场景理解, 基础模型评估, 多视角对应, 无需微调基准, MVImgNet数据集, 视觉特征质量

## 3 点简述
- 现有评估依赖下游微调，难以隔离预训练编码器的3D推理能力
- 基于Hummingbird框架扩展至3D场景，使用MVImgNet数据集进行多视角分割基准测试
- 评估8个模型，显示DINO编码器在大视角变化下保持竞争力，3D感知模型需调整

## 摘要（原文）

> Benchmarking 3D spatial understanding of foundation models is essential for real-world applications such as robotics and autonomous driving. Existing evaluations often rely on downstream finetuning with linear heads or task-specific decoders, making it difficult to isolate the intrinsic 3D reasoning ability of pretrained encoders. In this work, we introduce a novel benchmark for in-context 3D scene understanding that requires no finetuning and directly probes the quality of dense visual features. Building on the Hummingbird framework, which evaluates in-context 2D scene understanding, we extend the setup to the 3D Multi-View ImageNet (MVImgNet) dataset. Given a set of images from objects in specific angles (keys), we benchmark the performance of segmenting novel views (queries) and report the scores in 4 categories of easy, medium, hard, and extreme based on the key-query view contrast. We benchmark 8 state-of-the-art foundation models and show DINO-based encoders remain competitive across large viewpoint shifts, while 3D-aware models like VGGT require dedicated multi-view adjustments. Our code is publicly available at https://github.com/ToyeshC/open-hummingbird-3d-eval .

