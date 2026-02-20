---
layout: default
title: MeGU: Machine-Guided Unlearning with Target Feature Disentanglement
---

# MeGU: Machine-Guided Unlearning with Target Feature Disentanglement
**arXiv**：[2602.17088v1](https://arxiv.org/abs/2602.17088) · [PDF](https://arxiv.org/pdf/2602.17088.pdf)  
**作者**：Haoyu Wang, Zhuo Huang, Xiaolong Wang, Bo Han, Zhiwei Lin, Tongliang Liu  

**一句话要点**：提出MeGU框架，通过概念感知重对齐解决机器遗忘中的目标特征纠缠问题

**关键词**：机器遗忘, 特征解耦, 多模态大语言模型, 概念重对齐, 隐私保护

## 3 点简述
- 核心问题：现有遗忘方法在目标数据影响擦除与保留数据效用间存在权衡，特征纠缠限制有效性
- 方法要点：利用多模态大语言模型指导重对齐方向，引入正负特征噪声对显式解耦目标概念影响
- 实验或效果：实现可控选择性遗忘，有效缓解欠遗忘和过遗忘，提升遗忘效率与模型性能

## 摘要（原文）

> The growing concern over training data privacy has elevated the "Right to be Forgotten" into a critical requirement, thereby raising the demand for effective Machine Unlearning. However, existing unlearning approaches commonly suffer from a fundamental trade-off: aggressively erasing the influence of target data often degrades model utility on retained data, while conservative strategies leave residual target information intact. In this work, the intrinsic representation properties learned during model pretraining are analyzed. It is demonstrated that semantic class concepts are entangled at the feature-pattern level, sharing associated features while preserving concept-specific discriminative components. This entanglement fundamentally limits the effectiveness of existing unlearning paradigms. Motivated by this insight, we propose Machine-Guided Unlearning (MeGU), a novel framework that guides unlearning through concept-aware re-alignment. Specifically, Multi-modal Large Language Models (MLLMs) are leveraged to explicitly determine re-alignment directions for target samples by assigning semantically meaningful perturbing labels. To improve efficiency, inter-class conceptual similarities estimated by the MLLM are encoded into a lightweight transition matrix. Furthermore, MeGU introduces a positive-negative feature noise pair to explicitly disentangle target concept influence. During finetuning, the negative noise suppresses target-specific feature patterns, while the positive noise reinforces remaining associated features and aligns them with perturbing concepts. This coordinated design enables selective disruption of target-specific representations while preserving shared semantic structures. As a result, MeGU enables controlled and selective forgetting, effectively mitigating both under-unlearning and over-unlearning.

