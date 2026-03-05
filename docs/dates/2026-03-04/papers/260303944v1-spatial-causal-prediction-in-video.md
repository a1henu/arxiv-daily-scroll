---
layout: default
title: Spatial Causal Prediction in Video
---

# Spatial Causal Prediction in Video
**arXiv**：[2603.03944v1](https://arxiv.org/abs/2603.03944) · [PDF](https://arxiv.org/pdf/2603.03944.pdf)  
**作者**：Yanguang Zhao, Jie Yang, Shengqiong Wu, Shutong Hu, Hongbo Qiu, Yu Wang, Guijia Zhang, Tan Kai Ze, Hao Fei, Chia-Wen Lin, Mong-Li Lee, Wynne Hsu  

**一句话要点**：提出空间因果预测任务与基准，以评估视频中超越观测的空间推理能力。

**关键词**：空间因果预测, 视频理解, 基准评估, 时空推理, 模型性能分析

## 3 点简述
- 现有研究主要评估可见时空理解，忽略推断未观测空间状态的能力。
- 引入空间因果预测任务，构建包含2500个问答对的SCP-Bench基准。
- 实验揭示模型与人类性能差距大，提出感知增强和推理引导策略。

## 摘要（原文）

> Spatial reasoning, the ability to understand spatial relations, causality, and dynamic evolution, is central to human intelligence and essential for real-world applications such as autonomous driving and robotics. Existing studies, however, primarily assess models on visible spatio-temporal understanding, overlooking their ability to infer unseen past or future spatial states. In this work, we introduce Spatial Causal Prediction (SCP), a new task paradigm that challenges models to reason beyond observation and predict spatial causal outcomes. We further construct SCP-Bench, a benchmark comprising 2,500 QA pairs across 1,181 videos spanning diverse viewpoints, scenes, and causal directions, to support systematic evaluation. Through comprehensive experiments on {23} state-of-the-art models, we reveal substantial gaps between human and model performance, limited temporal extrapolation, and weak causal grounding. We further analyze key factors influencing performance and propose perception-enhancement and reasoning-guided strategies toward advancing spatial causal intelligence. The project page is https://guangstrip.github.io/SCP-Bench.

