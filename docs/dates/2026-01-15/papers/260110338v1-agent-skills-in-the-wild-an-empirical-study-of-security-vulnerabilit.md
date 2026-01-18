---
layout: default
title: Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale
---

# Agent Skills in the Wild: An Empirical Study of Security Vulnerabilities at Scale
**arXiv**：[2601.10338v1](https://arxiv.org/abs/2601.10338) · [PDF](https://arxiv.org/pdf/2601.10338.pdf)  
**作者**：Yi Liu, Weizhe Wang, Ruitao Feng, Yao Zhang, Guangquan Xu, Gelei Deng, Yuekang Li, Leo Zhang  

**一句话要点**：提出SkillScan框架，首次大规模实证分析AI代理技能的安全漏洞

**关键词**：AI代理安全, 漏洞检测, 静态分析, LLM语义分类, 技能市场, 实证研究

## 3 点简述
- 核心问题：AI代理技能因隐式信任和低审查，存在未表征的安全攻击面。
- 方法要点：集成静态分析与LLM语义分类的多阶段检测框架SkillScan。
- 实验或效果：分析31,132个技能，发现26.1%含漏洞，数据外泄和权限提升最普遍。

## 摘要（原文）

> The rise of AI agent frameworks has introduced agent skills, modular packages containing instructions and executable code that dynamically extend agent capabilities. While this architecture enables powerful customization, skills execute with implicit trust and minimal vetting, creating a significant yet uncharacterized attack surface. We conduct the first large-scale empirical security analysis of this emerging ecosystem, collecting 42,447 skills from two major marketplaces and systematically analyzing 31,132 using SkillScan, a multi-stage detection framework integrating static analysis with LLM-based semantic classification. Our findings reveal pervasive security risks: 26.1% of skills contain at least one vulnerability, spanning 14 distinct patterns across four categories: prompt injection, data exfiltration, privilege escalation, and supply chain risks. Data exfiltration (13.3%) and privilege escalation (11.8%) are most prevalent, while 5.2% of skills exhibit high-severity patterns strongly suggesting malicious intent. We find that skills bundling executable scripts are 2.12x more likely to contain vulnerabilities than instruction-only skills (OR=2.12, p<0.001). Our contributions include: (1) a grounded vulnerability taxonomy derived from 8,126 vulnerable skills, (2) a validated detection methodology achieving 86.7% precision and 82.5% recall, and (3) an open dataset and detection toolkit to support future research. These results demonstrate an urgent need for capability-based permission systems and mandatory security vetting before this attack vector is further exploited.

