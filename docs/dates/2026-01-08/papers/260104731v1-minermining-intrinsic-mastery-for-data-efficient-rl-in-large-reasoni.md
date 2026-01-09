---
layout: default
title: Miner:Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models
---

# Miner:Mining Intrinsic Mastery for Data-Efficient RL in Large Reasoning Models
**arXiv**：[2601.04731v1](https://arxiv.org/abs/2601.04731) · [PDF](https://arxiv.org/pdf/2601.04731.pdf)  
**作者**：Shuyang Jiang, Yuhao Wang, Ya Zhang, Yanfeng Wang, Yu Wang  

**一句话要点**：提出Miner方法，通过挖掘内在不确定性解决大型推理模型在正同质提示下强化学习效率低的问题。

**关键词**：强化学习, 推理模型, 不确定性挖掘, 自监督奖励, 信用分配, 优势校准

## 3 点简述
- 核心问题：当前无批评者强化学习方法在正同质提示（所有轨迹均正确）上训练效率低下，优势估计为零导致轨迹浪费。
- 方法要点：利用策略内在不确定性作为自监督奖励信号，引入令牌级焦点信用分配机制和自适应优势校准，无需外部监督或额外推理成本。
- 实验或效果：在Qwen3-4B和Qwen3-8B模型上评估六个推理基准，Miner在Pass@1和Pass@K上相比GRPO提升最高达4.58和6.66，优于其他算法。

## 摘要（原文）

> Current critic-free RL methods for large reasoning models suffer from severe inefficiency when training on positive homogeneous prompts (where all rollouts are correct), resulting in waste of rollouts due to zero advantage estimates. We introduce a radically simple yet powerful solution to \uline{M}ine \uline{in}trinsic mast\uline{er}y (Miner), that repurposes the policy's intrinsic uncertainty as a self-supervised reward signal, with no external supervision, auxiliary models, or additional inference cost. Our method pioneers two key innovations: (1) a token-level focal credit assignment mechanism that dynamically amplifies gradients on critical uncertain tokens while suppressing overconfident ones, and (2) adaptive advantage calibration to seamlessly integrate intrinsic and verifiable rewards. Evaluated across six reasoning benchmarks on Qwen3-4B and Qwen3-8B base models, Miner achieves state-of-the-art performance among the other four algorithms, yielding up to \textbf{4.58} absolute gains in Pass@1 and \textbf{6.66} gains in Pass@K compared to GRPO. Comparison with other methods targeted at exploration enhancement further discloses the superiority of the two newly proposed innovations. This demonstrates that latent uncertainty exploitation is both necessary and sufficient for efficient and scalable RL training of reasoning models.

