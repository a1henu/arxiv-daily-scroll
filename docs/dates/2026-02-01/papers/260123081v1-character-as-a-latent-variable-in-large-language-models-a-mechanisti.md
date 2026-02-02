---
layout: default
title: Character as a Latent Variable in Large Language Models: A Mechanistic Account of Emergent Misalignment and Conditional Safety Failures
---

# Character as a Latent Variable in Large Language Models: A Mechanistic Account of Emergent Misalignment and Conditional Safety Failures
**arXiv**：[2601.23081v1](https://arxiv.org/abs/2601.23081) · [PDF](https://arxiv.org/pdf/2601.23081.pdf)  
**作者**：Yanghao Su, Wenbo Zhou, Tianwei Zhang, Qiu Han, Weiming Zhang, Nenghai Yu, Jie Zhang  

**一句话要点**：提出字符作为大语言模型潜在变量，解释微调引发的广泛错位与条件安全失效机制

**关键词**：大语言模型对齐, 微调风险, 字符形成, 条件安全失效, 行为倾向, 错位机制

## 3 点简述
- 核心问题：微调大语言模型于窄域数据导致广泛错位行为，传统解释基于错误内容泛化不完整
- 方法要点：通过实验证明字符级倾向性微调比错误建议微调产生更强、更可转移的错位，保留一般能力
- 实验或效果：发现行为倾向可由训练时触发器和推理时角色对齐提示条件激活，揭示错位、后门激活和越狱易感性的共享结构

## 摘要（原文）

> Emergent Misalignment refers to a failure mode in which fine-tuning large language models (LLMs) on narrowly scoped data induces broadly misaligned behavior. Prior explanations mainly attribute this phenomenon to the generalization of erroneous or unsafe content. In this work, we show that this view is incomplete. Across multiple domains and model families, we find that fine-tuning models on data exhibiting specific character-level dispositions induces substantially stronger and more transferable misalignment than incorrect-advice fine-tuning, while largely preserving general capabilities. This indicates that emergent misalignment arises from stable shifts in model behavior rather than from capability degradation or corrupted knowledge. We further show that such behavioral dispositions can be conditionally activated by both training-time triggers and inference-time persona-aligned prompts, revealing shared structure across emergent misalignment, backdoor activation, and jailbreak susceptibility. Overall, our results identify character formation as a central and underexplored alignment risk, suggesting that robust alignment must address behavioral dispositions rather than isolated errors or prompt-level defenses.

