---
layout: default
title: Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge
---

# Breaking the Reversal Curse in Autoregressive Language Models via Identity Bridge
**arXiv**：[2602.02470v1](https://arxiv.org/abs/2602.02470) · [PDF](https://arxiv.org/pdf/2602.02470.pdf)  
**作者**：Xutao Ma, Yixiao Huang, Hanlin Zhu, Somayeh Sojoudi  

**一句话要点**：提出身份桥正则化数据配方以缓解自回归语言模型中的逆转诅咒

**关键词**：逆转诅咒, 自回归语言模型, 身份桥正则化, 梯度下降隐式偏差, 逻辑推理, 数据配方

## 3 点简述
- 核心问题：自回归大语言模型在训练前向知识数据后，无法推理逆转知识，即逆转诅咒。
- 方法要点：通过添加形式为“A→A”的身份桥数据，微调训练以促进模型学习高级规则。
- 实验或效果：1B参数模型微调后，在逆转任务上成功率从近零提升至40%。

## 摘要（原文）

> Autoregressive large language models (LLMs) have achieved remarkable success in many complex tasks, yet they can still fail in very simple logical reasoning such as the "reversal curse" -- when trained on forward knowledge data of the form "$A \rightarrow B$" (e.g., Alice's husband is Bob), the model is unable to deduce the reversal knowledge "$B \leftarrow A$" (e.g., Bob's wife is Alice) during test. Extensive prior research suggests that this failure is an inherent, fundamental limit of autoregressive causal LLMs, indicating that these models tend to memorize factual-level knowledge rather than capture higher-level rules. In this paper, we challenge this view by showing that this seemingly fundamental limit can be mitigated by slightly tweaking the training data with a simple regularization data recipe called the Identity Bridge of the form "$A \to A$" (e.g., The name of Alice is Alice). Theoretically, we prove that under this recipe, even a one-layer transformer can break the reversal curse by analyzing the implicit bias of gradient descent. Empirically, we show that a 1B pretrained language model finetuned with the proposed data recipe achieves a 40% success rate on reversal tasks, in stark contrast to a near-zero success rate when trained solely on forward-knowledge data. Our work provides a novel theoretical foundation for the reversal curse and offers a principled, low-cost path to encouraging LLMs to learn higher-level rules from data.

