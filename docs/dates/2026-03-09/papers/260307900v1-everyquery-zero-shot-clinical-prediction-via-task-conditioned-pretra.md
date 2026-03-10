---
layout: default
title: EveryQuery: Zero-Shot Clinical Prediction via Task-Conditioned Pretraining over Electronic Health Records
---

# EveryQuery: Zero-Shot Clinical Prediction via Task-Conditioned Pretraining over Electronic Health Records
**arXiv**：[2603.07900v1](https://arxiv.org/abs/2603.07900) · [PDF](https://arxiv.org/pdf/2603.07900.pdf)  
**作者**：Payal Chandak, Gregory Kondas, Isaac Kohane, Matthew McDermott  

**一句话要点**：提出EveryQuery，通过任务条件预训练实现电子健康记录的零样本临床预测

**关键词**：电子健康记录, 零样本预测, 任务条件预训练, 临床决策支持, 自回归推理替代

## 3 点简述
- 核心问题：现有EHR基础模型零样本预测依赖自回归推理，计算成本高、统计噪声大且无法直接提示。
- 方法要点：采用任务条件预训练，输入患者历史和结构化查询，单次前向传播直接估计未来结果概率。
- 实验或效果：在MIMIC-IV上，对39个随机任务，82%优于基线，平均AUC提升+0.16，但对多代码析取推理任务表现不足。

## 摘要（原文）

> Foundation models pretrained on electronic health records (EHR) have demonstrated zero-shot clinical prediction capabilities by generating synthetic patient futures and aggregating statistics over sampled trajectories. However, this autoregressive inference procedure is computationally expensive, statistically noisy, and not natively promptable because users cannot directly condition predictions on specific clinical questions. In this preliminary work, we introduce EveryQuery, an EHR foundation model that achieves zero-shot inference through task-conditioned pre-training. Rather than generating future events, EveryQuery takes as input a patient's history and a structured query specifying a clinical task, and directly estimates the likelihood of the outcome occurring in the future window via a single forward pass. EveryQuery realizes this capability by pre-training over randomly sampled combinations of query tasks and patient contexts, directly training the model to produce correct answers to arbitrary input prompts. This enables zero-shot prediction for any task in the query space without finetuning, linear probing, or trajectory generation. On MIMIC-IV, EveryQuery outperforms an autoregressive baseline on 82% of 39 randomly sampled prediction tasks, with a mean AUC improvement of +0.16 (95% CI: [0.10,0.22]). This advantage remains consistent on tasks that were explicitly held out from the pre-training distribution. Further, EveryQuery's performance gains are most pronounced for rare clinical events, affirming and demonstrating a solution to the fundamental limitation of autoregressive inference for low-prevalence outcomes. However, at present, EveryQuery underperforms on tasks requiring disjunctive reasoning over multiple codes, such as 30-day readmission, exposing a concrete expressiveness limitation of the current query language.

