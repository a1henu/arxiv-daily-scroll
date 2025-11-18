---
layout: default
title: Medal S: Spatio-Textual Prompt Model for Medical Segmentation
---

# Medal S: Spatio-Textual Prompt Model for Medical Segmentation
**arXiv**：[2511.13001v1](https://arxiv.org/abs/2511.13001) · [PDF](https://arxiv.org/pdf/2511.13001.pdf)  
**作者**：Pengcheng Shi, Jiawei Chen, Jiaqi Liu, Xinglin Zhang, Tao Chen, Lei Li  

**一句话要点**：提出Medal S医学分割基础模型，支持空间和文本提示以提升多类分割效率与精度

**关键词**：医学图像分割, 空间文本提示, 多模态处理, 并行推理, 3D卷积优化

## 3 点简述
- 核心问题：现有文本提示方法缺乏空间感知，导致分辨率不匹配和分割不准确
- 方法要点：通过通道对齐和轻量3D卷积模块，实现端到端空间与文本提示并行处理
- 实验或效果：在五模态验证集上，DSC达75.44，推理时间减少超90%，优于SAT和nnU-Net

## 摘要（原文）

> We introduce Medal S, a medical segmentation foundation model that supports native-resolution spatial and textual prompts within an end-to-end trainable framework. Unlike text-only methods lacking spatial awareness, Medal S achieves channel-wise alignment between volumetric prompts and text embeddings, mitigating inaccuracies from resolution mismatches. By preserving full 3D context, it efficiently processes multiple native-resolution masks in parallel, enhancing multi-class segmentation performance. A lightweight 3D convolutional module enables precise voxel-space refinement guided by both prompt types, supporting up to 243 classes across CT, MRI, PET, ultrasound, and microscopy modalities in the BiomedSegFM dataset. Medal S offers two prompting modes: a text-only mode, where model predictions serve as spatial prompts for self-refinement without human input, and a hybrid mode, incorporating manual annotations for enhanced flexibility. For 24-class segmentation, parallel spatial prompting reduces inference time by more than 90% compared to sequential prompting. We propose dynamic resampling to address target-patch ratio imbalance, extending SAT and nnU-Net for data augmentation. Furthermore, we develop optimized text preprocessing, a two-stage inference strategy, and post-processing techniques to improve memory efficiency, precision, and inference speed. On the five-modality average on the validation set, Medal S outperforms SAT with a DSC of 75.44 (vs. 69.83), NSD of 77.34 (vs. 71.06), F1 of 38.24 (vs. 24.88), and DSC TP of 65.46 (vs. 46.97). Medal S achieves excellent performance by harmonizing spatial precision with semantic textual guidance, demonstrating superior efficiency and accuracy in multi-class medical segmentation tasks compared to sequential prompt-based approaches. Medal S will be publicly available at https://github.com/yinghemedical/Medal-S.

