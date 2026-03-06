---
layout: default
title: Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups
---

# Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups
**arXiv**：[2603.05507v1](https://arxiv.org/abs/2603.05507) · [PDF](https://arxiv.org/pdf/2603.05507.pdf)  
**作者**：Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  

**一句话要点**：提出基于Transformer的实时3D流媒体修复方法，用于稀疏多相机设置中的纹理补全。

**关键词**：3D流媒体, 图像修复, Transformer网络, 多相机系统, 实时处理, 时空一致性

## 3 点简述
- 核心问题：稀疏多相机实时3D流媒体中，视图有限导致渲染图像缺失纹理和不完整表面。
- 方法要点：采用独立于底层表示的图像后处理，基于多视图感知Transformer网络，利用时空嵌入确保帧间一致性。
- 实验或效果：在实时约束下评估，模型在质量和速度间取得最佳平衡，优于现有修复技术。

## 摘要（原文）

> High-quality 3D streaming from multiple cameras is crucial for immersive experiences in many AR/VR applications. The limited number of views - often due to real-time constraints - leads to missing information and incomplete surfaces in the rendered images. Existing approaches typically rely on simple heuristics for the hole filling, which can result in inconsistencies or visual artifacts. We propose to complete the missing textures using a novel, application-targeted inpainting method independent of the underlying representation as an image-based post-processing step after the novel view rendering. The method is designed as a standalone module compatible with any calibrated multi-camera system. For this we introduce a multi-view aware, transformer-based network architecture using spatio-temporal embeddings to ensure consistency across frames while preserving fine details. Additionally, our resolution-independent design allows adaptation to different camera setups, while an adaptive patch selection strategy balances inference speed and quality, allowing real-time performance. We evaluate our approach against state-of-the-art inpainting techniques under the same real-time constraints and demonstrate that our model achieves the best trade-off between quality and speed, outperforming competitors in both image and video-based metrics.

