---
layout: default
title: From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty
---

# From Entropy to Calibrated Uncertainty: Training Language Models to Reason About Uncertainty
**arXiv**：[2603.06317v1](https://arxiv.org/abs/2603.06317) · [PDF](https://arxiv.org/pdf/2603.06317.pdf)  
**作者**：Azza Jenane, Nassim Walha, Lukas Kuhn, Florian Buettner  

**一句话要点**：提出三阶段后训练流程，使大语言模型高效推断校准的不确定性估计

**关键词**：不确定性校准, 大语言模型后训练, 强化学习对齐, 熵基不确定性, Platt缩放, 可解释不确定性

## 3 点简述
- 核心问题：大语言模型在关键领域需表达可解释且校准的不确定性，但现有后处理方法计算成本高或缺乏校准。
- 方法要点：通过基于熵的细粒度不确定性评分、Platt缩放校准和强化学习后训练，对齐模型策略与校准信号。
- 实验或效果：实验显示模型校准优于基线，无需额外处理即可泛化到未见任务，学习到稳健的不确定性推理行为。

## 摘要（原文）

> Large Language Models (LLMs) that can express interpretable and calibrated uncertainty are crucial in high-stakes domains. While methods to compute uncertainty post-hoc exist, they are often sampling-based and therefore computationally expensive or lack calibration. We propose a three-stage pipeline to post-train LLMs to efficiently infer calibrated uncertainty estimates for their responses. First, we compute fine-grained entropy-based uncertainty scores on the training data, capturing the distributional variability of model outputs in embedding space. Second, these scores are calibrated via Platt scaling, producing reliable and human-interpretable uncertainty signals. Finally, the target LLM is post-trained via reinforcement learning to align its policy with these calibrated signals through a verifiable reward function. Unlike post-hoc uncertainty estimation methods, our approach provides interpretable and computationally efficient uncertainty estimates at test time. Experiments show that models trained with our pipeline achieve better calibration than baselines and generalize to unseen tasks without further processing, suggesting that they learn a robust uncertainty reasoning behavior.

