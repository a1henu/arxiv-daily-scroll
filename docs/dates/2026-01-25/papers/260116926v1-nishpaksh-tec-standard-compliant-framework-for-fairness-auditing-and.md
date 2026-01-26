---
layout: default
title: Nishpaksh: TEC Standard-Compliant Framework for Fairness Auditing and Certification of AI Models
---

# Nishpaksh: TEC Standard-Compliant Framework for Fairness Auditing and Certification of AI Models
**arXiv**：[2601.16926v1](https://arxiv.org/abs/2601.16926) · [PDF](https://arxiv.org/pdf/2601.16926.pdf)  
**作者**：Shashank Prakash, Ranjitha Prasad, Avinash Agarwal  

**一句话要点**：提出Nishpaksh框架以解决AI模型在电信领域公平性评估的标准化与监管需求

**关键词**：公平性评估, AI监管, 电信标准, TEC合规, Web仪表板, COMPAS数据集

## 3 点简述
- 核心问题：AI模型在高风险决策中缺乏符合区域法规的公平性评估工具，现有工具如IBM AI Fairness 360未对齐印度TEC标准。
- 方法要点：基于TEC标准开发Nishpaksh工具，集成风险量化、阈值确定和公平性评估，提供可审计的Web仪表板。
- 实验或效果：在COMPAS数据集上验证，能识别属性特定偏差并生成符合TEC的标准化公平性分数。

## 摘要（原文）

> The growing reliance on Artificial Intelligence (AI) models in high-stakes decision-making systems, particularly within emerging telecom and 6G applications, underscores the urgent need for transparent and standardized fairness assessment frameworks. While global toolkits such as IBM AI Fairness 360 and Microsoft Fairlearn have advanced bias detection, they often lack alignment with region-specific regulatory requirements and national priorities. To address this gap, we propose Nishpaksh, an indigenous fairness evaluation tool that operationalizes the Telecommunication Engineering Centre (TEC) Standard for the Evaluation and Rating of Artificial Intelligence Systems. Nishpaksh integrates survey-based risk quantification, contextual threshold determination, and quantitative fairness evaluation into a unified, web-based dashboard. The tool employs vectorized computation, reactive state management, and certification-ready reporting to enable reproducible, audit-grade assessments, thereby addressing a critical post-standardization implementation need. Experimental validation on the COMPAS dataset demonstrates Nishpaksh's effectiveness in identifying attribute-specific bias and generating standardized fairness scores compliant with the TEC framework. The system bridges the gap between research-oriented fairness methodologies and regulatory AI governance in India, marking a significant step toward responsible and auditable AI deployment within critical infrastructure like telecommunications.

