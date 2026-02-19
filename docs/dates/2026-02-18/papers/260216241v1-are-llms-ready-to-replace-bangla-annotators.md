---
layout: default
title: Are LLMs Ready to Replace Bangla Annotators?
---

# Are LLMs Ready to Replace Bangla Annotators?
**arXiv**：[2602.16241v1](https://arxiv.org/abs/2602.16241) · [PDF](https://arxiv.org/pdf/2602.16241.pdf)  
**作者**：Md. Najib Hasan, Touseef Hasan, Souvika Sarkar  

**一句话要点**：评估大语言模型作为孟加拉语仇恨言论零样本标注者的可靠性与偏见

**关键词**：大语言模型评估, 零样本标注, 孟加拉语仇恨言论, 标注偏见, 低资源语言处理, 模型稳定性分析

## 3 点简述
- 核心问题：大语言模型在低资源语言和身份敏感任务中作为自动标注者的可靠性未知，尤其在孟加拉语仇恨言论标注中。
- 方法要点：系统评估17个大语言模型，使用统一框架分析其零样本标注行为，关注偏见和不稳定性。
- 实验或效果：发现模型规模增大不保证标注质量提升，小规模任务对齐模型表现更一致，揭示当前模型在敏感任务中的局限性。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly used as automated annotators to scale dataset creation, yet their reliability as unbiased annotators--especially for low-resource and identity-sensitive settings--remains poorly understood. In this work, we study the behavior of LLMs as zero-shot annotators for Bangla hate speech, a task where even human agreement is challenging, and annotator bias can have serious downstream consequences. We conduct a systematic benchmark of 17 LLMs using a unified evaluation framework. Our analysis uncovers annotator bias and substantial instability in model judgments. Surprisingly, increased model scale does not guarantee improved annotation quality--smaller, more task-aligned models frequently exhibit more consistent behavior than their larger counterparts. These results highlight important limitations of current LLMs for sensitive annotation tasks in low-resource languages and underscore the need for careful evaluation before deployment.

