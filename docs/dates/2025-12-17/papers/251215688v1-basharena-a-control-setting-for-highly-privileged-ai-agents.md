---
layout: default
title: BashArena: A Control Setting for Highly Privileged AI Agents
---

# BashArena: A Control Setting for Highly Privileged AI Agents
**arXiv**：[2512.15688v1](https://arxiv.org/abs/2512.15688) · [PDF](https://arxiv.org/pdf/2512.15688.pdf)  
**作者**：Adam Kaufman, James Lucassen, Tyler Tracy, Cody Rushing, Aryan Bhatt  

**一句话要点**：提出BashArena控制环境，用于研究高权限AI代理的安全控制技术

**关键词**：AI控制, 高权限代理, 安全评估, Linux系统任务, 破坏检测

## 3 点简述
- 研究高权限AI代理可能滥用权限造成的安全风险问题
- 构建包含637个Linux系统任务的测试环境与四种破坏目标
- 评估前沿LLM在任务完成、隐蔽破坏与检测方面的表现

## 摘要（原文）

> Future AI agents might run autonomously with elevated privileges. If these agents are misaligned, they might abuse these privileges to cause serious damage. The field of AI control develops techniques that make it harder for misaligned AIs to cause such damage, while preserving their usefulness. We introduce BashArena, a setting for studying AI control techniques in security-critical environments. BashArena contains 637 Linux system administration and infrastructure engineering tasks in complex, realistic environments, along with four sabotage objectives (execute malware, exfiltrate secrets, escalate privileges, and disable firewall) for a red team to target. We evaluate multiple frontier LLMs on their ability to complete tasks, perform sabotage undetected, and detect sabotage attempts. Claude Sonnet 4.5 successfully executes sabotage while evading monitoring by GPT-4.1 mini 26% of the time, at 4% trajectory-wise FPR. Our findings provide a baseline for designing more effective control protocols in BashArena. We release the dataset as a ControlArena setting and share our task generation pipeline.

