---
layout: default
title: Evaluating Parameter Efficient Methods for RLVR
---

# Evaluating Parameter Efficient Methods for RLVR
**arXiv**：[2512.23165v1](https://arxiv.org/abs/2512.23165) · [PDF](https://arxiv.org/pdf/2512.23165.pdf)  
**作者**：Qingyu Yin, Yulun Wu, Zhennan Shen, Sunbowen Li, Zhilin Wang, Yanshu Li, Chak Tou Leong, Jiale Kang, Jinjin Gu  

**一句话要点**：评估参数高效微调方法在RLVR范式下的性能，挑战LoRA默认选择并揭示优化瓶颈。

**关键词**：参数高效微调, 强化学习可验证奖励, 数学推理基准, LoRA变体, 谱崩溃现象, 模型优化

## 3 点简述
- 核心问题：RLVR中参数高效微调方法的最佳架构未知，需系统评估。
- 方法要点：在DeepSeek-R1-Distill模型上评估12种PEFT方法，包括LoRA变体与SVD初始化策略。
- 实验或效果：发现DoRA等结构变体优于LoRA，SVD策略因谱崩溃失败，极端参数削减限制推理能力。

## 摘要（原文）

> We systematically evaluate Parameter-Efficient Fine-Tuning (PEFT) methods under the paradigm of Reinforcement Learning with Verifiable Rewards (RLVR). RLVR incentivizes language models to enhance their reasoning capabilities through verifiable feedback; however, while methods like LoRA are commonly used, the optimal PEFT architecture for RLVR remains unidentified. In this work, we conduct the first comprehensive evaluation of over 12 PEFT methodologies across the DeepSeek-R1-Distill families on mathematical reasoning benchmarks. Our empirical results challenge the default adoption of standard LoRA with three main findings. First, we demonstrate that structural variants, such as DoRA, AdaLoRA, and MiSS, consistently outperform LoRA. Second, we uncover a spectral collapse phenomenon in SVD-informed initialization strategies (\textit{e.g.,} PiSSA, MiLoRA), attributing their failure to a fundamental misalignment between principal-component updates and RL optimization. Furthermore, our ablations reveal that extreme parameter reduction (\textit{e.g.,} VeRA, Rank-1) severely bottlenecks reasoning capacity. We further conduct ablation studies and scaling experiments to validate our findings. This work provides a definitive guide for advocating for more exploration for parameter-efficient RL methods.

