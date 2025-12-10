---
layout: default
title: OpenSubject: Leveraging Video-Derived Identity and Diversity Priors for Subject-driven Image Generation and Manipulation
---

# OpenSubject: Leveraging Video-Derived Identity and Diversity Priors for Subject-driven Image Generation and Manipulation
**arXiv**：[2512.08294v1](https://arxiv.org/abs/2512.08294) · [PDF](https://arxiv.org/pdf/2512.08294.pdf)  
**作者**：Yexin Liu, Manyuan Zhang, Yueze Wang, Hongyu Li, Dian Zheng, Weiming Zhang, Changsheng Lu, Xunliang Cai, Yan Feng, Peng Pei, Harry Yang  

**一句话要点**：提出OpenSubject数据集以解决主题驱动图像生成与编辑中的身份偏离和复杂场景难题

**关键词**：主题驱动图像生成, 视频衍生数据集, 身份先验, 图像编辑, 视觉语言模型, 复杂场景处理

## 3 点简述
- 当前主题驱动图像生成模型常偏离参考身份，在复杂多主题场景中表现不佳
- 构建视频衍生大规模数据集，通过四阶段流程利用跨帧身份先验，包括视频筛选、主题挖掘配对、身份保持图像合成和验证标注
- 实验表明使用OpenSubject训练能提升生成和编辑性能，尤其在复杂场景中

## 摘要（原文）

> Despite the promising progress in subject-driven image generation, current models often deviate from the reference identities and struggle in complex scenes with multiple subjects. To address this challenge, we introduce OpenSubject, a video-derived large-scale corpus with 2.5M samples and 4.35M images for subject-driven generation and manipulation. The dataset is built with a four-stage pipeline that exploits cross-frame identity priors. (i) Video Curation. We apply resolution and aesthetic filtering to obtain high-quality clips. (ii) Cross-Frame Subject Mining and Pairing. We utilize vision-language model (VLM)-based category consensus, local grounding, and diversity-aware pairing to select image pairs. (iii) Identity-Preserving Reference Image Synthesis. We introduce segmentation map-guided outpainting to synthesize the input images for subject-driven generation and box-guided inpainting to generate input images for subject-driven manipulation, together with geometry-aware augmentations and irregular boundary erosion. (iv) Verification and Captioning. We utilize a VLM to validate synthesized samples, re-synthesize failed samples based on stage (iii), and then construct short and long captions. In addition, we introduce a benchmark covering subject-driven generation and manipulation, and then evaluate identity fidelity, prompt adherence, manipulation consistency, and background consistency with a VLM judge. Extensive experiments show that training with OpenSubject improves generation and manipulation performance, particularly in complex scenes.

