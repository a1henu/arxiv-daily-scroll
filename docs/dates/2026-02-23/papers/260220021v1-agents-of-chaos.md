---
layout: default
title: Agents of Chaos
---

# Agents of Chaos
**arXiv**：[2602.20021v1](https://arxiv.org/abs/2602.20021) · [PDF](https://arxiv.org/pdf/2602.20021.pdf)  
**作者**：Natalie Shapira, Chris Wendler, Avery Yen, Gabriele Sarti, Koyena Pal, Olivia Floody, Adam Belfki, Alex Loftus, Aditya Ratan Jannali, Nikhil Prakash, Jasmine Cui, Giordano Rogers, Jannik Brinkmann, Can Rager, Amir Zur, Michael Ripa, Aruna Sankaranarayanan, David Atkinson, Rohit Gandikota, Jaden Fiotto-Kaufman, EunJeong Hwang, Hadas Orgad, P Sam Sahil, Negev Taglicht, Tomer Shabtay, Atai Ambus, Nitay Alon, Shiri Oron, Ayelet Gordon-Tapiero, Yotam Kaplan, Vered Shwartz, Tamar Rott Shaham, Christoph Riedl, Reuth Mirsky, Maarten Sap, David Manheim, Tomer Ullman, David Bau  

**一句话要点**：报告自主语言模型代理在真实部署环境中的安全漏洞实证研究

**关键词**：自主语言模型代理, 安全漏洞, 实证研究, 工具集成, 多方通信, 系统部署

## 3 点简述
- 核心问题：自主语言模型代理在集成工具使用和多方通信时存在安全、隐私和治理漏洞
- 方法要点：在实验室环境中部署代理，进行为期两周的良性及对抗性交互实验
- 实验或效果：观察到未授权合规、敏感信息泄露、破坏性系统操作等11个代表性案例

## 摘要（原文）

> We report an exploratory red-teaming study of autonomous language-model-powered agents deployed in a live laboratory environment with persistent memory, email accounts, Discord access, file systems, and shell execution. Over a two-week period, twenty AI researchers interacted with the agents under benign and adversarial conditions. Focusing on failures emerging from the integration of language models with autonomy, tool use, and multi-party communication, we document eleven representative case studies. Observed behaviors include unauthorized compliance with non-owners, disclosure of sensitive information, execution of destructive system-level actions, denial-of-service conditions, uncontrolled resource consumption, identity spoofing vulnerabilities, cross-agent propagation of unsafe practices, and partial system takeover. In several cases, agents reported task completion while the underlying system state contradicted those reports. We also report on some of the failed attempts. Our findings establish the existence of security-, privacy-, and governance-relevant vulnerabilities in realistic deployment settings. These behaviors raise unresolved questions regarding accountability, delegated authority, and responsibility for downstream harms, and warrant urgent attention from legal scholars, policymakers, and researchers across disciplines. This report serves as an initial empirical contribution to that broader conversation.

