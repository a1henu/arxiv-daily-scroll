---
layout: default
title: Sharp Structure-Agnostic Lower Bounds for General Functional Estimation
---

# Sharp Structure-Agnostic Lower Bounds for General Functional Estimation
**arXiv**：[2512.17341v1](https://arxiv.org/abs/2512.17341) · [PDF](https://arxiv.org/pdf/2512.17341.pdf)  
**作者**：Jikai Jin, Vasilis Syrgkanis  

**一句话要点**：建立结构无关估计的通用下界，验证去偏机器学习的最优性

**关键词**：结构无关估计, 去偏机器学习, 因果推断, 泛函估计, 误差下界, 双重稳健性

## 3 点简述
- 研究结构无关估计在统计与机器学习中的基本误差极限
- 证明双重稳健学习和去偏机器学习在因果推断与一般泛函估计中的最优性
- 区分双重稳健可达与不可达两种机制，推导显式最优速率

## 摘要（原文）

> The design of efficient nonparametric estimators has long been a central problem in statistics, machine learning, and decision making. Classical optimal procedures often rely on strong structural assumptions, which can be misspecified in practice and complicate deployment. This limitation has sparked growing interest in structure-agnostic approaches -- methods that debias black-box nuisance estimates without imposing structural priors. Understanding the fundamental limits of these methods is therefore crucial. This paper provides a systematic investigation of the optimal error rates achievable by structure-agnostic estimators. We first show that, for estimating the average treatment effect (ATE), a central parameter in causal inference, doubly robust learning attains optimal structure-agnostic error rates. We then extend our analysis to a general class of functionals that depend on unknown nuisance functions and establish the structure-agnostic optimality of debiased/double machine learning (DML). We distinguish two regimes -- one where double robustness is attainable and one where it is not -- leading to different optimal rates for first-order debiasing, and show that DML is optimal in both regimes. Finally, we instantiate our general lower bounds by deriving explicit optimal rates that recover existing results and extend to additional estimands of interest. Our results provide theoretical validation for widely used first-order debiasing methods and guidance for practitioners seeking optimal approaches in the absence of structural assumptions. This paper generalizes and subsumes the ATE lower bound established in \citet{jin2024structure} by the same authors.

