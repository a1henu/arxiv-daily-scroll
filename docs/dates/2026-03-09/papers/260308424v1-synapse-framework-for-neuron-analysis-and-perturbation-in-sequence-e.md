---
layout: default
title: SYNAPSE: Framework for Neuron Analysis and Perturbation in Sequence Encoding
---

# SYNAPSE: Framework for Neuron Analysis and Perturbation in Sequence Encoding
**arXiv**：[2603.08424v1](https://arxiv.org/abs/2603.08424) · [PDF](https://arxiv.org/pdf/2603.08424.pdf)  
**作者**：Jesús Sánchez Ochoa, Enrique Tomás Martínez Beltrán, Alberto Huertas Celdrán  

**一句话要点**：提出SYNAPSE框架，用于跨域Transformer模型的神经元分析与扰动测试

**关键词**：Transformer模型, 神经元分析, 可解释性, 鲁棒性测试, 跨域评估, 线性探针

## 3 点简述
- 核心问题：现有神经元级可解释性方法依赖任务或需重训练，缺乏系统化跨域评估工具
- 方法要点：提取层表示，训练线性探针进行神经元排序，通过前向钩子干预进行推理时扰动
- 实验或效果：揭示内部表示的冗余稳定性和类间不对称性，指导模型鲁棒性开发

## 摘要（原文）

> In recent years, Artificial Intelligence has become a powerful partner for complex tasks such as data analysis, prediction, and problem-solving, yet its lack of transparency raises concerns about its reliability. In sensitive domains such as healthcare or cybersecurity, ensuring transparency, trustworthiness, and robustness is essential, since the consequences of wrong decisions or successful attacks can be severe. Prior neuron-level interpretability approaches are primarily descriptive, task-dependent, or require retraining, which limits their use as systematic, reusable tools for evaluating internal robustness across architectures and domains. To overcome these limitations, this work proposes SYNAPSE, a systematic, training-free framework for understanding and stress-testing the internal behavior of Transformer models across domains. It extracts per-layer [CLS] representations, trains a lightweight linear probe to obtain global and per-class neuron rankings, and applies forward-hook interventions during inference. This design enables controlled experiments on internal representations without altering the original model, thereby allowing weaknesses, stability patterns, and label-specific sensitivities to be measured and compared directly across tasks and architectures. Across all experiments, SYNAPSE reveals a consistent, domain-independent organization of internal representations, in which task-relevant information is encoded in broad, overlapping neuron subsets. This redundancy provides a strong degree of functional stability, while class-wise asymmetries expose heterogeneous specialization patterns and enable label-aware analysis. In contrast, small structured manipulations in weight or logit space are sufficient to redirect predictions, highlighting complementary vulnerability profiles and illustrating how SYNAPSE can guide the development of more robust Transformer models.

