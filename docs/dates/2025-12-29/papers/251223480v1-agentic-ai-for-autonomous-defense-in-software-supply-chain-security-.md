---
layout: default
title: Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation
---

# Agentic AI for Autonomous Defense in Software Supply Chain Security: Beyond Provenance to Vulnerability Mitigation
**arXiv**：[2512.23480v1](https://arxiv.org/abs/2512.23480) · [PDF](https://arxiv.org/pdf/2512.23480.pdf)  
**作者**：Toqeer Ali Syed, Mohammad Riyaz Belgaum, Salman Jan, Asadullah Abdullah Khan, Saad Said Alqahtani  

**一句话要点**：提出基于代理人工智能的自主防御框架，以增强软件供应链安全，超越溯源实现漏洞缓解。

**关键词**：软件供应链安全, 代理人工智能, 漏洞缓解, 强化学习, 多代理系统, 区块链审计

## 3 点简述
- 核心问题：传统溯源机制如SLSA和SBOM无法主动识别和缓解软件供应链中的漏洞。
- 方法要点：结合LLM推理、强化学习和多代理协调，通过LangChain和MCP集成CI/CD环境，使用区块链记录确保完整性。
- 实验或效果：在模拟和真实CI/CD环境中测试，相比基线方法，检测准确率更高、缓解延迟更短、构建开销合理。

## 摘要（原文）

> The software supply chain attacks are becoming more and more focused on trusted development and delivery procedures, so the conventional post-build integrity mechanisms cannot be used anymore. The available frameworks like SLSA, SBOM and in toto are majorly used to offer provenance and traceability but do not have the capabilities of actively identifying and removing vulnerabilities in software production. The current paper includes an example of agentic artificial intelligence (AI) based on autonomous software supply chain security that combines large language model (LLM)-based reasoning, reinforcement learning (RL), and multi-agent coordination. The suggested system utilizes specialized security agents coordinated with the help of LangChain and LangGraph, communicates with actual CI/CD environments with the Model Context Protocol (MCP), and documents all the observations and actions in a blockchain security ledger to ensure integrity and auditing. Reinforcement learning can be used to achieve adaptive mitigation strategies that consider the balance between security effectiveness and the operational overhead, and LLMs can be used to achieve semantic vulnerability analysis, as well as explainable decisions. This framework is tested based on simulated pipelines, as well as, actual world CI/CD integrations on GitHub Actions and Jenkins, including injection attacks, insecure deserialization, access control violations, and configuration errors. Experimental outcomes indicate better detection accuracy, shorter mitigation latency and reasonable build-time overhead than rule-based, provenance only and RL only baselines. These results show that agentic AI can facilitate the transition to self defending, proactive software supply chains rather than reactive verification ones.

