---
layout: default
title: Dual-Encoder Transformer-Based Multimodal Learning for Ischemic Stroke Lesion Segmentation Using Diffusion MRI
---

# Dual-Encoder Transformer-Based Multimodal Learning for Ischemic Stroke Lesion Segmentation Using Diffusion MRI
**arXiv**：[2512.20436v1](https://arxiv.org/abs/2512.20436) · [PDF](https://arxiv.org/pdf/2512.20436.pdf)  
**作者**：Muhammad Usman, Azka Rehman, Muhammad Mutti Ur Rehman, Abd Ur Rehman, Muhammad Umar Farooq  

**一句话要点**：提出双编码器TransUNet架构，用于扩散MRI的缺血性卒中病灶分割。

**关键词**：缺血性卒中分割, 扩散MRI, 双编码器, TransUNet, 多模态学习

## 3 点简述
- 核心问题：扩散MRI中缺血性卒中病灶分割因病灶外观多变而具挑战性。
- 方法要点：基于TransUNet，设计双编码器从DWI和ADC学习模态特定表示，并整合相邻切片信息。
- 实验或效果：在ISLES 2022数据集上，该模型达到85.4%的Dice分数，优于卷积基线。

## 摘要（原文）

> Accurate segmentation of ischemic stroke lesions from diffusion magnetic resonance imaging (MRI) is essential for clinical decision-making and outcome assessment. Diffusion-Weighted Imaging (DWI) and Apparent Diffusion Coefficient (ADC) scans provide complementary information on acute and sub-acute ischemic changes; however, automated lesion delineation remains challenging due to variability in lesion appearance.
>   In this work, we study ischemic stroke lesion segmentation using multimodal diffusion MRI from the ISLES 2022 dataset. Several state-of-the-art convolutional and transformer-based architectures, including U-Net variants, Swin-UNet, and TransUNet, are benchmarked. Based on performance, a dual-encoder TransUNet architecture is proposed to learn modality-specific representations from DWI and ADC inputs. To incorporate spatial context, adjacent slice information is integrated using a three-slice input configuration.
>   All models are trained under a unified framework and evaluated using the Dice Similarity Coefficient (DSC). Results show that transformer-based models outperform convolutional baselines, and the proposed dual-encoder TransUNet achieves the best performance, reaching a Dice score of 85.4% on the test set. The proposed framework offers a robust solution for automated ischemic stroke lesion segmentation from diffusion MRI.

