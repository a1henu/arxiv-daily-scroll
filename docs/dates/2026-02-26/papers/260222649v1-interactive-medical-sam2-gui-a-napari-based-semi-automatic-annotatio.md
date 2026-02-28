---
layout: default
title: Interactive Medical-SAM2 GUI: A Napari-based semi-automatic annotation tool for medical images
---

# Interactive Medical-SAM2 GUI: A Napari-based semi-automatic annotation tool for medical images
**arXiv**：[2602.22649v1](https://arxiv.org/abs/2602.22649) · [PDF](https://arxiv.org/pdf/2602.22649.pdf)  
**作者**：Woojae Hong, Jong Ha Hwang, Jiyong Chung, Joongyeon Choi, Hyunngun Kim, Yong Hwy Kim  

**一句话要点**：提出基于Napari的交互式医学图像半自动标注工具，以解决3D医学图像标注效率低和流程不统一的问题。

**关键词**：医学图像标注, 半自动标注工具, SAM2传播, Napari集成, 3D图像处理, DICOM/NIfTI支持

## 3 点简述
- 核心问题：3D医学图像手动标注耗时昂贵，现有工具缺乏统一、面向队列的本地工作流。
- 方法要点：集成SAM2风格传播，通过框/点提示实现稀疏提示下的掩码传播，支持序列化标注和交互式修正。
- 实验或效果：提供本地优先工作流，支持多研究高效标注，输出时保留图像几何并支持体积测量和3D渲染。

## 摘要（原文）

> Interactive Medical-SAM2 GUI is an open-source desktop application for semi-automatic annotation of 2D and 3D medical images. Built on the Napari multi-dimensional viewer, box/point prompting is integrated with SAM2-style propagation by treating a 3D volume as a slice sequence, enabling mask propagation from sparse prompts using Medical-SAM2 on top of SAM2. Voxel-level annotation remains essential for developing and validating medical imaging algorithms, yet manual labeling is slow and expensive for 3D scans, and existing integrations frequently emphasize per-slice interaction without providing a unified, cohort-oriented workflow for navigation, propagation, interactive correction, and quantitative export in a single local pipeline. To address this practical limitation, a local-first Napari workflow is provided for efficient 3D annotation across multiple studies using standard DICOM series and/or NIfTI volumes. Users can annotate cases sequentially under a single root folder with explicit proceed/skip actions, initialize objects via box-first prompting (including first/last-slice initialization for single-object propagation), refine predictions with point prompts, and finalize labels through prompt-first correction prior to saving. During export, per-object volumetry and 3D volume rendering are supported, and image geometry is preserved via SimpleITK. The GUI is implemented in Python using Napari and PyTorch, with optional N4 bias-field correction, and is intended exclusively for research annotation workflows. The code is released on the project page: https://github.com/SKKU-IBE/Medical-SAM2GUI/.

