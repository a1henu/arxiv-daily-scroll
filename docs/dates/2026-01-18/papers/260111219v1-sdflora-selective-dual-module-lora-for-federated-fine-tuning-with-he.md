---
layout: default
title: SDFLoRA: Selective Dual-Module LoRA for Federated Fine-tuning with Heterogeneous Clients
---

# SDFLoRA: Selective Dual-Module LoRA for Federated Fine-tuning with Heterogeneous Clients
**arXiv**：[2601.11219v1](https://arxiv.org/abs/2601.11219) · [PDF](https://arxiv.org/pdf/2601.11219.pdf)  
**作者**：Zhikang Shen, Jianrong Lu, Haiyuan Wan, Jianhai Chen  

**一句话要点**：提出SDFLoRA以解决联邦学习中异构客户端LoRA聚合的偏差与隐私问题

**关键词**：联邦学习, LoRA, 异构客户端, 差分隐私, 参数高效微调, 大语言模型

## 3 点简述
- 核心问题：联邦学习中客户端LoRA配置异构导致聚合偏差，现有方法限制个性化且隐私保护弱
- 方法要点：将客户端适配器分解为全局模块（可聚合）和本地模块（私有），选择性对齐全局模块
- 实验或效果：在GLUE基准上优于基线，实现更好的效用-隐私权衡

## 摘要（原文）

> Federated learning (FL) for large language models (LLMs) has attracted increasing attention as a way to enable privacy-preserving adaptation over distributed data. Parameter-efficient methods such as LoRA are widely adopted to reduce communication and memory costs. Despite these advances, practical FL deployments often exhibit rank heterogeneity, since different clients may use different low-rank configurations. This makes direct aggregation of LoRA updates biased and unstable. Existing solutions typically enforce unified ranks or align heterogeneous updates into a shared subspace, which over-constrains client-specific semantics, limits personalization, and provides weak protection of local client information under differential privacy noise. To address this issue, we propose Selective Dual-module Federated LoRA (SDFLoRA), which decomposes each client adapter into a global module that captures transferable knowledge and a local module that preserves client-specific adaptations. The global module is selectively aligned and aggregated across clients, while local modules remain private. This design enables robust learning under rank heterogeneity and supports privacy-aware optimization by injecting differential privacy noise exclusively into the global module. Experiments on GLUE benchmarks demonstrate that SDFLoRA outperforms representative federated LoRA baselines and achieves a better utility-privacy trade-off.

