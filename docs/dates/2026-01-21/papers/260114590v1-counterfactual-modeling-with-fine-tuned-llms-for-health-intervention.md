---
layout: default
title: Counterfactual Modeling with Fine-Tuned LLMs for Health Intervention Design and Sensor Data Augmentation
---

# Counterfactual Modeling with Fine-Tuned LLMs for Health Intervention Design and Sensor Data Augmentation
**arXiv**：[2601.14590v1](https://arxiv.org/abs/2601.14590) · [PDF](https://arxiv.org/pdf/2601.14590.pdf)  
**作者**：Shovito Barua Soumma, Asiful Arefeen, Stephanie M. Carpenter, Melanie Hingle, Hassan Ghasemzadeh  

**一句话要点**：提出基于微调LLM的反事实建模方法，用于健康干预设计和传感器数据增强

**关键词**：反事实解释, 大语言模型微调, 健康干预设计, 数据增强, 传感器数据分析, 模型鲁棒性

## 3 点简述
- 核心问题：反事实解释在健康领域需高可信度和临床可操作性，传统优化方法灵活性不足。
- 方法要点：微调LLM（如LLaMA-3.1-8B）生成反事实，评估干预质量、特征多样性和增强效果。
- 实验或效果：在AI-READI数据集上，微调LLM生成反事实的合理性达99%，数据增强使F1分数平均恢复20%。

## 摘要（原文）

> Counterfactual explanations (CFEs) provide human-centric interpretability by identifying the minimal, actionable changes required to alter a machine learning model's prediction. Therefore, CFs can be used as (i) interventions for abnormality prevention and (ii) augmented data for training robust models. We conduct a comprehensive evaluation of CF generation using large language models (LLMs), including GPT-4 (zero-shot and few-shot) and two open-source models-BioMistral-7B and LLaMA-3.1-8B, in both pretrained and fine-tuned configurations. Using the multimodal AI-READI clinical dataset, we assess CFs across three dimensions: intervention quality, feature diversity, and augmentation effectiveness. Fine-tuned LLMs, particularly LLaMA-3.1-8B, produce CFs with high plausibility (up to 99%), strong validity (up to 0.99), and realistic, behaviorally modifiable feature adjustments. When used for data augmentation under controlled label-scarcity settings, LLM-generated CFs substantially restore classifier performance, yielding an average 20% F1 recovery across three scarcity scenarios. Compared with optimization-based baselines such as DiCE, CFNOW, and NICE, LLMs offer a flexible, model-agnostic approach that generates more clinically actionable and semantically coherent counterfactuals. Overall, this work demonstrates the promise of LLM-driven counterfactuals for both interpretable intervention design and data-efficient model training in sensor-based digital health.
>   Impact: SenseCF fine-tunes an LLM to generate valid, representative counterfactual explanations and supplement minority class in an imbalanced dataset for improving model training and boosting model robustness and predictive performance

