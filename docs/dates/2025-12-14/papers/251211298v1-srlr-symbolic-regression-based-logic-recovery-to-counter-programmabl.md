---
layout: default
title: SRLR: Symbolic Regression based Logic Recovery to Counter Programmable Logic Controller Attacks
---

# SRLR: Symbolic Regression based Logic Recovery to Counter Programmable Logic Controller Attacks
**arXiv**：[2512.11298v1](https://arxiv.org/abs/2512.11298) · [PDF](https://arxiv.org/pdf/2512.11298.pdf)  
**作者**：Hao Zhou, Suman Sourav, Binbin Chen, Ke Yu  

**一句话要点**：提出基于符号回归的逻辑恢复方法SRLR，以检测工业控制系统中的可编程逻辑控制器攻击。

**关键词**：符号回归, 工业控制系统安全, 可编程逻辑控制器, 逻辑恢复, 攻击检测

## 3 点简述
- 核心问题：现有PLC攻击检测方法依赖专家规范或机器学习模型，前者成本高，后者解释性差。
- 方法要点：SRLR仅基于输入输出恢复PLC逻辑，利用ICS特性（如频域表示、多模式操作）增强符号回归。
- 实验或效果：在多种ICS设置中，SRLR恢复准确率最高提升39%，并在大规模电网中验证稳定性。

## 摘要（原文）

> Programmable Logic Controllers (PLCs) are critical components in Industrial Control Systems (ICSs). Their potential exposure to external world makes them susceptible to cyber-attacks. Existing detection methods against controller logic attacks use either specification-based or learnt models. However, specification-based models require experts' manual efforts or access to PLC's source code, while machine learning-based models often fall short of providing explanation for their decisions. We design SRLR -- a it Symbolic Regression based Logic Recovery} solution to identify the logic of a PLC based only on its inputs and outputs. The recovered logic is used to generate explainable rules for detecting controller logic attacks. SRLR enhances the latest deep symbolic regression methods using the following ICS-specific properties: (1) some important ICS control logic is best represented in frequency domain rather than time domain; (2) an ICS controller can operate in multiple modes, each using different logic, where mode switches usually do not happen frequently; (3) a robust controller usually filters out outlier inputs as ICS sensor data can be noisy; and (4) with the above factors captured, the degree of complexity of the formulas is reduced, making effective search possible. Thanks to these enhancements, SRLR consistently outperforms all existing methods in a variety of ICS settings that we evaluate. In terms of the recovery accuracy, SRLR's gain can be as high as 39% in some challenging environment. We also evaluate SRLR on a distribution grid containing hundreds of voltage regulators, demonstrating its stability in handling large-scale, complex systems with varied configurations.

