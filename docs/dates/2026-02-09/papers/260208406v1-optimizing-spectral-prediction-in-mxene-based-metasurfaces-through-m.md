---
layout: default
title: Optimizing Spectral Prediction in MXene-Based Metasurfaces Through Multi-Channel Spectral Refinement and Savitzky-Golay Smoothing
---

# Optimizing Spectral Prediction in MXene-Based Metasurfaces Through Multi-Channel Spectral Refinement and Savitzky-Golay Smoothing
**arXiv**：[2602.08406v1](https://arxiv.org/abs/2602.08406) · [PDF](https://arxiv.org/pdf/2602.08406.pdf)  
**作者**：Shujaat Khan, Waleed Iqbal Waseer  

**一句话要点**：提出基于迁移学习、多通道谱细化和Savitzky-Golay平滑的深度学习框架，以高效预测MXene基超表面电磁谱。

**关键词**：MXene基超表面, 电磁谱预测, 迁移学习, 多通道谱细化, Savitzky-Golay平滑, 深度学习框架

## 3 点简述
- 核心问题：MXene基太阳能吸收器的电磁谱预测计算量大，传统全波求解器效率低。
- 方法要点：利用预训练MobileNetV2微调，结合多通道谱细化和Savitzky-Golay平滑增强特征提取和降噪。
- 实验或效果：模型在RMSE、R²和PSNR指标上优于基线CNN，提供可扩展的高效预测方案。

## 摘要（原文）

> The prediction of electromagnetic spectra for MXene-based solar absorbers is a computationally intensive task, traditionally addressed using full-wave solvers. This study introduces an efficient deep learning framework incorporating transfer learning, multi-channel spectral refinement (MCSR), and Savitzky-Golay smoothing to accelerate and enhance spectral prediction accuracy. The proposed architecture leverages a pretrained MobileNetV2 model, fine-tuned to predict 102-point absorption spectra from $64\times64$ metasurface designs. Additionally, the MCSR module processes the feature map through multi-channel convolutions, enhancing feature extraction, while Savitzky-Golay smoothing mitigates high-frequency noise. Experimental evaluations demonstrate that the proposed model significantly outperforms baseline Convolutional Neural Network (CNN) and deformable CNN models, achieving an average root mean squared error (RMSE) of 0.0245, coefficient of determination \( R^2 \) of 0.9578, and peak signal-to-noise ratio (PSNR) of 32.98 dB. The proposed framework presents a scalable and computationally efficient alternative to conventional solvers, positioning it as a viable candidate for rapid spectral prediction in nanophotonic design workflows.

