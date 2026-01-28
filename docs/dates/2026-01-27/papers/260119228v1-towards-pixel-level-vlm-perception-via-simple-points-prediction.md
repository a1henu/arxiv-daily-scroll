---
layout: default
title: Towards Pixel-Level VLM Perception via Simple Points Prediction
---

# Towards Pixel-Level VLM Perception via Simple Points Prediction
**arXiv**：[2601.19228v1](https://arxiv.org/abs/2601.19228) · [PDF](https://arxiv.org/pdf/2601.19228.pdf)  
**作者**：Tianhui Song, Haoyu Lu, Hao Yang, Lin Sui, Haoning Wu, Zaida Zhou, Zhiqi Huang, Yiping Bao, Y. Charles, Xinyu Zhou, Limin Wang  

**一句话要点**：提出SimpleSeg方法，通过简单点序列预测赋予多模态大语言模型原生像素级感知能力

**关键词**：像素级感知, 多模态大语言模型, 点序列预测, 强化学习训练, 图像分割, 统一视觉语言模型

## 3 点简述
- 核心问题：多模态大语言模型缺乏原生像素级感知，依赖复杂辅助组件进行分割
- 方法要点：将分割重构为语言空间内的点序列生成问题，采用两阶段SF→RL训练提升精度
- 实验或效果：在分割基准测试中性能媲美或超越任务特定方法，验证模型固有低级感知能力

## 摘要（原文）

> We present SimpleSeg, a strikingly simple yet highly effective approach to endow Multimodal Large Language Models (MLLMs) with native pixel-level perception. Our method reframes segmentation as a simple sequence generation problem: the model directly predicts sequences of points (textual coordinates) delineating object boundaries, entirely within its language space. To achieve high fidelity, we introduce a two-stage SF$\to$RL training pipeline, where Reinforcement Learning with an IoU-based reward refines the point sequences to accurately match ground-truth contours. We find that the standard MLLM architecture possesses a strong, inherent capacity for low-level perception that can be unlocked without any specialized architecture. On segmentation benchmarks, SimpleSeg achieves performance that is comparable to, and often surpasses, methods relying on complex, task-specific designs. This work lays out that precise spatial understanding can emerge from simple point prediction, challenging the prevailing need for auxiliary components and paving the way for more unified and capable VLMs. Homepage: https://simpleseg.github.io/

