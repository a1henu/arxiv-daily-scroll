---
layout: default
title: GeoBridge: A Semantic-Anchored Multi-View Foundation Model Bridging Images and Text for Geo-Localization
---

# GeoBridge: A Semantic-Anchored Multi-View Foundation Model Bridging Images and Text for Geo-Localization
**arXiv**：[2512.02697v1](https://arxiv.org/abs/2512.02697) · [PDF](https://arxiv.org/pdf/2512.02697.pdf)  
**作者**：Zixuan Song, Jing Zhang, Di Wang, Zidie Zhou, Wenbin Liu, Haonan Guo, En Wang, Bo Du  

**一句话要点**：提出GeoBridge基础模型，通过语义锚机制桥接多视图与多模态，提升跨视图地理定位的鲁棒性和灵活性。

**关键词**：跨视图地理定位, 多模态基础模型, 语义锚机制, GeoLoc数据集, 语言到图像检索

## 3 点简述
- 传统卫星中心范式在缺乏高分辨率或最新卫星图像时鲁棒性受限，且未充分利用多视图和多模态互补信息。
- GeoBridge基于语义锚机制，通过文本描述桥接多视图特征，支持双向跨视图匹配和语言到图像检索。
- 构建GeoLoc数据集进行预训练，实验表明显著提升地理定位精度，并促进跨域泛化和跨模态知识迁移。

## 摘要（原文）

> Cross-view geo-localization infers a location by retrieving geo-tagged reference images that visually correspond to a query image. However, the traditional satellite-centric paradigm limits robustness when high-resolution or up-to-date satellite imagery is unavailable. It further underexploits complementary cues across views (e.g., drone, satellite, and street) and modalities (e.g., language and image). To address these challenges, we propose GeoBridge, a foundation model that performs bidirectional matching across views and supports language-to-image retrieval. Going beyond traditional satellite-centric formulations, GeoBridge builds on a novel semantic-anchor mechanism that bridges multi-view features through textual descriptions for robust, flexible localization. In support of this task, we construct GeoLoc, the first large-scale, cross-modal, and multi-view aligned dataset comprising over 50,000 pairs of drone, street-view panorama, and satellite images as well as their textual descriptions, collected from 36 countries, ensuring both geographic and semantic alignment. We performed broad evaluations across multiple tasks. Experiments confirm that GeoLoc pre-training markedly improves geo-location accuracy for GeoBridge while promoting cross-domain generalization and cross-modal knowledge transfer. The dataset, source code, and pretrained models were released at https://github.com/MiliLab/GeoBridge.

