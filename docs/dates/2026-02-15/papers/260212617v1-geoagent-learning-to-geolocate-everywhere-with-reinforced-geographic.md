---
layout: default
title: GeoAgent: Learning to Geolocate Everywhere with Reinforced Geographic Characteristics
---

# GeoAgent: Learning to Geolocate Everywhere with Reinforced Geographic Characteristics
**arXiv**：[2602.12617v1](https://arxiv.org/abs/2602.12617) · [PDF](https://arxiv.org/pdf/2602.12617.pdf)  
**作者**：Modi Jin, Yiming Zhang, Boyuan Sun, Dingwen Zhang, MingMing Cheng, Qibin Hou  

**一句话要点**：提出GeoAgent模型，通过地理特征强化学习解决细粒度地址推理问题

**关键词**：地理定位, 强化学习, 思维链数据, 地理特征奖励, 一致性评估, 细粒度推理

## 3 点简述
- 核心问题：现有RL方法依赖AI生成的思维链数据，与地理特性冲突，影响性能和可解释性
- 方法要点：引入专家标注的GeoSeek数据集，设计地理相似性和一致性奖励以优化训练过程
- 实验或效果：在多个粒度上超越现有方法和通用VLLMs，生成与人类推理高度一致的输出

## 摘要（原文）

> This paper presents GeoAgent, a model capable of reasoning closely with humans and deriving fine-grained address conclusions. Previous RL-based methods have achieved breakthroughs in performance and interpretability but still remain concerns because of their reliance on AI-generated chain-of-thought (CoT) data and training strategies, which conflict with geographic characteristics. To address these issues, we first introduce GeoSeek, a new geolocation dataset comprising CoT data annotated by geographic experts and professional players. We further thoroughly explore the inherent characteristics of geographic tasks and propose a geo-similarity reward and a consistency reward assessed by a consistency agent to assist training. This encourages the model to converge towards correct answers from a geographic perspective while ensuring the integrity and consistency of its reasoning process. Experimental results show that GeoAgent outperforms existing methods and a series of general VLLMs across multiple grains, while generating reasoning that closely aligns with humans.

