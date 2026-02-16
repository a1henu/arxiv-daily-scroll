---
layout: default
title: Reliable Hierarchical Operating System Fingerprinting via Conformal Prediction
---

# Reliable Hierarchical Operating System Fingerprinting via Conformal Prediction
**arXiv**：[2602.12825v1](https://arxiv.org/abs/2602.12825) · [PDF](https://arxiv.org/pdf/2602.12825.pdf)  
**作者**：Rubén Pérez-Jove, Osvaldo Simeone, Alejandro Pazos, Jose Vázquez-Naya  

**一句话要点**：提出层次化操作系统指纹识别方法，通过保形预测提供不确定性量化，解决传统方法缺乏结构一致性问题。

**关键词**：操作系统指纹识别, 保形预测, 不确定性量化, 层次化分类, 网络安全, 结构一致性

## 3 点简述
- 核心问题：传统操作系统指纹识别缺乏不确定性量化，且忽略OS分类学结构，导致预测脆弱。
- 方法要点：引入两种结构化保形预测策略：独立校准层次级别的L-CP和确保结构一致性的P-CP。
- 实验或效果：两种方法均满足有效性保证，但L-CP效率高但结构不一致，P-CP结构一致但效率较低。

## 摘要（原文）

> Operating System (OS) fingerprinting is critical for network security, but conventional methods do not provide formal uncertainty quantification mechanisms. Conformal Prediction (CP) could be directly wrapped around existing methods to obtain prediction sets with guaranteed coverage. However, a direct application of CP would treat OS identification as a flat classification problem, ignoring the natural taxonomic structure of OSs and providing brittle point predictions. This work addresses these limitations by introducing and evaluating two distinct structured CP strategies: level-wise CP (L-CP), which calibrates each hierarchy level independently, and projection-based CP (P-CP), which ensures structural consistency by projecting leaf-level sets upwards. Our results demonstrate that, while both methods satisfy validity guarantees, they expose a fundamental trade-off between level-wise efficiency and structural consistency. L-CP yields tighter prediction sets suitable for human forensic analysis but suffers from taxonomic inconsistencies. Conversely, P-CP guarantees hierarchically consistent, nested sets ideal for automated policy enforcement, albeit at the cost of reduced efficiency at coarser levels.

