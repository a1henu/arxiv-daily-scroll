---
layout: default
title: MapViT: A Two-Stage ViT-Based Framework for Real-Time Radio Quality Map Prediction in Dynamic Environments
---

# MapViT: A Two-Stage ViT-Based Framework for Real-Time Radio Quality Map Prediction in Dynamic Environments
**arXiv**：[2601.15578v1](https://arxiv.org/abs/2601.15578) · [PDF](https://arxiv.org/pdf/2601.15578.pdf)  
**作者**：Cyril Shih-Huan Hsu, Xi Li, Lanfranco Zanzi, Zhiheng Yang, Chrysa Papagianni, Xavier Costa Pérez  

**一句话要点**：提出MapViT两阶段ViT框架，用于动态环境中实时无线电质量地图预测

**关键词**：无线电质量地图预测, Vision Transformer, 两阶段框架, 动态环境, 实时预测, 自监督预训练

## 3 点简述
- 核心问题：动态环境中机器人需准确理解环境和无线电信号质量，但此问题尚未解决
- 方法要点：采用两阶段Vision Transformer框架，受LLM预训练微调范式启发，预测环境变化和信号质量
- 实验或效果：ViT实现实现精度与计算效率平衡，支持实时预测，适用于资源受限平台

## 摘要（原文）

> Recent advancements in mobile and wireless networks are unlocking the full potential of robotic autonomy, enabling robots to take advantage of ultra-low latency, high data throughput, and ubiquitous connectivity. However, for robots to navigate and operate seamlessly, efficiently and reliably, they must have an accurate understanding of both their surrounding environment and the quality of radio signals. Achieving this in highly dynamic and ever-changing environments remains a challenging and largely unsolved problem. In this paper, we introduce MapViT, a two-stage Vision Transformer (ViT)-based framework inspired by the success of pre-train and fine-tune paradigm for Large Language Models (LLMs). MapViT is designed to predict both environmental changes and expected radio signal quality. We evaluate the framework using a set of representative Machine Learning (ML) models, analyzing their respective strengths and limitations across different scenarios. Experimental results demonstrate that the proposed two-stage pipeline enables real-time prediction, with the ViT-based implementation achieving a strong balance between accuracy and computational efficiency. This makes MapViT a promising solution for energy- and resource-constrained platforms such as mobile robots. Moreover, the geometry foundation model derived from the self-supervised pre-training stage improves data efficiency and transferability, enabling effective downstream predictions even with limited labeled data. Overall, this work lays the foundation for next-generation digital twin ecosystems, and it paves the way for a new class of ML foundation models driving multi-modal intelligence in future 6G-enabled systems.

