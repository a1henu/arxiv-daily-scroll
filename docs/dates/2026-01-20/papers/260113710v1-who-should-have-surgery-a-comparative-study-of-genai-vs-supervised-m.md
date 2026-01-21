---
layout: default
title: Who Should Have Surgery? A Comparative Study of GenAI vs Supervised ML for CRS Surgical Outcome Prediction
---

# Who Should Have Surgery? A Comparative Study of GenAI vs Supervised ML for CRS Surgical Outcome Prediction
**arXiv**：[2601.13710v1](https://arxiv.org/abs/2601.13710) · [PDF](https://arxiv.org/pdf/2601.13710.pdf)  
**作者**：Sayeed Shafayet Chowdhury, Snehasis Mukhopadhyay, Shiaofen Fang, Vijay R. Ramakrishnan  

**一句话要点**：比较生成式AI与监督式ML在慢性鼻窦炎手术效果预测中的性能，提出ML优先、GenAI增强的工作流程。

**关键词**：慢性鼻窦炎手术预测, 监督式机器学习, 生成式人工智能, 临床决策支持, 模型校准, 解释性分析

## 3 点简述
- 研究核心问题：基于术前临床数据预测慢性鼻窦炎手术效果，识别应避免手术的患者。
- 方法要点：对比监督式ML（逻辑回归、树集成、MLP）与生成式AI（ChatGPT等）在相同结构化输入下的预测性能。
- 实验效果：MLP模型在准确率、校准和决策曲线净效益上优于生成式AI，后者在零样本设置下表现不佳但解释性较好。

## 摘要（原文）

> Artificial intelligence has reshaped medical imaging, yet the use of AI on clinical data for prospective decision support remains limited. We study pre-operative prediction of clinically meaningful improvement in chronic rhinosinusitis (CRS), defining success as a more than 8.9-point reduction in SNOT-22 at 6 months (MCID). In a prospectively collected cohort where all patients underwent surgery, we ask whether models using only pre-operative clinical data could have identified those who would have poor outcomes, i.e. those who should have avoided surgery. We benchmark supervised ML (logistic regression, tree ensembles, and an in-house MLP) against generative AI (ChatGPT, Claude, Gemini, Perplexity), giving each the same structured inputs and constraining outputs to binary recommendations with confidence. Our best ML model (MLP) achieves 85 % accuracy with superior calibration and decision-curve net benefit. GenAI models underperform on discrimination and calibration across zero-shot setting. Notably, GenAI justifications align with clinician heuristics and the MLP's feature importance, repeatedly highlighting baseline SNOT-22, CT/endoscopy severity, polyp phenotype, and physchology/pain comorbidities. We provide a reproducible tabular-to-GenAI evaluation protocol and subgroup analyses. Findings support an ML-first, GenAI- augmented workflow: deploy calibrated ML for primary triage of surgical candidacy, with GenAI as an explainer to enhance transparency and shared decision-making.

