---
layout: default
title: Instruction-Following Evaluation of Large Vision-Language Models
---

# Instruction-Following Evaluation of Large Vision-Language Models
**arXiv**：[2512.23572v1](https://arxiv.org/abs/2512.23572) · [PDF](https://arxiv.org/pdf/2512.23572.pdf)  
**作者**：Daiki Shiono, Shumpei Miyawaki, Ryota Tanaka, Jun Suzuki  

**一句话要点**：量化评估大视觉语言模型指令跟随能力下降并提出缓解方法

**关键词**：大视觉语言模型, 指令跟随评估, 视觉指令微调, 输出格式指定, 能力下降分析

## 3 点简述
- 核心问题：大视觉语言模型在视觉指令微调后指令跟随能力下降，导致不按任务指令预期执行。
- 方法要点：构建新训练数据集，突出输出格式指定，研究微调中明确指示输出格式对指令跟随能力的影响。
- 实验或效果：定量评估确认能力下降，发现包含输出格式指令的数据集训练模型能更准确跟随指令。

## 摘要（原文）

> Following the initial flourishing of large language models (LLMs), there has been a surge in proposed large vision-language models (LVLMs) that integrate LLMs with vision capabilities. However, it has been observed that LVLMs, after tuning to visual instruction using commonly used training datasets, often fail to exhibit the instruction-following ability that was present in the LLM before integration, leading to results in which they do not follow task instructions as expected. This study quantitatively demonstrates that LVLMs' instruction-following ability declines after fine-tuning and analyzes its underlying causes. In particular, we constructed new training datasets highlighting whether the output format is specified. Then, we investigated how explicitly indicating the output format during fine-tuning affects LVLMs' instruction-following ability. Our quantitative evaluation confirmed that LVLMs' instruction-following ability declines after fine-tuning with commonly used datasets. Furthermore, we found that LVLMs trained with datasets, including instructions on output format, tend to follow instructions more accurately than models that do not. These findings suggest that including samples with instructions on output format during (visual) instruction tuning may help mitigate the decline in instruction-following abilities.

