---
layout: default
title: Vichara: Appellate Judgment Prediction and Explanation for the Indian Judicial System
---

# Vichara: Appellate Judgment Prediction and Explanation for the Indian Judicial System
**arXiv**：[2602.18346v1](https://arxiv.org/abs/2602.18346) · [PDF](https://arxiv.org/pdf/2602.18346.pdf)  
**作者**：Pavithra PM Nair, Preethu Rose Anish  

**一句话要点**：提出Vichara框架，为印度司法系统预测和解释上诉判决以应对案件积压。

**关键词**：上诉判决预测, 法律人工智能, 结构化解释, 印度司法系统, 大型语言模型

## 3 点简述
- 核心问题：印度法院案件积压严重，上诉判决预测需准确且可解释。
- 方法要点：将上诉案件文档分解为决策点，结构化表示以支持预测和解释。
- 实验或效果：在PredEx和ILDC_expert数据集上超越基准，GPT-4o mini性能最佳，解释性获人类评估认可。

## 摘要（原文）

> In jurisdictions like India, where courts face an extensive backlog of cases, artificial intelligence offers transformative potential for legal judgment prediction. A critical subset of this backlog comprises appellate cases, which are formal decisions issued by higher courts reviewing the rulings of lower courts. To this end, we present Vichara, a novel framework tailored to the Indian judicial system that predicts and explains appellate judgments. Vichara processes English-language appellate case proceeding documents and decomposes them into decision points. Decision points are discrete legal determinations that encapsulate the legal issue, deciding authority, outcome, reasoning, and temporal context. The structured representation isolates the core determinations and their context, enabling accurate predictions and interpretable explanations. Vichara's explanations follow a structured format inspired by the IRAC (Issue-Rule-Application-Conclusion) framework and adapted for Indian legal reasoning. This enhances interpretability, allowing legal professionals to assess the soundness of predictions efficiently. We evaluate Vichara on two datasets, PredEx and the expert-annotated subset of the Indian Legal Documents Corpus (ILDC_expert), using four large language models: GPT-4o mini, Llama-3.1-8B, Mistral-7B, and Qwen2.5-7B. Vichara surpasses existing judgment prediction benchmarks on both datasets, with GPT-4o mini achieving the highest performance (F1: 81.5 on PredEx, 80.3 on ILDC_expert), followed by Llama-3.1-8B. Human evaluation of the generated explanations across Clarity, Linking, and Usefulness metrics highlights GPT-4o mini's superior interpretability.

