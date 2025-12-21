---
layout: default
title: C-DGPA: Class-Centric Dual-Alignment Generative Prompt Adaptation
---

# C-DGPA: Class-Centric Dual-Alignment Generative Prompt Adaptation
**arXiv**：[2512.16164v1](https://arxiv.org/abs/2512.16164) · [PDF](https://arxiv.org/pdf/2512.16164.pdf)  
**作者**：Chao Li, Dasha Hu, Chengyang Li, Yuming Jiang, Yuncheng Shen  

**一句话要点**：提出C-DGPA以解决视觉语言模型在无监督域适应中提示调优的分布对齐问题

**关键词**：无监督域适应, 视觉语言模型, 提示调优, 分布对齐, 对抗训练, 类别映射

## 3 点简述
- 核心问题：现有提示调优方法仅对齐边缘分布，忽略条件分布差异，导致类别原型错位和语义判别性下降
- 方法要点：通过双分支架构协同优化边缘分布对齐和条件分布对齐，引入类别映射机制标准化语义提示理解
- 实验或效果：在OfficeHome、Office31和VisDA-2017基准测试中取得新的最优结果

## 摘要（原文）

> Unsupervised Domain Adaptation transfers knowledge from a labeled source domain to an unlabeled target domain. Directly deploying Vision-Language Models (VLMs) with prompt tuning in downstream UDA tasks faces the signifi cant challenge of mitigating domain discrepancies. Existing prompt-tuning strategies primarily align marginal distribu tion, but neglect conditional distribution discrepancies, lead ing to critical issues such as class prototype misalignment and degraded semantic discriminability. To address these lim itations, the work proposes C-DGPA: Class-Centric Dual Alignment Generative Prompt Adaptation. C-DGPA syner gistically optimizes marginal distribution alignment and con ditional distribution alignment through a novel dual-branch architecture. The marginal distribution alignment branch em ploys a dynamic adversarial training framework to bridge marginal distribution discrepancies. Simultaneously, the con ditional distribution alignment branch introduces a Class Mapping Mechanism (CMM) to align conditional distribu tion discrepancies by standardizing semantic prompt under standing and preventing source domain over-reliance. This dual alignment strategy effectively integrates domain knowl edge into prompt learning via synergistic optimization, ensur ing domain-invariant and semantically discriminative repre sentations. Extensive experiments on OfficeHome, Office31, and VisDA-2017 validate the superiority of C-DGPA. It achieves new state-of-the-art results on all benchmarks.

