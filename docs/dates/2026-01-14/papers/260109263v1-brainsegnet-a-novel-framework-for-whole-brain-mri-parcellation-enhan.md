---
layout: default
title: BrainSegNet: A Novel Framework for Whole-Brain MRI Parcellation Enhanced by Large Models
---

# BrainSegNet: A Novel Framework for Whole-Brain MRI Parcellation Enhanced by Large Models
**arXiv**：[2601.09263v1](https://arxiv.org/abs/2601.09263) · [PDF](https://arxiv.org/pdf/2601.09263.pdf)  
**作者**：Yucheng Li, Xiaofan Wang, Junyi Wang, Yijie Li, Xi Zhu, Mubai Du, Dian Sheng, Wei Zhang, Fan Zhang  

**一句话要点**：提出BrainSegNet框架，通过增强SAM实现高精度全脑MRI分割为95个区域。

**关键词**：全脑分割, MRI分割, SAM增强, 多尺度注意力, 边界细化, 深度学习

## 3 点简述
- 核心问题：全脑MRI分割因区域小且形状不规则而具挑战性，传统方法精度不足。
- 方法要点：结合U-Net跳跃连接与SAM编码器-解码器，引入多尺度注意力和边界细化模块。
- 实验或效果：在HCP数据集上优于现有方法，提升复杂多标签分割的准确性和鲁棒性。

## 摘要（原文）

> Whole-brain parcellation from MRI is a critical yet challenging task due to the complexity of subdividing the brain into numerous small, irregular shaped regions. Traditionally, template-registration methods were used, but recent advances have shifted to deep learning for faster workflows. While large models like the Segment Anything Model (SAM) offer transferable feature representations, they are not tailored for the high precision required in brain parcellation. To address this, we propose BrainSegNet, a novel framework that adapts SAM for accurate whole-brain parcellation into 95 regions. We enhance SAM by integrating U-Net skip connections and specialized modules into its encoder and decoder, enabling fine-grained anatomical precision. Key components include a hybrid encoder combining U-Net skip connections with SAM's transformer blocks, a multi-scale attention decoder with pyramid pooling for varying-sized structures, and a boundary refinement module to sharpen edges. Experimental results on the Human Connectome Project (HCP) dataset demonstrate that BrainSegNet outperforms several state-of-the-art methods, achieving higher accuracy and robustness in complex, multi-label parcellation.

