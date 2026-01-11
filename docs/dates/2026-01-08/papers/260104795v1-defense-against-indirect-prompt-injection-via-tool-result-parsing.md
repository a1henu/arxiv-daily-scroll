---
layout: default
title: Defense Against Indirect Prompt Injection via Tool Result Parsing
---

# Defense Against Indirect Prompt Injection via Tool Result Parsing
**arXiv**：[2601.04795v1](https://arxiv.org/abs/2601.04795) · [PDF](https://arxiv.org/pdf/2601.04795.pdf)  
**作者**：Qiang Yu, Xinran Cheng, Chuanyi Liu  

**一句话要点**：提出基于工具结果解析的方法以防御间接提示注入攻击，提升LLM代理在物理控制场景中的安全性。

**关键词**：间接提示注入防御, 工具结果解析, LLM代理安全, 物理控制系统, 攻击成功率降低

## 3 点简述
- 核心问题：间接提示注入攻击通过工具调用结果嵌入恶意指令，威胁LLM代理在自主系统中的决策安全。
- 方法要点：通过工具结果解析提供精确数据，同时过滤恶意代码，无需依赖高开销检测模型或易受攻击的提示工程。
- 实验或效果：在保持竞争性攻击下实用性的同时，实现了最低的攻击成功率，显著优于现有方法。

## 摘要（原文）

> As LLM agents transition from digital assistants to physical controllers in autonomous systems and robotics, they face an escalating threat from indirect prompt injection. By embedding adversarial instructions into the results of tool calls, attackers can hijack the agent's decision-making process to execute unauthorized actions. This vulnerability poses a significant risk as agents gain more direct control over physical environments. Existing defense mechanisms against Indirect Prompt Injection (IPI) generally fall into two categories. The first involves training dedicated detection models; however, this approach entails high computational overhead for both training and inference, and requires frequent updates to keep pace with evolving attack vectors. Alternatively, prompt-based methods leverage the inherent capabilities of LLMs to detect or ignore malicious instructions via prompt engineering. Despite their flexibility, most current prompt-based defenses suffer from high Attack Success Rates (ASR), demonstrating limited robustness against sophisticated injection attacks. In this paper, we propose a novel method that provides LLMs with precise data via tool result parsing while effectively filtering out injected malicious code. Our approach achieves competitive Utility under Attack (UA) while maintaining the lowest Attack Success Rate (ASR) to date, significantly outperforming existing methods. Code is available at GitHub.

