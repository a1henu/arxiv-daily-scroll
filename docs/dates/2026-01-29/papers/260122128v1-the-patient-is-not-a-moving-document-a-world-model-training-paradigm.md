---
layout: default
title: The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR
---

# The Patient is not a Moving Document: A World Model Training Paradigm for Longitudinal EHR
**arXiv**：[2601.22128v1](https://arxiv.org/abs/2601.22128) · [PDF](https://arxiv.org/pdf/2601.22128.pdf)  
**作者**：Irsyad Adam, Zekai Chen, David Laprade, Shaun Porwal, David Laub, Erik Reinertsen, Arda Pekis, Kevin Brown  

**一句话要点**：提出SMB-Structure世界模型，结合JEPA与SFT训练范式，以模拟纵向电子健康记录中的患者动态系统。

**关键词**：电子健康记录, 世界模型, 联合嵌入预测, 患者动态模拟, 临床基础模型

## 3 点简述
- 核心问题：现有LLM将患者视为静态文档，而非动态系统，无法有效模拟疾病轨迹演变。
- 方法要点：结合联合嵌入预测架构（JEPA）与下一个令牌预测（SFT），在潜在空间预测未来患者状态。
- 实验或效果：在大型肿瘤和肺栓塞队列中验证，学习到的嵌入能捕获疾病动态，优于自回归基线。

## 摘要（原文）

> Large language models (LLMs) trained with next-word-prediction have achieved success as clinical foundation models. Representations from these language backbones yield strong linear probe performance across biomedical tasks, suggesting that patient semantics emerge from next-token prediction at scale. However, this paradigm treats patients as a document to be summarized rather than a dynamical system to be simulated; a patient's trajectory emerges from their state evolving under interventions and time, requiring models that simulate dynamics rather than predict tokens. To address this, we introduce SMB-Structure, a world model for structured EHR that grounds a joint-embedding prediction architecture (JEPA) with next-token prediction (SFT). SFT grounds our model to reconstruct future patient states in token space, while JEPA predicts those futures in latent space from the initial patient representation alone, forcing trajectory dynamics to be encoded before the next state is observed. We validate across two large-scale cohorts: Memorial Sloan Kettering (23,319 oncology patients; 323,000+ patient-years) and INSPECT (19,402 pulmonary embolism patients). Using a linear probe evaluated at multiple points along the disease trajectory, we demonstrate that our training paradigm learns embeddings that capture disease dynamics not recoverable by autoregressive baselines, enabling SMB-Structure to achieve competitive performance on complex tasks characterized by high patient heterogeneity. Model weights are available at https://huggingface.co/standardmodelbio/SMB-v1-1.7B-Structure.

