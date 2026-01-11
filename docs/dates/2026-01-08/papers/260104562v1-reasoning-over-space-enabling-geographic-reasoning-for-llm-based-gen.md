---
layout: default
title: Reasoning Over Space: Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation
---

# Reasoning Over Space: Enabling Geographic Reasoning for LLM-Based Generative Next POI Recommendation
**arXiv**：[2601.04562v1](https://arxiv.org/abs/2601.04562) · [PDF](https://arxiv.org/pdf/2601.04562.pdf)  
**作者**：Dongyi Lv, Qiuyu Ding, Heng-Da Xu, Zhaoxu Sun, Zhi Wang, Feng Xiong, Mu Xu  

**一句话要点**：提出ROS框架，通过地理推理增强LLM在移动和本地服务场景中的下一个POI推荐能力。

**关键词**：地理推理, 生成推荐, 大语言模型, POI推荐, 强化学习, 空间语义ID

## 3 点简述
- 现有LLM推荐器在利用地理信号方面受限，影响移动和本地服务场景的准确性。
- ROS引入分层空间语义ID和移动链式思维范式，将地理信息融入推理过程。
- 实验显示ROS在三个LBSN数据集上命中率相对提升超10%，并改善跨城市迁移性能。

## 摘要（原文）

> Generative recommendation with large language models (LLMs) reframes prediction as sequence generation, yet existing LLM-based recommenders remain limited in leveraging geographic signals that are crucial in mobility and local-services scenarios. Here, we present Reasoning Over Space (ROS), a framework that utilizes geography as a vital decision variable within the reasoning process. ROS introduces a Hierarchical Spatial Semantic ID (SID) that discretizes coarse-to-fine locality and POI semantics into compositional tokens, and endows LLM with a three-stage Mobility Chain-of-Thought (CoT) paradigm that models user personality, constructs an intent-aligned candidate space, and performs locality informed pruning. We further align the model with real world geography via spatial-guided Reinforcement Learning (RL). Experiments on three widely used location-based social network (LBSN) datasets show that ROS achieves over 10% relative gains in hit rate over strongest LLM-based baselines and improves cross-city transfer, despite using a smaller backbone model.

