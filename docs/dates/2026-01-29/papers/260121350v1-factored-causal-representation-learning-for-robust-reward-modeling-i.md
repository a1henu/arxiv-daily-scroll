---
layout: default
title: Factored Causal Representation Learning for Robust Reward Modeling in RLHF
---

# Factored Causal Representation Learning for Robust Reward Modeling in RLHF
**arXiv**：[2601.21350v1](https://arxiv.org/abs/2601.21350) · [PDF](https://arxiv.org/pdf/2601.21350.pdf)  
**作者**：Yupei Yang, Lin Yang, Wanxi Deng, Lin Qu, Fan Feng, Biwei Huang, Shikui Tu, Lei Xu  

**一句话要点**：提出因子化因果表示学习框架，以增强RLHF中奖励模型的鲁棒性

**关键词**：因果表示学习, 奖励建模, 强化学习人类反馈, 鲁棒性, 奖励黑客

## 3 点简述
- 核心问题：标准奖励模型易受与人类标签无因果关系的虚假特征影响，导致奖励黑客行为。
- 方法要点：将上下文嵌入分解为因果因子和非因果因子，奖励头仅依赖因果因子，并引入对抗头抑制非因果因子编码奖励信息。
- 实验或效果：在数学和对话任务上验证了方法能学习更鲁棒的奖励模型，提升下游RLHF性能，并有效缓解长度和谄媚偏见。

## 摘要（原文）

> A reliable reward model is essential for aligning large language models with human preferences through reinforcement learning from human feedback. However, standard reward models are susceptible to spurious features that are not causally related to human labels. This can lead to reward hacking, where high predicted reward does not translate into better behavior. In this work, we address this problem from a causal perspective by proposing a factored representation learning framework that decomposes the model's contextual embedding into (1) causal factors that are sufficient for reward prediction and (2) non-causal factors that capture reward-irrelevant attributes such as length or sycophantic bias. The reward head is then constrained to depend only on the causal component. In addition, we introduce an adversarial head trained to predict reward from the non-causal factors, while applying gradient reversal to discourage them from encoding reward-relevant information. Experiments on both mathematical and dialogue tasks demonstrate that our method learns more robust reward models and consistently improves downstream RLHF performance over state-of-the-art baselines. Analyses on length and sycophantic bias further validate the effectiveness of our method in mitigating reward hacking behaviors.

