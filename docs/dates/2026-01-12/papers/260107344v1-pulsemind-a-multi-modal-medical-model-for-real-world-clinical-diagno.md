---
layout: default
title: PulseMind: A Multi-Modal Medical Model for Real-World Clinical Diagnosis
---

# PulseMind: A Multi-Modal Medical Model for Real-World Clinical Diagnosis
**arXiv**：[2601.07344v1](https://arxiv.org/abs/2601.07344) · [PDF](https://arxiv.org/pdf/2601.07344.pdf)  
**作者**：Jiao Xu, Junwei Liu, Jiangwei Lao, Qi Zhu, Yunpeng Zhao, Congyun Jin, Shinan Liu, Zhihong Lu, Lihe Zhang, Xin Chen, Jian Wang, Ping Wang  

**一句话要点**：提出PulseMind多模态医疗模型，以解决真实世界临床诊断中多轮交互与异质输入整合的挑战。

**关键词**：多模态医疗模型, 临床诊断, 多轮咨询, 强化学习, 医疗数据集, 评估基准

## 3 点简述
- 核心问题：现有医疗多模态模型专注于专科图像分析，未充分处理真实临床诊断的多轮交互与异质输入复杂性。
- 方法要点：构建MediScope数据集和PulseMind基准，并设计基于比较的强化策略优化训练框架。
- 实验或效果：在诊断咨询基准和公共医疗基准上表现出竞争性性能，验证了模型的有效性。

## 摘要（原文）

> Recent advances in medical multi-modal models focus on specialized image analysis like dermatology, pathology, or radiology. However, they do not fully capture the complexity of real-world clinical diagnostics, which involve heterogeneous inputs and require ongoing contextual understanding during patient-physician interactions. To bridge this gap, we introduce PulseMind, a new family of multi-modal diagnostic models that integrates a systematically curated dataset, a comprehensive evaluation benchmark, and a tailored training framework. Specifically, we first construct a diagnostic dataset, MediScope, which comprises 98,000 real-world multi-turn consultations and 601,500 medical images, spanning over 10 major clinical departments and more than 200 sub-specialties. Then, to better reflect the requirements of real-world clinical diagnosis, we develop the PulseMind Benchmark, a multi-turn diagnostic consultation benchmark with a four-dimensional evaluation protocol comprising proactiveness, accuracy, usefulness, and language quality. Finally, we design a training framework tailored for multi-modal clinical diagnostics, centered around a core component named Comparison-based Reinforcement Policy Optimization (CRPO). Compared to absolute score rewards, CRPO uses relative preference signals from multi-dimensional com-parisons to provide stable and human-aligned training guidance. Extensive experiments demonstrate that PulseMind achieves competitive performance on both the diagnostic consultation benchmark and public medical benchmarks.

