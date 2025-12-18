---
layout: default
title: CLIP-FTI: Fine-Grained Face Template Inversion via CLIP-Driven Attribute Conditioning
---

# CLIP-FTI: Fine-Grained Face Template Inversion via CLIP-Driven Attribute Conditioning
**arXiv**：[2512.15433v1](https://arxiv.org/abs/2512.15433) · [PDF](https://arxiv.org/pdf/2512.15433.pdf)  
**作者**：Longchen Dai, Zixuan Shen, Zhiheng Zhou, Peipeng Yu, Zhihua Xia  

**一句话要点**：提出CLIP-FTI框架，通过CLIP驱动的属性条件化解决人脸模板反演中面部属性过平滑和可迁移性差的问题。

**关键词**：人脸模板反演, CLIP模型, 属性条件化, StyleGAN生成, 跨模态交互, 隐私攻击

## 3 点简述
- 人脸模板泄露后，现有反演方法重建图像面部属性过平滑且可迁移性有限。
- 利用CLIP提取面部特征语义嵌入，通过跨模态交互网络与模板融合，驱动StyleGAN生成细粒度面部属性。
- 实验表明，该方法在身份识别准确率、属性相似度和跨模型攻击可迁移性上优于先前方法。

## 摘要（原文）

> Face recognition systems store face templates for efficient matching. Once leaked, these templates pose a threat: inverting them can yield photorealistic surrogates that compromise privacy and enable impersonation. Although existing research has achieved relatively realistic face template inversion, the reconstructed facial images exhibit over-smoothed facial-part attributes (eyes, nose, mouth) and limited transferability. To address this problem, we present CLIP-FTI, a CLIP-driven fine-grained attribute conditioning framework for face template inversion. Our core idea is to use the CLIP model to obtain the semantic embeddings of facial features, in order to realize the reconstruction of specific facial feature attributes. Specifically, facial feature attribute embeddings extracted from CLIP are fused with the leaked template via a cross-modal feature interaction network and projected into the intermediate latent space of a pretrained StyleGAN. The StyleGAN generator then synthesizes face images with the same identity as the templates but with more fine-grained facial feature attributes. Experiments across multiple face recognition backbones and datasets show that our reconstructions (i) achieve higher identification accuracy and attribute similarity, (ii) recover sharper component-level attribute semantics, and (iii) improve cross-model attack transferability compared to prior reconstruction attacks. To the best of our knowledge, ours is the first method to use additional information besides the face template attack to realize face template inversion and obtains SOTA results.

