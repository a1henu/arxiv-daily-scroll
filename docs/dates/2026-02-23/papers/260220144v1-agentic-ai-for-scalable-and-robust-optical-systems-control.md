---
layout: default
title: Agentic AI for Scalable and Robust Optical Systems Control
---

# Agentic AI for Scalable and Robust Optical Systems Control
**arXiv**：[2602.20144v1](https://arxiv.org/abs/2602.20144) · [PDF](https://arxiv.org/pdf/2602.20144.pdf)  
**作者**：Zehao Wang, Mingzhe Han, Wei Cheng, Yue-Kai Huang, Philip Ji, Denton Wu, Mahdi Safari, Flemming Holtorf, Kenaish AlQubaisi, Norbert M. Linke, Danyang Zhuo, Yiran Chen, Ting Wang, Dirk Englund, Tingjun Chen  

**一句话要点**：提出AgentOptics框架，基于MCP实现异构光学系统的高保真自主控制

**关键词**：光学系统控制, 模型上下文协议, 自主代理框架, 异构设备集成, 任务基准评估

## 3 点简述
- 核心问题：光学系统控制需处理自然语言任务与异构设备，传统方法成功率低
- 方法要点：基于MCP构建工具抽象层，实现64个标准化工具，支持多步协调与错误处理
- 实验效果：在410任务基准上，任务成功率87.7%–99.0%，显著优于代码生成基线

## 摘要（原文）

> We present AgentOptics, an agentic AI framework for high-fidelity, autonomous optical system control built on the Model Context Protocol (MCP). AgentOptics interprets natural language tasks and executes protocol-compliant actions on heterogeneous optical devices through a structured tool abstraction layer. We implement 64 standardized MCP tools across 8 representative optical devices and construct a 410-task benchmark to evaluate request understanding, role-aware responses, multi-step coordination, robustness to linguistic variation, and error handling. We assess two deployment configurations--commercial online LLMs and locally hosted open-source LLMs--and compare them with LLM-based code generation baselines. AgentOptics achieves 87.7%--99.0% average task success rates, significantly outperforming code-generation approaches, which reach up to 50% success. We further demonstrate broader applicability through five case studies extending beyond device-level control to system orchestration, monitoring, and closed-loop optimization. These include DWDM link provisioning and coordinated monitoring of coherent 400 GbE and analog radio-over-fiber (ARoF) channels; autonomous characterization and bias optimization of a wideband ARoF link carrying 5G fronthaul traffic; multi-span channel provisioning with launch power optimization; closed-loop fiber polarization stabilization; and distributed acoustic sensing (DAS)-based fiber monitoring with LLM-assisted event detection. These results establish AgentOptics as a scalable, robust paradigm for autonomous control and orchestration of heterogeneous optical systems.

