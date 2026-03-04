---
layout: default
title: VLMFusionOcc3D: VLM Assisted Multi-Modal 3D Semantic Occupancy Prediction
---

# VLMFusionOcc3D: VLM Assisted Multi-Modal 3D Semantic Occupancy Prediction
**arXiv**：[2603.02609v1](https://arxiv.org/abs/2603.02609) · [PDF](https://arxiv.org/pdf/2603.02609.pdf)  
**作者**：A. Enes Doruk, Hasan F. Ates  

**一句话要点**：提出VLMFusionOcc3D，利用视觉语言模型增强多模态3D语义占据预测，以解决稀疏几何网格中的语义模糊和恶劣天气下的性能下降问题。

**关键词**：3D语义占据预测, 视觉语言模型, 多模态融合, 自动驾驶, 恶劣天气鲁棒性, 体素网格

## 3 点简述
- 核心问题：当前基于体素的占据模型在稀疏几何网格中语义模糊，且在恶劣天气下性能下降。
- 方法要点：采用双分支特征提取，引入实例驱动的VLM注意力和天气感知自适应融合机制，注入高级语义和地理先验。
- 实验或效果：在nuScenes和SemanticKITTI数据集上验证，显著提升基线性能，尤其在恶劣天气场景中表现突出。

## 摘要（原文）

> This paper introduces VLMFusionOcc3D, a robust multimodal framework for dense 3D semantic occupancy prediction in autonomous driving. Current voxel-based occupancy models often struggle with semantic ambiguity in sparse geometric grids and performance degradation under adverse weather conditions. To address these challenges, we leverage the rich linguistic priors of Vision-Language Models (VLMs) to anchor ambiguous voxel features to stable semantic concepts. Our framework initiates with a dual-branch feature extraction pipeline that projects multi-view images and LiDAR point clouds into a unified voxel space. We propose Instance-driven VLM Attention (InstVLM), which utilizes gated cross-attention and LoRA-adapted CLIP embeddings to inject high-level semantic and geographic priors directly into the 3D voxels. Furthermore, we introduce Weather-Aware Adaptive Fusion (WeathFusion), a dynamic gating mechanism that utilizes vehicle metadata and weather-conditioned prompts to re-weight sensor contributions based on real-time environmental reliability. To ensure structural consistency, a Depth-Aware Geometric Alignment (DAGA) loss is employed to align dense camera-derived geometry with sparse, spatially accurate LiDAR returns. Extensive experiments on the nuScenes and SemanticKITTI datasets demonstrate that our plug-and-play modules consistently enhance the performance of state-of-the-art voxel-based baselines. Notably, our approach achieves significant improvements in challenging weather scenarios, offering a scalable and robust solution for complex urban navigation.

