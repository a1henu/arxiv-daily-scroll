---
layout: default
title: BalDRO: A Distributionally Robust Optimization based Framework for Large Language Model Unlearning
---

# BalDRO: A Distributionally Robust Optimization based Framework for Large Language Model Unlearning
**arXiv**：[2601.09172v1](https://arxiv.org/abs/2601.09172) · [PDF](https://arxiv.org/pdf/2601.09172.pdf)  
**作者**：Pengyang Shao, Naixin Zhai, Lei Chen, Yonghui Yang, Fengbin Zhu, Xun Yang, Meng Wang  

**一句话要点**：提出BalDRO框架，基于分布鲁棒优化解决大语言模型遗忘中的样本不平衡问题。

**关键词**：大语言模型遗忘, 分布鲁棒优化, 样本不平衡, 异步遗忘, 模型效用

## 3 点简述
- 核心问题：遗忘集中样本遗忘难度差异大，导致异步遗忘，影响遗忘质量与模型效用。
- 方法要点：将遗忘建模为min-sup过程，内层识别最坏数据分布强调难遗忘样本，外层更新模型参数。
- 实验或效果：在TOFU和MUSE数据集上，BalDRO显著提升遗忘质量和模型效用，优于现有方法。

## 摘要（原文）

> As Large Language Models (LLMs) increasingly shape online content, removing targeted information from well-trained LLMs (also known as LLM unlearning) has become critical for web governance. A key challenge lies in sample-wise imbalance within the forget set: different samples exhibit widely varying unlearning difficulty, leading to asynchronous forgetting where some knowledge remains insufficiently erased while others become over-forgotten. To address this, we propose BalDRO, a novel and efficient framework for balanced LLM unlearning. BalDRO formulates unlearning as a min-sup process: an inner step identifies a worst-case data distribution that emphasizes hard-to-unlearn samples, while an outer step updates model parameters under this distribution. We instantiate BalDRO via two efficient variants: BalDRO-G, a discrete GroupDRO-based approximation focusing on high-loss subsets, and BalDRO-DV, a continuous Donsker-Varadhan dual method enabling smooth adaptive weighting within standard training pipelines. Experiments on TOFU and MUSE show that BalDRO significantly improves both forgetting quality and model utility over existing methods, and we release code for reproducibility.

