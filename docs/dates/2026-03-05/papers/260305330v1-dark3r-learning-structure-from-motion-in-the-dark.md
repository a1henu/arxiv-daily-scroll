---
layout: default
title: Dark3R: Learning Structure from Motion in the Dark
---

# Dark3R: Learning Structure from Motion in the Dark
**arXiv**：[2603.05330v1](https://arxiv.org/abs/2603.05330) · [PDF](https://arxiv.org/pdf/2603.05330.pdf)  
**作者**：Andrew Y Guo, Anagh Malik, SaiKiran Tedla, Yutong Dai, Yiqian Qin, Zach Salehe, Benjamin Attal, Sotiris Nousias, Kyros Kutulakos, David B. Lindell  

**一句话要点**：提出Dark3R框架，通过师生蒸馏适应极端低光条件，实现信噪比低于-4 dB的原始图像运动结构恢复。

**关键词**：低光运动结构恢复, 师生蒸馏, 原始图像处理, 无监督3D学习, 新视角合成

## 3 点简述
- 核心问题：传统方法在信噪比低于-4 dB的极端低光原始图像中失效，无法进行特征匹配和相机姿态估计。
- 方法要点：利用大规模3D基础模型，通过师生蒸馏过程适应低光，无需3D监督，仅需噪声-干净原始图像对训练。
- 实验或效果：引入新曝光数据集，包含约42,000张多视角原始图像，在低信噪比下实现最先进的运动结构恢复和新视角合成。

## 摘要（原文）

> We introduce Dark3R, a framework for structure from motion in the dark that operates directly on raw images with signal-to-noise ratios (SNRs) below $-4$ dB -- a regime where conventional feature- and learning-based methods break down. Our key insight is to adapt large-scale 3D foundation models to extreme low-light conditions through a teacher--student distillation process, enabling robust feature matching and camera pose estimation in low light. Dark3R requires no 3D supervision; it is trained solely on noisy--clean raw image pairs, which can be either captured directly or synthesized using a simple Poisson--Gaussian noise model applied to well-exposed raw images. To train and evaluate our approach, we introduce a new, exposure-bracketed dataset that includes $\sim$42,000 multi-view raw images with ground-truth 3D annotations, and we demonstrate that Dark3R achieves state-of-the-art structure from motion in the low-SNR regime. Further, we demonstrate state-of-the-art novel view synthesis in the dark using Dark3R's predicted poses and a coarse-to-fine radiance field optimization procedure.

