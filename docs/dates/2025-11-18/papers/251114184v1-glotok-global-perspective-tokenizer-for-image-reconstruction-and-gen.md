---
layout: default
title: GloTok: Global Perspective Tokenizer for Image Reconstruction and Generation
---

# GloTok: Global Perspective Tokenizer for Image Reconstruction and Generation
**arXiv**：[2511.14184v1](https://arxiv.org/abs/2511.14184) · [PDF](https://arxiv.org/pdf/2511.14184.pdf)  
**作者**：Xuan Zhao, Zhongyu Zhang, Yuge Huang, Yuxi Mi, Guodong Mu, Shouhong Ding, Jun Wang, Rizen Guo, Shuigeng Zhou  

**一句话要点**：提出GloTok全局视角分词器，利用全局关系信息改善图像重建与生成质量。

**关键词**：图像分词, 语义分布均匀化, 代码本学习, 残差学习, 图像生成, 自回归模型

## 3 点简述
- 现有图像分词方法依赖局部语义监督，导致语义分布不均匀，限制生成性能。
- GloTok采用代码本直方图关系学习和残差模块，建模均匀语义分布并恢复细节。
- 在ImageNet-1k基准测试中，实现最优重建和生成质量，无需预训练模型直接访问。

## 摘要（原文）

> Existing state-of-the-art image tokenization methods leverage diverse semantic features from pre-trained vision models for additional supervision, to expand the distribution of latent representations and thereby improve the quality of image reconstruction and generation. These methods employ a locally supervised approach for semantic supervision, which limits the uniformity of semantic distribution. However, VA-VAE proves that a more uniform feature distribution yields better generation performance. In this work, we introduce a Global Perspective Tokenizer (GloTok), which utilizes global relational information to model a more uniform semantic distribution of tokenized features. Specifically, a codebook-wise histogram relation learning method is proposed to transfer the semantics, which are modeled by pre-trained models on the entire dataset, to the semantic codebook. Then, we design a residual learning module that recovers the fine-grained details to minimize the reconstruction error caused by quantization. Through the above design, GloTok delivers more uniformly distributed semantic latent representations, which facilitates the training of autoregressive (AR) models for generating high-quality images without requiring direct access to pre-trained models during the training process. Experiments on the standard ImageNet-1k benchmark clearly show that our proposed method achieves state-of-the-art reconstruction performance and generation quality.

