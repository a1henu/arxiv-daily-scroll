---
layout: default
title: DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation
---

# DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation
**arXiv**：[2601.18492v1](https://arxiv.org/abs/2601.18492) · [PDF](https://arxiv.org/pdf/2601.18492.pdf)  
**作者**：Zijun Li, Shijie Li, Zhenxi Zhang, Bin Li, Shoujun Zhou  

**一句话要点**：提出DV-VLN框架，通过双验证机制提升基于大语言模型的视觉与语言导航可靠性

**关键词**：视觉与语言导航, 大语言模型, 双验证机制, 生成-验证范式, 可靠性提升, 参数高效适配

## 3 点简述
- 核心问题：LLM基导航代理依赖单次动作决策，易受噪声观察和推理错误影响，导致路径偏差和可靠性下降
- 方法要点：采用生成-验证范式，先适配LLaMA-2生成结构化导航思维链，再通过真伪验证和掩码实体验证双通道验证候选动作
- 实验或效果：在R2R、RxR和REVERIE数据集上验证，相比直接预测和采样基线，性能提升，在纯语言VLN代理中具有竞争力

## 摘要（原文）

> Vision-and-Language Navigation (VLN) requires an embodied agent to navigate in a complex 3D environment according to natural language instructions. Recent progress in large language models (LLMs) has enabled language-driven navigation with improved interpretability. However, most LLM-based agents still rely on single-shot action decisions, where the model must choose one option from noisy, textualized multi-perspective observations. Due to local mismatches and imperfect intermediate reasoning, such decisions can easily deviate from the correct path, leading to error accumulation and reduced reliability in unseen environments. In this paper, we propose DV-VLN, a new VLN framework that follows a generate-then-verify paradigm. DV-VLN first performs parameter-efficient in-domain adaptation of an open-source LLaMA-2 backbone to produce a structured navigational chain-of-thought, and then verifies candidate actions with two complementary channels: True-False Verification (TFV) and Masked-Entity Verification (MEV). DV-VLN selects actions by aggregating verification successes across multiple samples, yielding interpretable scores for reranking. Experiments on R2R, RxR (English subset), and REVERIE show that DV-VLN consistently improves over direct prediction and sampling-only baselines, achieving competitive performance among language-only VLN agents and promising results compared with several cross-modal systems.Code is available at https://github.com/PlumJun/DV-VLN.

