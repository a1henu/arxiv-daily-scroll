---
layout: default
title: Stabilized Fine-Tuning with LoRA in Federated Learning: Mitigating the Side Effect of Client Size and Rank via the Scaling Factor
---

# Stabilized Fine-Tuning with LoRA in Federated Learning: Mitigating the Side Effect of Client Size and Rank via the Scaling Factor
**arXiv**：[2603.08058v1](https://arxiv.org/abs/2603.08058) · [PDF](https://arxiv.org/pdf/2603.08058.pdf)  
**作者**：Jiayu Huang, Xiaohu Wu, Tiantian He, Qicheng Lao  

**一句话要点**：提出SFed-LoRA框架，通过优化缩放因子解决联邦学习中LoRA高秩适配器聚合不稳定的问题。

**关键词**：联邦学习, 低秩适配, 参数高效微调, 缩放因子优化, 大语言模型, 分布式训练

## 3 点简述
- 核心问题：联邦学习中聚合多客户端LoRA更新时，统计方差随客户端数增加，导致高秩适配器梯度崩溃。
- 方法要点：理论分析适配器秩与联邦聚合的交互，推导最优缩放因子以减轻聚合误差，不改变模型架构或推理延迟。
- 实验或效果：在多样化任务和异构数据上验证，SFed-LoRA防止高秩崩溃，提升稳定性和收敛速度优于基线。

## 摘要（原文）

> Large Language Models (LLMs) are pivotal in natural language processing. The impracticality of full fine-tuning has prompted Parameter-Efficient Fine-Tuning (PEFT) methods like Low-Rank Adaptation (LoRA), optimizing low-rank matrices A and B. In distributed scenarios where privacy constraints necessitate Federated Learning (FL), however, the integration of LoRA is often unstable. Specifically, we identify that aggregating updates from multiple clients introduces statistical variance that scales with the client count, causing gradient collapse when using high-rank adapters. Existing scaling factor candidates, such as the one used by Rank-Stabilized LoRA, ignore the interaction caused by the aggregation process. To bridge this gap, this paper introduces Stabilized Federated LoRA (SFed-LoRA), a framework that theoretically characterizes the interaction between adapter rank and federated aggregation. We derive an optimal scaling factor designed to effectively mitigate the aggregation error accumulating across N clients. By correcting the scaling mismatch inherent in previous approaches, SFed-LoRA restores the efficacy of high-rank adaptation without altering the original model architecture or increasing inference latency. Extensive experiments in diverse tasks, model architectures, and heterogeneous data distributions are conducted to validate our results. We demonstrate that SFed-LoRA prevents high-rank collapse, and achieves significantly improved stability and faster convergence compared with state-of-the-art baselines for high-rank adaptation.

