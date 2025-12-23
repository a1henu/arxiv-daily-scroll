---
layout: default
title: Interpretable Hybrid Deep Q-Learning Framework for IoT-Based Food Spoilage Prediction with Synthetic Data Generation and Hardware Validation
---

# Interpretable Hybrid Deep Q-Learning Framework for IoT-Based Food Spoilage Prediction with Synthetic Data Generation and Hardware Validation
**arXiv**：[2512.19361v1](https://arxiv.org/abs/2512.19361) · [PDF](https://arxiv.org/pdf/2512.19361.pdf)  
**作者**：Isshaan Singh, Divyansh Chawla, Anshu Garg, Shivin Mangal, Pallavi Gupta, Khushi Agarwal, Nimrat Singh Khalsa, Nandan Patel  

**一句话要点**：提出基于LSTM和RNN的混合深度Q学习框架，用于物联网食品腐败预测，结合合成数据生成和硬件验证。

**关键词**：物联网食品监测, 混合深度强化学习, 可解释人工智能, LSTM-RNN集成, 合成数据生成, 硬件验证

## 3 点简述
- 核心问题：现有方法在动态环境下适应性差，难以实时优化决策，影响食品供应链腐败预测。
- 方法要点：集成LSTM和RNN的强化学习框架，结合基于规则的分类器环境，提升预测准确性和可解释性。
- 实验或效果：在模拟和实时硬件数据上评估，显示优于其他强化学习方法，保持高准确率和决策效率。

## 摘要（原文）

> The need for an intelligent, real-time spoilage prediction system has become critical in modern IoT-driven food supply chains, where perishable goods are highly susceptible to environmental conditions. Existing methods often lack adaptability to dynamic conditions and fail to optimize decision making in real time. To address these challenges, we propose a hybrid reinforcement learning framework integrating Long Short-Term Memory (LSTM) and Recurrent Neural Networks (RNN) for enhanced spoilage prediction. This hybrid architecture captures temporal dependencies within sensor data, enabling robust and adaptive decision making. In alignment with interpretable artificial intelligence principles, a rule-based classifier environment is employed to provide transparent ground truth labeling of spoilage levels based on domain-specific thresholds. This structured design allows the agent to operate within clearly defined semantic boundaries, supporting traceable and interpretable decisions. Model behavior is monitored using interpretability-driven metrics, including spoilage accuracy, reward-to-step ratio, loss reduction rate, and exploration decay. These metrics provide both quantitative performance evaluation and insights into learning dynamics. A class-wise spoilage distribution visualization is used to analyze the agents decision profile and policy behavior. Extensive evaluations on simulated and real-time hardware data demonstrate that the LSTM and RNN based agent outperforms alternative reinforcement learning approaches in prediction accuracy and decision efficiency while maintaining interpretability. The results highlight the potential of hybrid deep reinforcement learning with integrated interpretability for scalable IoT-based food monitoring systems.

