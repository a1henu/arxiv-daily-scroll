---
layout: default
title: AMLRIS: Alignment-aware Masked Learning for Referring Image Segmentation
---

# AMLRIS: Alignment-aware Masked Learning for Referring Image Segmentation
**arXiv**：[2602.22740v1](https://arxiv.org/abs/2602.22740) · [PDF](https://arxiv.org/pdf/2602.22740.pdf)  
**作者**：Tongfei Chen, Shuo Yang, Yuguang Yang, Linlin Yang, Runtang Guo, Changbai Li, He Long, Chunyu Xie, Dawei Leng, Baochang Zhang  

**一句话要点**：提出对齐感知掩码学习以增强指称图像分割，通过估计像素级对齐并过滤不可靠区域。

**关键词**：指称图像分割, 视觉-语言对齐, 掩码学习, 像素级估计, 鲁棒性增强

## 3 点简述
- 指称图像分割旨在根据自然语言描述分割图像中的对象，面临视觉-语言对齐挑战。
- 引入对齐感知掩码学习，在训练中显式估计像素级对齐，过滤对齐差的区域以聚焦可信线索。
- 在RefCOCO数据集上实现最先进性能，并提升对多样化描述和场景的鲁棒性。

## 摘要（原文）

> Referring Image Segmentation (RIS) aims to segment an object in an image identified by a natural language expression. The paper introduces Alignment-Aware Masked Learning (AML), a training strategy to enhance RIS by explicitly estimating pixel-level vision-language alignment, filtering out poorly aligned regions during optimization, and focusing on trustworthy cues. This approach results in state-of-the-art performance on RefCOCO datasets and also enhances robustness to diverse descriptions and scenarios

