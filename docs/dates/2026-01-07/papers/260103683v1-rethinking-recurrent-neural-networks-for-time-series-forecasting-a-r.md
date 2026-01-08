---
layout: default
title: Rethinking Recurrent Neural Networks for Time Series Forecasting: A Reinforced Recurrent Encoder with Prediction-Oriented Proximal Policy Optimization
---

# Rethinking Recurrent Neural Networks for Time Series Forecasting: A Reinforced Recurrent Encoder with Prediction-Oriented Proximal Policy Optimization
**arXiv**：[2601.03683v1](https://arxiv.org/abs/2601.03683) · [PDF](https://arxiv.org/pdf/2601.03683.pdf)  
**作者**：Xin Lai, Shiming Deng, Lu Yu, Yumin Lai, Shenghao Qiao, Xinze Zhang  

**一句话要点**：提出RRE-PPO4Pred方法，通过强化学习优化RNN在时间序列预测中的建模能力。

**关键词**：时间序列预测, 强化学习, 循环神经网络, 马尔可夫决策过程, 预测优化

## 3 点简述
- 传统RNN预测器平等处理所有时间步和隐藏状态，导致性能不佳。
- RRE框架将RNN内部适应建模为马尔可夫决策过程，统一学习特征选择、隐藏跳跃连接和目标选择。
- 在五个真实数据集上评估，方法优于现有基线，准确度超越最先进的Transformer模型。

## 摘要（原文）

> Time series forecasting plays a crucial role in contemporary engineering information systems for supporting decision-making across various industries, where Recurrent Neural Networks (RNNs) have been widely adopted due to their capability in modeling sequential data. Conventional RNN-based predictors adopt an encoder-only strategy with sliding historical windows as inputs to forecast future values. However, this approach treats all time steps and hidden states equally without considering their distinct contributions to forecasting, leading to suboptimal performance. To address this limitation, we propose a novel Reinforced Recurrent Encoder with Prediction-oriented Proximal Policy Optimization, RRE-PPO4Pred, which significantly improves time series modeling capacity and forecasting accuracy of the RNN models. The core innovations of this method are: (1) A novel Reinforced Recurrent Encoder (RRE) framework that enhances RNNs by formulating their internal adaptation as a Markov Decision Process, creating a unified decision environment capable of learning input feature selection, hidden skip connection, and output target selection; (2) An improved Prediction-oriented Proximal Policy Optimization algorithm, termed PPO4Pred, which is equipped with a Transformer-based agent for temporal reasoning and develops a dynamic transition sampling strategy to enhance sampling efficiency; (3) A co-evolutionary optimization paradigm to facilitate the learning of the RNN predictor and the policy agent, providing adaptive and interactive time series modeling. Comprehensive evaluations on five real-world datasets indicate that our method consistently outperforms existing baselines, and attains accuracy better than state-of-the-art Transformer models, thus providing an advanced time series predictor in engineering informatics.

