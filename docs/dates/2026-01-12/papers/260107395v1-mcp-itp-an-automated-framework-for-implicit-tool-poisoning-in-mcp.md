---
layout: default
title: MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP
---

# MCP-ITP: An Automated Framework for Implicit Tool Poisoning in MCP
**arXiv**：[2601.07395v1](https://arxiv.org/abs/2601.07395) · [PDF](https://arxiv.org/pdf/2601.07395.pdf)  
**作者**：Ruiqi Li, Zhiqiang Wang, Yunhao Yao, Xiang-Yang Li  

**一句话要点**：提出MCP-ITP框架以自动化生成隐式工具投毒攻击，在MCP生态中提升攻击成功率并规避检测。

**关键词**：隐式工具投毒, 模型上下文协议, 黑盒优化, 攻击成功率, 恶意工具检测, 自动化框架

## 3 点简述
- 核心问题：MCP中工具集成引入隐式投毒攻击风险，恶意元数据诱导代理调用高权限工具执行恶意操作。
- 方法要点：将投毒工具生成建模为黑盒优化问题，利用评估和检测LLM的反馈迭代优化攻击成功率。
- 实验或效果：在MCPTox数据集上测试12个LLM代理，攻击成功率最高达84.2%，恶意工具检测率低至0.3%。

## 摘要（原文）

> To standardize interactions between LLM-based agents and their environments, the Model Context Protocol (MCP) was proposed and has since been widely adopted. However, integrating external tools expands the attack surface, exposing agents to tool poisoning attacks. In such attacks, malicious instructions embedded in tool metadata are injected into the agent context during MCP registration phase, thereby manipulating agent behavior. Prior work primarily focuses on explicit tool poisoning or relied on manually crafted poisoned tools. In contrast, we focus on a particularly stealthy variant: implicit tool poisoning, where the poisoned tool itself remains uninvoked. Instead, the instructions embedded in the tool metadata induce the agent to invoke a legitimate but high-privilege tool to perform malicious operations. We propose MCP-ITP, the first automated and adaptive framework for implicit tool poisoning within the MCP ecosystem. MCP-ITP formulates poisoned tool generation as a black-box optimization problem and employs an iterative optimization strategy that leverages feedback from both an evaluation LLM and a detection LLM to maximize Attack Success Rate (ASR) while evading current detection mechanisms. Experimental results on the MCPTox dataset across 12 LLM agents demonstrate that MCP-ITP consistently outperforms the manually crafted baseline, achieving up to 84.2% ASR while suppressing the Malicious Tool Detection Rate (MDR) to as low as 0.3%.

