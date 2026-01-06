---
layout: default
title: Prithvi-Complimentary Adaptive Fusion Encoder (CAFE): unlocking full-potential for flood inundation mapping
---

# Prithvi-Complimentary Adaptive Fusion Encoder (CAFE): unlocking full-potential for flood inundation mapping
**arXiv**：[2601.02315v1](https://arxiv.org/abs/2601.02315) · [PDF](https://arxiv.org/pdf/2601.02315.pdf)  
**作者**：Saurabh Kaushik, Lalit Maurya, Beth Tellman  

**一句话要点**：提出Prithvi-CAFE以解决洪水淹没制图中地理基础模型捕获局部细节不足的问题

**关键词**：洪水淹没制图, 地理基础模型, 自适应融合编码器, 语义分割, 多模态数据融合, 卷积注意力模块

## 3 点简述
- 地理基础模型在洪水制图任务中难以超越基线U-Net，因缺乏局部细节捕捉能力
- Prithvi-CAFE集成预训练编码器与CNN残差分支，通过适配器快速微调并融合多尺度特征
- 在Sen1Flood11和FloodPlanet数据集上实现最优性能，显著提升IoU指标

## 摘要（原文）

> Geo-Foundation Models (GFMs), have proven effective in diverse downstream applications, including semantic segmentation, classification, and regression tasks. However, in case of flood mapping using Sen1Flood11 dataset as a downstream task, GFMs struggles to outperform the baseline U-Net, highlighting model's limitation in capturing critical local nuances. To address this, we present the Prithvi-Complementary Adaptive Fusion Encoder (CAFE), which integrate Prithvi GFM pretrained encoder with a parallel CNN residual branch enhanced by Convolutional Attention Modules (CAM). Prithvi-CAFE enables fast and efficient fine-tuning through adapters in Prithvi and performs multi-scale, multi-level fusion with CNN features, capturing critical local details while preserving long-range dependencies. We achieve state-of-the-art results on two comprehensive flood mapping datasets: Sen1Flood11 and FloodPlanet. On Sen1Flood11 test data, Prithvi-CAFE (IoU 83.41) outperforms the original Prithvi (IoU 82.50) and other major GFMs (TerraMind 82.90, DOFA 81.54, spectralGPT: 81.02). The improvement is even more pronounced on the hold-out test site, where Prithvi-CAFE achieves an IoU of 81.37 compared to the baseline U-Net (70.57) and original Prithvi (72.42). On FloodPlanet, Prithvi-CAFE also surpasses the baseline U-Net and other GFMs, achieving an IoU of 64.70 compared to U-Net (60.14), Terramind (62.33), DOFA (59.15) and Prithvi 2.0 (61.91). Our proposed simple yet effective Prithvi-CAFE demonstrates strong potential for improving segmentation tasks where multi-channel and multi-modal data provide complementary information and local details are critical. The code is released on \href{https://github.com/Sk-2103/Prithvi-CAFE}{Prithvi-CAFE Github}

