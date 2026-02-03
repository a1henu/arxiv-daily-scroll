---
layout: default
title: Lung Nodule Image Synthesis Driven by Two-Stage Generative Adversarial Networks
---

# Lung Nodule Image Synthesis Driven by Two-Stage Generative Adversarial Networks
**arXiv**：[2602.02171v1](https://arxiv.org/abs/2602.02171) · [PDF](https://arxiv.org/pdf/2602.02171.pdf)  
**作者**：Lu Cao, Xiquan He, Junying Zeng, Chaoyun Mai, Min Luo  

**一句话要点**：提出两阶段生成对抗网络以增强肺结节CT图像合成的多样性和可控性

**关键词**：肺结节合成, 生成对抗网络, 图像分割, CT图像增强, 医学影像生成

## 3 点简述
- 肺结节CT数据集样本有限且多样性不足，影响检测模型性能
- 采用两阶段方法：首阶段生成语义分割掩码控制结构，次阶段转换为CT图像增强纹理
- 在LUNA16数据集上，准确率提升4.6%，mAP提升4%

## 摘要（原文）

> The limited sample size and insufficient diversity of lung nodule CT datasets severely restrict the performance and generalization ability of detection models. Existing methods generate images with insufficient diversity and controllability, suffering from issues such as monotonous texture features and distorted anatomical structures. Therefore, we propose a two-stage generative adversarial network (TSGAN) to enhance the diversity and spatial controllability of synthetic data by decoupling the morphological structure and texture features of lung nodules. In the first stage, StyleGAN is used to generate semantic segmentation mask images, encoding lung nodules and tissue backgrounds to control the anatomical structure of lung nodule images; The second stage uses the DL-Pix2Pix model to translate the mask map into CT images, employing local importance attention to capture local features, while utilizing dynamic weight multi-head window attention to enhance the modeling capability of lung nodule texture and background. Compared to the original dataset, the accuracy improved by 4.6% and mAP by 4% on the LUNA16 dataset. Experimental results demonstrate that TSGAN can enhance the quality of synthetic images and the performance of detection models.

