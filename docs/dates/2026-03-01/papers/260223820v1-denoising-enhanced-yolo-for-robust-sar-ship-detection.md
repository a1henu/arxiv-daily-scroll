---
layout: default
title: Denoising-Enhanced YOLO for Robust SAR Ship Detection
---

# Denoising-Enhanced YOLO for Robust SAR Ship Detection
**arXiv**：[2602.23820v1](https://arxiv.org/abs/2602.23820) · [PDF](https://arxiv.org/pdf/2602.23820.pdf)  
**作者**：Xiaojing Zhao, Shiyang Li, Zena Chu, Ying Zhang, Peinan Hao, Tianzi Yan, Jiajia Chen, Huicong Ning  

**一句话要点**：提出CPN-YOLO以解决SAR图像中复杂场景下船舶检测的鲁棒性问题

**关键词**：SAR船舶检测, 去噪增强, 注意力机制, YOLOv8, 归一化Wasserstein距离, 小目标检测

## 3 点简述
- 核心问题：SAR图像中杂波和斑点噪声导致误检，小目标易漏检。
- 方法要点：引入可学习大核去噪模块、PPA注意力增强特征提取、基于NWD的高斯相似度损失。
- 实验或效果：在SSDD数据集上达到97.0%精度、95.1%召回率和98.9% mAP，优于YOLOv8基线和其他方法。

## 摘要（原文）

> With the rapid advancement of deep learning, synthetic aperture radar (SAR) imagery has become a key modality for ship detection. However, robust performance remains challenging in complex scenes, where clutter and speckle noise can induce false alarms and small targets are easily missed. To address these issues, we propose CPN-YOLO, a high-precision ship detection framework built upon YOLOv8 with three targeted improvements. First, we introduce a learnable large-kernel denoising module for input pre-processing, producing cleaner representations and more discriminative features across diverse ship types. Second, we design a feature extraction enhancement strategy based on the PPA attention mechanism to strengthen multi-scale modeling and improve sensitivity to small ships. Third, we incorporate a Gaussian similarity loss derived from the normalized Wasserstein distance (NWD) to better measure similarity under complex bounding-box distributions and improve generalization. Extensive experiments on HRSID and SSDD demonstrate the effectiveness of our method. On SSDD, CPN-YOLO surpasses the YOLOv8 baseline, achieving 97.0% precision, 95.1% recall, and 98.9% mAP, and consistently outperforms other representative deep-learning detectors in overall performance.

