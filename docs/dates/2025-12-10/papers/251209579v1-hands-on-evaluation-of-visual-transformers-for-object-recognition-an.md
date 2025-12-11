---
layout: default
title: Hands-on Evaluation of Visual Transformers for Object Recognition and Detection
---

# Hands-on Evaluation of Visual Transformers for Object Recognition and Detection
**arXiv**：[2512.09579v1](https://arxiv.org/abs/2512.09579) · [PDF](https://arxiv.org/pdf/2512.09579.pdf)  
**作者**：Dimitrios N. Vlachogiannis, Dimitrios A. Koutsomitropoulos  

**一句话要点**：评估视觉Transformer在物体识别与检测中的性能，发现其在全局理解任务中优于传统CNN

**关键词**：视觉Transformer, 物体识别, 物体检测, 医疗图像分类, 自注意力机制, 数据增强

## 3 点简述
- 核心问题：CNN在图像全局上下文理解上存在局限，而ViT通过自注意力机制能捕捉全图关系。
- 方法要点：比较纯、分层和混合ViT与传统CNN，在ImageNet、COCO和ChestX-ray14数据集上进行测试。
- 实验或效果：混合和分层Transformer（如Swin和CvT）在精度与计算资源间取得平衡，数据增强在医疗图像上显著提升性能。

## 摘要（原文）

> Convolutional Neural Networks (CNNs) for computer vision sometimes struggle with understanding images in a global context, as they mainly focus on local patterns. On the other hand, Vision Transformers (ViTs), inspired by models originally created for language processing, use self-attention mechanisms, which allow them to understand relationships across the entire image. In this paper, we compare different types of ViTs (pure, hierarchical, and hybrid) against traditional CNN models across various tasks, including object recognition, detection, and medical image classification. We conduct thorough tests on standard datasets like ImageNet for image classification and COCO for object detection. Additionally, we apply these models to medical imaging using the ChestX-ray14 dataset. We find that hybrid and hierarchical transformers, especially Swin and CvT, offer a strong balance between accuracy and computational resources. Furthermore, by experimenting with data augmentation techniques on medical images, we discover significant performance improvements, particularly with the Swin Transformer model. Overall, our results indicate that Vision Transformers are competitive and, in many cases, outperform traditional CNNs, especially in scenarios requiring the understanding of global visual contexts like medical imaging.

