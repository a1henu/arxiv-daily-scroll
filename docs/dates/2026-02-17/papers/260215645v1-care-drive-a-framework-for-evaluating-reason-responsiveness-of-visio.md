---
layout: default
title: CARE Drive A Framework for Evaluating Reason-Responsiveness of Vision Language Models in Automated Driving
---

# CARE Drive A Framework for Evaluating Reason-Responsiveness of Vision Language Models in Automated Driving
**arXiv**：[2602.15645v1](https://arxiv.org/abs/2602.15645) · [PDF](https://arxiv.org/pdf/2602.15645.pdf)  
**作者**：Lucas Elbert Suryana, Farah Bierenga, Sanne van Buuren, Pepijn Kooij, Elsefien Tulleners, Federico Scari, Simeon Calvert, Bart van Arem, Arkady Zgonnikov  

**一句话要点**：提出CARE Drive框架以评估自动驾驶中视觉语言模型的原因响应性

**关键词**：自动驾驶评估, 视觉语言模型, 原因响应性, 上下文扰动, 安全关键系统, 模型不可知框架

## 3 点简述
- 现有评估方法主要关注结果性能，未验证模型决策是否基于人类相关原因
- CARE Drive通过上下文扰动比较基线模型与原因增强模型，评估原因对决策的因果影响
- 在超车场景实验中，人类原因显著改善模型决策，但响应性因上下文因素而异

## 摘要（原文）

> Foundation models, including vision language models, are increasingly used in automated driving to interpret scenes, recommend actions, and generate natural language explanations. However, existing evaluation methods primarily assess outcome based performance, such as safety and trajectory accuracy, without determining whether model decisions reflect human relevant considerations. As a result, it remains unclear whether explanations produced by such models correspond to genuine reason responsive decision making or merely post hoc rationalizations. This limitation is especially significant in safety critical domains because it can create false confidence. To address this gap, we propose CARE Drive, Context Aware Reasons Evaluation for Driving, a model agnostic framework for evaluating reason responsiveness in vision language models applied to automated driving. CARE Drive compares baseline and reason augmented model decisions under controlled contextual variation to assess whether human reasons causally influence decision behavior. The framework employs a two stage evaluation process. Prompt calibration ensures stable outputs. Systematic contextual perturbation then measures decision sensitivity to human reasons such as safety margins, social pressure, and efficiency constraints. We demonstrate CARE Drive in a cyclist overtaking scenario involving competing normative considerations. Results show that explicit human reasons significantly influence model decisions, improving alignment with expert recommended behavior. However, responsiveness varies across contextual factors, indicating uneven sensitivity to different types of reasons. These findings provide empirical evidence that reason responsiveness in foundation models can be systematically evaluated without modifying model parameters.

