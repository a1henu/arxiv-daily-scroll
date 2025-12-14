---
layout: default
title: Self-Supervised Contrastive Embedding Adaptation for Endoscopic Image Matching
---

# Self-Supervised Contrastive Embedding Adaptation for Endoscopic Image Matching
**arXiv**：[2512.10379v1](https://arxiv.org/abs/2512.10379) · [PDF](https://arxiv.org/pdf/2512.10379.pdf)  
**作者**：Alberto Rota, Elena De Momi  

**一句话要点**：提出自监督对比嵌入适应方法，以解决内窥镜图像匹配中的特征对应问题。

**关键词**：内窥镜图像匹配, 自监督学习, 对比学习, 特征嵌入适应, 新视图合成, Transformer优化

## 3 点简述
- 核心问题：内窥镜图像匹配因弱透视、非朗伯反射和可变形解剖而困难，传统方法性能受限。
- 方法要点：利用新视图合成生成真实对应，通过对比学习优化Transformer层，增强DINOv2骨干以产生直接匹配的嵌入。
- 实验或效果：在SCARED数据集上超越现有方法，匹配精度更高，极线误差更低。

## 摘要（原文）

> Accurate spatial understanding is essential for image-guided surgery, augmented reality integration and context awareness. In minimally invasive procedures, where visual input is the sole intraoperative modality, establishing precise pixel-level correspondences between endoscopic frames is critical for 3D reconstruction, camera tracking, and scene interpretation. However, the surgical domain presents distinct challenges: weak perspective cues, non-Lambertian tissue reflections, and complex, deformable anatomy degrade the performance of conventional computer vision techniques. While Deep Learning models have shown strong performance in natural scenes, their features are not inherently suited for fine-grained matching in surgical images and require targeted adaptation to meet the demands of this domain. This research presents a novel Deep Learning pipeline for establishing feature correspondences in endoscopic image pairs, alongside a self-supervised optimization framework for model training. The proposed methodology leverages a novel-view synthesis pipeline to generate ground-truth inlier correspondences, subsequently utilized for mining triplets within a contrastive learning paradigm. Through this self-supervised approach, we augment the DINOv2 backbone with an additional Transformer layer, specifically optimized to produce embeddings that facilitate direct matching through cosine similarity thresholding. Experimental evaluation demonstrates that our pipeline surpasses state-of-the-art methodologies on the SCARED datasets improved matching precision and lower epipolar error compared to the related work. The proposed framework constitutes a valuable contribution toward enabling more accurate high-level computer vision applications in surgical endoscopy.

