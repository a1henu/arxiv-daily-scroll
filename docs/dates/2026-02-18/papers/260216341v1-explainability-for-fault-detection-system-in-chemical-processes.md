---
layout: default
title: Explainability for Fault Detection System in Chemical Processes
---

# Explainability for Fault Detection System in Chemical Processes
**arXiv**：[2602.16341v1](https://arxiv.org/abs/2602.16341) · [PDF](https://arxiv.org/pdf/2602.16341.pdf)  
**作者**：Georgios Gravanis, Dimitrios Kyriakou, Spyros Voutetakis, Simira Papadopoulou, Konstantinos Diamantaras  

**一句话要点**：应用集成梯度和SHAP方法解释化学过程故障检测的LSTM分类器决策

**关键词**：可解释人工智能, 故障检测, 长短期记忆网络, 化学过程, 集成梯度, SHAP

## 3 点简述
- 核心问题：解释高精度LSTM分类器在化学过程故障检测中的决策，以识别故障子系统。
- 方法要点：比较两种模型无关的XAI方法（集成梯度和SHAP），分析其在田纳西伊士曼过程基准上的应用。
- 实验或效果：SHAP方法在某些情况下更接近故障根源，方法可推广至类似问题。

## 摘要（原文）

> In this work, we apply and compare two state-of-the-art eXplainability Artificial Intelligence (XAI) methods, the Integrated Gradients (IG) and the SHapley Additive exPlanations (SHAP), that explain the fault diagnosis decisions of a highly accurate Long Short-Time Memory (LSTM) classifier. The classifier is trained to detect faults in a benchmark non-linear chemical process, the Tennessee Eastman Process (TEP). It is highlighted how XAI methods can help identify the subsystem of the process where the fault occurred. Using our knowledge of the process, we note that in most cases the same features are indicated as the most important for the decision, while insome cases the SHAP method seems to be more informative and closer to the root cause of the fault. Finally, since the used XAI methods are model-agnostic, the proposed approach is not limited to the specific process and can also be used in similar problems.

