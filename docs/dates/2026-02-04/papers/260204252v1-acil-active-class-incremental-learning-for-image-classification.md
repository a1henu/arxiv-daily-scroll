---
layout: default
title: ACIL: Active Class Incremental Learning for Image Classification
---

# ACIL: Active Class Incremental Learning for Image Classification
**arXiv**：[2602.04252v1](https://arxiv.org/abs/2602.04252) · [PDF](https://arxiv.org/pdf/2602.04252.pdf)  
**作者**：Aditya R. Bhattacharya, Debanjan Goswami, Shayok Chakraborty  

**一句话要点**：提出ACIL框架，结合主动学习与类增量学习以降低标注成本并避免灾难性遗忘。

**关键词**：类增量学习, 主动学习, 图像分类, 灾难性遗忘, 标注成本降低

## 3 点简述
- 核心问题：类增量学习中标注成本高，现有方法假设所有样本已标注，导致资源浪费。
- 方法要点：基于不确定性和多样性准则，在每轮中选择需标注的样本，减少标注量并保留关键信息。
- 实验或效果：在多个视觉数据集上验证，ACIL能显著降低标注成本，同时有效避免灾难性遗忘。

## 摘要（原文）

> Continual learning (or class incremental learning) is a realistic learning scenario for computer vision systems, where deep neural networks are trained on episodic data, and the data from previous episodes are generally inaccessible to the model. Existing research in this domain has primarily focused on avoiding catastrophic forgetting, which occurs due to the continuously changing class distributions in each episode and the inaccessibility of the data from previous episodes. However, these methods assume that all the training samples in every episode are annotated; this not only incurs a huge annotation cost, but also results in a wastage of annotation effort, since most of the samples in a given episode will not be accessible to the model in subsequent episodes. Active learning algorithms identify the salient and informative samples from large amounts of unlabeled data and are instrumental in reducing the human annotation effort in inducing a deep neural network. In this paper, we propose ACIL, a novel active learning framework for class incremental learning settings. We exploit a criterion based on uncertainty and diversity to identify the exemplar samples that need to be annotated in each episode, and will be appended to the data in the next episode. Such a framework can drastically reduce annotation cost and can also avoid catastrophic forgetting. Our extensive empirical analyses on several vision datasets corroborate the promise and potential of our framework against relevant baselines.

