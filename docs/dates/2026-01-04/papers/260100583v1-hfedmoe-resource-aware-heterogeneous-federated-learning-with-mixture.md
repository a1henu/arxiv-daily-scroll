---
layout: default
title: HFedMoE: Resource-aware Heterogeneous Federated Learning with Mixture-of-Experts
---

# HFedMoE: Resource-aware Heterogeneous Federated Learning with Mixture-of-Experts
**arXiv**：[2601.00583v1](https://arxiv.org/abs/2601.00583) · [PDF](https://arxiv.org/pdf/2601.00583.pdf)  
**作者**：Zihan Fang, Zheng Lin, Senkang Hu, Yanan Ma, Yihang Tao, Yiqin Deng, Xianhao Chen, Yuguang Fang  

**一句话要点**：提出HFedMoE以解决异构联邦学习中MoE模型在资源受限设备上的高效微调问题

**关键词**：异构联邦学习, 混合专家模型, 资源感知优化, 大语言模型微调, 稀疏模型聚合

## 3 点简述
- 核心问题：MoE模型在异构联邦学习中面临专家选择困难、资源异构性干扰和全局聚合不一致的挑战
- 方法要点：基于专家重要性评估和资源感知的自适应专家子集选择，结合稀疏感知的模型聚合策略
- 实验或效果：在训练准确性和收敛速度上优于现有基准，验证了框架的有效性

## 摘要（原文）

> While federated learning (FL) enables fine-tuning of large language models (LLMs) without compromising data privacy, the substantial size of an LLM renders on-device training impractical for resource-constrained clients, such as mobile devices. Thus, Mixture-of-Experts (MoE) models have emerged as a computation-efficient solution, which activates only a sparse subset of experts during model training to reduce computing burden without sacrificing performance. Though integrating MoE into FL fine-tuning holds significant potential, it still encounters three key challenges: i) selecting appropriate experts for clients remains challenging due to the lack of a reliable metric to measure each expert's impact on local fine-tuning performance, ii) the heterogeneous computing resources across clients severely hinder MoE-based LLM fine-tuning, as dynamic expert activations across diverse input samples can overwhelm resource-constrained devices, and iii) client-specific expert subsets and routing preference undermine global aggregation, where misaligned expert updates and inconsistent gating networks in troduce destructive interference. To address these challenges, we propose HFedMoE, a heterogeneous MoE-based FL fine-tuning framework that customizes a subset of experts to each client for computation-efficient LLM fine-tuning. Specifically, HFedMoE identifies the expert importance based on its contributions to fine-tuning performance, and then adaptively selects a subset of experts from an information bottleneck perspective to align with each client' s computing budget. A sparsity-aware model aggregation strategy is also designed to aggregate the actively fine-tuned experts and gating parameters with importance weighted contributions. Extensive experiments demonstrate that HFedMoE outperforms state-of-the-art benchmarks in training accuracy and convergence speed.

