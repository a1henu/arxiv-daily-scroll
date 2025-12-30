---
layout: default
title: Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems
---

# Multi-Agent Framework for Threat Mitigation and Resilience in AI-Based Systems
**arXiv**：[2512.23132v1](https://arxiv.org/abs/2512.23132) · [PDF](https://arxiv.org/pdf/2512.23132.pdf)  
**作者**：Armstrong Foundjem, Lionel Nganyewou Tidjon, Leuson Da Silva, Foutse Khomh  

**一句话要点**：提出多智能体框架以增强基于AI系统的威胁缓解与韧性

**关键词**：多智能体框架, 威胁缓解, AI系统韧性, 威胁图分析, ML安全风险, 漏洞集群

## 3 点简述
- 核心问题：传统网络安全缺乏针对基础模型、多模态和RAG系统的ML特定威胁建模
- 方法要点：通过多智能体RAG系统构建本体驱动的威胁图，链接TTPs、漏洞和生命周期阶段
- 实验或效果：识别未报告威胁如商业LLM API模型窃取，并分析漏洞集群在库中的传播问题

## 摘要（原文）

> Machine learning (ML) underpins foundation models in finance, healthcare, and critical infrastructure, making them targets for data poisoning, model extraction, prompt injection, automated jailbreaking, and preference-guided black-box attacks that exploit model comparisons. Larger models can be more vulnerable to introspection-driven jailbreaks and cross-modal manipulation. Traditional cybersecurity lacks ML-specific threat modeling for foundation, multimodal, and RAG systems. Objective: Characterize ML security risks by identifying dominant TTPs, vulnerabilities, and targeted lifecycle stages. Methods: We extract 93 threats from MITRE ATLAS (26), AI Incident Database (12), and literature (55), and analyze 854 GitHub/Python repositories. A multi-agent RAG system (ChatGPT-4o, temp 0.4) mines 300+ articles to build an ontology-driven threat graph linking TTPs, vulnerabilities, and stages. Results: We identify unreported threats including commercial LLM API model stealing, parameter memorization leakage, and preference-guided text-only jailbreaks. Dominant TTPs include MASTERKEY-style jailbreaking, federated poisoning, diffusion backdoors, and preference optimization leakage, mainly impacting pre-training and inference. Graph analysis reveals dense vulnerability clusters in libraries with poor patch propagation. Conclusion: Adaptive, ML-specific security frameworks, combining dependency hygiene, threat intelligence, and monitoring, are essential to mitigate supply-chain and inference risks across the ML lifecycle.

