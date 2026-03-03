---
layout: default
title: Uncertainty Quantification of Click and Conversion Estimates for the Autobidding
---

# Uncertainty Quantification of Click and Conversion Estimates for the Autobidding
**arXiv**：[2603.01825v1](https://arxiv.org/abs/2603.01825) · [PDF](https://arxiv.org/pdf/2603.01825.pdf)  
**作者**：Ivan Zhigalskii, Andrey Pudovikov, Aleksandr Katrutsa, Egor Samosvat  

**一句话要点**：提出DenoiseBid方法，通过贝叶斯去噪提升自动出价中点击率和转化率估计的准确性。

**关键词**：自动出价, 不确定性量化, 贝叶斯方法, 点击率估计, 转化率估计, 电子商务拍卖

## 3 点简述
- 核心问题：自动出价算法依赖预训练模型的点击率和转化率估计，但预测不确定性影响性能。
- 方法要点：采用贝叶斯方法，用恢复分布替换噪声估计，优化出价效率。
- 实验或效果：在合成、iPinYou和BAT数据集上验证，评估对噪声尺度的鲁棒性。

## 摘要（原文）

> Modern e-commerce platforms employ various auction mechanisms to allocate paid slots for a given item. To scale this approach to the millions of auctions, the platforms suggest promotion tools based on the autobidding algorithms. These algorithms typically depend on the Click-Through-Rate (CTR) and Conversion-Rate (CVR) estimates provided by a pre-trained machine learning model. However, the predictions of such models are uncertain and can significantly affect the performance of the autobidding algorithm. To address this issue, we propose the DenoiseBid method, which corrects the generated CTRs and CVRs to make the resulting bids more efficient in auctions. The underlying idea of our method is to employ a Bayesian approach and replace noisy CTR or CVR estimates with those from recovered distributions. To demonstrate the performance of the proposed approach, we perform extensive experiments on the synthetic, iPinYou, and BAT datasets. To evaluate the robustness of our approach to the noise scale, we use synthetic noise and noise estimated from the predictions of the pre-trained machine learning model.

