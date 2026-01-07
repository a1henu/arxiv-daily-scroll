---
layout: default
title: Lesion Segmentation in FDG-PET/CT Using Swin Transformer U-Net 3D: A Robust Deep Learning Framework
---

# Lesion Segmentation in FDG-PET/CT Using Swin Transformer U-Net 3D: A Robust Deep Learning Framework
**arXiv**：[2601.02864v1](https://arxiv.org/abs/2601.02864) · [PDF](https://arxiv.org/pdf/2601.02864.pdf)  
**作者**：Shovini Guha, Dwaipayan Nandi  

**一句话要点**：提出Swin Transformer U-Net 3D框架，用于FDG-PET/CT扫描中的病灶分割，提升癌症诊断精度。

**关键词**：病灶分割, PET/CT成像, Swin Transformer, 3D U-Net, 深度学习框架, 癌症诊断

## 3 点简述
- 核心问题：PET/CT成像中病灶分割的自动化与准确性对癌症诊疗至关重要。
- 方法要点：结合移位窗口自注意力与U-Net跳跃连接，捕获全局上下文和精细解剖细节。
- 实验或效果：在AutoPET III数据集上，Dice分数达0.88，优于基线3D U-Net，推理速度更快。

## 摘要（原文）

> Accurate and automated lesion segmentation in Positron Emission Tomography / Computed Tomography (PET/CT) imaging is essential for cancer diagnosis and therapy planning. This paper presents a Swin Transformer UNet 3D (SwinUNet3D) framework for lesion segmentation in Fluorodeoxyglucose Positron Emission Tomography / Computed Tomography (FDG-PET/CT) scans. By combining shifted window self-attention with U-Net style skip connections, the model captures both global context and fine anatomical detail. We evaluate SwinUNet3D on the AutoPET III FDG dataset and compare it against a baseline 3D U-Net. Results show that SwinUNet3D achieves a Dice score of 0.88 and IoU of 0.78, surpassing 3D U-Net (Dice 0.48, IoU 0.32) while also delivering faster inference times. Qualitative analysis demonstrates improved detection of small and irregular lesions, reduced false positives, and more accurate PET/CT fusion. While the framework is currently limited to FDG scans and trained under modest GPU resources, it establishes a strong foundation for future multi-tracer, multi-center evaluations and benchmarking against other transformer-based architectures. Overall, SwinUNet3D represents an efficient and robust approach to PET/CT lesion segmentation, advancing the integration of transformer-based models into oncology imaging workflows.

