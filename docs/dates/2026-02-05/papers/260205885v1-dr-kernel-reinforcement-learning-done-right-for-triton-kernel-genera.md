---
layout: default
title: Dr. Kernel: Reinforcement Learning Done Right for Triton Kernel Generations
---

# Dr. Kernel: Reinforcement Learning Done Right for Triton Kernel Generations
**arXiv**：[2602.05885v1](https://arxiv.org/abs/2602.05885) · [PDF](https://arxiv.org/pdf/2602.05885.pdf)  
**作者**：Wei Liu, Jiawei Xu, Yingru Li, Longtao Zheng, Tianjian Li, Qian Liu, Junxian He  

**一句话要点**：提出TRLOO和Profiling-based Rewards以解决强化学习在Triton内核生成中的奖励黑客和懒惰优化问题。

**关键词**：强化学习, 内核生成, 奖励黑客, 多轮交互, 性能优化, Triton

## 3 点简述
- 核心问题：强化学习训练内核生成模型易受奖励黑客和懒惰优化影响，导致模型追求表面正确性而非实际加速。
- 方法要点：设计KernelGYM环境，提出TRLOO进行无偏优势估计，并引入Profiling-based Rewards和Rejection Sampling提升训练稳定性。
- 实验或效果：Dr.Kernel-14B在KernelBench上性能优于Claude-4.5-Sonnet和GPT-5，生成内核加速率最高达47.8%。

## 摘要（原文）

> High-quality kernel is critical for scalable AI systems, and enabling LLMs to generate such code would advance AI development. However, training LLMs for this task requires sufficient data, a robust environment, and the process is often vulnerable to reward hacking and lazy optimization. In these cases, models may hack training rewards and prioritize trivial correctness over meaningful speedup. In this paper, we systematically study reinforcement learning (RL) for kernel generation. We first design KernelGYM, a robust distributed GPU environment that supports reward hacking check, data collection from multi-turn interactions and long-term RL training. Building on KernelGYM, we investigate effective multi-turn RL methods and identify a biased policy gradient issue caused by self-inclusion in GRPO. To solve this, we propose Turn-level Reinforce-Leave-One-Out (TRLOO) to provide unbiased advantage estimation for multi-turn RL. To alleviate lazy optimization, we incorporate mismatch correction for training stability and introduce Profiling-based Rewards (PR) and Profiling-based Rejection Sampling (PRS) to overcome the issue. The trained model, Dr.Kernel-14B, reaches performance competitive with Claude-4.5-Sonnet in Kernelbench. Finally, we study sequential test-time scaling for Dr.Kernel-14B. On the KernelBench Level-2 subset, 31.6% of the generated kernels achieve at least a 1.2x speedup over the Torch reference, surpassing Claude-4.5-Sonnet (26.7%) and GPT-5 (28.6%). When selecting the best candidate across all turns, this 1.2x speedup rate further increases to 47.8%. All resources, including environment, training code, models, and dataset, are included in https://www.github.com/hkust-nlp/KernelGYM.

