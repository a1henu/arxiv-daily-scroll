---
layout: default
title: Mining Forgery Traces from Reconstruction Error: A Weakly Supervised Framework for Multimodal Deepfake Temporal Localization
---

# Mining Forgery Traces from Reconstruction Error: A Weakly Supervised Framework for Multimodal Deepfake Temporal Localization
**arXiv**：[2601.21458v1](https://arxiv.org/abs/2601.21458) · [PDF](https://arxiv.org/pdf/2601.21458.pdf)  
**作者**：Midou Guo, Qilin Yin, Wei Lu, Xiangyang Luo, Rui Yang  

**一句话要点**：提出RT-DeepLoc框架，通过重建误差实现弱监督多模态深度伪造视频时序定位

**关键词**：弱监督学习, 时序定位, 深度伪造检测, 重建误差, 多模态视频分析

## 3 点简述
- 核心问题：深度伪造视频呈现局部间歇性篡改，需细粒度时序定位，但帧级标注成本高。
- 方法要点：使用仅基于真实数据训练的MAE学习时空模式，通过重建误差识别伪造段；引入AICL损失增强局部判别性。
- 实验或效果：在LAV-DF等大规模数据集上验证，RT-DeepLoc在弱监督时序伪造定位中达到先进性能。

## 摘要（原文）

> Modern deepfakes have evolved into localized and intermittent manipulations that require fine-grained temporal localization. The prohibitive cost of frame-level annotation makes weakly supervised methods a practical necessity, which rely only on video-level labels. To this end, we propose Reconstruction-based Temporal Deepfake Localization (RT-DeepLoc), a weakly supervised temporal forgery localization framework that identifies forgeries via reconstruction errors. Our framework uses a Masked Autoencoder (MAE) trained exclusively on authentic data to learn its intrinsic spatiotemporal patterns; this allows the model to produce significant reconstruction discrepancies for forged segments, effectively providing the missing fine-grained cues for localization. To robustly leverage these indicators, we introduce a novel Asymmetric Intra-video Contrastive Loss (AICL). By focusing on the compactness of authentic features guided by these reconstruction cues, AICL establishes a stable decision boundary that enhances local discrimination while preserving generalization to unseen forgeries. Extensive experiments on large-scale datasets, including LAV-DF, demonstrate that RT-DeepLoc achieves state-of-the-art performance in weakly-supervised temporal forgery localization.

