---
layout: default
title: The Prism Hypothesis: Harmonizing Semantic and Pixel Representations via Unified Autoencoding
---

# The Prism Hypothesis: Harmonizing Semantic and Pixel Representations via Unified Autoencoding
**arXiv**：[2512.19693v1](https://arxiv.org/abs/2512.19693) · [PDF](https://arxiv.org/pdf/2512.19693.pdf)  
**作者**：Weichen Fan, Haiwen Diao, Quan Wang, Dahua Lin, Ziwei Liu  

**一句话要点**：提出统一自编码器以融合语义与像素表示，实现多模态特征谱和谐共存。

**关键词**：多模态表示, 特征谱分析, 统一自编码, 频率调制, 语义像素融合

## 3 点简述
- 核心问题：语义与像素编码器在特征谱上存在低频抽象与高频细节的分离，缺乏统一表示。
- 方法要点：基于棱镜假设，设计频率带调制器，通过统一自编码器协调语义结构和像素细节。
- 实验或效果：在ImageNet和MS-COCO基准测试中验证，实现语义抽象与像素保真度的先进性能。

## 摘要（原文）

> Deep representations across modalities are inherently intertwined. In this paper, we systematically analyze the spectral characteristics of various semantic and pixel encoders. Interestingly, our study uncovers a highly inspiring and rarely explored correspondence between an encoder's feature spectrum and its functional role: semantic encoders primarily capture low-frequency components that encode abstract meaning, whereas pixel encoders additionally retain high-frequency information that conveys fine-grained detail. This heuristic finding offers a unifying perspective that ties encoder behavior to its underlying spectral structure. We define it as the Prism Hypothesis, where each data modality can be viewed as a projection of the natural world onto a shared feature spectrum, just like the prism. Building on this insight, we propose Unified Autoencoding (UAE), a model that harmonizes semantic structure and pixel details via an innovative frequency-band modulator, enabling their seamless coexistence. Extensive experiments on ImageNet and MS-COCO benchmarks validate that our UAE effectively unifies semantic abstraction and pixel-level fidelity into a single latent space with state-of-the-art performance.

