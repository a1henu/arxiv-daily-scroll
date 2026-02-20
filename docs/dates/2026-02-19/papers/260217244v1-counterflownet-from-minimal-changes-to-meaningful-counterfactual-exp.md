---
layout: default
title: CounterFlowNet: From Minimal Changes to Meaningful Counterfactual Explanations
---

# CounterFlowNet: From Minimal Changes to Meaningful Counterfactual Explanations
**arXiv**：[2602.17244v1](https://arxiv.org/abs/2602.17244) · [PDF](https://arxiv.org/pdf/2602.17244.pdf)  
**作者**：Oleksii Furman, Patryk Marszałek, Jan Masłowski, Piotr Gaiński, Maciej Zięba, Marek Śmieja  

**一句话要点**：提出CounterFlowNet以生成满足约束的高质量反事实解释，适用于异构表格数据。

**关键词**：反事实解释, 生成流网络, 表格数据, 可解释人工智能, 序列生成

## 3 点简述
- 现有方法难以生成多高质量反事实解释，需满足稀疏性、异构特征和用户约束。
- 使用条件生成流网络将反事实生成建模为序列特征修改，通过奖励函数编码关键需求。
- 在八个数据集上实验显示，该方法在有效性、稀疏性、合理性和多样性间取得优越权衡。

## 摘要（原文）

> Counterfactual explanations (CFs) provide human-interpretable insights into model's predictions by identifying minimal changes to input features that would alter the model's output. However, existing methods struggle to generate multiple high-quality explanations that (1) affect only a small portion of the features, (2) can be applied to tabular data with heterogeneous features, and (3) are consistent with the user-defined constraints. We propose CounterFlowNet, a generative approach that formulates CF generation as sequential feature modification using conditional Generative Flow Networks (GFlowNet). CounterFlowNet is trained to sample CFs proportionally to a user-specified reward function that can encode key CF desiderata: validity, sparsity, proximity and plausibility, encouraging high-quality explanations. The sequential formulation yields highly sparse edits, while a unified action space seamlessly supports continuous and categorical features. Moreover, actionability constraints, such as immutability and monotonicity of features, can be enforced at inference time via action masking, without retraining. Experiments on eight datasets under two evaluation protocols demonstrate that CounterFlowNet achieves superior trade-offs between validity, sparsity, plausibility, and diversity with full satisfaction of the given constraints.

