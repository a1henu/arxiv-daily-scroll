---
layout: default
title: Entropy-Adaptive Fine-Tuning: Resolving Confident Conflicts to Mitigate Forgetting
---

# Entropy-Adaptive Fine-Tuning: Resolving Confident Conflicts to Mitigate Forgetting
**arXiv**：[2601.02151v1](https://arxiv.org/abs/2601.02151) · [PDF](https://arxiv.org/pdf/2601.02151.pdf)  
**作者**：Muxi Diao, Lele Yang, Wuxuan Gong, Yutong Zhang, Zhonghao Yan, Yufei Han, Kongming Liang, Weiran Xu, Zhanyu Ma  

**一句话要点**：提出熵自适应微调以解决监督微调中的灾难性遗忘问题

**关键词**：监督微调, 灾难性遗忘, 熵自适应微调, 自信冲突, 梯度抑制, 模型泛化

## 3 点简述
- 核心问题：监督微调导致灾难性遗忘，源于模型内部信念与外部监督的分布差异，表现为低概率低熵的自信冲突。
- 方法要点：利用词级熵作为门控机制，区分认知不确定性与知识冲突，抑制冲突数据的梯度更新。
- 实验或效果：在Qwen和GLM系列模型上验证，下游性能匹配标准监督微调，同时显著缓解通用能力退化。

## 摘要（原文）

> Supervised Fine-Tuning (SFT) is the standard paradigm for domain adaptation, yet it frequently incurs the cost of catastrophic forgetting. In sharp contrast, on-policy Reinforcement Learning (RL) effectively preserves general capabilities. We investigate this discrepancy and identify a fundamental distributional gap: while RL aligns with the model's internal belief, SFT forces the model to fit external supervision. This mismatch often manifests as "Confident Conflicts" tokens characterized by low probability but low entropy. In these instances, the model is highly confident in its own prediction but is forced to learn a divergent ground truth, triggering destructive gradient updates. To address this, we propose Entropy-Adaptive Fine-Tuning (EAFT). Unlike methods relying solely on prediction probability, EAFT utilizes token-level entropy as a gating mechanism to distinguish between epistemic uncertainty and knowledge conflict. This allows the model to learn from uncertain samples while suppressing gradients on conflicting data. Extensive experiments on Qwen and GLM series (ranging from 4B to 32B parameters) across mathematical, medical, and agentic domains confirm our hypothesis. EAFT consistently matches the downstream performance of standard SFT while significantly mitigating the degradation of general capabilities.

