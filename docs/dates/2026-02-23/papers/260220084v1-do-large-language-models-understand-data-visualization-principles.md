---
layout: default
title: Do Large Language Models Understand Data Visualization Principles?
---

# Do Large Language Models Understand Data Visualization Principles?
**arXiv**：[2602.20084v1](https://arxiv.org/abs/2602.20084) · [PDF](https://arxiv.org/pdf/2602.20084.pdf)  
**作者**：Martin Sinnona, Valentin Bonas, Viviana Siless, Emmanuel Iarussi  

**一句话要点**：评估大语言模型与视觉语言模型在数据可视化原则推理中的能力

**关键词**：数据可视化原则, 大语言模型评估, 视觉语言模型, Vega-Lite规范, 答案集编程, 图表修复

## 3 点简述
- 核心问题：大语言模型和视觉语言模型是否能直接推理并执行数据可视化原则，而非仅生成图表或检测误导性图表。
- 方法要点：使用基于答案集编程的硬验证真值，构建包含约2000个Vega-Lite规范的数据集，评估模型在检查和修复任务中的表现。
- 实验或效果：模型在修复违规方面优于检测，但与符号求解器在视觉感知细微方面存在差距，展示了作为灵活验证器和编辑器的潜力。

## 摘要（原文）

> Data visualization principles, derived from decades of research in design and perception, ensure proper visual communication. While prior work has shown that large language models (LLMs) can generate charts or flag misleading figures, it remains unclear whether they and their vision-language counterparts (VLMs) can reason about and enforce visualization principles directly. Constraint based systems encode these principles as logical rules for precise automated checks, but translating them into formal specifications demands expert knowledge. This motivates leveraging LLMs and VLMs as principle checkers that can reason about visual design directly, bypassing the need for symbolic rule specification. In this paper, we present the first systematic evaluation of both LLMs and VLMs on their ability to reason about visualization principles, using hard verification ground truth derived from Answer Set Programming (ASP). We compiled a set of visualization principles expressed as natural-language statements and generated a controlled dataset of approximately 2,000 Vega-Lite specifications annotated with explicit principle violations, complemented by over 300 real-world Vega-Lite charts. We evaluated both checking and fixing tasks, assessing how well models detect principle violations and correct flawed chart specifications. Our work highlights both the promise of large (vision-)language models as flexible validators and editors of visualization designs and the persistent gap with symbolic solvers on more nuanced aspects of visual perception. They also reveal an interesting asymmetry: frontier models tend to be more effective at correcting violations than at detecting them reliably.

