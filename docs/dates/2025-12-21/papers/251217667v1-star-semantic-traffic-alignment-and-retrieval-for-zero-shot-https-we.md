---
layout: default
title: STAR: Semantic-Traffic Alignment and Retrieval for Zero-Shot HTTPS Website Fingerprinting
---

# STAR: Semantic-Traffic Alignment and Retrieval for Zero-Shot HTTPS Website Fingerprinting
**arXiv**：[2512.17667v1](https://arxiv.org/abs/2512.17667) · [PDF](https://arxiv.org/pdf/2512.17667.pdf)  
**作者**：Yifei Cheng, Yujia Zhu, Baiyang Li, Xinhao Deng, Yitong Cai, Yaochen Ren, Qingyun Liu  

**一句话要点**：提出STAR方法，通过零样本跨模态检索解决加密HTTPS流量中的网站指纹识别问题。

**关键词**：网站指纹识别, 零样本学习, 跨模态检索, 加密流量分析, 语义对齐, HTTPS隐私

## 3 点简述
- 核心问题：现代HTTPS机制如ECH和加密DNS仍易受网站指纹攻击，现有方法依赖监督学习，难以处理未见网站。
- 方法要点：将网站指纹识别重构为零样本跨模态检索，使用双编码器架构学习流量轨迹与逻辑配置文件的联合嵌入空间。
- 实验或效果：在1,600个未见网站上，STAR达到87.9% top-1准确率和0.963 AUC，优于监督和少样本基线。

## 摘要（原文）

> Modern HTTPS mechanisms such as Encrypted Client Hello (ECH) and encrypted DNS improve privacy but remain vulnerable to website fingerprinting (WF) attacks, where adversaries infer visited sites from encrypted traffic patterns. Existing WF methods rely on supervised learning with site-specific labeled traces, which limits scalability and fails to handle previously unseen websites. We address these limitations by reformulating WF as a zero-shot cross-modal retrieval problem and introducing STAR. STAR learns a joint embedding space for encrypted traffic traces and crawl-time logic profiles using a dual-encoder architecture. Trained on 150K automatically collected traffic-logic pairs with contrastive and consistency objectives and structure-aware augmentation, STAR retrieves the most semantically aligned profile for a trace without requiring target-side traffic during training. Experiments on 1,600 unseen websites show that STAR achieves 87.9 percent top-1 accuracy and 0.963 AUC in open-world detection, outperforming supervised and few-shot baselines. Adding an adapter with only four labeled traces per site further boosts top-5 accuracy to 98.8 percent. Our analysis reveals intrinsic semantic-traffic alignment in modern web protocols, identifying semantic leakage as the dominant privacy risk in encrypted HTTPS traffic. We release STAR's datasets and code to support reproducibility and future research.

