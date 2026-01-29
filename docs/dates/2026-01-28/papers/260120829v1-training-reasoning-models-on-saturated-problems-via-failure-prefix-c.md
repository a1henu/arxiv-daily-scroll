---
layout: default
title: Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning
---

# Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning
**arXiv**：[2601.20829v1](https://arxiv.org/abs/2601.20829) · [PDF](https://arxiv.org/pdf/2601.20829.pdf)  
**作者**：Minwu Kim, Safal Shrestha, Keith Ross  

**一句话要点**：提出失败前缀条件化方法，以解决强化学习验证奖励训练在饱和问题上的停滞问题。

**关键词**：强化学习验证奖励, 推理模型训练, 失败前缀条件化, 饱和问题, 性能提升, 迭代训练

## 3 点简述
- 核心问题：饱和问题中信息性失败难以访问，导致学习信号稀少。
- 方法要点：基于罕见错误推理轨迹的前缀重新分配探索，暴露模型于易失败状态。
- 实验或效果：性能提升匹配中等难度问题训练，保持标记效率，迭代方法可突破平台期。

## 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved the reasoning abilities of large language models (LLMs), yet training often stalls as problems become saturated. We identify the core challenge as the poor accessibility of informative failures: learning signals exist but are rarely encountered during standard rollouts. To address this, we propose failure-prefix conditioning, a simple and effective method for learning from saturated problems. Rather than starting from the original question, our approach reallocates exploration by conditioning training on prefixes derived from rare incorrect reasoning trajectories, thereby exposing the model to failure-prone states. We observe that failure-prefix conditioning yields performance gains matching those of training on medium-difficulty problems, while preserving token efficiency. Furthermore, we analyze the model's robustness, finding that our method reduces performance degradation under misleading failure prefixes, albeit with a mild trade-off in adherence to correct early reasoning. Finally, we demonstrate that an iterative approach, which refreshes failure prefixes during training, unlocks additional gains after performance plateaus. Overall, our results suggest that failure-prefix conditioning offers an effective pathway to extend RLVR training on saturated problems.

