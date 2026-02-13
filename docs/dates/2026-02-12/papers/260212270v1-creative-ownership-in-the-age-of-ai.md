---
layout: default
title: Creative Ownership in the Age of AI
---

# Creative Ownership in the Age of AI
**arXiv**：[2602.12270v1](https://arxiv.org/abs/2602.12270) · [PDF](https://arxiv.org/pdf/2602.12270.pdf)  
**作者**：Annie Liang, Jay Lu  

**一句话要点**：提出基于训练依赖的侵权新标准，以解决生成式AI模仿风格的法律挑战。

**关键词**：生成式AI, 版权侵权, 训练依赖, 闭包算子, 渐近分析

## 3 点简述
- 核心问题：生成式AI能模仿风格而不复制内容，现有侵权定义不适用。
- 方法要点：将生成系统建模为闭包算子，定义输出侵权需依赖训练语料中的作品。
- 实验或效果：分析可容许生成的结构特性，揭示轻尾与重尾创作下的渐近二分法。

## 摘要（原文）

> Copyright law focuses on whether a new work is "substantially similar" to an existing one, but generative AI can closely imitate style without copying content, a capability now central to ongoing litigation. We argue that existing definitions of infringement are ill-suited to this setting and propose a new criterion: a generative AI output infringes on an existing work if it could not have been generated without that work in its training corpus. To operationalize this definition, we model generative systems as closure operators mapping a corpus of existing works to an output of new works. AI generated outputs are \emph{permissible} if they do not infringe on any existing work according to our criterion. Our results characterize structural properties of permissible generation and reveal a sharp asymptotic dichotomy: when the process of organic creations is light-tailed, dependence on individual works eventually vanishes, so that regulation imposes no limits on AI generation; with heavy-tailed creations, regulation can be persistently constraining.

