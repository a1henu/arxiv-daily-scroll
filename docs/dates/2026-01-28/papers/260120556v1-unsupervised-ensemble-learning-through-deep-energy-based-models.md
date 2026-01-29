---
layout: default
title: Unsupervised Ensemble Learning Through Deep Energy-based Models
---

# Unsupervised Ensemble Learning Through Deep Energy-based Models
**arXiv**：[2601.20556v1](https://arxiv.org/abs/2601.20556) · [PDF](https://arxiv.org/pdf/2601.20556.pdf)  
**作者**：Ariel Maymon, Yanir Buznah, Uri Shaham  

**一句话要点**：提出基于深度能量模型的元学习方法，以解决无监督集成学习中仅利用预测构建准确元学习器的问题。

**关键词**：无监督集成学习, 深度能量模型, 元学习, 条件独立性, 专家混合, 集体智能

## 3 点简述
- 核心问题：无监督集成学习需结合多个学习器预测，但缺乏真实标签或额外数据，评估个体性能困难。
- 方法要点：基于深度能量模型，仅用个体学习器预测构建元学习器，无需标签、特征或问题特定信息，理论保证条件独立时有效。
- 实验或效果：在标准集成数据集和定制数据集上表现优异，尤其在专家混合等挑战性场景中验证了模型融合多源专业知识的能力。

## 摘要（原文）

> Unsupervised ensemble learning emerged to address the challenge of combining multiple learners' predictions without access to ground truth labels or additional data. This paradigm is crucial in scenarios where evaluating individual classifier performance or understanding their strengths is challenging due to limited information. We propose a novel deep energy-based method for constructing an accurate meta-learner using only the predictions of individual learners, potentially capable of capturing complex dependence structures between them. Our approach requires no labeled data, learner features, or problem-specific information, and has theoretical guarantees for when learners are conditionally independent. We demonstrate superior performance across diverse ensemble scenarios, including challenging mixture of experts settings. Our experiments span standard ensemble datasets and curated datasets designed to test how the model fuses expertise from multiple sources. These results highlight the potential of unsupervised ensemble learning to harness collective intelligence, especially in data-scarce or privacy-sensitive environments.

