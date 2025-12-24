---
layout: default
title: Reason2Decide: Rationale-Driven Multi-Task Learning
---

# Reason2Decide: Rationale-Driven Multi-Task Learning
**arXiv**：[2512.20074v1](https://arxiv.org/abs/2512.20074) · [PDF](https://arxiv.org/pdf/2512.20074.pdf)  
**作者**：H M Quamran Hasan, Housam Khalifa Bashier, Jiayi Dai, Mi-Young Kim, Randy Goebel  

**一句话要点**：提出Reason2Decide两阶段训练框架，以解决临床决策支持系统中预测与解释对齐的挑战。

**关键词**：临床决策支持, 自解释模型, 多任务学习, 计划采样, 解释对齐, 医疗数据集

## 3 点简述
- 核心问题：LLM在临床决策中面临预测准确性与解释对齐的挑战，现有方法存在暴露偏差。
- 方法要点：采用两阶段训练，首阶段训练解释生成，次阶段联合训练预测与解释，使用计划采样减少偏差。
- 实验或效果：在医疗数据集上优于基线，模型小40倍，减少对人标注的依赖，提升解释保真度。

## 摘要（原文）

> Despite the wide adoption of Large Language Models (LLM)s, clinical decision support systems face a critical challenge: achieving high predictive accuracy while generating explanations aligned with the predictions. Current approaches suffer from exposure bias leading to misaligned explanations. We propose Reason2Decide, a two-stage training framework that addresses key challenges in self-rationalization, including exposure bias and task separation. In Stage-1, our model is trained on rationale generation, while in Stage-2, we jointly train on label prediction and rationale generation, applying scheduled sampling to gradually transition from conditioning on gold labels to model predictions. We evaluate Reason2Decide on three medical datasets, including a proprietary triage dataset and public biomedical QA datasets. Across model sizes, Reason2Decide outperforms other fine-tuning baselines and some zero-shot LLMs in prediction (F1) and rationale fidelity (BERTScore, BLEU, LLM-as-a-Judge). In triage, Reason2Decide is rationale source-robust across LLM-generated, nurse-authored, and nurse-post-processed rationales. In our experiments, while using only LLM-generated rationales in Stage-1, Reason2Decide outperforms other fine-tuning variants. This indicates that LLM-generated rationales are suitable for pretraining models, reducing reliance on human annotations. Remarkably, Reason2Decide achieves these gains with models 40x smaller than contemporary foundation models, making clinical reasoning more accessible for resource-constrained deployments while still providing explainable decision support.

