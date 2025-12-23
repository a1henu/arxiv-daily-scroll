---
layout: default
title: Augmenting Intelligence: A Hybrid Framework for Scalable and Stable Explanations
---

# Augmenting Intelligence: A Hybrid Framework for Scalable and Stable Explanations
**arXiv**：[2512.19557v1](https://arxiv.org/abs/2512.19557) · [PDF](https://arxiv.org/pdf/2512.19557.pdf)  
**作者**：Lawrence Krukrubo, Julius Odede, Olawande Olusegun  

**一句话要点**：提出混合LRR-TED框架以解决可解释AI的可扩展性与稳定性困境，应用于客户流失预测。

**关键词**：可解释人工智能, 混合框架, 客户流失预测, 规则学习, 人机协同, 可扩展性

## 3 点简述
- 核心问题：可解释AI面临可扩展性与稳定性困境，后处理方法不稳定，监督方法需大量人工标注。
- 方法要点：结合自动规则学习与人工规则，通过不对称发现机制，减少人工标注工作量。
- 实验或效果：在客户流失预测中，仅用4条人工规则实现94.00%预测准确率，优于全人工基准，减少50%人工标注。

## 摘要（原文）

> Current approaches to Explainable AI (XAI) face a "Scalability-Stability Dilemma." Post-hoc methods (e.g., LIME, SHAP) may scale easily but suffer from instability, while supervised explanation frameworks (e.g., TED) offer stability but require prohibitive human effort to label every training instance. This paper proposes a Hybrid LRR-TED framework that addresses this dilemma through a novel "Asymmetry of Discovery." When applied to customer churn prediction, we demonstrate that automated rule learners (GLRM) excel at identifying broad "Safety Nets" (retention patterns) but struggle to capture specific "Risk Traps" (churn triggers)-a phenomenon we term the Anna Karenina Principle of Churn. By initialising the explanation matrix with automated safety rules and augmenting it with a Pareto-optimal set of just four human-defined risk rules, our approach achieves 94.00% predictive accuracy. This configuration outperforms the full 8-rule manual expert baseline while reducing human annotation effort by 50%, proposing a shift in the paradigm for Human-in-the-Loop AI: moving experts from the role of "Rule Writers" to "Exception Handlers."

