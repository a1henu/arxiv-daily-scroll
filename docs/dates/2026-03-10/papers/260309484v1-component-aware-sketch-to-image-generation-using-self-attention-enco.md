---
layout: default
title: Component-Aware Sketch-to-Image Generation Using Self-Attention Encoding and Coordinate-Preserving Fusion
---

# Component-Aware Sketch-to-Image Generation Using Self-Attention Encoding and Coordinate-Preserving Fusion
**arXiv**：[2603.09484v1](https://arxiv.org/abs/2603.09484) · [PDF](https://arxiv.org/pdf/2603.09484.pdf)  
**作者**：Ali Zia, Muhammad Umer Ramzan, Usman Ali, Muhammad Faheem, Abdelwahed Khamis, Shahnawaz Qureshi  

**一句话要点**：提出基于自注意力编码与坐标保持融合的组件感知草图到图像生成框架，以提升细节重建与空间对齐能力。

**关键词**：草图到图像生成, 自注意力编码, 坐标保持融合, 组件感知框架, 图像合成

## 3 点简述
- 核心问题：草图抽象稀疏且风格多样，现有方法难以重建细节和保持空间对齐。
- 方法要点：采用两阶段架构，包括自注意力自编码器捕获局部特征和坐标保持门控融合模块整合空间布局。
- 实验或效果：在面部和非面部数据集上优于现有方法，在CelebAMask-HQ上FID提升21%，IS提升58%。

## 摘要（原文）

> Translating freehand sketches into photorealistic images remains a fundamental challenge in image synthesis, particularly due to the abstract, sparse, and stylistically diverse nature of sketches. Existing approaches, including GAN-based and diffusion-based models, often struggle to reconstruct fine-grained details, maintain spatial alignment, or adapt across different sketch domains. In this paper, we propose a component-aware, self-refining framework for sketch-to-image generation that addresses these challenges through a novel two-stage architecture. A Self-Attention-based Autoencoder Network (SA2N) first captures localised semantic and structural features from component-wise sketch regions, while a Coordinate-Preserving Gated Fusion (CGF) module integrates these into a coherent spatial layout. Finally, a Spatially Adaptive Refinement Revisor (SARR), built on a modified StyleGAN2 backbone, enhances realism and consistency through iterative refinement guided by spatial context. Extensive experiments across both facial (CelebAMask-HQ, CUFSF) and non-facial (Sketchy, ChairsV2, ShoesV2) datasets demonstrate the robustness and generalizability of our method. The proposed framework consistently outperforms state-of-the-art GAN and diffusion models, achieving significant gains in image fidelity, semantic accuracy, and perceptual quality. On CelebAMask-HQ, our model improves over prior methods by 21% (FID), 58% (IS), 41% (KID), and 20% (SSIM). These results, along with higher efficiency and visual coherence across diverse domains, position our approach as a strong candidate for applications in forensics, digital art restoration, and general sketch-based image synthesis.

