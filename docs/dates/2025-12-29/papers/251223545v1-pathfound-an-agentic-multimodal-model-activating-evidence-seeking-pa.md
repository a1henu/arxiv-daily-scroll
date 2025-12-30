---
layout: default
title: PathFound: An Agentic Multimodal Model Activating Evidence-seeking Pathological Diagnosis
---

# PathFound: An Agentic Multimodal Model Activating Evidence-seeking Pathological Diagnosis
**arXiv**：[2512.23545v1](https://arxiv.org/abs/2512.23545) · [PDF](https://arxiv.org/pdf/2512.23545.pdf)  
**作者**：Shengyi Hua, Jianfeng Wu, Tianle Shen, Kangzhe Hu, Zhongzhen Huang, Shujuan Ni, Zhihong Zhang, Yuan Li, Zhe Wang, Xiaofan Zhang  

**一句话要点**：提出PathFound代理多模态模型，以支持病理诊断中的证据寻求推理。

**关键词**：病理诊断, 多模态模型, 证据寻求推理, 强化学习, 视觉语言模型

## 3 点简述
- 核心问题：现有病理基础模型依赖静态推理，缺乏临床诊断中的重复观察和证据获取能力。
- 方法要点：集成病理视觉基础模型、视觉语言模型和强化学习推理模型，实现主动信息获取和诊断细化。
- 实验或效果：在多个大型多模态模型中提升诊断准确性，在多样临床场景中达到最先进性能。

## 摘要（原文）

> Recent pathological foundation models have substantially advanced visual representation learning and multimodal interaction. However, most models still rely on a static inference paradigm in which whole-slide images are processed once to produce predictions, without reassessment or targeted evidence acquisition under ambiguous diagnoses. This contrasts with clinical diagnostic workflows that refine hypotheses through repeated slide observations and further examination requests. We propose PathFound, an agentic multimodal model designed to support evidence-seeking inference in pathological diagnosis. PathFound integrates the power of pathological visual foundation models, vision-language models, and reasoning models trained with reinforcement learning to perform proactive information acquisition and diagnosis refinement by progressing through the initial diagnosis, evidence-seeking, and final decision stages. Across several large multimodal models, adopting this strategy consistently improves diagnostic accuracy, indicating the effectiveness of evidence-seeking workflows in computational pathology. Among these models, PathFound achieves state-of-the-art diagnostic performance across diverse clinical scenarios and demonstrates strong potential to discover subtle details, such as nuclear features and local invasions.

