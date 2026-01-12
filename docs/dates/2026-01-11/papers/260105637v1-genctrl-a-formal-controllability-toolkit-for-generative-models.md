---
layout: default
title: GenCtrl -- A Formal Controllability Toolkit for Generative Models
---

# GenCtrl -- A Formal Controllability Toolkit for Generative Models
**arXiv**：[2601.05637v1](https://arxiv.org/abs/2601.05637) · [PDF](https://arxiv.org/pdf/2601.05637.pdf)  
**作者**：Emily Cheng, Carmen Amo Alonso, Federico Danieli, Arno Blaas, Luca Zappella, Pau Rodriguez, Xavier Suau  

**一句话要点**：提出GenCtrl形式化可控性工具包，用于评估生成模型在对话设置中的可控性。

**关键词**：生成模型可控性, 形式化分析, 对话控制, PAC界, 黑盒系统

## 3 点简述
- 核心问题：生成模型是否真正可控，现有方法缺乏理论基础。
- 方法要点：基于控制过程框架，提出算法估计可控集，提供分布无关的PAC误差界。
- 实验或效果：在对话和文本到图像任务中验证，显示模型可控性脆弱且依赖设置。

## 摘要（原文）

> As generative models become ubiquitous, there is a critical need for fine-grained control over the generation process. Yet, while controlled generation methods from prompting to fine-tuning proliferate, a fundamental question remains unanswered: are these models truly controllable in the first place? In this work, we provide a theoretical framework to formally answer this question. Framing human-model interaction as a control process, we propose a novel algorithm to estimate the controllable sets of models in a dialogue setting. Notably, we provide formal guarantees on the estimation error as a function of sample complexity: we derive probably-approximately correct bounds for controllable set estimates that are distribution-free, employ no assumptions except for output boundedness, and work for any black-box nonlinear control system (i.e., any generative model). We empirically demonstrate the theoretical framework on different tasks in controlling dialogue processes, for both language models and text-to-image generation. Our results show that model controllability is surprisingly fragile and highly dependent on the experimental setting. This highlights the need for rigorous controllability analysis, shifting the focus from simply attempting control to first understanding its fundamental limits.

