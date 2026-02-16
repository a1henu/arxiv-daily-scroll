---
layout: default
title: Jointly Optimizing Debiased CTR and Uplift for Coupons Marketing: A Unified Causal Framework
---

# Jointly Optimizing Debiased CTR and Uplift for Coupons Marketing: A Unified Causal Framework
**arXiv**：[2602.12972v1](https://arxiv.org/abs/2602.12972) · [PDF](https://arxiv.org/pdf/2602.12972.pdf)  
**作者**：Siyun Yang, Shixiao Yang, Jian Wang, Di Fan, Kehe Cai, Haoyan Fu, Jiaming Zhang, Wenjin Wu, Peng Jiang  

**一句话要点**：提出UniMVT统一因果框架，以解决优惠券营销中CTR预测的混淆偏差问题。

**关键词**：点击率预测, 因果推断, 去偏估计, 提升建模, 多值处理, 在线广告

## 3 点简述
- 核心问题：优惠券等营销干预引入混淆偏差，导致CTR预测失真，影响排序和计费决策。
- 方法要点：UniMVT通过解耦混淆因素和全空间反事实推断，联合优化去偏CTR和提升估计。
- 实验或效果：在合成和工业数据集上验证了预测准确性和校准优势，A/B测试显示显著提升业务指标。

## 摘要（原文）

> In online advertising, marketing interventions such as coupons introduce significant confounding bias into Click-Through Rate (CTR) prediction. Observed clicks reflect a mixture of users' intrinsic preferences and the uplift induced by these interventions. This causes conventional models to miscalibrate base CTRs, which distorts downstream ranking and billing decisions. Furthermore, marketing interventions often operate as multi-valued treatments with varying magnitudes, introducing additional complexity to CTR prediction.
>   To address these issues, we propose the \textbf{Uni}fied \textbf{M}ulti-\textbf{V}alued \textbf{T}reatment Network (UniMVT). Specifically, UniMVT disentangles confounding factors from treatment-sensitive representations, enabling a full-space counterfactual inference module to jointly reconstruct the debiased base CTR and intensity-response curves. To handle the complexity of multi-valued treatments, UniMVT employs an auxiliary intensity estimation task to capture treatment propensities and devise a unit uplift objective that normalizes the intervention effect. This ensures comparable estimation across the continuous coupon-value spectrum. UniMVT simultaneously achieves debiased CTR prediction for accurate system calibration and precise uplift estimation for incentive allocation. Extensive experiments on synthetic and industrial datasets demonstrate UniMVT's superiority in both predictive accuracy and calibration. Furthermore, real-world A/B tests confirm that UniMVT significantly improves business metrics through more effective coupon distribution.

