---
layout: default
title: Do Large Language Models Understand Data Visualization Rules?
---

# Do Large Language Models Understand Data Visualization Rules?
**arXiv**：[2602.20137v1](https://arxiv.org/abs/2602.20137) · [PDF](https://arxiv.org/pdf/2602.20137.pdf)  
**作者**：Martin Sinnona, Valentin Bonas, Emmanuel Iarussi, Viviana Siless  

**一句话要点**：评估大语言模型对数据可视化规则的理解能力，揭示其作为灵活验证器的潜力与局限

**关键词**：大语言模型, 数据可视化规则, 规则验证, 自然语言处理, 符号约束, 评估基准

## 3 点简述
- 核心问题：大语言模型能否直接推理并执行数据可视化规则，以替代基于符号约束的专家系统
- 方法要点：将Draco的约束转化为自然语言，构建带违规标注的Vega-Lite数据集，进行系统评估
- 实验或效果：前沿模型在常见违规检测中表现良好（F1最高0.82），但对细微感知规则效果差（F1<0.15）

## 摘要（原文）

> Data visualization rules-derived from decades of research in design and perception-ensure trustworthy chart communication. While prior work has shown that large language models (LLMs) can generate charts or flag misleading figures, it remains unclear whether they can reason about and enforce visualization rules directly. Constraint-based systems such as Draco encode these rules as logical constraints for precise automated checks, but maintaining symbolic encodings requires expert effort, motivating the use of LLMs as flexible rule validators. In this paper, we present the first systematic evaluation of LLMs against visualization rules using hard-verification ground truth derived from Answer Set Programming (ASP). We translated a subset of Draco's constraints into natural-language statements and generated a controlled dataset of 2,000 Vega-Lite specifications annotated with explicit rule violations. LLMs were evaluated on both accuracy in detecting violations and prompt adherence, which measures whether outputs follow the required structured format. Results show that frontier models achieve high adherence (Gemma 3 4B / 27B: 100%, GPT-oss 20B: 98%) and reliably detect common violations (F1 up to 0.82),yet performance drops for subtler perceptual rules (F1 < 0.15 for some categories) and for outputs generated from technical ASP formulations.Translating constraints into natural language improved performance by up to 150% for smaller models. These findings demonstrate the potential of LLMs as flexible, language-driven validators while highlighting their current limitations compared to symbolic solvers.

