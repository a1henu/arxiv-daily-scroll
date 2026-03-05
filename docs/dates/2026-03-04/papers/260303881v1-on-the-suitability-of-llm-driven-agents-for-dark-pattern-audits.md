---
layout: default
title: On the Suitability of LLM-Driven Agents for Dark Pattern Audits
---

# On the Suitability of LLM-Driven Agents for Dark Pattern Audits
**arXiv**：[2603.03881v1](https://arxiv.org/abs/2603.03881) · [PDF](https://arxiv.org/pdf/2603.03881.pdf)  
**作者**：Chen Sun, Yash Vekaria, Rishab Nithyanand  

**一句话要点**：提出LLM驱动代理用于暗模式审计，评估其在数据经纪人网站CCPA请求流程中的可行性与局限性。

**关键词**：LLM驱动代理, 暗模式审计, CCPA数据权利, 界面设计评估, 自动化审计

## 3 点简述
- 核心问题：LLM驱动代理能否可靠识别界面设计中的暗模式，如摩擦、误导和胁迫。
- 方法要点：设计代理进行端到端工作流遍历、结构化证据收集和暗模式分类。
- 实验或效果：在456个数据经纪人网站上评估代理的流程完成能力、分类可靠性及失败条件。

## 摘要（原文）

> As LLM-driven agents begin to autonomously navigate the web, their ability to interpret and respond to manipulative interface design becomes critical. A fundamental question that emerges is: can such agents reliably recognize patterns of friction, misdirection, and coercion in interface design (i.e., dark patterns)? We study this question in a setting where the workflows are consequential: website portals associated with the submission of CCPA-related data rights requests. These portals operationalize statutory rights, but they are implemented as interactive interfaces whose design can be structured to facilitate, burden, or subtly discourage the exercise of those rights. We design and deploy an LLM-driven auditing agent capable of end-to-end traversal of rights-request workflows, structured evidence gathering, and classification of potential dark patterns. Across a set of 456 data broker websites, we evaluate: (1) the ability of the agent to consistently locate and complete request flows, (2) the reliability and reproducibility of its dark pattern classifications, and (3) the conditions under which it fails or produces poor judgments. Our findings characterize both the feasibility and the limitations of using LLM-driven agents for scalable dark pattern auditing.

