---
layout: default
title: Diff2DGS: Reliable Reconstruction of Occluded Surgical Scenes via 2D Gaussian Splatting
---

# Diff2DGS: Reliable Reconstruction of Occluded Surgical Scenes via 2D Gaussian Splatting
**arXiv**：[2602.18314v1](https://arxiv.org/abs/2602.18314) · [PDF](https://arxiv.org/pdf/2602.18314.pdf)  
**作者**：Tianyi Song, Danail Stoyanov, Evangelos Mazomenos, Francisco Vasconcelos  

**一句话要点**：提出Diff2DGS框架，通过扩散模型与2D高斯泼溅实现手术场景遮挡区域的可靠三维重建。

**关键词**：手术场景重建, 高斯泼溅, 扩散模型, 遮挡修复, 深度准确性评估, 可学习变形模型

## 3 点简述
- 核心问题：手术场景中遮挡区域重建质量受限，且深度准确性评估不足，缺乏三维真值基准。
- 方法要点：采用两阶段框架，先基于扩散模型修复遮挡组织，再结合可学习变形模型优化2D高斯泼溅以捕捉动态变形。
- 实验或效果：在EndoNeRF和StereoMIS数据集上PSNR达38.02 dB和34.40 dB，并扩展评估至深度准确性分析，优化几何保真度。

## 摘要（原文）

> Real-time reconstruction of deformable surgical scenes is vital for advancing robotic surgery, improving surgeon guidance, and enabling automation. Recent methods achieve dense reconstructions from da Vinci robotic surgery videos, with Gaussian Splatting (GS) offering real-time performance via graphics acceleration. However, reconstruction quality in occluded regions remains limited, and depth accuracy has not been fully assessed, as benchmarks like EndoNeRF and StereoMIS lack 3D ground truth. We propose Diff2DGS, a novel two-stage framework for reliable 3D reconstruction of occluded surgical scenes. In the first stage, a diffusion-based video module with temporal priors inpaints tissue occluded by instruments with high spatial-temporal consistency. In the second stage, we adapt 2D Gaussian Splatting (2DGS) with a Learnable Deformation Model (LDM) to capture dynamic tissue deformation and anatomical geometry. We also extend evaluation beyond prior image-quality metrics by performing quantitative depth accuracy analysis on the SCARED dataset. Diff2DGS outperforms state-of-the-art approaches in both appearance and geometry, reaching 38.02 dB PSNR on EndoNeRF and 34.40 dB on StereoMIS. Furthermore, our experiments demonstrate that optimizing for image quality alone does not necessarily translate into optimal 3D reconstruction accuracy. To address this, we further optimize the depth quality of the reconstructed 3D results, ensuring more faithful geometry in addition to high-fidelity appearance.

