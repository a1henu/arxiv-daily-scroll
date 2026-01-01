---
layout: default
title: BatteryAgent: Synergizing Physics-Informed Interpretation with LLM Reasoning for Intelligent Battery Fault Diagnosis
---

# BatteryAgent: Synergizing Physics-Informed Interpretation with LLM Reasoning for Intelligent Battery Fault Diagnosis
**arXiv**：[2512.24686v1](https://arxiv.org/abs/2512.24686) · [PDF](https://arxiv.org/pdf/2512.24686.pdf)  
**作者**：Songqi Zhou, Ruixue Liu, Boman Su, Jiazhou Wang, Yixing Wang, Benben Jiang  

**一句话要点**：提出BatteryAgent框架，融合物理特征与LLM推理，实现锂离子电池智能故障诊断

**关键词**：锂离子电池故障诊断, 物理信息特征, 大语言模型推理, 可解释人工智能, 梯度提升决策树, SHAP归因分析

## 3 点简述
- 核心问题：现有深度学习方法在电池故障诊断中缺乏可解释性，且受限于二元分类，难以提供根因分析与维护建议。
- 方法要点：构建三层框架，包括物理感知层提取机制特征、检测归因层量化特征贡献、推理诊断层利用LLM生成综合报告。
- 实验或效果：在硬边界样本上纠正误分类，AUROC达0.986，优于现有方法，并扩展至多类型可解释诊断。

## 摘要（原文）

> Fault diagnosis of lithium-ion batteries is critical for system safety. While existing deep learning methods exhibit superior detection accuracy, their "black-box" nature hinders interpretability. Furthermore, restricted by binary classification paradigms, they struggle to provide root cause analysis and maintenance recommendations. To address these limitations, this paper proposes BatteryAgent, a hierarchical framework that integrates physical knowledge features with the reasoning capabilities of Large Language Models (LLMs). The framework comprises three core modules: (1) A Physical Perception Layer that utilizes 10 mechanism-based features derived from electrochemical principles, balancing dimensionality reduction with physical fidelity; (2) A Detection and Attribution Layer that employs Gradient Boosting Decision Trees and SHAP to quantify feature contributions; and (3) A Reasoning and Diagnosis Layer that leverages an LLM as the agent core. This layer constructs a "numerical-semantic" bridge, combining SHAP attributions with a mechanism knowledge base to generate comprehensive reports containing fault types, root cause analysis, and maintenance suggestions. Experimental results demonstrate that BatteryAgent effectively corrects misclassifications on hard boundary samples, achieving an AUROC of 0.986, which significantly outperforms current state-of-the-art methods. Moreover, the framework extends traditional binary detection to multi-type interpretable diagnosis, offering a new paradigm shift from "passive detection" to "intelligent diagnosis" for battery safety management.

