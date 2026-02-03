---
layout: default
title: Synesthesia of Vehicles: Tactile Data Synthesis from Visual Inputs
---

# Synesthesia of Vehicles: Tactile Data Synthesis from Visual Inputs
**arXiv**：[2602.01832v1](https://arxiv.org/abs/2602.01832) · [PDF](https://arxiv.org/pdf/2602.01832.pdf)  
**作者**：Rui Wang, Yaoguang Cao, Yuyi Chen, Jianyi Xu, Zhuoyang Li, Jiachen Shang, Shichun Yang  

**一句话要点**：提出Synesthesia of Vehicles框架，通过视觉输入预测触觉激励以增强自动驾驶安全。

**关键词**：自动驾驶, 多模态融合, 触觉数据合成, 视觉-触觉生成, 潜在扩散模型, 跨模态对齐

## 3 点简述
- 核心问题：自动驾驶中视觉传感器无法检测道路激励，影响动态控制。
- 方法要点：开发跨模态时空对齐和基于潜在扩散的视觉-触觉生成模型。
- 实验或效果：在真实车辆数据集上验证，模型在时域、频域和分类性能上优于现有方法。

## 摘要（原文）

> Autonomous vehicles (AVs) rely on multi-modal fusion for safety, but current visual and optical sensors fail to detect road-induced excitations which are critical for vehicles' dynamic control. Inspired by human synesthesia, we propose the Synesthesia of Vehicles (SoV), a novel framework to predict tactile excitations from visual inputs for autonomous vehicles. We develop a cross-modal spatiotemporal alignment method to address temporal and spatial disparities. Furthermore, a visual-tactile synesthetic (VTSyn) generative model using latent diffusion is proposed for unsupervised high-quality tactile data synthesis. A real-vehicle perception system collected a multi-modal dataset across diverse road and lighting conditions. Extensive experiments show that VTSyn outperforms existing models in temporal, frequency, and classification performance, enhancing AV safety through proactive tactile perception.

