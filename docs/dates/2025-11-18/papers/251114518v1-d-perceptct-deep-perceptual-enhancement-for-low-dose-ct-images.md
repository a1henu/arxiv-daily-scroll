---
layout: default
title: D-PerceptCT: Deep Perceptual Enhancement for Low-Dose CT Images
---

# D-PerceptCT: Deep Perceptual Enhancement for Low-Dose CT Images
**arXiv**：[2511.14518v1](https://arxiv.org/abs/2511.14518) · [PDF](https://arxiv.org/pdf/2511.14518.pdf)  
**作者**：Taifour Yousra Nabila, Azeddine Beghdadi, Marie Luong, Zuheng Ming, Habib Zaidi, Faouzi Alaya Cheikh  

**一句话要点**：提出D-PerceptCT以增强低剂量CT图像，保留感知相关特征

**关键词**：低剂量CT增强, 人类视觉系统, 语义感知, 状态空间模型, 感知损失函数

## 3 点简述
- 低剂量CT图像质量因噪声和过度平滑而下降，影响诊断细节
- 方法结合人类视觉系统，使用视觉双路径提取器和全局-局部状态空间块
- 在Mayo2016数据集上实验，优于现有方法，保留结构和纹理信息

## 摘要（原文）

> Low Dose Computed Tomography (LDCT) is widely used as an imaging solution to aid diagnosis and other clinical tasks. However, this comes at the price of a deterioration in image quality due to the low dose of radiation used to reduce the risk of secondary cancer development. While some efficient methods have been proposed to enhance LDCT quality, many overestimate noise and perform excessive smoothing, leading to a loss of critical details. In this paper, we introduce D-PerceptCT, a novel architecture inspired by key principles of the Human Visual System (HVS) to enhance LDCT images. The objective is to guide the model to enhance or preserve perceptually relevant features, thereby providing radiologists with CT images where critical anatomical structures and fine pathological details are perceptu- ally visible. D-PerceptCT consists of two main blocks: 1) a Visual Dual-path Extractor (ViDex), which integrates semantic priors from a pretrained DINOv2 model with local spatial features, allowing the network to incorporate semantic-awareness during enhancement; (2) a Global-Local State-Space block that captures long-range information and multiscale features to preserve the important structures and fine details for diagnosis. In addition, we propose a novel deep perceptual loss, designated as the Deep Perceptual Relevancy Loss Function (DPRLF), which is inspired by human contrast sensitivity, to further emphasize perceptually important features. Extensive experiments on the Mayo2016 dataset demonstrate the effectiveness of D-PerceptCT method for LDCT enhancement, showing better preservation of structural and textural information within LDCT images compared to SOTA methods.

