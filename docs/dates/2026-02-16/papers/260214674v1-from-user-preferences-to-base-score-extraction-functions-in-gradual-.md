---
layout: default
title: From User Preferences to Base Score Extraction Functions in Gradual Argumentation
---

# From User Preferences to Base Score Extraction Functions in Gradual Argumentation
**arXiv**：[2602.14674v1](https://arxiv.org/abs/2602.14674) · [PDF](https://arxiv.org/pdf/2602.14674.pdf)  
**作者**：Aniol Civit, Antonio Rago, Antonio Andriella, Guillem Alenyà, Francesca Toni  

**一句话要点**：提出基分提取函数以从用户偏好映射到基分，应用于机器人等场景的渐进论证框架。

**关键词**：渐进论证, 基分提取, 用户偏好, 双极论证框架, 机器人应用, 符号AI

## 3 点简述
- 核心问题：渐进论证中基分选择依赖专家知识，用户偏好组织可简化任务。
- 方法要点：定义基分提取函数，将偏好映射为基分，支持非线性偏好近似。
- 实验或效果：在机器人设置中进行理论和实验评估，提供渐进语义选择建议。

## 摘要（原文）

> Gradual argumentation is a field of symbolic AI which is attracting attention for its ability to support transparent and contestable AI systems. It is considered a useful tool in domains such as decision-making, recommendation, debate analysis, and others. The outcomes in such domains are usually dependent on the arguments' base scores, which must be selected carefully. Often, this selection process requires user expertise and may not always be straightforward. On the other hand, organising the arguments by preference could simplify the task. In this work, we introduce \emph{Base Score Extraction Functions}, which provide a mapping from users' preferences over arguments to base scores. These functions can be applied to the arguments of a \emph{Bipolar Argumentation Framework} (BAF), supplemented with preferences, to obtain a \emph{Quantitative Bipolar Argumentation Framework} (QBAF), allowing the use of well-established computational tools in gradual argumentation. We outline the desirable properties of base score extraction functions, discuss some design choices, and provide an algorithm for base score extraction. Our method incorporates an approximation of non-linearities in human preferences to allow for better approximation of the real ones. Finally, we evaluate our approach both theoretically and experimentally in a robotics setting, and offer recommendations for selecting appropriate gradual semantics in practice.

