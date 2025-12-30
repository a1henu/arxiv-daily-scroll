---
layout: default
title: ForCM: Forest Cover Mapping from Multispectral Sentinel-2 Image by Integrating Deep Learning with Object-Based Image Analysis
---

# ForCM: Forest Cover Mapping from Multispectral Sentinel-2 Image by Integrating Deep Learning with Object-Based Image Analysis
**arXiv**：[2512.23196v1](https://arxiv.org/abs/2512.23196) · [PDF](https://arxiv.org/pdf/2512.23196.pdf)  
**作者**：Maisha Haque, Israt Jahan Ayshi, Sadaf M. Anis, Nahian Tasnim, Mithila Moontaha, Md. Sabbir Ahmed, Muhammad Iqbal Hossain, Mohammad Zavid Parvez, Subrata Chakraborty, Biswajeet Pradhan, Biswajit Banik  

**一句话要点**：提出ForCM方法，结合深度学习与对象分析，用于Sentinel-2影像的森林覆盖制图。

**关键词**：森林覆盖制图, 深度学习, 对象分析, Sentinel-2影像, 亚马逊雨林

## 3 点简述
- 核心问题：传统对象分析在森林覆盖制图中精度有限，需提升准确性。
- 方法要点：集成UNet、ResUNet等深度学习模型与对象分析，优化处理流程。
- 实验或效果：在亚马逊雨林数据上，ResUNet-OBIA和AttentionUNet-OBIA分别达到94.54%和95.64%的总体精度。

## 摘要（原文）

> This research proposes "ForCM", a novel approach to forest cover mapping that combines Object-Based Image Analysis (OBIA) with Deep Learning (DL) using multispectral Sentinel-2 imagery. The study explores several DL models, including UNet, UNet++, ResUNet, AttentionUNet, and ResNet50-Segnet, applied to high-resolution Sentinel-2 Level 2A satellite images of the Amazon Rainforest. The datasets comprise three collections: two sets of three-band imagery and one set of four-band imagery. After evaluation, the most effective DL models are individually integrated with the OBIA technique to enhance mapping accuracy. The originality of this work lies in evaluating different deep learning models combined with OBIA and comparing them with traditional OBIA methods. The results show that the proposed ForCM method improves forest cover mapping, achieving overall accuracies of 94.54 percent with ResUNet-OBIA and 95.64 percent with AttentionUNet-OBIA, compared to 92.91 percent using traditional OBIA. This research also demonstrates the potential of free and user-friendly tools such as QGIS for accurate mapping within their limitations, supporting global environmental monitoring and conservation efforts.

