---
layout: default
title: LCMem: A Universal Model for Robust Image Memorization Detection
---

# LCMem: A Universal Model for Robust Image Memorization Detection
**arXiv**：[2512.14421v1](https://arxiv.org/abs/2512.14421) · [PDF](https://arxiv.org/pdf/2512.14421.pdf)  
**作者**：Mischa Dombrowski, Felix Nützel, Bernhard Kainz  

**一句话要点**：提出LCMem模型，通过统一再识别与复制检测解决跨域图像记忆检测问题。

**关键词**：图像记忆检测, 隐私审计, 再识别, 复制检测, 跨域模型, 对比学习

## 3 点简述
- 核心问题：生成图像模型隐私共享中缺乏可靠记忆检测机制，现有方法泛化性差。
- 方法要点：采用两阶段训练策略，先学习身份一致性，再结合增强鲁棒的复制检测。
- 实验或效果：在六个基准数据集上，再识别提升达16个百分点，复制检测提升达30个百分点。

## 摘要（原文）

> Recent advances in generative image modeling have achieved visual realism sufficient to deceive human experts, yet their potential for privacy preserving data sharing remains insufficiently understood. A central obstacle is the absence of reliable memorization detection mechanisms, limited quantitative evaluation, and poor generalization of existing privacy auditing methods across domains. To address this, we propose to view memorization detection as a unified problem at the intersection of re-identification and copy detection, whose complementary goals cover both identity consistency and augmentation-robust duplication, and introduce Latent Contrastive Memorization Network (LCMem), a cross-domain model evaluated jointly on both tasks. LCMem achieves this through a two-stage training strategy that first learns identity consistency before incorporating augmentation-robust copy detection. Across six benchmark datasets, LCMem achieves improvements of up to 16 percentage points on re-identification and 30 percentage points on copy detection, enabling substantially more reliable memorization detection at scale. Our results show that existing privacy filters provide limited performance and robustness, highlighting the need for stronger protection mechanisms. We show that LCMem sets a new standard for cross-domain privacy auditing, offering reliable and scalable memorization detection. Code and model is publicly available at https://github.com/MischaD/LCMem.

