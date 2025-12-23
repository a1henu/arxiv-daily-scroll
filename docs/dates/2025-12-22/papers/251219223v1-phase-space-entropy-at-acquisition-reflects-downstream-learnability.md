---
layout: default
title: Phase-space entropy at acquisition reflects downstream learnability
---

# Phase-space entropy at acquisition reflects downstream learnability
**arXiv**：[2512.19223v1](https://arxiv.org/abs/2512.19223) · [PDF](https://arxiv.org/pdf/2512.19223.pdf)  
**作者**：Xiu-Cheng Wang, Jun-Jie Zhanga, Nan Cheng, Long-Gang Pang, Taijiao Du, Deyu Meng  

**一句话要点**：提出相空间熵ΔS_B以量化采集过程对下游学习信息的影响

**关键词**：相空间熵, 信息量化, 采样理论, 跨模态学习, 无训练评估, 采集优化

## 3 点简述
- 核心问题：如何跨模态量化采集过程对下游学习可用信息的保留或破坏
- 方法要点：基于仪器分辨相空间定义标量ΔS_B，直接评估空间-频率结构混合或移除
- 实验或效果：在图像分类、加速MRI和大规模MIMO中，ΔS_B能无训练预测下游性能并优化采样策略

## 摘要（原文）

> Modern learning systems work with data that vary widely across domains, but they all ultimately depend on how much structure is already present in the measurements before any model is trained. This raises a basic question: is there a general, modality-agnostic way to quantify how acquisition itself preserves or destroys the information that downstream learners could use? Here we propose an acquisition-level scalar $ΔS_{\mathcal B}$ based on instrument-resolved phase space. Unlike pixelwise distortion or purely spectral errors that often saturate under aggressive undersampling, $ΔS_{\mathcal B}$ directly quantifies how acquisition mixes or removes joint space--frequency structure at the instrument scale. We show theoretically that \(ΔS_{\mathcal B}\) correctly identifies the phase-space coherence of periodic sampling as the physical source of aliasing, recovering classical sampling-theorem consequences. Empirically, across masked image classification, accelerated MRI, and massive MIMO (including over-the-air measurements), $\|ΔS_{\mathcal B}\|$ consistently ranks sampling geometries and predicts downstream reconstruction/recognition difficulty \emph{without training}. In particular, minimizing $\|ΔS_{\mathcal B}\|$ enables zero-training selection of variable-density MRI mask parameters that matches designs tuned by conventional pre-reconstruction criteria. These results suggest that phase-space entropy at acquisition reflects downstream learnability, enabling pre-training selection of candidate sampling policies and as a shared notion of information preservation across modalities.

