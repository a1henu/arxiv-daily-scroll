---
layout: default
title: Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning
---

# Correct, Concise and Complete: Multi-stage Training For Adaptive Reasoning
**arXiv**：[2601.02972v1](https://arxiv.org/abs/2601.02972) · [PDF](https://arxiv.org/pdf/2601.02972.pdf)  
**作者**：Nathanaël Carraz Rakotonirina, Ren Pang, Neha Anna John, Michael Bohlke-Schneider, Momchil Hardalov  

**一句话要点**：提出多阶段高效推理方法，通过监督微调与强化学习减少大语言模型过思考问题。

**关键词**：大语言模型推理, 链式思维优化, 多阶段训练, 自适应长度惩罚, 强化学习微调, 过思考调整

## 3 点简述
- 核心问题：链式思维推理常导致过思考，增加计算成本且可能降低准确性。
- 方法要点：结合监督微调（如拒绝采样或推理轨迹重构）与带自适应长度惩罚的强化学习。
- 实验效果：在七项推理任务中，平均减少响应长度28%-40%，性能仅轻微下降1.6-2.5点。

## 摘要（原文）

> The reasoning capabilities of large language models (LLMs) have improved substantially through increased test-time computation, typically in the form of intermediate tokens known as chain-of-thought (CoT). However, CoT often becomes unnecessarily long, increasing computation cost without actual accuracy gains or sometimes even degrading performance, a phenomenon known as ``overthinking''. We propose a multi-stage efficient reasoning method that combines supervised fine-tuning -- via rejection sampling or reasoning trace reformatting -- with reinforcement learning using an adaptive length penalty. We introduce a lightweight reward function that penalizes tokens generated after the first correct answer but encouraging self-verification only when beneficial. We conduct a holistic evaluation across seven diverse reasoning tasks, analyzing the accuracy--response length trade-off. Our approach reduces response length by an average of 28\% for 8B models and 40\% for 32B models, while incurring only minor performance drops of 1.6 and 2.5 points, respectively. Despite its conceptual simplicity, it achieves a superior trade-off compared to more complex state-of-the-art efficient reasoning methods, scoring 76.6, in terms of the area under the Overthinking-Adjusted Accuracy curve ($\text{AUC}_{\text{OAA}}$) -- 5 points above the base model and 2.5 points above the second-best approach.

