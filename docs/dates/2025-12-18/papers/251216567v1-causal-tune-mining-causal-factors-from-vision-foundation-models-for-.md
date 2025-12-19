---
layout: default
title: Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation
---

# Causal-Tune: Mining Causal Factors from Vision Foundation Models for Domain Generalized Semantic Segmentation
**arXiv**：[2512.16567v1](https://arxiv.org/abs/2512.16567) · [PDF](https://arxiv.org/pdf/2512.16567.pdf)  
**作者**：Yin Zhang, Yongqiang Zhang, Yaoyue Zheng, Bogdan Raducanu, Dan Liu  

**一句话要点**：提出Causal-Tune方法，通过因果因子挖掘提升视觉基础模型在域泛化语义分割中的性能

**关键词**：域泛化语义分割, 视觉基础模型, 因果因子挖掘, 频率域分析, 轻量微调

## 3 点简述
- 核心问题：视觉基础模型中的非因果因子（如频谱高低频伪影）阻碍域泛化语义分割性能
- 方法要点：使用DCT和带通滤波器分离因果与非因果因子，引入可学习令牌优化因果因子
- 实验或效果：在跨域任务中表现优异，雪天条件下mIoU提升4.8%

## 摘要（原文）

> Fine-tuning Vision Foundation Models (VFMs) with a small number of parameters has shown remarkable performance in Domain Generalized Semantic Segmentation (DGSS). Most existing works either train lightweight adapters or refine intermediate features to achieve better generalization on unseen domains. However, they both overlook the fact that long-term pre-trained VFMs often exhibit artifacts, which hinder the utilization of valuable representations and ultimately degrade DGSS performance. Inspired by causal mechanisms, we observe that these artifacts are associated with non-causal factors, which usually reside in the low- and high-frequency components of the VFM spectrum. In this paper, we explicitly examine the causal and non-causal factors of features within VFMs for DGSS, and propose a simple yet effective method to identify and disentangle them, enabling more robust domain generalization. Specifically, we propose Causal-Tune, a novel fine-tuning strategy designed to extract causal factors and suppress non-causal ones from the features of VFMs. First, we extract the frequency spectrum of features from each layer using the Discrete Cosine Transform (DCT). A Gaussian band-pass filter is then applied to separate the spectrum into causal and non-causal components. To further refine the causal components, we introduce a set of causal-aware learnable tokens that operate in the frequency domain, while the non-causal components are discarded. Finally, refined features are transformed back into the spatial domain via inverse DCT and passed to the next layer. Extensive experiments conducted on various cross-domain tasks demonstrate the effectiveness of Causal-Tune. In particular, our method achieves superior performance under adverse weather conditions, improving +4.8% mIoU over the baseline in snow conditions.

