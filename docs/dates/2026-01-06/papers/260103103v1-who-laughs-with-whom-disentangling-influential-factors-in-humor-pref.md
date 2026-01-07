---
layout: default
title: Who Laughs with Whom? Disentangling Influential Factors in Humor Preferences across User Clusters and LLMs
---

# Who Laughs with Whom? Disentangling Influential Factors in Humor Preferences across User Clusters and LLMs
**arXiv**：[2601.03103v1](https://arxiv.org/abs/2601.03103) · [PDF](https://arxiv.org/pdf/2601.03103.pdf)  
**作者**：Soichiro Murakami, Hidetaka Kamigaito, Hiroya Takamura, Manabu Okumura  

**一句话要点**：提出基于用户聚类与Bradley-Terry-Luce模型的方法，以解析日本Oogiri游戏中的幽默偏好异质性，并评估大语言模型的相似性。

**关键词**：幽默偏好建模, 用户聚类, Bradley-Terry-Luce模型, 大语言模型评估, 角色提示, Oogiri游戏

## 3 点简述
- 核心问题：幽默偏好因个体和文化而异，使得大语言模型评估幽默变得复杂。
- 方法要点：通过投票日志聚类用户，并使用Bradley-Terry-Luce模型估计可解释偏好因素的集群特定权重。
- 实验或效果：发现用户集群有独特偏好模式，大语言模型结果可模拟特定集群，且通过角色提示可引导模型偏好。

## 摘要（原文）

> Humor preferences vary widely across individuals and cultures, complicating the evaluation of humor using large language models (LLMs). In this study, we model heterogeneity in humor preferences in Oogiri, a Japanese creative response game, by clustering users with voting logs and estimating cluster-specific weights over interpretable preference factors using Bradley-Terry-Luce models. We elicit preference judgments from LLMs by prompting them to select the funnier response and found that user clusters exhibit distinct preference patterns and that the LLM results can resemble those of particular clusters. Finally, we demonstrate that, by persona prompting, LLM preferences can be directed toward a specific cluster. The scripts for data collection and analysis will be released to support reproducibility.

