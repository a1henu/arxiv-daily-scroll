---
layout: default
title: DA-DPO: Cost-efficient Difficulty-aware Preference Optimization for Reducing MLLM Hallucinations
---

# DA-DPO: Cost-efficient Difficulty-aware Preference Optimization for Reducing MLLM Hallucinations
**arXiv**：[2601.00623v1](https://arxiv.org/abs/2601.00623) · [PDF](https://arxiv.org/pdf/2601.00623.pdf)  
**作者**：Longtian Qiu, Shan Ning, Chuyu Zhang, Jiaxuan Sun, Xuming He  

**一句话要点**：提出DA-DPO以解决多模态大语言模型偏好优化中的难度不平衡问题

**关键词**：多模态大语言模型, 偏好优化, 幻觉抑制, 难度感知, 直接偏好优化, 计算效率

## 3 点简述
- 核心问题：现有多模态DPO方法因偏好数据难度不平衡导致过拟合，阻碍细粒度幻觉抑制。
- 方法要点：DA-DPO通过无额外训练的难度估计和基于难度的训练重加权，平衡学习过程。
- 实验或效果：实验表明DA-DPO提升多模态偏好优化，增强幻觉鲁棒性和泛化能力，保持计算高效。

## 摘要（原文）

> Direct Preference Optimization (DPO) has shown strong potential for mitigating hallucinations in Multimodal Large Language Models (MLLMs). However, existing multimodal DPO approaches often suffer from overfitting due to the difficulty imbalance in preference data. Our analysis shows that MLLMs tend to overemphasize easily distinguishable preference pairs, which hinders fine-grained hallucination suppression and degrades overall performance. To address this issue, we propose Difficulty-Aware Direct Preference Optimization (DA-DPO), a cost-effective framework designed to balance the learning process. DA-DPO consists of two main components: (1) Difficulty Estimation leverages pre-trained vision--language models with complementary generative and contrastive objectives, whose outputs are integrated via a distribution-aware voting strategy to produce robust difficulty scores without additional training; and (2) Difficulty-Aware Training reweights preference pairs based on their estimated difficulty, down-weighting easy samples while emphasizing harder ones to alleviate overfitting. This framework enables more effective preference optimization by prioritizing challenging examples, without requiring new data or extra fine-tuning stages. Extensive experiments demonstrate that DA-DPO consistently improves multimodal preference optimization, yielding stronger robustness to hallucinations and better generalization across standard benchmarks, while remaining computationally efficient. The project page is available at https://artanic30.github.io/project_pages/DA-DPO/.

