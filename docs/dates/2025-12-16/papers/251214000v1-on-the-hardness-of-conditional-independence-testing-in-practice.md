---
layout: default
title: On the Hardness of Conditional Independence Testing In Practice
---

# On the Hardness of Conditional Independence Testing In Practice
**arXiv**：[2512.14000v1](https://arxiv.org/abs/2512.14000) · [PDF](https://arxiv.org/pdf/2512.14000.pdf)  
**作者**：Zheng He, Roman Pogodin, Yazhe Li, Namrata Deka, Arthur Gretton, Danica J. Sutherland  

**一句话要点**：分析KCI测试在实践中失败的关键因素，聚焦条件均值嵌入误差与核选择

**关键词**：条件独立性测试, 核方法, I类错误, 条件均值嵌入, 因果发现, 机器学习评估

## 3 点简述
- 核心问题：条件独立性测试在实践中常失败，Shah和Peters的理论结果未完全解释此现象
- 方法要点：研究KCI测试，识别条件均值嵌入估计误差影响I类错误，核选择对功效至关重要
- 实验或效果：指出核选择虽提升功效但易增加I类错误，为改进测试提供实用指导

## 摘要（原文）

> Tests of conditional independence (CI) underpin a number of important problems in machine learning and statistics, from causal discovery to evaluation of predictor fairness and out-of-distribution robustness. Shah and Peters (2020) showed that, contrary to the unconditional case, no universally finite-sample valid test can ever achieve nontrivial power. While informative, this result (based on "hiding" dependence) does not seem to explain the frequent practical failures observed with popular CI tests. We investigate the Kernel-based Conditional Independence (KCI) test - of which we show the Generalized Covariance Measure underlying many recent tests is nearly a special case - and identify the major factors underlying its practical behavior. We highlight the key role of errors in the conditional mean embedding estimate for the Type-I error, while pointing out the importance of selecting an appropriate conditioning kernel (not recognized in previous work) as being necessary for good test power but also tending to inflate Type-I error.

