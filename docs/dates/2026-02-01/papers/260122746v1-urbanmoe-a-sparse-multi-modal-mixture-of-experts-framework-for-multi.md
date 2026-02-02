---
layout: default
title: UrbanMoE: A Sparse Multi-Modal Mixture-of-Experts Framework for Multi-Task Urban Region Profiling
---

# UrbanMoE: A Sparse Multi-Modal Mixture-of-Experts Framework for Multi-Task Urban Region Profiling
**arXiv**：[2601.22746v1](https://arxiv.org/abs/2601.22746) · [PDF](https://arxiv.org/pdf/2601.22746.pdf)  
**作者**：Pingping Liu, Jiamiao Liu, Zijian Zhang, Hao Miao, Qi Jiang, Qingliang Li, Qiuzhan Zhou, Irwin King  

**一句话要点**：提出UrbanMoE稀疏多模态专家混合框架以解决多任务城市区域画像问题

**关键词**：城市区域画像, 多任务学习, 稀疏专家混合, 多模态特征, 基准构建, 城市分析

## 3 点简述
- 现有城市区域画像方法多为单任务预测，缺乏多任务标准化基准，阻碍公平比较
- UrbanMoE采用稀疏专家混合架构，动态路由多模态特征至专用子网络，实现多指标同时预测
- 在三个真实数据集上实验，UrbanMoE性能优于所有基线，验证了其有效性和效率

## 摘要（原文）

> Urban region profiling, the task of characterizing geographical areas, is crucial for urban planning and resource allocation. However, existing research in this domain faces two significant limitations. First, most methods are confined to single-task prediction, failing to capture the interconnected, multi-faceted nature of urban environments where numerous indicators are deeply correlated. Second, the field lacks a standardized experimental benchmark, which severely impedes fair comparison and reproducible progress. To address these challenges, we first establish a comprehensive benchmark for multi-task urban region profiling, featuring multi-modal features and a diverse set of strong baselines to ensure a fair and rigorous evaluation environment. Concurrently, we propose UrbanMoE, the first sparse multi-modal, multi-expert framework specifically architected to solve the multi-task challenge. Leveraging a sparse Mixture-of-Experts architecture, it dynamically routes multi-modal features to specialized sub-networks, enabling the simultaneous prediction of diverse urban indicators. We conduct extensive experiments on three real-world datasets within our benchmark, where UrbanMoE consistently demonstrates superior performance over all baselines. Further in-depth analysis validates the efficacy and efficiency of our approach, setting a new state-of-the-art and providing the community with a valuable tool for future research in urban analytics

