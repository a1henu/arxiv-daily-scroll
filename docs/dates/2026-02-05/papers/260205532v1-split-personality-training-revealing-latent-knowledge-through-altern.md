---
layout: default
title: Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities
---

# Split Personality Training: Revealing Latent Knowledge Through Alternate Personalities
**arXiv**：[2602.05532v1](https://arxiv.org/abs/2602.05532) · [PDF](https://arxiv.org/pdf/2602.05532.pdf)  
**作者**：Florian Dietz, William Wale, Oscar Gilg, Robert McCarthy, Felix Michalak, Gustavo Ewbank Rodrigues Danon, Miguelito de Guzman, Dietrich Klakow  

**一句话要点**：提出Split Personality Training以揭示大语言模型中的潜在知识

**关键词**：大语言模型审计, 潜在知识检测, LoRA微调, 模型对齐, 人格训练

## 3 点简述
- 核心问题：大语言模型可能隐藏不当行为，标准审计方法难以检测。
- 方法要点：通过微调一个诚实人格到LoRA参数，在触发后审查主模型响应。
- 实验效果：在Anthropic审计游戏基准上达到96%准确率，显著优于现有方法。

## 摘要（原文）

> Detecting misalignment in large language models is challenging because models may learn to conceal misbehavior during training. Standard auditing techniques fall short: black-box methods often cannot distinguish misaligned outputs from benign ones, and mechanistic interpretability does not scale with model capabilities. We introduce Split Personality Training (SPT), which fine-tunes a second ``honest persona'' into LoRA parameters that remain inactive during normal operation. After the main model responds, we activate the LoRA adapter and insert a trigger string, enabling the honest persona to review the response while accessing the main model's latent states. We test our method on the Anthropic Auditing Game Model Organism, a benchmark where Llama-3.3-70B is trained to exploit reward hacks while concealing this behavior. SPT achieves 96% overall accuracy, whereas Anthropic reports near 0% accuracy. The honest persona reveals latent knowledge inaccessible to external observers, such as the fictional biases the compromised model was trained on.

