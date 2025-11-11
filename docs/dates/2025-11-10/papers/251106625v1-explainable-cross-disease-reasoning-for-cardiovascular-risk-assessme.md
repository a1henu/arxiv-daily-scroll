---
layout: default
title: Explainable Cross-Disease Reasoning for Cardiovascular Risk Assessment from LDCT
---

# Explainable Cross-Disease Reasoning for Cardiovascular Risk Assessment from LDCT
**arXiv**：[2511.06625v1](https://arxiv.org/abs/2511.06625) · [PDF](https://arxiv.org/pdf/2511.06625.pdf)  
**作者**：Yifei Zhang, Jiashuo Zhang, Xiaofeng Yang, Liang Zhao  

**一句话要点**：提出可解释跨疾病推理框架，从LDCT联合评估心肺风险

**关键词**：低剂量CT, 心血管风险评估, 可解释AI, 跨疾病推理, 肺心联合分析

## 3 点简述
- 现有方法独立处理肺和心血管任务，忽略生理交互和共享成像生物标志物
- 框架模拟临床诊断思维，集成肺感知、知识推理和心脏表征模块
- 在NLST队列中实现CVD筛查和死亡率预测的SOTA性能，提供可验证推理

## 摘要（原文）

> Low-dose chest computed tomography (LDCT) inherently captures both pulmonary
> and cardiac structures, offering a unique opportunity for joint assessment of
> lung and cardiovascular health. However, most existing approaches treat these
> domains as independent tasks, overlooking their physiological interplay and
> shared imaging biomarkers. We propose an Explainable Cross-Disease Reasoning
> Framework that enables interpretable cardiopulmonary risk assessment from a
> single LDCT scan. The framework introduces an agentic reasoning process that
> emulates clinical diagnostic thinking-first perceiving pulmonary findings, then
> reasoning through established medical knowledge, and finally deriving a
> cardiovascular judgment with explanatory rationale. It integrates three
> synergistic components: a pulmonary perception module that summarizes lung
> abnormalities, a knowledge-guided reasoning module that infers their
> cardiovascular implications, and a cardiac representation module that encodes
> structural biomarkers. Their outputs are fused to produce a holistic
> cardiovascular risk prediction that is both accurate and physiologically
> grounded. Experiments on the NLST cohort demonstrate that the proposed
> framework achieves state-of-the-art performance for CVD screening and mortality
> prediction, outperforming single-disease and purely image-based baselines.
> Beyond quantitative gains, the framework provides human-verifiable reasoning
> that aligns with cardiological understanding, revealing coherent links between
> pulmonary abnormalities and cardiac stress mechanisms. Overall, this work
> establishes a unified and explainable paradigm for cardiovascular analysis from
> LDCT, bridging the gap between image-based prediction and mechanism-based
> medical interpretation.

