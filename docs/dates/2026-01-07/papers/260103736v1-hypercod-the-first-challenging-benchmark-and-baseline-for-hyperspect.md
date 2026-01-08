---
layout: default
title: HyperCOD: The First Challenging Benchmark and Baseline for Hyperspectral Camouflaged Object Detection
---

# HyperCOD: The First Challenging Benchmark and Baseline for Hyperspectral Camouflaged Object Detection
**arXiv**：[2601.03736v1](https://arxiv.org/abs/2601.03736) · [PDF](https://arxiv.org/pdf/2601.03736.pdf)  
**作者**：Shuyan Bai, Tingfa Xu, Peifu Liu, Yuhao Qiu, Huiyan Bai, Huan Chen, Yanyan Peng, Jianan Li  

**一句话要点**：提出HyperCOD基准和HSC-SAM基线以解决高光谱伪装目标检测的挑战

**关键词**：高光谱伪装目标检测, 基准数据集, SAM适配, 光谱显著性, 模态转换

## 3 点简述
- 核心问题：RGB图像在颜色纹理模糊场景中检测伪装目标困难，高光谱图像缺乏大规模基准。
- 方法要点：HSC-SAM将高光谱图像解耦为空间图和光谱显著性图，作为SAM的自适应提示。
- 实验或效果：HSC-SAM在HyperCOD基准上达到新SOTA，并泛化至其他高光谱数据集。

## 摘要（原文）

> RGB-based camouflaged object detection struggles in real-world scenarios where color and texture cues are ambiguous. While hyperspectral image offers a powerful alternative by capturing fine-grained spectral signatures, progress in hyperspectral camouflaged object detection (HCOD) has been critically hampered by the absence of a dedicated, large-scale benchmark. To spur innovation, we introduce HyperCOD, the first challenging benchmark for HCOD. Comprising 350 high-resolution hyperspectral images, It features complex real-world scenarios with minimal objects, intricate shapes, severe occlusions, and dynamic lighting to challenge current models. The advent of foundation models like the Segment Anything Model (SAM) presents a compelling opportunity. To adapt the Segment Anything Model (SAM) for HCOD, we propose HyperSpectral Camouflage-aware SAM (HSC-SAM). HSC-SAM ingeniously reformulates the hyperspectral image by decoupling it into a spatial map fed to SAM's image encoder and a spectral saliency map that serves as an adaptive prompt. This translation effectively bridges the modality gap. Extensive experiments show that HSC-SAM sets a new state-of-the-art on HyperCOD and generalizes robustly to other public HSI datasets. The HyperCOD dataset and our HSC-SAM baseline provide a robust foundation to foster future research in this emerging area.

