---
layout: default
title: RepoLaunch: Automating Build&Test Pipeline of Code Repositories on ANY Language and ANY Platform
---

# RepoLaunch: Automating Build&Test Pipeline of Code Repositories on ANY Language and ANY Platform
**arXiv**：[2603.05026v1](https://arxiv.org/abs/2603.05026) · [PDF](https://arxiv.org/pdf/2603.05026.pdf)  
**作者**：Kenan Li, Rongzhi Li, Linghao Zhang, Qirui Jin, Liao Zhu, Xiaosong Huang, Geng Zhang, Yikai Zhang, Shilin He, Chengxing Xie, Xin Zhang, Zijian Jin, Bowen Li, Chaoyun Zhang, Yu Kang, Yufan Huang, Elsie Nallipogu, Saravan Rajmohan, Qingwei Lin, Dongmei Zhang  

**一句话要点**：提出RepoLaunch以自动化跨语言跨平台的代码仓库构建与测试流程

**关键词**：软件工程自动化, LLM代理, 代码构建测试, 跨平台兼容, 数据集生成

## 3 点简述
- 软件仓库构建依赖人工配置，自动化程度低
- 基于LLM代理自动解析依赖、编译代码并提取测试结果
- 应用于SWE数据集创建，实现任务生成的自动化

## 摘要（原文）

> Building software repositories typically requires significant manual effort. Recent advances in large language model (LLM) agents have accelerated automation in software engineering (SWE). We introduce RepoLaunch, the first agent capable of automatically resolving dependencies, compiling source code, and extracting test results for repositories across arbitrary programming languages and operating systems. To demonstrate its utility, we further propose a fully automated pipeline for SWE dataset creation, where task design is the only human intervention. RepoLaunch automates the remaining steps, enabling scalable benchmarking and training of coding agents and LLMs. Notably, several works on agentic benchmarking and training have recently adopted RepoLaunch for automated task generation.

