---
layout: default
title: A Practical Framework for Evaluating Medical AI Security: Reproducible Assessment of Jailbreaking and Privacy Vulnerabilities Across Clinical Specialties
---

# A Practical Framework for Evaluating Medical AI Security: Reproducible Assessment of Jailbreaking and Privacy Vulnerabilities Across Clinical Specialties
**arXiv**：[2512.08185v1](https://arxiv.org/abs/2512.08185) · [PDF](https://arxiv.org/pdf/2512.08185.pdf)  
**作者**：Jinghao Wang, Ping Zhang, Carter Yagemann  

**一句话要点**：提出可复现框架以评估医疗AI在资源受限下的安全漏洞

**关键词**：医疗大语言模型, 安全评估框架, 对抗性攻击, 隐私保护, 可复现性, 临床专科

## 3 点简述
- 核心问题：医疗大语言模型在临床部署中面临对抗性滥用和隐私泄露风险，缺乏可访问的安全评估方法。
- 方法要点：设计涵盖多专科的威胁模型，使用合成患者记录，支持在消费级CPU硬件上运行，无需GPU或受保护数据。
- 实验或效果：提供框架规范，包括攻击类型（如越狱和隐私提取）、数据生成、评估协议和评分标准，促进比较安全评估。

## 摘要（原文）

> Medical Large Language Models (LLMs) are increasingly deployed for clinical decision support across diverse specialties, yet systematic evaluation of their robustness to adversarial misuse and privacy leakage remains inaccessible to most researchers. Existing security benchmarks require GPU clusters, commercial API access, or protected health data -- barriers that limit community participation in this critical research area. We propose a practical, fully reproducible framework for evaluating medical AI security under realistic resource constraints. Our framework design covers multiple medical specialties stratified by clinical risk -- from high-risk domains such as emergency medicine and psychiatry to general practice -- addressing jailbreaking attacks (role-playing, authority impersonation, multi-turn manipulation) and privacy extraction attacks. All evaluation utilizes synthetic patient records requiring no IRB approval. The framework is designed to run entirely on consumer CPU hardware using freely available models, eliminating cost barriers. We present the framework specification including threat models, data generation methodology, evaluation protocols, and scoring rubrics. This proposal establishes a foundation for comparative security assessment of medical-specialist models and defense mechanisms, advancing the broader goal of ensuring safe and trustworthy medical AI systems.

