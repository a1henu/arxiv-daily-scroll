---
layout: default
title: The Neural Compass: Probabilistic Relative Feature Fields for Robotic Search
---

# The Neural Compass: Probabilistic Relative Feature Fields for Robotic Search
**arXiv**：[2603.08544v1](https://arxiv.org/abs/2603.08544) · [PDF](https://arxiv.org/pdf/2603.08544.pdf)  
**作者**：Gabriele Somaschini, Adrian Röfer, Abhinav Valada  

**一句话要点**：提出ProReFF模型，通过概率相对特征场从无标注数据学习物体共现关系，以提升机器人搜索效率。

**关键词**：机器人搜索, 特征场模型, 无监督学习, 物体共现, 视觉语言模型, 概率分布

## 3 点简述
- 核心问题：能否仅从无标注观测中隐式学习物体共现关系，用于机器人搜索。
- 方法要点：训练特征场模型预测预训练视觉语言模型特征的相对分布，并引入对齐策略处理不一致数据。
- 实验或效果：在Matterport3D模拟器中，搜索代理比最强基线效率高20%，达到人类性能的80%。

## 摘要（原文）

> Object co-occurrences provide a key cue for finding objects successfully and efficiently in unfamiliar environments. Typically, one looks for cups in kitchens and views fridges as evidence of being in a kitchen. Such priors have also been exploited in artificial agents, but they are typically learned from explicitly labeled data or queried from language models. It is still unclear whether these relations can be learned implicitly from unlabeled observations alone. In this work, we address this problem and propose ProReFF, a feature field model trained to predict relative distributions of features obtained from pre-trained vision language models. In addition, we introduce a learning-based strategy that enables training from unlabeled and potentially contradictory data by aligning inconsistent observations into a coherent relative distribution. For the downstream object search task, we propose an agent that leverages predicted feature distributions as a semantic prior to guide exploration toward regions with a high likelihood of containing the object. We present extensive evaluations demonstrating that ProReFF captures meaningful relative feature distributions in natural scenes and provides insight into the impact of our proposed alignment step. We further evaluate the performance of our search agent in 100 challenges in the Matterport3D simulator, comparing with feature-based baselines and human participants. The proposed agent is 20% more efficient than the strongest baseline and achieves up to 80% of human performance.

