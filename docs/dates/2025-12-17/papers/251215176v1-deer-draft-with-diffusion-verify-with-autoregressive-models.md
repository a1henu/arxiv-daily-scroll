---
layout: default
title: DEER: Draft with Diffusion, Verify with Autoregressive Models
---

# DEER: Draft with Diffusion, Verify with Autoregressive Models
**arXiv**：[2512.15176v1](https://arxiv.org/abs/2512.15176) · [PDF](https://arxiv.org/pdf/2512.15176.pdf)  
**作者**：Zicong Cheng, Guo-Wei Yang, Jia Li, Zhijie Deng, Meng-Hao Guo, Shi-Min Hu  

**一句话要点**：提出DEER框架，使用扩散模型草拟与自回归模型验证，以提升大语言模型推理效率

**关键词**：推测解码, 扩散大语言模型, 自回归模型, 并行解码, 训练对齐, 效率优化

## 3 点简述
- 核心问题：自回归解码延迟限制LLM代理系统效率，现有推测解码依赖自回归草拟模型，导致信任崩溃和顺序解码，提速有限
- 方法要点：采用扩散大语言模型作为草拟器，通过并行解码和两阶段训练对齐目标模型，生成长草拟段
- 实验或效果：在HumanEval测试中，DEER实现5.54倍加速，草拟接受长度达32个词元，远超EAGLE-3的2.41倍加速和10个词元

## 摘要（原文）

> Efficiency, as a critical practical challenge for LLM-driven agentic and reasoning systems, is increasingly constrained by the inherent latency of autoregressive (AR) decoding. Speculative decoding mitigates this cost through a draft-verify scheme, yet existing approaches rely on AR draft models (a.k.a., drafters), which introduce two fundamental issues: (1) step-wise uncertainty accumulation leads to a progressive collapse of trust between the target model and the drafter, and (2) inherently sequential decoding of AR drafters. Together, these factors cause limited speedups. In this paper, we show that a diffusion large language model (dLLM) drafters can naturally overcome these issues through its fundamentally different probabilistic modeling and efficient parallel decoding strategy. Building on this insight, we introduce DEER, an efficient speculative decoding framework that drafts with diffusion and verifies with AR models. To enable high-quality drafting, DEER employs a two-stage training pipeline to align the dLLM-based drafters with the target AR model, and further adopts single-step decoding to generate long draft segments. Experiments show DEER reaches draft acceptance lengths of up to 32 tokens, far surpassing the 10 tokens achieved by EAGLE-3. Moreover, on HumanEval with Qwen3-30B-A3B, DEER attains a 5.54x speedup, while EAGLE-3 achieves only 2.41x. Code, model, demo, etc, will be available at https://czc726.github.io/DEER/

