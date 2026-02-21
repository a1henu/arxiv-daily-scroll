---
layout: default
title: Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers
---

# Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers
**arXiv**：[2602.17410v1](https://arxiv.org/abs/2602.17410) · [PDF](https://arxiv.org/pdf/2602.17410.pdf)  
**作者**：Bingqian Li, Bowen Zheng, Xiaolei Wang, Long Zhang, Jinpeng Wang, Sheng Chen, Wayne Xin Zhao, Ji-rong Wen  

**一句话要点**：提出ILRec框架，利用中间层自硬负信号增强基于LLM的推荐系统偏好学习

**关键词**：基于LLM的推荐, 偏好学习, 自硬负样本, 中间层信号, 跨层蒸馏

## 3 点简述
- 现有方法依赖离线生成的序列级负样本，在大型负项空间中区分性和信息性不足
- ILRec从中间层提取自硬负标记作为细粒度负监督，设计跨层偏好优化与蒸馏两阶段框架
- 在三个数据集上实验验证ILRec能有效提升基于LLM的推荐系统性能

## 摘要（原文）

> Large language models (LLMs) have shown great promise in recommender systems, where supervised fine-tuning (SFT) is commonly used for adaptation. Subsequent studies further introduce preference learning to incorporate negative samples into the training process. However, existing methods rely on sequence-level, offline-generated negatives, making them less discriminative and informative when adapting LLMs to recommendation tasks with large negative item spaces. To address these challenges, we propose ILRec, a novel preference fine-tuning framework for LLM-based recommendation, leveraging self-hard negative signals extracted from intermediate layers to improve preference learning. Specifically, we identify self-hard negative tokens from intermediate layers as fine-grained negative supervision that dynamically reflects the model's preference learning process. To effectively integrate these signals into training, we design a two-stage framework comprising cross-layer preference optimization and cross-layer preference distillation, enabling the model to jointly discriminate informative negatives and enhance the quality of negative signals from intermediate layers. In addition, we introduce a lightweight collaborative filtering model to assign token-level rewards for negative signals, mitigating the risk of over-penalizing false negatives. Extensive experiments on three datasets demonstrate ILRec's effectiveness in enhancing the performance of LLM-based recommender systems.

