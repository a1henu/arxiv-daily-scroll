---
layout: default
title: RQ-GMM: Residual Quantized Gaussian Mixture Model for Multimodal Semantic Discretization in CTR Prediction
---

# RQ-GMM: Residual Quantized Gaussian Mixture Model for Multimodal Semantic Discretization in CTR Prediction
**arXiv**：[2602.12593v1](https://arxiv.org/abs/2602.12593) · [PDF](https://arxiv.org/pdf/2602.12593.pdf)  
**作者**：Ziye Tong, Jiahao Liu, Weimin Zhang, Hongji Ruan, Derick Tang, Zhanpeng Zeng, Qinsong Zeng, Peng Zhang, Tun Lu, Ning Gu  

**一句话要点**：提出RQ-GMM以解决多模态CTR预测中语义离散化问题，提升代码本利用率和重建精度。

**关键词**：点击率预测, 多模态嵌入, 语义离散化, 高斯混合模型, 残差量化, 在线部署

## 3 点简述
- 核心问题：多模态嵌入直接用于CTR预测效果不佳，现有离散化方法代码本利用率低、重建精度差。
- 方法要点：结合高斯混合模型与残差量化，概率建模捕捉嵌入空间统计结构，优化语义离散化。
- 实验或效果：公开数据集和在线A/B测试显示，Advertiser Value提升1.502%，已部署服务数亿用户。

## 摘要（原文）

> Multimodal content is crucial for click-through rate (CTR) prediction. However, directly incorporating continuous embeddings from pre-trained models into CTR models yields suboptimal results due to misaligned optimization objectives and convergence speed inconsistency during joint training. Discretizing embeddings into semantic IDs before feeding them into CTR models offers a more effective solution, yet existing methods suffer from limited codebook utilization, reconstruction accuracy, and semantic discriminability. We propose RQ-GMM (Residual Quantized Gaussian Mixture Model), which introduces probabilistic modeling to better capture the statistical structure of multimodal embedding spaces. Through Gaussian Mixture Models combined with residual quantization, RQ-GMM achieves superior codebook utilization and reconstruction accuracy. Experiments on public datasets and online A/B tests on a large-scale short-video platform serving hundreds of millions of users demonstrate substantial improvements: RQ-GMM yields a 1.502% gain in Advertiser Value over strong baselines. The method has been fully deployed, serving daily recommendations for hundreds of millions of users.

