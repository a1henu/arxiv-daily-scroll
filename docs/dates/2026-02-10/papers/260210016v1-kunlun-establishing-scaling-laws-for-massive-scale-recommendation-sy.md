---
layout: default
title: Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design
---

# Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design
**arXiv**：[2602.10016v1](https://arxiv.org/abs/2602.10016) · [PDF](https://arxiv.org/pdf/2602.10016.pdf)  
**作者**：Bojian Hou, Xiaolong Liu, Xiaoyi Liu, Jiaqi Xu, Yasmine Badr, Mengyue Hang, Sudhanshu Chanpuriya, Junqing Zhou, Yuhang Yang, Han Xu, Qiuling Suo, Laming Chen, Yuxi Hu, Jiasheng Zhang, Huaqing Xiong, Yuzhen Huang, Chao Chen, Yue Dong, Yi Yang, Shuo Chang, Xiaorui Gan, Wenlin Chen, Santanu Kolay, Darren Liu, Jade Nie, Chunzhi Yang, Jiyan Yang, Huayu Li  

**一句话要点**：提出Kunlun架构以解决大规模推荐系统可预测扩展性难题

**关键词**：大规模推荐系统, 扩展定律, 模型效率优化, 资源分配, 注意力机制, 个性化推荐

## 3 点简述
- 核心问题：大规模推荐系统缺乏可预测扩展定律，源于低模型FLOPs利用率和次优资源分配
- 方法要点：通过GDPA、HSP、Sliding Window Attention等低层优化及CompSkip、事件级个性化等高层创新提升效率
- 实验或效果：在NVIDIA B200 GPU上将MFU从17%提升至37%，扩展效率翻倍，已部署于Meta Ads模型

## 摘要（原文）

> Deriving predictable scaling laws that govern the relationship between model performance and computational investment is crucial for designing and allocating resources in massive-scale recommendation systems. While such laws are established for large language models, they remain challenging for recommendation systems, especially those processing both user history and context features. We identify poor scaling efficiency as the main barrier to predictable power-law scaling, stemming from inefficient modules with low Model FLOPs Utilization (MFU) and suboptimal resource allocation. We introduce Kunlun, a scalable architecture that systematically improves model efficiency and resource allocation. Our low-level optimizations include Generalized Dot-Product Attention (GDPA), Hierarchical Seed Pooling (HSP), and Sliding Window Attention. Our high-level innovations feature Computation Skip (CompSkip) and Event-level Personalization. These advances increase MFU from 17% to 37% on NVIDIA B200 GPUs and double scaling efficiency over state-of-the-art methods. Kunlun is now deployed in major Meta Ads models, delivering significant production impact.

