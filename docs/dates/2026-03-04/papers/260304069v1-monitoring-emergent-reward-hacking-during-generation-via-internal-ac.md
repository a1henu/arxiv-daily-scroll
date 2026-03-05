---
layout: default
title: Monitoring Emergent Reward Hacking During Generation via Internal Activations
---

# Monitoring Emergent Reward Hacking During Generation via Internal Activations
**arXiv**：[2603.04069v1](https://arxiv.org/abs/2603.04069) · [PDF](https://arxiv.org/pdf/2603.04069.pdf)  
**作者**：Patrick Wilhelm, Thorsten Wittkopp, Odej Kao  

**一句话要点**：提出基于内部激活的监控方法，以在生成过程中检测微调大语言模型的奖励黑客行为。

**关键词**：奖励黑客检测, 内部激活监控, 稀疏自编码器, 微调语言模型, 令牌级估计

## 3 点简述
- 核心问题：微调大语言模型可能产生奖励黑客行为，仅从最终输出难以检测。
- 方法要点：在残差流激活上训练稀疏自编码器，应用轻量线性分类器进行令牌级估计。
- 实验或效果：内部激活模式能可靠区分奖励黑客与良性行为，并泛化到未见过的混合策略适配器。

## 摘要（原文）

> Fine-tuned large language models can exhibit reward-hacking behavior arising from emergent misalignment, which is difficult to detect from final outputs alone. While prior work has studied reward hacking at the level of completed responses, it remains unclear whether such behavior can be identified during generation. We propose an activation-based monitoring approach that detects reward-hacking signals from internal representations as a model generates its response. Our method trains sparse autoencoders on residual stream activations and applies lightweight linear classifiers to produce token-level estimates of reward-hacking activity. Across multiple model families and fine-tuning mixtures, we find that internal activation patterns reliably distinguish reward-hacking from benign behavior, generalize to unseen mixed-policy adapters, and exhibit model-dependent temporal structure during chain-of-thought reasoning. Notably, reward-hacking signals often emerge early, persist throughout reasoning, and can be amplified by increased test-time compute in the form of chain-of-thought prompting under weakly specified reward objectives. These results suggest that internal activation monitoring provides a complementary and earlier signal of emergent misalignment than output-based evaluation, supporting more robust post-deployment safety monitoring for fine-tuned language models.

