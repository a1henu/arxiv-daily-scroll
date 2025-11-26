---
layout: default
title: Directional Optimization Asymmetry in Transformers: A Synthetic Stress Test
---

# Directional Optimization Asymmetry in Transformers: A Synthetic Stress Test
**arXiv**：[2511.19997v1](https://arxiv.org/abs/2511.19997) · [PDF](https://arxiv.org/pdf/2511.19997.pdf)  
**作者**：Mihir Sahasrabudhe  

**一句话要点**：提出合成基准以揭示Transformer在方向优化中的内在不对称性

**关键词**：Transformer架构, 方向优化, 合成基准, 熵控制, 因果训练, 模型偏差

## 3 点简述
- 核心问题：Transformer架构是否本身存在方向学习偏差，而非仅源于语言统计
- 方法要点：使用可控熵的随机字符串映射构建正向和逆向任务进行压力测试
- 实验或效果：GPT-2模型在逆向任务中损失显著高于理论下限，显示方向优化差距

## 摘要（原文）

> Transformers are theoretically reversal-invariant: their function class does not prefer left-to-right over right-to-left mappings. Yet empirical studies on natural language repeatedly report a "reversal curse," and recent work on temporal asymmetry in LLMs suggests that real-world corpora carry their own arrow of time. This leaves an unresolved question: do directional failures stem from linguistic statistics, or from the architecture itself? We cut through this ambiguity with a fully synthetic, entropy-controlled benchmark designed as a clean-room stress test for directional learning. Using random string mappings with tunable branching factor K, we construct forward tasks with zero conditional entropy and inverse tasks with analytically determined entropy floors. Excess loss above these floors reveals that even scratch-trained GPT-2 models exhibit a strong, reproducible directional optimization gap (e.g., 1.16 nats at K=5), far larger than that of an MLP trained on the same data. Pre-trained initializations shift optimization behavior but do not eliminate this gap, while LoRA encounters a sharp capacity wall on high-entropy inverse mappings. Together, these results isolate a minimal, semantics-free signature of directional friction intrinsic to causal Transformer training-one that persists even when linguistic priors, token frequencies, and corpus-level temporal asymmetries are removed. Our benchmark provides a controlled instrument for dissecting directional biases in modern sequence models and motivates deeper mechanistic study of why inversion remains fundamentally harder for Transformers.

