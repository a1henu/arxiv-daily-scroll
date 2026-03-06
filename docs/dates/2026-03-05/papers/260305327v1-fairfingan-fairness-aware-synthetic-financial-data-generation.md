---
layout: default
title: FairFinGAN: Fairness-aware Synthetic Financial Data Generation
---

# FairFinGAN: Fairness-aware Synthetic Financial Data Generation
**arXiv**：[2603.05327v1](https://arxiv.org/abs/2603.05327) · [PDF](https://arxiv.org/pdf/2603.05327.pdf)  
**作者**：Tai Le Quy, Dung Nguyen Tuan, Trung Nguyen Thanh, Duy Tran Cong, Huyen Giang Thi Thu, Frank Hopfgartner  

**一句话要点**：提出FairFinGAN以解决金融数据生成中的偏见问题

**关键词**：公平性数据生成, WGAN框架, 金融数据合成, 偏见缓解, 下游任务效用

## 3 点简述
- 金融数据常含偏见，导致自动化决策不公
- 基于WGAN框架，通过分类器引入公平约束生成合成数据
- 在五个真实数据集上验证，公平性提升且数据效用保持

## 摘要（原文）

> Financial datasets often suffer from bias that can lead to unfair decision-making in automated systems. In this work, we propose FairFinGAN, a WGAN-based framework designed to generate synthetic financial data while mitigating bias with respect to the protected attribute. Our approach incorporates fairness constraints directly into the training process through a classifier, ensuring that the synthetic data is both fair and preserves utility for downstream predictive tasks. We evaluate our proposed model on five real-world financial datasets and compare it with existing GAN-based data generation methods. Experimental results show that our approach achieves superior fairness metrics without significant loss in data utility, demonstrating its potential as a tool for bias-aware data generation in financial applications.

