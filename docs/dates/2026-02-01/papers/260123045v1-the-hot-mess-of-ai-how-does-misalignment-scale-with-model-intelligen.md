---
layout: default
title: The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?
---

# The Hot Mess of AI: How Does Misalignment Scale With Model Intelligence and Task Complexity?
**arXiv**：[2601.23045v1](https://arxiv.org/abs/2601.23045) · [PDF](https://arxiv.org/pdf/2601.23045.pdf)  
**作者**：Alexander Hägele, Aryo Pradipta Gema, Henry Sleight, Ethan Perez, Jascha Sohl-Dickstein  

**一句话要点**：探究AI模型失败模式：任务复杂度与模型智能如何影响不连贯行为

**关键词**：AI对齐, 偏差-方差分解, 任务复杂度, 模型规模, 不连贯行为, 失败模式

## 3 点简述
- 核心问题：AI模型失败时是系统性追求错误目标还是行为不连贯？
- 方法要点：通过偏差-方差分解量化模型在任务中的不连贯性。
- 实验或效果：前沿模型在复杂任务中失败时更易表现出不连贯行为。

## 摘要（原文）

> As AI becomes more capable, we entrust it with more general and consequential tasks. The risks from failure grow more severe with increasing task scope. It is therefore important to understand how extremely capable AI models will fail: Will they fail by systematically pursuing goals we do not intend? Or will they fail by being a hot mess, and taking nonsensical actions that do not further any goal? We operationalize this question using a bias-variance decomposition of the errors made by AI models: An AI's \emph{incoherence} on a task is measured over test-time randomness as the fraction of its error that stems from variance rather than bias in task outcome. Across all tasks and frontier models we measure, the longer models spend reasoning and taking actions, \emph{the more incoherent} their failures become. Incoherence changes with model scale in a way that is experiment dependent. However, in several settings, larger, more capable models are more incoherent than smaller models. Consequently, scale alone seems unlikely to eliminate incoherence. Instead, as more capable AIs pursue harder tasks, requiring more sequential action and thought, our results predict failures to be accompanied by more incoherent behavior. This suggests a future where AIs sometimes cause industrial accidents (due to unpredictable misbehavior), but are less likely to exhibit consistent pursuit of a misaligned goal. This increases the relative importance of alignment research targeting reward hacking or goal misspecification.

