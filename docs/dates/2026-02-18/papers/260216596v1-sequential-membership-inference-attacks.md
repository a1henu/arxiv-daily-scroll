---
layout: default
title: Sequential Membership Inference Attacks
---

# Sequential Membership Inference Attacks
**arXiv**：[2602.16596v1](https://arxiv.org/abs/2602.16596) · [PDF](https://arxiv.org/pdf/2602.16596.pdf)  
**作者**：Thomas Michel, Debabrota Basu, Emilie Kaufmann  

**一句话要点**：提出SeMI*攻击以利用模型更新序列增强成员推理攻击和隐私审计

**关键词**：成员推理攻击, 隐私审计, 模型更新序列, 动态AI模型, DP-SGD训练

## 3 点简述
- 针对动态AI模型更新场景，分析现有成员推理攻击在有限样本下的局限性
- 开发基于模型更新序列的最优攻击SeMI*，避免信号稀释并支持插入时间与数据调优
- 通过实验验证SeMI*变体在多种数据分布和DP-SGD训练模型上优于基线方法

## 摘要（原文）

> Modern AI models are not static. They go through multiple updates in their lifecycles. Thus, exploiting the model dynamics to create stronger Membership Inference (MI) attacks and tighter privacy audits are timely questions. Though the literature empirically shows that using a sequence of model updates can increase the power of MI attacks, rigorous analysis of the `optimal' MI attacks is limited to static models with infinite samples. Hence, we develop an `optimal' MI attack, SeMI*, that uses the sequence of model updates to identify the presence of a target inserted at a certain update step. For the empirical mean computation, we derive the optimal power of SeMI*, while accessing a finite number of samples with or without privacy. Our results retrieve the existing asymptotic analysis. We observe that having access to the model sequence avoids the dilution of MI signals unlike the existing attacks on the final model, where the MI signal vanishes as training data accumulates. Furthermore, an adversary can use SeMI* to tune both the insertion time and the canary to yield tighter privacy audits. Finally, we conduct experiments across data distributions and models trained or fine-tuned with DP-SGD demonstrating that practical variants of SeMI* lead to tighter privacy audits than the baselines.

