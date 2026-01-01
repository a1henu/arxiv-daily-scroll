---
layout: default
title: Scaling Open-Ended Reasoning to Predict the Future
---

# Scaling Open-Ended Reasoning to Predict the Future
**arXiv**：[2512.25070v1](https://arxiv.org/abs/2512.25070) · [PDF](https://arxiv.org/pdf/2512.25070.pdf)  
**作者**：Nikhil Chandak, Shashwat Goel, Ameya Prabhu, Moritz Hardt, Jonas Geiping  

**一句话要点**：提出OpenForecaster 8B模型以解决开放端预测问题，通过自动化合成训练数据提升预测准确性。

**关键词**：开放端预测, 语言模型训练, 数据合成, 强化学习, 校准改进, 离线新闻检索

## 3 点简述
- 核心问题：高风险决策需基于未来不确定性进行开放端预测，现有方法数据不足且易泄露未来信息。
- 方法要点：从离线新闻自动合成预测问题训练Qwen3模型，结合检索和改进的奖励函数进行强化学习。
- 实验或效果：在2025年5月至8月测试中，模型匹配更大专有模型，提升准确性、校准和一致性，校准改进泛化至基准测试。

## 摘要（原文）

> High-stakes decision making involves reasoning under uncertainty about the future. In this work, we train language models to make predictions on open-ended forecasting questions. To scale up training data, we synthesize novel forecasting questions from global events reported in daily news, using a fully automated, careful curation recipe. We train the Qwen3 thinking models on our dataset, OpenForesight. To prevent leakage of future information during training and evaluation, we use an offline news corpus, both for data generation and retrieval in our forecasting system. Guided by a small validation set, we show the benefits of retrieval, and an improved reward function for reinforcement learning (RL). Once we obtain our final forecasting system, we perform held-out testing between May to August 2025. Our specialized model, OpenForecaster 8B, matches much larger proprietary models, with our training improving the accuracy, calibration, and consistency of predictions. We find calibration improvements from forecasting training generalize across popular benchmarks. We open-source all our models, code, and data to make research on language model forecasting broadly accessible.

