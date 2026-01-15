---
layout: default
title: RISER: Orchestrating Latent Reasoning Skills for Adaptive Activation Steering
---

# RISER: Orchestrating Latent Reasoning Skills for Adaptive Activation Steering
**arXiv**：[2601.09269v1](https://arxiv.org/abs/2601.09269) · [PDF](https://arxiv.org/pdf/2601.09269.pdf)  
**作者**：Wencheng Ye, Liang Peng, Xiaoyang Yuan, Yi Bin, Pengpeng Zeng, Hengyu Jin, Heng Tao Shen  

**一句话要点**：提出RISER框架，通过自适应激活引导解决LLM复杂推理中的动态适应问题。

**关键词**：激活引导, 推理增强, 强化学习, 参数高效, 自适应控制, 零样本学习

## 3 点简述
- 核心问题：现有激活引导方法采用静态干预，难以适应复杂推理的动态性。
- 方法要点：构建可重用推理向量库，使用轻量级路由器动态组合，通过强化学习优化。
- 实验或效果：在七个基准测试中，零样本准确率提升3.4-6.5%，token效率比CoT高2-3倍。

## 摘要（原文）

> Recent work on domain-specific reasoning with large language models (LLMs) often relies on training-intensive approaches that require parameter updates. While activation steering has emerged as a parameter efficient alternative, existing methods apply static, manual interventions that fail to adapt to the dynamic nature of complex reasoning. To address this limitation, we propose RISER (Router-based Intervention for Steerable Enhancement of Reasoning), a plug-and-play intervention framework that adaptively steers LLM reasoning in activation space. RISER constructs a library of reusable reasoning vectors and employs a lightweight Router to dynamically compose them for each input. The Router is optimized via reinforcement learning under task-level rewards, activating latent cognitive primitives in an emergent and compositional manner. Across seven diverse benchmarks, RISER yields 3.4-6.5% average zero-shot accuracy improvements over the base model while surpassing CoT-style reasoning with 2-3x higher token efficiency and robust accuracy gains. Further analysis shows that RISER autonomously combines multiple vectors into interpretable, precise control strategies, pointing toward more controllable and efficient LLM reasoning.

