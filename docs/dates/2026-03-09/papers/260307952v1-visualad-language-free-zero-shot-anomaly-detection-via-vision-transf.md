---
layout: default
title: VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer
---

# VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer
**arXiv**：[2603.07952v1](https://arxiv.org/abs/2603.07952) · [PDF](https://arxiv.org/pdf/2603.07952.pdf)  
**作者**：Yanning Hou, Peiyuan Li, Zirui Liu, Yitong Wang, Yanran Ruan, Jianfeng Qiu, Ke Xu  

**一句话要点**：提出VisualAD，一种基于视觉Transformer的无语言零样本异常检测方法

**关键词**：零样本异常检测, 视觉Transformer, 无语言框架, 可学习令牌, 自注意力机制, 跨域适应

## 3 点简述
- 核心问题：零样本异常检测依赖文本编码器，导致训练不稳定和参数冗余
- 方法要点：在冻结骨干中引入可学习令牌，通过自注意力直接编码正常与异常概念
- 实验或效果：在13个工业与医学基准上达到最先进性能，适配多种预训练视觉骨干

## 摘要（原文）

> Zero-shot anomaly detection (ZSAD) requires detecting and localizing anomalies without access to target-class anomaly samples. Mainstream methods rely on vision-language models (VLMs) such as CLIP: they build hand-crafted or learned prompt sets for normal and abnormal semantics, then compute image-text similarities for open-set discrimination. While effective, this paradigm depends on a text encoder and cross-modal alignment, which can lead to training instability and parameter redundancy. This work revisits the necessity of the text branch in ZSAD and presents VisualAD, a purely visual framework built on Vision Transformers. We introduce two learnable tokens within a frozen backbone to directly encode normality and abnormality. Through multi-layer self-attention, these tokens interact with patch tokens, gradually acquiring high-level notions of normality and anomaly while guiding patches to highlight anomaly-related cues. Additionally, we incorporate a Spatial-Aware Cross-Attention (SCA) module and a lightweight Self-Alignment Function (SAF): SCA injects fine-grained spatial information into the tokens, and SAF recalibrates patch features before anomaly scoring. VisualAD achieves state-of-the-art performance on 13 zero-shot anomaly detection benchmarks spanning industrial and medical domains, and adapts seamlessly to pretrained vision backbones such as the CLIP image encoder and DINOv2. Code: https://github.com/7HHHHH/VisualAD

