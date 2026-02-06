---
layout: default
title: xList-Hate: A Checklist-Based Framework for Interpretable and Generalizable Hate Speech Detection
---

# xList-Hate: A Checklist-Based Framework for Interpretable and Generalizable Hate Speech Detection
**arXiv**：[2602.05874v1](https://arxiv.org/abs/2602.05874) · [PDF](https://arxiv.org/pdf/2602.05874.pdf)  
**作者**：Adrián Girón, Pablo Miralles, Javier Huertas-Tato, Sergio D'Antonio, David Camacho  

**一句话要点**：提出xList-Hate框架，通过清单式诊断提升仇恨言论检测的鲁棒性与可解释性

**关键词**：仇恨言论检测, 可解释人工智能, 大型语言模型, 诊断框架, 跨域鲁棒性

## 3 点简述
- 仇恨言论检测常因定义不一致导致模型过拟合和跨域性能差
- 框架将检测分解为基于规范准则的概念级问题，由LLM独立回答生成诊断信号
- 实验显示在跨数据集鲁棒性和可解释性方面优于零样本LLM和微调方法

## 摘要（原文）

> Hate speech detection is commonly framed as a direct binary classification problem despite being a composite concept defined through multiple interacting factors that vary across legal frameworks, platform policies, and annotation guidelines. As a result, supervised models often overfit dataset-specific definitions and exhibit limited robustness under domain shift and annotation noise.
>   We introduce xList-Hate, a diagnostic framework that decomposes hate speech detection into a checklist of explicit, concept-level questions grounded in widely shared normative criteria. Each question is independently answered by a large language model (LLM), producing a binary diagnostic representation that captures hateful content features without directly predicting the final label. These diagnostic signals are then aggregated by a lightweight, fully interpretable decision tree, yielding transparent and auditable predictions.
>   We evaluate it across multiple hate speech benchmarks and model families, comparing it against zero-shot LLM classification and in-domain supervised fine-tuning. While supervised methods typically maximize in-domain performance, we consistently improves cross-dataset robustness and relative performance under domain shift. In addition, qualitative analysis of disagreement cases provides evidence that the framework can be less sensitive to certain forms of annotation inconsistency and contextual ambiguity. Crucially, the approach enables fine-grained interpretability through explicit decision paths and factor-level analysis.
>   Our results suggest that reframing hate speech detection as a diagnostic reasoning task, rather than a monolithic classification problem, provides a robust, explainable, and extensible alternative for content moderation.

