---
layout: default
title: Tool Verification for Test-Time Reinforcement Learning
---

# Tool Verification for Test-Time Reinforcement Learning
**arXiv**：[2603.02203v1](https://arxiv.org/abs/2603.02203) · [PDF](https://arxiv.org/pdf/2603.02203.pdf)  
**作者**：Ruotong Liao, Nikolai Röhrich, Xiaohan Wang, Yuhui Zhang, Yasaman Samadzadeh, Volker Tresp, Serena Yeung-Levy  

**一句话要点**：提出T^3RL工具验证方法，以解决测试时强化学习中伪共识导致的模式崩溃问题。

**关键词**：测试时强化学习, 工具验证, 伪标签生成, 模式崩溃, 在线适应, 大型推理模型

## 3 点简述
- 核心问题：测试时强化学习因未验证的高频伪共识产生偏差奖励，导致模式崩溃。
- 方法要点：引入工具验证，通过外部证据（如代码执行）在投票中加权已验证轨迹，提升伪标签可靠性。
- 实验或效果：在多种数学数据集和骨干模型上显著优于TTRL，尤其在难题上增益更大。

## 摘要（原文）

> Test-time reinforcement learning (TTRL) has emerged as a promising paradigm for self-evolving large reasoning models (LRMs), enabling online adaptation on unlabeled test inputs via self-induced rewards through majority voting. However, a spurious yet high-frequency unverified consensus can become a biased and reinforced reward signal, leading to incorrect mode collapse. We address this failure mode with T^3RL (Tool-Verification for Test-Time Reinforcement Learning), which introduces test-time tool verification into reward estimation. Concretely, a verifier uses an external tool as evidence (e.g., from code execution) to upweight verified rollouts in a verification-aware voting, producing more reliable pseudo-labels for training. Across various math difficulties (MATH-500, AMC, and AIME 2024) and diverse backbone types, T^3RL significantly improves over TTRL, with larger gains on harder problems. More broadly, T^3RL can be viewed as verified online data synthesis, highlighting test-time tool verification as a key mechanism for stabilizing self-evolution.

