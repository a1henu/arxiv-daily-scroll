---
layout: default
title: SMGeo: Cross-View Object Geo-Localization with Grid-Level Mixture-of-Experts
---

# SMGeo: Cross-View Object Geo-Localization with Grid-Level Mixture-of-Experts
**arXiv**：[2511.14093v1](https://arxiv.org/abs/2511.14093) · [PDF](https://arxiv.org/pdf/2511.14093.pdf)  
**作者**：Fan Zhang, Haoyuan Ren, Fei Ma, Qiang Yin, Yongsheng Zhou  

**一句话要点**：提出SMGeo模型以解决跨视角对象地理定位问题

**关键词**：跨视角地理定位, Transformer模型, 网格级专家混合, 端到端学习, 无人机-卫星匹配

## 3 点简述
- 核心问题：跨视角对象地理定位因视角和尺度差异及背景干扰，传统方法易累积误差。
- 方法要点：采用端到端Transformer架构，引入网格级稀疏专家混合以自适应处理特征。
- 实验效果：在无人机到卫星任务中，SMGeo在IoU=0.25和mIoU指标上领先现有方法。

## 摘要（原文）

> Cross-view object Geo-localization aims to precisely pinpoint the same object across large-scale satellite imagery based on drone images. Due to significant differences in viewpoint and scale, coupled with complex background interference, traditional multi-stage "retrieval-matching" pipelines are prone to cumulative errors. To address this, we present SMGeo, a promptable end-to-end transformer-based model for object Geo-localization. This model supports click prompting and can output object Geo-localization in real time when prompted to allow for interactive use. The model employs a fully transformer-based architecture, utilizing a Swin-Transformer for joint feature encoding of both drone and satellite imagery and an anchor-free transformer detection head for coordinate regression. In order to better capture both inter-modal and intra-view dependencies, we introduce a grid-level sparse Mixture-of-Experts (GMoE) into the cross-view encoder, allowing it to adaptively activate specialized experts according to the content, scale and source of each grid. We also employ an anchor-free detection head for coordinate regression, directly predicting object locations via heat-map supervision in the reference images. This approach avoids scale bias and matching complexity introduced by predefined anchor boxes. On the drone-to-satellite task, SMGeo achieves leading performance in accuracy at IoU=0.25 and mIoU metrics (e.g., 87.51%, 62.50%, and 61.45% in the test set, respectively), significantly outperforming representative methods such as DetGeo (61.97%, 57.66%, and 54.05%, respectively). Ablation studies demonstrate complementary gains from shared encoding, query-guided fusion, and grid-level sparse mixture-of-experts.

