---
layout: default
title: Dementia-R1: Reinforced Pretraining and Reasoning from Unstructured Clinical Notes for Real-World Dementia Prognosis
---

# Dementia-R1: Reinforced Pretraining and Reasoning from Unstructured Clinical Notes for Real-World Dementia Prognosis
**arXiv**：[2601.03018v1](https://arxiv.org/abs/2601.03018) · [PDF](https://arxiv.org/pdf/2601.03018.pdf)  
**作者**：Choonghan Kim, Hyunmin Hwang, Hangeol Chang, Jaemin Kim, Jinse Park, Jae-Sung Lim, Jong Chul Ye  

**一句话要点**：提出Dementia-R1框架，通过强化学习从非结构化临床笔记解决痴呆症纵向预测问题。

**关键词**：痴呆症预测, 强化学习, 临床笔记分析, 纵向预测, 冷启动策略

## 3 点简述
- 核心问题：大语言模型在痴呆症纵向预测中难以处理非单调症状轨迹。
- 方法要点：采用冷启动强化学习策略，预训练模型预测临床指标以增强推理能力。
- 实验或效果：在真实数据集上F1分数达77.03%，7B模型在ADNI基准上媲美GPT-4o。

## 摘要（原文）

> While Large Language Models (LLMs) have shown strong performance on clinical text understanding, they struggle with longitudinal prediction tasks such as dementia prognosis, which require reasoning over complex, non-monotonic symptom trajectories across multiple visits. Standard supervised training lacks explicit annotations for symptom evolution, while direct Reinforcement Learning (RL) is hindered by sparse binary rewards. To address this challenge, we introduce Dementia-R1, an RL-based framework for longitudinal dementia prognosis from unstructured clinical notes. Our approach adopts a Cold-Start RL strategy that pre-trains the model to predict verifiable clinical indices extracted from patient histories, enhancing the capability to reason about disease progression before determining the final clinical status. Extensive experiments demonstrate that Dementia-R1 achieves an F1 score of 77.03% on real-world unstructured clinical datasets. Notably, on the ADNI benchmark, our 7B model rivals GPT-4o, effectively capturing fluctuating cognitive trajectories. Code is available at https://anonymous.4open.science/r/dementiar1-CDB5

