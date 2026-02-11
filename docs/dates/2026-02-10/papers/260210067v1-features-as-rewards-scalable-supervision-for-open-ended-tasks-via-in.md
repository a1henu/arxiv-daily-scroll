---
layout: default
title: Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability
---

# Features as Rewards: Scalable Supervision for Open-Ended Tasks via Interpretability
**arXiv**：[2602.10067v1](https://arxiv.org/abs/2602.10067) · [PDF](https://arxiv.org/pdf/2602.10067.pdf)  
**作者**：Aaditya Vikram Prasad, Connor Watts, Jack Merullo, Dhruvil Gala, Owen Lewis, Thomas McGrath, Ekdeep Singh Lubana  

**一句话要点**：提出基于特征奖励的强化学习框架，以可扩展监督解决开放任务中的幻觉问题。

**关键词**：特征奖励, 强化学习, 幻觉减少, 可解释性, 开放任务监督

## 3 点简述
- 核心问题：语言模型在开放任务中易产生幻觉，传统监督方法难以规模化。
- 方法要点：利用可解释特征作为奖励函数，设计RLFR框架引导模型干预和修正不确定输出。
- 实验或效果：在Gemma-3-12B-IT上实现幻觉率降低58%，同时保持基准性能。

## 摘要（原文）

> Language models trained on large-scale datasets have been shown to learn features that encode abstract concepts such as factuality or intent. Such features are traditionally used for test-time monitoring or steering. We present an alternative affordance: features as scalable supervision for open-ended tasks. We consider the case of hallucination-reduction as a desirable, yet open-ended behavior and design a reinforcement learning (RL) pipeline, titled RLFR (Reinforcement Learning from Feature Rewards), that uses features as reward functions. Grounded in a novel probing framework that identifies candidate hallucinated claims, our pipeline teaches a model to intervene and correct its completions when it is uncertain of their factuality. Furthermore, the pipeline enables scalable test-time compute, guided once more by our reward features. This end-to-end process operationalized on Gemma-3-12B-IT results in a policy that is 58% less likely to hallucinate compared to the original model, while preserving performance on standard benchmarks. Taken together, by grounding supervision in the language of features, this paper introduces a novel paradigm in the use of interpretability for learning open-ended tasks.

