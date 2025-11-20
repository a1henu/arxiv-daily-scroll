---
layout: default
title: D4C: Data-free Quantization for Contrastive Language-Image Pre-training Models
---

# D4C: Data-free Quantization for Contrastive Language-Image Pre-training Models
**arXiv**：[2511.15411v1](https://arxiv.org/abs/2511.15411) · [PDF](https://arxiv.org/pdf/2511.15411.pdf)  
**作者**：Wenlun Zhang, Yunshan Zhong, Zihao Ding, Xinyu Li, Kentaro Yoshioka  

**一句话要点**：提出D4C框架以解决CLIP模型数据无关量化中的语义不足和多样性低问题

**关键词**：数据无关量化, 对比语言图像预训练, 模型压缩, 伪图像合成, 零-shot分类, 隐私保护

## 3 点简述
- 核心问题：现有数据无关量化方法直接应用于CLIP模型时，因合成样本语义内容不足和图像内多样性低导致性能显著下降
- 方法要点：通过提示引导语义注入、结构对比生成和扰动感知增强合成语义丰富且结构多样的伪图像
- 实验或效果：在多种比特宽度和模型上验证，例如W4A8设置下，CIFAR-10零-shot分类Top-1准确率提升达12.4%和18.9%

## 摘要（原文）

> Data-Free Quantization (DFQ) offers a practical solution for model compression without requiring access to real data, making it particularly attractive in privacy-sensitive scenarios. While DFQ has shown promise for unimodal models, its extension to Vision-Language Models such as Contrastive Language-Image Pre-training (CLIP) models remains underexplored. In this work, we reveal that directly applying existing DFQ techniques to CLIP results in substantial performance degradation due to two key limitations: insufficient semantic content and low intra-image diversity in synthesized samples. To tackle these challenges, we propose D4C, the first DFQ framework tailored for CLIP. D4C synthesizes semantically rich and structurally diverse pseudo images through three key components: (1) Prompt-Guided Semantic Injection aligns generated images with real-world semantics using text prompts; (2) Structural Contrastive Generation reproduces compositional structures of natural images by leveraging foreground-background contrastive synthesis; and (3) Perturbation-Aware Enhancement applies controlled perturbations to improve sample diversity and robustness. These components jointly empower D4C to synthesize images that are both semantically informative and structurally diverse, effectively bridging the performance gap of DFQ on CLIP. Extensive experiments validate the effectiveness of D4C, showing significant performance improvements on various bit-widths and models. For example, under the W4A8 setting with CLIP ResNet-50 and ViT-B/32, D4C achieves Top-1 accuracy improvement of 12.4% and 18.9% on CIFAR-10, 6.8% and 19.7% on CIFAR-100, and 1.4% and 5.7% on ImageNet-1K in zero-shot classification, respectively.

