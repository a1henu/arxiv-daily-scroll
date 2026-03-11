---
layout: default
title: TubeMLLM: A Foundation Model for Topology Knowledge Exploration in Vessel-like Anatomy
---

# TubeMLLM: A Foundation Model for Topology Knowledge Exploration in Vessel-like Anatomy
**arXiv**：[2603.09217v1](https://arxiv.org/abs/2603.09217) · [PDF](https://arxiv.org/pdf/2603.09217.pdf)  
**作者**：Yaoyu Liu, Minghui Zhang, Xin You, Hanxiao Zhang, Yun Gu  

**一句话要点**：提出TubeMLLM基础模型，通过拓扑先验与可控生成解决医学管状解剖建模中的拓扑不一致问题。

**关键词**：医学管状解剖建模, 拓扑感知, 多模态大语言模型, 零样本泛化, 可控生成, 跨模态迁移

## 3 点简述
- 核心问题：医学管状解剖建模因复杂拓扑和数据集偏移导致拓扑不一致，如虚假断开或合并。
- 方法要点：集成拓扑先验于多模态大语言模型，通过自然语言提示和共享注意力架构增强拓扑感知。
- 实验或效果：在十五个数据集上实现最优分布外性能，显著降低拓扑误差，并展示零样本跨模态迁移能力。

## 摘要（原文）

> Modeling medical vessel-like anatomy is challenging due to its intricate topology and sensitivity to dataset shifts. Consequently, task-specific models often suffer from topological inconsistencies, including artificial disconnections and spurious merges. Motivated by the promise of multimodal large language models (MLLMs) for zero-shot generalization, we propose TubeMLLM, a unified foundation model that couples structured understanding with controllable generation for medical vessel-like anatomy. By integrating topological priors through explicit natural language prompting and aligning them with visual representations in a shared-attention architecture, TubeMLLM significantly enhances topology-aware perception. Furthermore, we construct TubeMData, a pionner multimodal benchmark comprising comprehensive topology-centric tasks, and introduce an adaptive loss weighting strategy to emphasize topology-critical regions during training. Extensive experiments on fifteen diverse datasets demonstrate our superiority. Quantitatively, TubeMLLM achieves state-of-the-art out-of-distribution performance, substantially reducing global topological discrepancies on color fundus photography (decreasing the $β_{0}$ number error from 37.42 to 8.58 compared to baselines). Notably, TubeMLLM exhibits exceptional zero-shot cross-modality transferring ability on unseen X-ray angiography, achieving a Dice score of 67.50% while significantly reducing the $β_{0}$ error to 1.21. TubeMLLM also maintains robustness against degradations such as blur, noise, and low resolution. Furthermore, in topology-aware understanding tasks, the model achieves 97.38% accuracy in evaluating mask topological quality, significantly outperforming standard vision-language baselines.

