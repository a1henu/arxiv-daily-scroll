---
layout: default
title: Explainability Methods for Hardware Trojan Detection: A Systematic Comparison
---

# Explainability Methods for Hardware Trojan Detection: A Systematic Comparison
**arXiv**：[2601.18696v1](https://arxiv.org/abs/2601.18696) · [PDF](https://arxiv.org/pdf/2601.18696.pdf)  
**作者**：Paul Whitten, Francis Wolff, Chris Papachristou  

**一句话要点**：系统比较硬件木马检测的可解释性方法，提升安全工程师验证能力

**关键词**：硬件木马检测, 可解释性方法, 电路属性分析, 案例推理, 特征归因, XGBoost分类

## 3 点简述
- 核心问题：硬件木马检测需准确识别并提供可解释结果，以支持安全工程师验证和行动。
- 方法要点：比较三类可解释性方法：基于电路属性的分析、基于案例的推理和模型无关特征归因。
- 实验或效果：XGBoost分类在测试集上实现46.15%精确率和52.17%召回率，假阳性率降至0.25%。

## 摘要（原文）

> Hardware trojan detection requires accurate identification and interpretable explanations for security engineers to validate and act on results. This work compares three explainability categories for gate-level trojan detection on the Trust-Hub benchmark: (1) domain-aware property-based analysis of 31 circuit-specific features from gate fanin patterns, flip-flop distances, and I/O connectivity; (2) case-based reasoning using k-nearest neighbors for precedent-based explanations; and (3) model-agnostic feature attribution (LIME, SHAP, gradient).
>   Results show different advantages per approach. Property-based analysis provides explanations through circuit concepts like "high fanin complexity near outputs indicates potential triggers." Case-based reasoning achieves 97.4% correspondence between predictions and training exemplars, offering justifications grounded in precedent. LIME and SHAP provide feature attributions with strong inter-method correlation (r=0.94, p<0.001) but lack circuit-level context for validation.
>   XGBoost classification achieves 46.15% precision and 52.17% recall on 11,392 test samples, a 9-fold precision improvement over prior work (Hasegawa et al.: 5.13%) while reducing false positive rates from 5.6% to 0.25%. Gradient-based attribution runs 481 times faster than SHAP but provides similar domain-opaque insights.
>   This work demonstrates that property-based and case-based approaches offer domain alignment and precedent-based interpretability compared to generic feature rankings, with implications for XAI deployment where practitioners must validate ML predictions.

