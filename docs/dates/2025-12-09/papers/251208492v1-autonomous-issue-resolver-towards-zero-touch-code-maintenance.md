---
layout: default
title: Autonomous Issue Resolver: Towards Zero-Touch Code Maintenance
---

# Autonomous Issue Resolver: Towards Zero-Touch Code Maintenance
**arXiv**：[2512.08492v1](https://arxiv.org/abs/2512.08492) · [PDF](https://arxiv.org/pdf/2512.08492.pdf)  
**作者**：Aliaksei Kaliutau  

**一句话要点**：提出数据转换图与多智能体框架，实现零接触代码维护以解决仓库级程序修复难题。

**关键词**：自动程序修复, 数据转换图, 多智能体框架, 神经符号推理, 零接触代码维护

## 3 点简述
- 核心问题：当前仓库级自动程序修复方法受限于控制中心范式，导致智能体陷入复杂目录和无关控制逻辑的语义陷阱。
- 方法要点：从代码属性图转向数据转换图，以数据状态为节点、函数为边，通过数据谱系追踪逻辑缺陷，结合神经符号推理。
- 实验或效果：在SWE-Verified基准测试中达到87.1%的解决率，验证了方法的有效性。

## 摘要（原文）

> Recent advances in Large Language Models have revolutionized function-level code generation; however, repository-scale Automated Program Repair (APR) remains a significant challenge. Current approaches typically employ a control-centric paradigm, forcing agents to navigate complex directory structures and irrelevant control logic. In this paper, we propose a paradigm shift from the standard Code Property Graphs (CPGs) to the concept of Data Transformation Graph (DTG) that inverts the topology by modeling data states as nodes and functions as edges, enabling agents to trace logic defects through data lineage rather than control flow. We introduce a multi-agent framework that reconciles data integrity navigation with control flow logic. Our theoretical analysis and case studies demonstrate that this approach resolves the "Semantic Trap" inherent in standard RAG systems in modern coding agents. We provide a comprehensive implementation in the form of Autonomous Issue Resolver (AIR), a self-improvement system for zero-touch code maintenance that utilizes neuro-symbolic reasoning and uses the DTG structure for scalable logic repair. Our approach has demonstrated good results on several SWE benchmarks, reaching a resolution rate of 87.1% on SWE-Verified benchmark. Our approach directly addresses the core limitations of current AI code-assistant tools and tackles the critical need for a more robust foundation for our increasingly software-dependent world.

