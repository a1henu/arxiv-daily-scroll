---
layout: default
title: Improving segmentation of retinal arteries and veins using cardiac signal in doppler holograms
---

# Improving segmentation of retinal arteries and veins using cardiac signal in doppler holograms
**arXiv**：[2511.14654v1](https://arxiv.org/abs/2511.14654) · [PDF](https://arxiv.org/pdf/2511.14654.pdf)  
**作者**：Marius Dubosc, Yann Fischer, Zacharie Auray, Nicolas Boutry, Edwin Carlinet, Michael Atlan, Thierry Geraud  

**一句话要点**：提出结合心搏信号的方法以改进多普勒全息图中视网膜动静脉分割

**关键词**：多普勒全息术, 视网膜血管分割, 时间动态分析, U-Net架构, 心搏信号处理

## 3 点简述
- 传统分割方法仅利用空间信息，忽略多普勒全息数据的时间动态。
- 通过脉冲分析提取特征，使标准U-Net能利用时间动态进行分割。
- 实验显示性能与复杂模型相当，数据集已公开供研究使用。

## 摘要（原文）

> Doppler holography is an emerging retinal imaging technique that captures the dynamic behavior of blood flow with high temporal resolution, enabling quantitative assessment of retinal hemodynamics. This requires accurate segmentation of retinal arteries and veins, but traditional segmentation methods focus solely on spatial information and overlook the temporal richness of holographic data. In this work, we propose a simple yet effective approach for artery-vein segmentation in temporal Doppler holograms using standard segmentation architectures. By incorporating features derived from a dedicated pulse analysis pipeline, our method allows conventional U-Nets to exploit temporal dynamics and achieve performance comparable to more complex attention- or iteration-based models. These findings demonstrate that time-resolved preprocessing can unlock the full potential of deep learning for Doppler holography, opening new perspectives for quantitative exploration of retinal hemodynamics. The dataset is publicly available at https://huggingface.co/datasets/DigitalHolography/

