---
layout: default
title: SecureCAI: Injection-Resilient LLM Assistants for Cybersecurity Operations
---

# SecureCAI: Injection-Resilient LLM Assistants for Cybersecurity Operations
**arXiv**：[2601.07835v1](https://arxiv.org/abs/2601.07835) · [PDF](https://arxiv.org/pdf/2601.07835.pdf)  
**作者**：Mohammed Himayath Ali, Mohammed Aqib Abdullah, Mohammed Mudassir Uddin, Shahnawaz Alam  

**一句话要点**：提出SecureCAI框架以解决网络安全操作中LLM易受提示注入攻击的问题

**关键词**：提示注入攻击, 网络安全操作, 宪法AI, 直接偏好优化, 自适应防御, 语言模型安全

## 3 点简述
- 核心问题：LLM在网络安全环境中部署时，易受恶意指令嵌入的提示注入攻击，传统安全机制不足。
- 方法要点：扩展宪法AI原则，结合安全感知护栏、自适应宪法演化和直接偏好优化，以消除不安全响应模式。
- 实验或效果：攻击成功率降低94.7%，良性任务准确率保持95.1%，宪法遵循分数超过0.92，支持动态适应新攻击策略。

## 摘要（原文）

> Large Language Models have emerged as transformative tools for Security Operations Centers, enabling automated log analysis, phishing triage, and malware explanation; however, deployment in adversarial cybersecurity environments exposes critical vulnerabilities to prompt injection attacks where malicious instructions embedded in security artifacts manipulate model behavior. This paper introduces SecureCAI, a novel defense framework extending Constitutional AI principles with security-aware guardrails, adaptive constitution evolution, and Direct Preference Optimization for unlearning unsafe response patterns, addressing the unique challenges of high-stakes security contexts where traditional safety mechanisms prove insufficient against sophisticated adversarial manipulation. Experimental evaluation demonstrates that SecureCAI reduces attack success rates by 94.7% compared to baseline models while maintaining 95.1% accuracy on benign security analysis tasks, with the framework incorporating continuous red-teaming feedback loops enabling dynamic adaptation to emerging attack strategies and achieving constitution adherence scores exceeding 0.92 under sustained adversarial pressure, thereby establishing a foundation for trustworthy integration of language model capabilities into operational cybersecurity workflows and addressing a critical gap in current approaches to AI safety within adversarial domains.

