---
layout: default
title: Understanding Degradation with Vision Language Model
---

# Understanding Degradation with Vision Language Model
**arXiv**：[2602.04565v1](https://arxiv.org/abs/2602.04565) · [PDF](https://arxiv.org/pdf/2602.04565.pdf)  
**作者**：Guanzhou Lan, Chenyi Liao, Yuqi Yang, Qianli Ma, Zhigang Wang, Dong Wang, Bin Zhao, Xuelong Li  

**一句话要点**：提出DU-VLM以解决视觉退化理解问题，通过层次化结构化预测统一参数估计，并实现零样本图像恢复。

**关键词**：视觉退化理解, 层次化结构化预测, 视觉语言模型, 零样本图像恢复, 强化学习, DU-110k数据集

## 3 点简述
- 核心问题：视觉语言模型在理解图像退化的物理参数方面存在不足，需同时估计退化类型、参数键和连续值。
- 方法要点：将退化理解定义为层次化结构化预测任务，基于自回归下一个令牌预测范式，结合监督微调和强化学习训练DU-VLM。
- 实验或效果：在DU-110k数据集上验证，DU-VLM在准确性和鲁棒性上显著优于基线，并能零样本控制扩散模型进行图像恢复。

## 摘要（原文）

> Understanding visual degradations is a critical yet challenging problem in computer vision. While recent Vision-Language Models (VLMs) excel at qualitative description, they often fall short in understanding the parametric physics underlying image degradations. In this work, we redefine degradation understanding as a hierarchical structured prediction task, necessitating the concurrent estimation of degradation types, parameter keys, and their continuous physical values. Although these sub-tasks operate in disparate spaces, we prove that they can be unified under one autoregressive next-token prediction paradigm, whose error is bounded by the value-space quantization grid. Building on this insight, we introduce DU-VLM, a multimodal chain-of-thought model trained with supervised fine-tuning and reinforcement learning using structured rewards. Furthermore, we show that DU-VLM can serve as a zero-shot controller for pre-trained diffusion models, enabling high-fidelity image restoration without fine-tuning the generative backbone. We also introduce \textbf{DU-110k}, a large-scale dataset comprising 110,000 clean-degraded pairs with grounded physical annotations. Extensive experiments demonstrate that our approach significantly outperforms generalist baselines in both accuracy and robustness, exhibiting generalization to unseen distributions.

