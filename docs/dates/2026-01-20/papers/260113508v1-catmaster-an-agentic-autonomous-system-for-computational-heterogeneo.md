---
layout: default
title: CatMaster: An Agentic Autonomous System for Computational Heterogeneous Catalysis Research
---

# CatMaster: An Agentic Autonomous System for Computational Heterogeneous Catalysis Research
**arXiv**：[2601.13508v1](https://arxiv.org/abs/2601.13508) · [PDF](https://arxiv.org/pdf/2601.13508.pdf)  
**作者**：Honghao Chen, Jiangjie Qiu, Yi Shen Tew, Xiaonan Wang  

**一句话要点**：提出CatMaster系统以解决计算异相催化研究中工作流管理繁琐的问题

**关键词**：计算异相催化, 大语言模型代理, 工作流自动化, 多保真度计算, DFT计算

## 3 点简述
- 核心问题：DFT计算工作流成本高、迭代多、设置敏感，且手动管理易出错、难复现
- 方法要点：基于大语言模型的代理系统，将自然语言请求转化为完整计算工作空间，支持持久记录和多保真度工具库
- 实验或效果：通过四个复杂度递增的演示验证，包括远程执行、协议敏感性研究、高通量筛选和扩展工具集应用

## 摘要（原文）

> Density functional theory (DFT) is widely used to connect atomic structure with catalytic behavior, but computational heterogeneous catalysis studies often require long workflows that are costly, iterative, and sensitive to setup choices. Besides the intrinsic cost and accuracy limits of first-principles calculations, practical workflow issues such as keeping references consistent, preparing many related inputs, recovering from failed runs on computing clusters, and maintaining a complete record of what was done, can slow down projects and make results difficult to reproduce or extend.
>   Here we present CatMaster, a large-language-model (LLM)-driven agent system that turns natural language requests into complete calculation workspaces, including structures, inputs, outputs, logs, and a concise run record. CatMaster maintains a persistent project record of key facts, constraints, and file pointers to support inspection and restartability. It is paired with a multi-fidelity tool library that covers rapid surrogate relaxations and high-fidelity DFT calculations for validation when needed. We demonstrate CatMaster on four demonstrations of increasing complexity: an O2 spin-state check with remote execution, BCC Fe surface energies with a protocol-sensitivity study and CO adsorption site ranking, high-throughput Pt--Ni--Cu alloy screening for hydrogen evolution reaction (HER) descriptors with surrogate-to-DFT validation, and a demonstration beyond the predefined tool set, including equation-of-state fitting for BCC Fe and CO-FeN4-graphene single-atom catalyst geometry preparation. By reducing manual scripting and bookkeeping while keeping the full evidence trail, CatMaster aims to help catalysis researchers focus on modeling choices and chemical interpretation rather than workflow management.

