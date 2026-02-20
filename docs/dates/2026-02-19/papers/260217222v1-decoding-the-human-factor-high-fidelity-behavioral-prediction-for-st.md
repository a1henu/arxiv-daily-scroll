---
layout: default
title: Decoding the Human Factor: High Fidelity Behavioral Prediction for Strategic Foresight
---

# Decoding the Human Factor: High Fidelity Behavioral Prediction for Strategic Foresight
**arXiv**：[2602.17222v1](https://arxiv.org/abs/2602.17222) · [PDF](https://arxiv.org/pdf/2602.17222.pdf)  
**作者**：Ben Yellin, Ehud Ezra, Mark Foreman, Shula Grinapol  

**一句话要点**：提出大型行为模型以高保真预测个体战略决策，应用于战略预见等领域。

**关键词**：行为预测, 战略决策, 心理特质建模, 微调训练, 高保真模拟, 大型语言模型

## 3 点简述
- 核心问题：LLMs在预测个体一致行为时存在身份漂移和复杂性上限，难以处理心理特质与情境约束的交互。
- 方法要点：通过行为嵌入替代瞬时提示，基于结构化高维特质配置文件微调，学习从心理档案到离散动作的映射。
- 实验或效果：在保留场景评估中，LBM相比未适应骨干模型提升预测性能，且性能随特质维度增加而持续改善。

## 摘要（原文）

> Predicting human decision-making in high-stakes environments remains a central challenge for artificial intelligence. While large language models (LLMs) demonstrate strong general reasoning, they often struggle to generate consistent, individual-specific behavior, particularly when accurate prediction depends on complex interactions between psychological traits and situational constraints. Prompting-based approaches can be brittle in this setting, exhibiting identity drift and limited ability to leverage increasingly detailed persona descriptions. To address these limitations, we introduce the Large Behavioral Model (LBM), a behavioral foundation model fine-tuned to predict individual strategic choices with high fidelity. LBM shifts from transient persona prompting to behavioral embedding by conditioning on a structured, high-dimensional trait profile derived from a comprehensive psychometric battery. Trained on a proprietary dataset linking stable dispositions, motivational states, and situational constraints to observed choices, LBM learns to map rich psychological profiles to discrete actions across diverse strategic dilemmas. In a held-out scenario evaluation, LBM fine-tuning improves behavioral prediction relative to the unadapted Llama-3.1-8B-Instruct backbone and performs comparably to frontier baselines when conditioned on Big Five traits. Moreover, we find that while prompting-based baselines exhibit a complexity ceiling, LBM continues to benefit from increasingly dense trait profiles, with performance improving as additional trait dimensions are provided. Together, these results establish LBM as a scalable approach for high-fidelity behavioral simulation, enabling applications in strategic foresight, negotiation analysis, cognitive security, and decision support.

