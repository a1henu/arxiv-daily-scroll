---
layout: default
title: MOON Embedding: Multimodal Representation Learning for E-commerce Search Advertising
---

# MOON Embedding: Multimodal Representation Learning for E-commerce Search Advertising
**arXiv**：[2511.11305v1](https://arxiv.org/abs/2511.11305) · [PDF](https://arxiv.org/pdf/2511.11305.pdf)  
**作者**：Chenghan Fu, Daoze Zhang, Yukang Lin, Zhanheng Nie, Xiang Zhang, Jianyu Liu, Yueran Liu, Wanxian Guan, Pengjie Wang, Jian Xu, Bo Zheng  

**一句话要点**：提出MOON多模态表示学习框架以优化电商搜索广告系统

**关键词**：多模态表示学习, 电商搜索广告, 点击率预测, 三阶段训练, 交换率分析, 缩放定律研究

## 3 点简述
- 核心问题：多模态表示学习与下游任务目标不匹配，影响电商广告效果。
- 方法要点：采用三阶段训练范式，定义交换率量化中间指标与下游增益关系。
- 实验或效果：在线点击率提升20.00%，已部署于淘宝搜索广告全阶段。

## 摘要（原文）

> We introduce MOON, our comprehensive set of sustainable iterative practices for multimodal representation learning for e-commerce applications. MOON has already been fully deployed across all stages of Taobao search advertising system, including retrieval, relevance, ranking, and so on. The performance gains are particularly significant on click-through rate (CTR) prediction task, which achieves an overall +20.00% online CTR improvement. Over the past three years, this project has delivered the largest improvement on CTR prediction task and undergone five full-scale iterations. Throughout the exploration and iteration of our MOON, we have accumulated valuable insights and practical experience that we believe will benefit the research community. MOON contains a three-stage training paradigm of "Pretraining, Post-training, and Application", allowing effective integration of multimodal representations with downstream tasks. Notably, to bridge the misalignment between the objectives of multimodal representation learning and downstream training, we define the exchange rate to quantify how effectively improvements in an intermediate metric can translate into downstream gains. Through this analysis, we identify the image-based search recall as a critical intermediate metric guiding the optimization of multimodal models. Over three years and five iterations, MOON has evolved along four critical dimensions: data processing, training strategy, model architecture, and downstream application. The lessons and insights gained through the iterative improvements will also be shared. As part of our exploration into scaling effects in the e-commerce field, we further conduct a systematic study of the scaling laws governing multimodal representation learning, examining multiple factors such as the number of training tokens, negative samples, and the length of user behavior sequences.

