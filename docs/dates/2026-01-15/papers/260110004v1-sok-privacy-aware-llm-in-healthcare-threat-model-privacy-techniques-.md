---
layout: default
title: SoK: Privacy-aware LLM in Healthcare: Threat Model, Privacy Techniques, Challenges and Recommendations
---

# SoK: Privacy-aware LLM in Healthcare: Threat Model, Privacy Techniques, Challenges and Recommendations
**arXiv**：[2601.10004v1](https://arxiv.org/abs/2601.10004) · [PDF](https://arxiv.org/pdf/2601.10004.pdf)  
**作者**：Mohoshin Ara Tahera, Karamveer Singh Sidhu, Shuvalaxmi Dass, Sajal Saha  

**一句话要点**：系统化分析医疗LLM隐私威胁模型与防护技术，提出阶段感知建议

**关键词**：医疗大语言模型, 隐私威胁模型, 隐私保护技术, 系统化知识, 阶段感知建议, 临床数据安全

## 3 点简述
- 核心问题：LLM在医疗应用中面临数据敏感性和部署环境异质性带来的隐私安全挑战
- 方法要点：基于数据预处理、微调和推理三阶段构建威胁模型，系统化评估隐私保护技术
- 实验或效果：分析现有防护技术的局限性，为受监管环境提供强化隐私保证的研究方向

## 摘要（原文）

> Large Language Models (LLMs) are increasingly adopted in healthcare to support clinical decision-making, summarize electronic health records (EHRs), and enhance patient care. However, this integration introduces significant privacy and security challenges, driven by the sensitivity of clinical data and the high-stakes nature of medical workflows. These risks become even more pronounced across heterogeneous deployment environments, ranging from small on-premise hospital systems to regional health networks, each with unique resource limitations and regulatory demands. This Systematization of Knowledge (SoK) examines the evolving threat landscape across the three core LLM phases: Data preprocessing, Fine-tuning, and Inference within realistic healthcare settings. We present a detailed threat model that characterizes adversaries, capabilities, and attack surfaces at each phase, and we systematize how existing privacy-preserving techniques (PPTs) attempt to mitigate these vulnerabilities. While existing defenses show promise, our analysis identifies persistent limitations in securing sensitive clinical data across diverse operational tiers. We conclude with phase-aware recommendations and future research directions aimed at strengthening privacy guarantees for LLMs in regulated environments. This work provides a foundation for understanding the intersection of LLMs, threats, and privacy in healthcare, offering a roadmap toward more robust and clinically trustworthy AI systems.

