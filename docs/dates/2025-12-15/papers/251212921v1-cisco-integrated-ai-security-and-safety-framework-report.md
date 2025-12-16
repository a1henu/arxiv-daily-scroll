---
layout: default
title: Cisco Integrated AI Security and Safety Framework Report
---

# Cisco Integrated AI Security and Safety Framework Report
**arXiv**：[2512.12921v1](https://arxiv.org/abs/2512.12921) · [PDF](https://arxiv.org/pdf/2512.12921.pdf)  
**作者**：Amy Chang, Tiffany Saade, Sanket Mendapara, Adam Swanda, Ankit Garg  

**一句话要点**：提出思科集成AI安全与安全框架，以统一分类和操作化AI风险，覆盖全生命周期和多模态部署。

**关键词**：AI安全框架, 生命周期风险管理, 多模态AI部署, 威胁分类, 操作化防御, 生态系统安全

## 3 点简述
- 核心问题：AI系统快速普及导致攻击面扩大，威胁包括内容安全失败、模型完整性受损、运行时操纵和生态系统风险。
- 方法要点：设计统一、生命周期感知的分类和操作化框架，整合现有框架如MITRE ATLAS和NIST AI 100-2，覆盖多模态、代理和管道。
- 实验或效果：分析现有框架的差距，讨论设计原则，展示分类如何帮助理解AI系统失败、对手利用方式，并构建防御措施。

## 摘要（原文）

> Artificial intelligence (AI) systems are being readily and rapidly adopted, increasingly permeating critical domains: from consumer platforms and enterprise software to networked systems with embedded agents. While this has unlocked potential for human productivity gains, the attack surface has expanded accordingly: threats now span content safety failures (e.g., harmful or deceptive outputs), model and data integrity compromise (e.g., poisoning, supply-chain tampering), runtime manipulations (e.g., prompt injection, tool and agent misuse), and ecosystem risks (e.g., orchestration abuse, multi-agent collusion). Existing frameworks such as MITRE ATLAS, National Institute of Standards and Technology (NIST) AI 100-2 Adversarial Machine Learning (AML) taxonomy, and OWASP Top 10s for Large Language Models (LLMs) and Agentic AI Applications provide valuable viewpoints, but each covers only slices of this multi-dimensional space.
>   This paper presents Cisco's Integrated AI Security and Safety Framework ("AI Security Framework"), a unified, lifecycle-aware taxonomy and operationalization framework that can be used to classify, integrate, and operationalize the full range of AI risks. It integrates AI security and AI safety across modalities, agents, pipelines, and the broader ecosystem. The AI Security Framework is designed to be practical for threat identification, red-teaming, risk prioritization, and it is comprehensive in scope and can be extensible to emerging deployments in multimodal contexts, humanoids, wearables, and sensory infrastructures. We analyze gaps in prevailing frameworks, discuss design principles for our framework, and demonstrate how the taxonomy provides structure for understanding how modern AI systems fail, how adversaries exploit these failures, and how organizations can build defenses across the AI lifecycle that evolve alongside capability advancements.

