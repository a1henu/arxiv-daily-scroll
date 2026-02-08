---
layout: default
title: PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction
---

# PoseGaussian: Pose-Driven Novel View Synthesis for Robust 3D Human Reconstruction
**arXiv**：[2602.05190v1](https://arxiv.org/abs/2602.05190) · [PDF](https://arxiv.org/pdf/2602.05190.pdf)  
**作者**：Ju Shen, Chen Chen, Tam V. Nguyen, Vijayan K. Asari  

**一句话要点**：提出PoseGaussian，一种姿态引导的高斯泼溅框架，用于高保真人体新视角合成，以增强动态场景的鲁棒性。

**关键词**：新视角合成, 高斯泼溅, 人体姿态引导, 动态场景重建, 实时渲染

## 3 点简述
- 核心问题：解决动态人体场景中关节运动和严重自遮挡带来的新视角合成挑战。
- 方法要点：将人体姿态作为结构先验和时间线索，嵌入几何和时序阶段，实现端到端可训练。
- 实验或效果：在多个数据集上验证，实现实时渲染（100 FPS），在感知质量和结构准确性上达到先进水平。

## 摘要（原文）

> We propose PoseGaussian, a pose-guided Gaussian Splatting framework for high-fidelity human novel view synthesis. Human body pose serves a dual purpose in our design: as a structural prior, it is fused with a color encoder to refine depth estimation; as a temporal cue, it is processed by a dedicated pose encoder to enhance temporal consistency across frames. These components are integrated into a fully differentiable, end-to-end trainable pipeline. Unlike prior works that use pose only as a condition or for warping, PoseGaussian embeds pose signals into both geometric and temporal stages to improve robustness and generalization. It is specifically designed to address challenges inherent in dynamic human scenes, such as articulated motion and severe self-occlusion. Notably, our framework achieves real-time rendering at 100 FPS, maintaining the efficiency of standard Gaussian Splatting pipelines. We validate our approach on ZJU-MoCap, THuman2.0, and in-house datasets, demonstrating state-of-the-art performance in perceptual quality and structural accuracy (PSNR 30.86, SSIM 0.979, LPIPS 0.028).

