---
layout: default
title: K-Sort Eval: Efficient Preference Evaluation for Visual Generation via Corrected VLM-as-a-Judge
---

# K-Sort Eval: Efficient Preference Evaluation for Visual Generation via Corrected VLM-as-a-Judge
**arXiv**：[2602.09411v1](https://arxiv.org/abs/2602.09411) · [PDF](https://arxiv.org/pdf/2602.09411.pdf)  
**作者**：Zhikai Li, Jiatong Li, Xuewen Liu, Wangbo Zhao, Pan Du, Kaicheng Zhou, Qingyi Gu, Yang You, Zhen Dong, Kurt Keutzer  

**一句话要点**：提出K-Sort Eval框架，通过后验校正和动态匹配实现高效可靠的视觉生成模型偏好评估

**关键词**：视觉生成模型评估, 偏好评估, 后验校正, 动态匹配, VLM-as-a-Judge

## 3 点简述
- 核心问题：视觉生成模型评估依赖耗时耗力的人类投票，而基于VLM的替代方法存在幻觉和偏见，且静态评估效率低
- 方法要点：利用人类投票数据集，结合后验校正提升VLM与人类偏好对齐，并采用动态匹配策略优化比较效率
- 实验或效果：实验显示K-Sort Eval与K-Sort Arena结果一致，通常需少于90次模型运行，验证了其高效性和可靠性

## 摘要（原文）

> The rapid development of visual generative models raises the need for more scalable and human-aligned evaluation methods. While the crowdsourced Arena platforms offer human preference assessments by collecting human votes, they are costly and time-consuming, inherently limiting their scalability. Leveraging vision-language model (VLMs) as substitutes for manual judgments presents a promising solution. However, the inherent hallucinations and biases of VLMs hinder alignment with human preferences, thus compromising evaluation reliability. Additionally, the static evaluation approach lead to low efficiency. In this paper, we propose K-Sort Eval, a reliable and efficient VLM-based evaluation framework that integrates posterior correction and dynamic matching. Specifically, we curate a high-quality dataset from thousands of human votes in K-Sort Arena, with each instance containing the outputs and rankings of K models. When evaluating a new model, it undergoes (K+1)-wise free-for-all comparisons with existing models, and the VLM provide the rankings. To enhance alignment and reliability, we propose a posterior correction method, which adaptively corrects the posterior probability in Bayesian updating based on the consistency between the VLM prediction and human supervision. Moreover, we propose a dynamic matching strategy, which balances uncertainty and diversity to maximize the expected benefit of each comparison, thus ensuring more efficient evaluation. Extensive experiments show that K-Sort Eval delivers evaluation results consistent with K-Sort Arena, typically requiring fewer than 90 model runs, demonstrating both its efficiency and reliability.

