---
layout: default
title: DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning
---

# DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning
**arXiv**：[2603.08095v1](https://arxiv.org/abs/2603.08095) · [PDF](https://arxiv.org/pdf/2603.08095.pdf)  
**作者**：Chi-Min Chan, Ehsan Hajiramezanali, Xiner Li, Edward De Brouwer, Carl Edwards, Wei Xue, Sirui Han, Yike Guo, Gabriele Scalia  

**一句话要点**：提出DC-W2S框架以解决生物推理中过程奖励模型训练依赖昂贵专家标注的问题

**关键词**：过程奖励建模, 弱监督学习, 生物推理, 数据可靠性分层, 课程学习, 噪声数据筛选

## 3 点简述
- 核心问题：过程奖励模型训练需专家验证的逐步标注，成本高昂，现有弱到强泛化理论缺乏从噪声数据选择高质量信号的指导
- 方法要点：通过自共识与邻域共识指标分层监督信号可靠性，采用课程学习和掩码策略指导训练
- 实验或效果：证明DC-W2S能在无大量专家标注下训练鲁棒过程奖励模型，策略性数据筛选优于大规模噪声数据训练

## 摘要（原文）

> In scientific reasoning tasks, the veracity of the reasoning process is as critical as the final outcome. While Process Reward Models (PRMs) offer a solution to the coarse-grained supervision problems inherent in Outcome Reward Models (ORMs), their deployment is hindered by the prohibitive cost of obtaining expert-verified step-wise labels. This paper addresses the challenge of training reliable PRMs using abundant but noisy "weak" supervision. We argue that existing Weak-to-Strong Generalization (W2SG) theories lack prescriptive guidelines for selecting high-quality training signals from noisy data. To bridge this gap, we introduce the Dual-Consensus Weak-to-Strong (DC-W2S) framework. By intersecting Self-Consensus (SC) metrics among weak supervisors with Neighborhood-Consensus (NC) metrics in the embedding space, we stratify supervision signals into distinct reliability regimes. We then employ a curriculum of instance-level balanced sampling and label-level reliability-aware masking to guide the training process. We demonstrate that DC-W2S enables the training of robust PRMs for complex reasoning without exhaustive expert annotation, proving that strategic data curation is more effective than indiscriminate training on large-scale noisy datasets.

