---
layout: default
title: Tiny Recursive Reasoning with Mamba-2 Attention Hybrid
---

# Tiny Recursive Reasoning with Mamba-2 Attention Hybrid
**arXiv**：[2602.12078v1](https://arxiv.org/abs/2602.12078) · [PDF](https://arxiv.org/pdf/2602.12078.pdf)  
**作者**：Wenlong Wang, Fergal Reid  

**一句话要点**：提出Mamba-2混合算子以增强递归推理模型的候选覆盖能力

**关键词**：递归推理, Mamba-2, 状态空间模型, 抽象推理, 参数效率

## 3 点简述
- 核心问题：Mamba-2状态空间循环是否适合作为递归推理的算子，并保持推理能力
- 方法要点：在TRM中用Mamba-2混合算子替换Transformer块，保持参数规模相近
- 实验或效果：在ARC-AGI-1上，pass@2提升2.0%，高K值表现更优，验证推理能力保留

## 摘要（原文）

> Recent work on recursive reasoning models like TRM demonstrates that tiny networks (7M parameters) can achieve strong performance on abstract reasoning tasks through latent recursion -- iterative refinement in hidden representation space without emitting intermediate tokens. This raises a natural question about operator choice: Mamba-2's state space recurrence is itself a form of iterative refinement, making it a natural candidate for recursive reasoning -- but does introducing Mamba-2 into the recursive scaffold preserve reasoning capability? We investigate this by replacing the Transformer blocks in TRM with Mamba-2 hybrid operators while maintaining parameter parity (6.83M vs 6.86M parameters). On ARC-AGI-1, we find that the hybrid improves pass@2 (the official metric) by +2.0\% (45.88\% vs 43.88\%) and consistently outperforms at higher K values (+4.75\% at pass@100), whilst maintaining pass@1 parity. This suggests improved candidate coverage -- the model generates correct solutions more reliably -- with similar top-1 selection. Our results validate that Mamba-2 hybrid operators preserve reasoning capability within the recursive scaffold, establishing SSM-based operators as viable candidates in the recursive operator design space and taking a first step towards understanding the best mixing strategies for recursive reasoning.

