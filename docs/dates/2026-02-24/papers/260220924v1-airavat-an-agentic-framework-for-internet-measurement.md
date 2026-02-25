---
layout: default
title: Airavat: An Agentic Framework for Internet Measurement
---

# Airavat: An Agentic Framework for Internet Measurement
**arXiv**：[2602.20924v1](https://arxiv.org/abs/2602.20924) · [PDF](https://arxiv.org/pdf/2602.20924.pdf)  
**作者**：Alagappan Ramanathan, Eunju Kang, Dongsu Han, Sangeetha Abdu Jyothi  

**一句话要点**：提出Airavat框架以解决互联网测量中工作流生成与验证的自动化挑战

**关键词**：互联网测量, 工作流生成, 代理框架, 方法验证, 知识图谱

## 3 点简述
- 核心问题：互联网测量需专家级工具编排，但实现易有方法缺陷且难验证。
- 方法要点：基于代理架构生成工作流，结合知识图谱验证和验证引擎确保方法正确性。
- 实验或效果：通过案例研究展示生成专家级工作流、处理新问题及识别方法缺陷的能力。

## 摘要（原文）

> Internet measurement faces twin challenges: complex analyses require expert-level orchestration of tools, yet even syntactically correct implementations can have methodological flaws and can be difficult to verify. Democratizing measurement capabilities thus demands automating both workflow generation and verification against methodological standards established through decades of research.
>   We present Airavat, the first agentic framework for Internet measurement workflow generation with systematic verification and validation. Airavat coordinates a set of agents mirroring expert reasoning: three agents handle problem decomposition, solution design, and code implementation, with assistance from a registry of existing tools. Two specialized engines ensure methodological correctness: a Verification Engine evaluates workflows against a knowledge graph encoding five decades of measurement research, while a Validation Engine identifies appropriate validation techniques grounded in established methodologies. Through four Internet measurement case studies, we demonstrate that Airavat (i) generates workflows matching expert-level solutions, (ii) makes sound architectural decisions, (iii) addresses novel problems without ground truth, and (iv) identifies methodological flaws missed by standard execution-based testing.

