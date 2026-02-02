---
layout: default
title: PEAR: Pixel-aligned Expressive humAn mesh Recovery
---

# PEAR: Pixel-aligned Expressive humAn mesh Recovery
**arXiv**：[2601.22693v1](https://arxiv.org/abs/2601.22693) · [PDF](https://arxiv.org/pdf/2601.22693.pdf)  
**作者**：Jiahao Wu, Yunfei Liu, Lijian Lin, Ye Zhu, Lei Zhu, Jingyi Li, Yu Li  

**一句话要点**：提出PEAR框架以快速从单张图像恢复像素对齐的3D人体网格

**关键词**：3D人体重建, 像素对齐, SMPLX参数推断, 实时推理, ViT模型, 数据增强

## 3 点简述
- 现有SMPLX方法存在推理慢、姿态粗糙、细节区域对齐差等问题
- 采用统一ViT模型实现实时推理，并通过像素级监督优化几何细节
- 在多个基准数据集上实验显示姿态估计精度显著提升

## 摘要（原文）

> Reconstructing detailed 3D human meshes from a single in-the-wild image remains a fundamental challenge in computer vision. Existing SMPLX-based methods often suffer from slow inference, produce only coarse body poses, and exhibit misalignments or unnatural artifacts in fine-grained regions such as the face and hands. These issues make current approaches difficult to apply to downstream tasks. To address these challenges, we propose PEAR-a fast and robust framework for pixel-aligned expressive human mesh recovery. PEAR explicitly tackles three major limitations of existing methods: slow inference, inaccurate localization of fine-grained human pose details, and insufficient facial expression capture. Specifically, to enable real-time SMPLX parameter inference, we depart from prior designs that rely on high resolution inputs or multi-branch architectures. Instead, we adopt a clean and unified ViT-based model capable of recovering coarse 3D human geometry. To compensate for the loss of fine-grained details caused by this simplified architecture, we introduce pixel-level supervision to optimize the geometry, significantly improving the reconstruction accuracy of fine-grained human details. To make this approach practical, we further propose a modular data annotation strategy that enriches the training data and enhances the robustness of the model. Overall, PEAR is a preprocessing-free framework that can simultaneously infer EHM-s (SMPLX and scaled-FLAME) parameters at over 100 FPS. Extensive experiments on multiple benchmark datasets demonstrate that our method achieves substantial improvements in pose estimation accuracy compared to previous SMPLX-based approaches. Project page: https://wujh2001.github.io/PEAR

