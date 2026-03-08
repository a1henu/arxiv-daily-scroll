---
layout: default
title: EVMbench: Evaluating AI Agents on Smart Contract Security
---

# EVMbench: Evaluating AI Agents on Smart Contract Security
**arXiv**：[2603.04915v1](https://arxiv.org/abs/2603.04915) · [PDF](https://arxiv.org/pdf/2603.04915.pdf)  
**作者**：Justin Wang, Andreas Bigger, Xiaohai Xu, Justin W. Lin, Andy Applebaum, Tejal Patwardhan, Alpin Yukseloglu, Olivia Watkins  

**一句话要点**：提出EVMbench以评估AI代理在智能合约安全中的检测、修补和利用能力。

**关键词**：智能合约安全, AI代理评估, 漏洞检测, 以太坊环境, 程序化评分

## 3 点简述
- 核心问题：智能合约漏洞导致重大损失，需评估AI代理在安全改进与风险增加方面的能力。
- 方法要点：基于117个精选漏洞，在本地以太坊环境中使用程序化评分进行端到端评估。
- 实验或效果：前沿代理能发现并利用漏洞，发布代码和工具支持持续测量。

## 摘要（原文）

> Smart contracts on public blockchains now manage large amounts of value, and vulnerabilities in these systems can lead to substantial losses. As AI agents become more capable at reading, writing, and running code, it is natural to ask how well they can already navigate this landscape, both in ways that improve security and in ways that might increase risk. We introduce EVMbench, an evaluation that measures the ability of agents to detect, patch, and exploit smart contract vulnerabilities. EVMbench draws on 117 curated vulnerabilities from 40 repositories and, in the most realistic setting, uses programmatic grading based on tests and blockchain state under a local Ethereum execution environment. We evaluate a range of frontier agents and find that they are capable of discovering and exploiting vulnerabilities end-to-end against live blockchain instances. We release code, tasks, and tooling to support continued measurement of these capabilities and future work on security.

