---
layout: default
title: Test-Time Adaptation via Many-Shot Prompting: Benefits, Limits, and Pitfalls
---

# Test-Time Adaptation via Many-Shot Prompting: Benefits, Limits, and Pitfalls
**arXiv**：[2603.05829v1](https://arxiv.org/abs/2603.05829) · [PDF](https://arxiv.org/pdf/2603.05829.pdf)  
**作者**：Shubhangi Upasani, Chen Wu, Jay Rainton, Bo Li, Changran Hu, Qizheng Zhang, Urmish Thakker  

**一句话要点**：实证研究多示例提示在测试时适应中的效果、局限与陷阱

**关键词**：测试时适应, 多示例提示, 上下文学习, 大语言模型, 输入空间更新

## 3 点简述
- 核心问题：多示例提示作为测试时适应方法的可靠性和限制，尤其在开源模型中未充分理解
- 方法要点：分析性能随更新幅度、示例顺序和选择策略的变化，并研究动态和强化ICL作为替代策略
- 实验或效果：多示例提示对结构化任务有效，但对选择策略敏感，在开放生成任务中益处有限

## 摘要（原文）

> Test-time adaptation enables large language models (LLMs) to modify their behavior at inference without updating model parameters. A common approach is many-shot prompting, where large numbers of in-context learning (ICL) examples are injected as an input-space test-time update. Although performance can improve as more demonstrations are added, the reliability and limits of this update mechanism remain poorly understood, particularly for open-source models. We present an empirical study of many-shot prompting across tasks and model backbones, analyzing how performance varies with update magnitude, example ordering, and selection policy. We further study Dynamic and Reinforced ICL as alternative test-time update strategies that control which information is injected and how it constrains model behavior. We find that many-shot prompting is effective for structured tasks where demonstrations provide high information gain, but is highly sensitive to selection strategy and often shows limited benefits for open-ended generation tasks. Overall, we characterize the practical limits of prompt-based test-time adaptation and outline when input-space updates are beneficial versus harmful.

