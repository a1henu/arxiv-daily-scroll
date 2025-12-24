---
layout: default
title: KAN-AFT: An Interpretable Nonlinear Survival Model Integrating Kolmogorov-Arnold Networks with Accelerated Failure Time Analysis
---

# KAN-AFT: An Interpretable Nonlinear Survival Model Integrating Kolmogorov-Arnold Networks with Accelerated Failure Time Analysis
**arXiv**：[2512.20305v1](https://arxiv.org/abs/2512.20305) · [PDF](https://arxiv.org/pdf/2512.20305.pdf)  
**作者**：Mebin Jose, Jisha Francis, Sudheesh Kumar Kattumannil  

**一句话要点**：提出KAN-AFT模型，将Kolmogorov-Arnold网络集成到加速失效时间分析中，以提升生存分析的可解释性和非线性建模能力。

**关键词**：生存分析, 加速失效时间模型, Kolmogorov-Arnold网络, 可解释性, 非线性建模, 右删失处理

## 3 点简述
- 核心问题：传统生存模型如CoxPH和AFT在非线性关系和可解释性方面存在局限，深度学习模型如DeepAFT虽提升预测精度但缺乏透明性。
- 方法要点：首次将KANs应用于AFT框架，通过样条函数建模复杂非线性关系，并采用Buckley-James和IPCW等优化策略处理右删失数据。
- 实验或效果：在多个数据集上验证，KAN-AFT性能与DeepAFT相当或更优，并能将学习函数转换为符号方程，提供可解释的生存过程模型。

## 摘要（原文）

> Survival analysis relies fundamentally on the semi-parametric Cox Proportional Hazards (CoxPH) model and the parametric Accelerated Failure Time (AFT) model. CoxPH assumes constant hazard ratios, often failing to capture real-world dynamics, while traditional AFT models are limited by rigid distributional assumptions. Although deep learning models like DeepAFT address these constraints by improving predictive accuracy and handling censoring, they inherit the significant challenge of black-box interpretability. The recent introduction of CoxKAN demonstrated the successful integration of Kolmogorov-Arnold Networks (KANs), a novel architecture that yields highly accurate and interpretable symbolic representations, within the CoxPH framework. Motivated by the interpretability gains of CoxKAN, we introduce KAN-AFT (Kolmogorov Arnold Network-based AFT), the first framework to apply KANs to the AFT model. KAN-AFT effectively models complex nonlinear relationships within the AFT framework. Our primary contributions include: (i) a principled AFT-KAN formulation, (ii) robust optimization strategies for right-censored observations (e.g., Buckley-James and IPCW), and (iii) an interpretability pipeline that converts the learned spline functions into closed-form symbolic equations for survival time. Empirical results on multiple datasets confirm that KAN-AFT achieves performance comparable to or better than DeepAFT, while uniquely providing transparent, symbolic models of the survival process.

