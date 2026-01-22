---
layout: default
title: Multimodal Rumor Detection Enhanced by External Evidence and Forgery Features
---

# Multimodal Rumor Detection Enhanced by External Evidence and Forgery Features
**arXiv**：[2601.14954v1](https://arxiv.org/abs/2601.14954) · [PDF](https://arxiv.org/pdf/2601.14954.pdf)  
**作者**：Han Li, Hua Sun  

**一句话要点**：提出融合外部证据与伪造特征的多模态谣言检测模型，以解决社交媒体图文谣言检测难题。

**关键词**：多模态谣言检测, 外部证据融合, 伪造特征提取, 对比学习, 自适应特征融合, 社交媒体分析

## 3 点简述
- 核心问题：社交媒体图文谣言检测面临深层语义不一致、伪造内容及缺乏外部证据验证的挑战。
- 方法要点：结合ResNet34和BERT编码器，通过傅里叶变换提取伪造特征，并引入BLIP生成图像描述以增强语义对齐。
- 实验或效果：在微博和Twitter数据集上，模型在宏观准确率、召回率和F1分数上优于主流基线方法。

## 摘要（原文）

> Social media increasingly disseminates information through mixed image text posts, but rumors often exploit subtle inconsistencies and forged content, making detection based solely on post content difficult. Deep semantic mismatch rumors, which superficially align images and texts, pose particular challenges and threaten online public opinion. Existing multimodal rumor detection methods improve cross modal modeling but suffer from limited feature extraction, noisy alignment, and inflexible fusion strategies, while ignoring external factual evidence necessary for verifying complex rumors. To address these limitations, we propose a multimodal rumor detection model enhanced with external evidence and forgery features. The model uses a ResNet34 visual encoder, a BERT text encoder, and a forgery feature module extracting frequency-domain traces and compression artifacts via Fourier transformation. BLIP-generated image descriptions bridge image and text semantic spaces. A dual contrastive learning module computes contrastive losses between text image and text description pairs, improving detection of semantic inconsistencies. A gated adaptive feature-scaling fusion mechanism dynamically adjusts multimodal fusion and reduces redundancy. Experiments on Weibo and Twitter datasets demonstrate that our model outperforms mainstream baselines in macro accuracy, recall, and F1 score.

