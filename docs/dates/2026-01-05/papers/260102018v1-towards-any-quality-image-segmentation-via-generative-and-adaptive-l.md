---
layout: default
title: Towards Any-Quality Image Segmentation via Generative and Adaptive Latent Space Enhancement
---

# Towards Any-Quality Image Segmentation via Generative and Adaptive Latent Space Enhancement
**arXiv**：[2601.02018v1](https://arxiv.org/abs/2601.02018) · [PDF](https://arxiv.org/pdf/2601.02018.pdf)  
**作者**：Guangqian Guo, Aixi Ren, Yong Guo, Xuehui Yu, Jiacheng Tian, Wenli Li, Yaoxing Wang, Shan Gao  

**一句话要点**：提出GleSAM++以增强任意质量图像分割的鲁棒性

**关键词**：图像分割, 鲁棒性增强, 潜在空间增强, 退化感知, 零样本学习, 自适应机制

## 3 点简述
- 核心问题：SAM在低质量图像上性能显著下降，限制实际应用。
- 方法要点：结合生成式潜在空间增强、特征分布对齐、通道复制扩展和退化感知自适应增强机制。
- 实验或效果：显著提升复杂退化下的分割鲁棒性，保持对清晰图像的泛化能力，并在未见退化上表现良好。

## 摘要（原文）

> Segment Anything Models (SAMs), known for their exceptional zero-shot segmentation performance, have garnered significant attention in the research community. Nevertheless, their performance drops significantly on severely degraded, low-quality images, limiting their effectiveness in real-world scenarios. To address this, we propose GleSAM++, which utilizes Generative Latent space Enhancement to boost robustness on low-quality images, thus enabling generalization across various image qualities. Additionally, to improve compatibility between the pre-trained diffusion model and the segmentation framework, we introduce two techniques, i.e., Feature Distribution Alignment (FDA) and Channel Replication and Expansion (CRE). However, the above components lack explicit guidance regarding the degree of degradation. The model is forced to implicitly fit a complex noise distribution that spans conditions from mild noise to severe artifacts, which substantially increases the learning burden and leads to suboptimal reconstructions. To address this issue, we further introduce a Degradation-aware Adaptive Enhancement (DAE) mechanism. The key principle of DAE is to decouple the reconstruction process for arbitrary-quality features into two stages: degradation-level prediction and degradation-aware reconstruction. Our method can be applied to pre-trained SAM and SAM2 with only minimal additional learnable parameters, allowing for efficient optimization. Extensive experiments demonstrate that GleSAM++ significantly improves segmentation robustness on complex degradations while maintaining generalization to clear images. Furthermore, GleSAM++ also performs well on unseen degradations, underscoring the versatility of our approach and dataset.

