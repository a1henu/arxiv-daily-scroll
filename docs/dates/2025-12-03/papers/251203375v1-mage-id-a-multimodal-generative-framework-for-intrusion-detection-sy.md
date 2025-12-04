---
layout: default
title: MAGE-ID: A Multimodal Generative Framework for Intrusion Detection Systems
---

# MAGE-ID: A Multimodal Generative Framework for Intrusion Detection Systems
**arXiv**：[2512.03375v1](https://arxiv.org/abs/2512.03375) · [PDF](https://arxiv.org/pdf/2512.03375.pdf)  
**作者**：Mahdi Arab Loodaricheh, Mohammad Hossein Manshaei, Anita Raja  

**一句话要点**：提出MAGE-ID多模态生成框架，通过扩散模型增强入侵检测系统的数据平衡与性能。

**关键词**：入侵检测系统, 多模态生成, 扩散模型, 数据增强, Transformer, CNN

## 3 点简述
- 核心问题：入侵检测系统面临网络流量异构、威胁演变和数据不平衡的挑战。
- 方法要点：基于扩散模型，联合训练Transformer和CNN编码器，实现表格特征与图像的多模态生成。
- 实验或效果：在CIC-IDS-2017和NSL-KDD数据集上，优于TabSyn和TabDDPM，提升保真度、多样性和检测性能。

## 摘要（原文）

> Modern Intrusion Detection Systems (IDS) face severe challenges due to heterogeneous network traffic, evolving cyber threats, and pronounced data imbalance between benign and attack flows. While generative models have shown promise in data augmentation, existing approaches are limited to single modalities and fail to capture cross-domain dependencies. This paper introduces MAGE-ID (Multimodal Attack Generator for Intrusion Detection), a diffusion-based generative framework that couples tabular flow features with their transformed images through a unified latent prior. By jointly training Transformer and CNN-based variational encoders with an EDM style denoiser, MAGE-ID achieves balanced and coherent multimodal synthesis. Evaluations on CIC-IDS-2017 and NSL-KDD demonstrate significant improvements in fidelity, diversity, and downstream detection performance over TabSyn and TabDDPM, highlighting the effectiveness of MAGE-ID for multimodal IDS augmentation.

