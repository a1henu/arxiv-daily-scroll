---
layout: default
title: Sequential Counterfactual Inference for Temporal Clinical Data: Addressing the Time Traveler Dilemma
---

# Sequential Counterfactual Inference for Temporal Clinical Data: Addressing the Time Traveler Dilemma
**arXiv**：[2602.21168v1](https://arxiv.org/abs/2602.21168) · [PDF](https://arxiv.org/pdf/2602.21168.pdf)  
**作者**：Jingya Cheng, Alaleh Azhir, Jiazi Tian, Hossein Estiri  

**一句话要点**：提出序列反事实框架以解决临床时序数据中的时间旅行者困境

**关键词**：反事实推理, 时序临床数据, 电子健康记录, 干预传播, 长COVID, 心肾级联

## 3 点简述
- 核心问题：传统反事实方法假设特征独立和同时可修改，不适用于纵向临床数据。
- 方法要点：区分不可变特征与可控特征，建模干预在时间上的传播。
- 实验或效果：应用于COVID-19患者数据，识别出心肾级联效应，提供临床可行见解。

## 摘要（原文）

> Counterfactual inference enables clinicians to ask "what if" questions about patient outcomes, but standard methods assume feature independence and simultaneous modifiability -- assumptions violated by longitudinal clinical data. We introduce the Sequential Counterfactual Framework, which respects temporal dependencies in electronic health records by distinguishing immutable features (chronic diagnoses) from controllable features (lab values) and modeling how interventions propagate through time. Applied to 2,723 COVID-19 patients (383 Long COVID heart failure cases, 2,340 matched controls), we demonstrate that 38-67% of patients with chronic conditions would require biologically impossible counterfactuals under naive methods. We identify a cardiorenal cascade (CKD -> AKI -> HF) with relative risks of 2.27 and 1.19 at each step, illustrating temporal propagation that sequential -- but not naive -- counterfactuals can capture. Our framework transforms counterfactual explanation from "what if this feature were different?" to "what if we had intervened earlier, and how would that propagate forward?" --  yielding clinically actionable insights grounded in biological plausibility.

