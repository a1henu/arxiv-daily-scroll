---
layout: default
title: C-GRASP: Clinically-Grounded Reasoning for Affective Signal Processing
---

# C-GRASP: Clinically-Grounded Reasoning for Affective Signal Processing
**arXiv**：[2601.10342v1](https://arxiv.org/abs/2601.10342) · [PDF](https://arxiv.org/pdf/2601.10342.pdf)  
**作者**：Cheng Lin Cheng, Ting Chuan Lin, Chai Kai Chang  

**一句话要点**：提出C-GRASP以解决大语言模型在心率变异性解释中的生理幻觉问题

**关键词**：心率变异性解释, 临床推理增强, 检索增强生成, 情感信号处理, 个体化基线建模, 生理幻觉缓解

## 3 点简述
- 核心问题：大语言模型在心率变异性解释中易产生生理幻觉，如呼吸性窦性心律失常污染和忽略个体化基线。
- 方法要点：采用基于检索增强生成的防护管道，通过Z分数优先级层次和个体化Delta Z分数模块增强临床推理。
- 实验或效果：在DREAMER数据集上评估，C-GRASP在情感分类和临床推理一致性方面表现优于基线模型。

## 摘要（原文）

> Heart rate variability (HRV) is a pivotal noninvasive marker for autonomic monitoring; however, applying Large Language Models (LLMs) to HRV interpretation is hindered by physiological hallucinations. These include respiratory sinus arrhythmia (RSA) contamination, short-data instability in nonlinear metrics, and the neglect of individualized baselines in favor of population norms. We propose C-GRASP (Clinically-Grounded Reasoning for Affective Signal Processing), a guardrailed RAG-enhanced pipeline that decomposes HRV interpretation into eight traceable reasoning steps. Central to C-GRASP is a Z-score Priority Hierarchy that enforces the weighting of individualized baseline shifts over normative statistics. The system effectively mitigates spectral hallucinations through automated RSA-aware guardrails, preventing contamination of frequency-domain indices. Evaluated on 414 trials from the DREAMER dataset, C-GRASP integrated with high-scale reasoning models (e.g., MedGemma3-thinking) achieved superior performance in 4-class emotion classification (37.3% accuracy) and a Clinical Reasoning Consistency (CRC) score of 69.6%. Ablation studies confirm that the individualized Delta Z-score module serves as the critical logical anchor, preventing the "population bias" common in native LLMs. Ultimately, C-GRASP transitions affective computing from black-box classification to transparent, evidence-based clinical decision support, paving the way for safer AI integration in biomedical engineering.

