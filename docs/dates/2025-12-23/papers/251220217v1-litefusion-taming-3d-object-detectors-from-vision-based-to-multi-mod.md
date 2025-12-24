---
layout: default
title: LiteFusion: Taming 3D Object Detectors from Vision-Based to Multi-Modal with Minimal Adaptation
---

# LiteFusion: Taming 3D Object Detectors from Vision-Based to Multi-Modal with Minimal Adaptation
**arXiv**：[2512.20217v1](https://arxiv.org/abs/2512.20217) · [PDF](https://arxiv.org/pdf/2512.20217.pdf)  
**作者**：Xiangxuan Ren, Zhongdao Wang, Pin Tang, Guoqing Wang, Jilai Zheng, Chao Ma  

**一句话要点**：提出LiteFusion，通过将LiDAR作为几何信息补充增强相机检测，解决多模态3D检测器依赖复杂架构和部署困难的问题。

**关键词**：3D目标检测, 多模态融合, 部署友好, 四元数空间, 几何信息增强, 相机-LiDAR融合

## 3 点简述
- 核心问题：多模态3D检测器依赖LiDAR和3D稀疏卷积，导致性能下降和部署受限。
- 方法要点：在四元数空间集成LiDAR点云特征到图像特征，消除3D主干网络，实现紧凑跨模态嵌入。
- 实验或效果：在nuScenes数据集上提升基线相机检测器+20.4% mAP，参数仅增1.1%，无LiDAR时仍保持强健性能。

## 摘要（原文）

> 3D object detection is fundamental for safe and robust intelligent transportation systems. Current multi-modal 3D object detectors often rely on complex architectures and training strategies to achieve higher detection accuracy. However, these methods heavily rely on the LiDAR sensor so that they suffer from large performance drops when LiDAR is absent, which compromises the robustness and safety of autonomous systems in practical scenarios. Moreover, existing multi-modal detectors face difficulties in deployment on diverse hardware platforms, such as NPUs and FPGAs, due to their reliance on 3D sparse convolution operators, which are primarily optimized for NVIDIA GPUs. To address these challenges, we reconsider the role of LiDAR in the camera-LiDAR fusion paradigm and introduce a novel multi-modal 3D detector, LiteFusion. Instead of treating LiDAR point clouds as an independent modality with a separate feature extraction backbone, LiteFusion utilizes LiDAR data as a complementary source of geometric information to enhance camera-based detection. This straightforward approach completely eliminates the reliance on a 3D backbone, making the method highly deployment-friendly. Specifically, LiteFusion integrates complementary features from LiDAR points into image features within a quaternion space, where the orthogonal constraints are well-preserved during network training. This helps model domain-specific relations across modalities, yielding a compact cross-modal embedding. Experiments on the nuScenes dataset show that LiteFusion improves the baseline vision-based detector by +20.4% mAP and +19.7% NDS with a minimal increase in parameters (1.1%) without using dedicated LiDAR encoders. Notably, even in the absence of LiDAR input, LiteFusion maintains strong results , highlighting its favorable robustness and effectiveness across diverse fusion paradigms and deployment scenarios.

