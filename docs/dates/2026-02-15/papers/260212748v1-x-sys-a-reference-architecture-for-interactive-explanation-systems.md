---
layout: default
title: X-SYS: A Reference Architecture for Interactive Explanation Systems
---

# X-SYS: A Reference Architecture for Interactive Explanation Systems
**arXiv**：[2602.12748v1](https://arxiv.org/abs/2602.12748) · [PDF](https://arxiv.org/pdf/2602.12748.pdf)  
**作者**：Tobias Labarta, Nhi Hoang, Maximilian Dreyer, Jim Berend, Oleg Hein, Jackie Ma, Wojciech Samek, Sebastian Lapuschkin  

**一句话要点**：提出X-SYS参考架构以解决交互式可解释AI系统部署挑战

**关键词**：可解释AI系统, 参考架构, 交互式解释, 系统设计, 质量属性, 服务分解

## 3 点简述
- 核心问题：可解释AI研究缺乏系统化部署方案，难以支持交互、模型演化与治理约束
- 方法要点：基于STAR质量属性（可扩展性、可追溯性、响应性、适应性）设计五组件架构，解耦用户界面与后端计算
- 实验或效果：通过SemanticLens系统实例化，展示服务边界、离线/在线分离和状态管理如何提升系统性能

## 摘要（原文）

> The explainable AI (XAI) research community has proposed numerous technical methods, yet deploying explainability as systems remains challenging: Interactive explanation systems require both suitable algorithms and system capabilities that maintain explanation usability across repeated queries, evolving models and data, and governance constraints. We argue that operationalizing XAI requires treating explainability as an information systems problem where user interaction demands induce specific system requirements. We introduce X-SYS, a reference architecture for interactive explanation systems, that guides (X)AI researchers, developers and practitioners in connecting interactive explanation user interfaces (XUI) with system capabilities. X-SYS organizes around four quality attributes named STAR (scalability, traceability, responsiveness, and adaptability), and specifies a five-component decomposition (XUI Services, Explanation Services, Model Services, Data Services, Orchestration and Governance). It maps interaction patterns to system capabilities to decouple user interface evolution from backend computation. We implement X-SYS through SemanticLens, a system for semantic search and activation steering in vision-language models. SemanticLens demonstrates how contract-based service boundaries enable independent evolution, offline/online separation ensures responsiveness, and persistent state management supports traceability. Together, this work provides a reusable blueprint and concrete instantiation for interactive explanation systems supporting end-to-end design under operational constraints.

