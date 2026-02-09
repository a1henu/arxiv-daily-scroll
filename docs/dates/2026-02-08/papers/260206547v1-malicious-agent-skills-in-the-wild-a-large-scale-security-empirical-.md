---
layout: default
title: Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study
---

# Malicious Agent Skills in the Wild: A Large-Scale Security Empirical Study
**arXiv**：[2602.06547v1](https://arxiv.org/abs/2602.06547) · [PDF](https://arxiv.org/pdf/2602.06547.pdf)  
**作者**：Yi Liu, Zhihao Chen, Yanjun Zhang, Gelei Deng, Yuekang Li, Jianting Ning, Leo Yu Zhang  

**一句话要点**：构建首个恶意代理技能数据集，揭示社区注册表中数据窃取与代理劫持两大攻击模式。

**关键词**：代理技能安全, 恶意软件分析, 数据集构建, 漏洞检测, 社区注册表, 行为验证

## 3 点简述
- 核心问题：第三方代理技能缺乏真实恶意数据集，存在权限滥用与安全威胁。
- 方法要点：行为验证98,380个技能，确认157个恶意技能并分析其漏洞与攻击链。
- 实验或效果：发现技能平均4.03个漏洞，披露后93.6%在30天内被移除。

## 摘要（原文）

> Third-party agent skills extend LLM-based agents with instruction files and executable code that run on users' machines. Skills execute with user privileges and are distributed through community registries with minimal vetting, but no ground-truth dataset exists to characterize the resulting threats. We construct the first labeled dataset of malicious agent skills by behaviorally verifying 98,380 skills from two community registries, confirming 157 malicious skills with 632 vulnerabilities. These attacks are not incidental. Malicious skills average 4.03 vulnerabilities across a median of three kill chain phases, and the ecosystem has split into two archetypes: Data Thieves that exfiltrate credentials through supply chain techniques, and Agent Hijackers that subvert agent decision-making through instruction manipulation. A single actor accounts for 54.1\% of confirmed cases through templated brand impersonation. Shadow features, capabilities absent from public documentation, appear in 0\% of basic attacks but 100\% of advanced ones; several skills go further by exploiting the AI platform's own hook system and permission flags. Responsible disclosure led to 93.6\% removal within 30 days. We release the dataset and analysis pipeline to support future work on agent skill security.

