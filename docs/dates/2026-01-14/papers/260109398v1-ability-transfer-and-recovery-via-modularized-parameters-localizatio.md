---
layout: default
title: Ability Transfer and Recovery via Modularized Parameters Localization
---

# Ability Transfer and Recovery via Modularized Parameters Localization
**arXiv**：[2601.09398v1](https://arxiv.org/abs/2601.09398) · [PDF](https://arxiv.org/pdf/2601.09398.pdf)  
**作者**：Songyao Jin, Kun Zhou, Wenqi Li, Peng Wang, Biwei Huang  

**一句话要点**：提出ACT方法，通过激活引导的通道级能力转移，解决大语言模型能力遗忘与整合问题。

**关键词**：能力转移, 参数定位, 激活分析, 轻量微调, 多语言推理, 模型整合

## 3 点简述
- 核心问题：大语言模型在特定领域微调时易导致能力遗忘，影响其他技能。
- 方法要点：基于激活差异定位能力相关通道，选择性转移参数，结合轻量微调确保兼容性。
- 实验效果：在跨语言数学与科学推理任务中，ACT能恢复遗忘能力并整合多模型能力，减少干扰。

## 摘要（原文）

> Large language models can be continually pre-trained or fine-tuned to improve performance in specific domains, languages, or skills, but this specialization often degrades other capabilities and may cause catastrophic forgetting. We investigate how abilities are distributed within LLM parameters by analyzing module activations under domain- and language-specific inputs for closely related models. Across layers and modules, we find that ability-related activations are highly concentrated in a small set of channels (typically <5\%), and these channels are largely disentangled with good sufficiency and stability. Building on these observations, we propose ACT (Activation-Guided Channel-wise Ability Transfer), which localizes ability-relevant channels via activation differences and selectively transfers only the corresponding parameters, followed by lightweight fine-tuning for compatibility. Experiments on multilingual mathematical and scientific reasoning show that ACT can recover forgotten abilities while preserving retained skills. It can also merge multiple specialized models to integrate several abilities into a single model with minimal interference. Our code and data will be publicly released.

