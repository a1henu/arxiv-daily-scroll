---
layout: default
title: Copyright Infringement Risk Reduction via Chain-of-Thought and Task Instruction Prompting
---

# Copyright Infringement Risk Reduction via Chain-of-Thought and Task Instruction Prompting
**arXiv**：[2512.15442v1](https://arxiv.org/abs/2512.15442) · [PDF](https://arxiv.org/pdf/2512.15442.pdf)  
**作者**：Neeraj Sarna, Yuanyuan Li, Michael von Gablenz  

**一句话要点**：提出结合思维链与任务指令提示的方法，以减少文本到图像生成模型中的版权侵权风险。

**关键词**：文本到图像生成, 版权侵权风险, 思维链提示, 任务指令提示, 负向提示, 提示重写

## 3 点简述
- 核心问题：大规模文本到图像生成模型可能记忆并复制受版权保护的训练数据，导致侵权风险。
- 方法要点：结合思维链和任务指令提示，并整合负向提示和提示重写策略，以降低版权内容生成。
- 实验或效果：通过数值实验评估生成图像与版权图像的相似性及用户输入相关性，分析不同模型复杂度下的技术有效性。

## 摘要（原文）

> Large scale text-to-image generation models can memorize and reproduce their training dataset. Since the training dataset often contains copyrighted material, reproduction of training dataset poses a copyright infringement risk, which could result in legal liabilities and financial losses for both the AI user and the developer. The current works explores the potential of chain-of-thought and task instruction prompting in reducing copyrighted content generation. To this end, we present a formulation that combines these two techniques with two other copyright mitigation strategies: a) negative prompting, and b) prompt re-writing. We study the generated images in terms their similarity to a copyrighted image and their relevance of the user input. We present numerical experiments on a variety of models and provide insights on the effectiveness of the aforementioned techniques for varying model complexity.

