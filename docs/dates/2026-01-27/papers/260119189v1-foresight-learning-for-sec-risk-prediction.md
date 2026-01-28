---
layout: default
title: Foresight Learning for SEC Risk Prediction
---

# Foresight Learning for SEC Risk Prediction
**arXiv**：[2601.19189v1](https://arxiv.org/abs/2601.19189) · [PDF](https://arxiv.org/pdf/2601.19189.pdf)  
**作者**：Benjamin Turtel, Paul Wilczewski, Danny Franklin, Kris Skotheim  

**一句话要点**：提出前瞻学习框架，利用公开SEC文件自动训练风险预测模型

**关键词**：SEC风险预测, 前瞻学习, 自动化数据生成, 大型语言模型, 概率校准

## 3 点简述
- 核心问题：SEC风险披露缺乏量化概率，难以进行概率分析
- 方法要点：构建自动化管道，从风险因素生成查询并基于后续披露自动标注
- 实验或效果：模型在概率准确性和校准上优于GPT-5等基准，可单GPU部署

## 摘要（原文）

> Risk disclosures in SEC filings describe potential adverse events but rarely quantify their likelihood, limiting their usefulness for probabilistic analysis. A central obstacle is the absence of large-scale, risk-level supervision linking disclosed risks to realized outcomes.
>   We introduce a fully automated data generation pipeline that converts qualitative SEC risk disclosures into temporally grounded supervision using only public data. For each filing, the pipeline generates firm-specific, time-bounded risk queries from the Risk Factors section and labels them by automatically resolving outcomes against subsequent disclosures.
>   Using this dataset of risk queries and outcomes grounded in SEC filings, we train a compact large language model to estimate the probability that a disclosed risk will materialize within a specified horizon. Despite its modest size, the resulting model substantially improves over pretrained and heuristic baselines, and outperforms frontier general-purpose models, including GPT-5, on probabilistic accuracy and calibration.
>   More broadly, this work demonstrates that Foresight Learning enables scalable and fully automated training of domain-specific expert models using only raw, chronological, in-domain text -- without proprietary data, external corpora, or manual annotation. The resulting models achieve frontier-level performance while remaining deployable on a single GPU. This result suggests a general pathway for learning calibrated, decision-relevant signals from naturally occurring enterprise documents.
>   To support transparency and reproducibility, we open-source the evaluation dataset used in this study.
>   Evaluation Data: https://huggingface.co/datasets/LightningRodLabs/sec_risk_questions_test_set
>   Data Generation Platform: https://lightningrod.ai/
>   SDK: https://github.com/lightning-rod-labs/lightningrod-python-sdk

