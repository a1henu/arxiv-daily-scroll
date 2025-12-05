---
layout: default
title: Automating Complex Document Workflows via Stepwise and Rollback-Enabled Operation Orchestration
---

# Automating Complex Document Workflows via Stepwise and Rollback-Enabled Operation Orchestration
**arXiv**：[2512.04445v1](https://arxiv.org/abs/2512.04445) · [PDF](https://arxiv.org/pdf/2512.04445.pdf)  
**作者**：Yanbin Zhang, Hanhui Ye, Yue Bai, Qiming Zhang, Liao Xiang, Wu Mianzhi, Renjun Hu  

**一句话要点**：提出AutoDW框架，通过逐步和可回滚的操作编排自动化复杂文档工作流

**关键词**：文档工作流自动化, 操作编排, 回滚机制, 长程任务执行, API规划

## 3 点简述
- 核心问题：现有代理系统难以自动化多步骤、会话级文档工作流，缺乏过程控制
- 方法要点：AutoDW基于用户指令、API候选和文档状态逐步规划，支持参数和API级回滚机制
- 实验或效果：在250个会话基准上，指令和会话级任务完成率分别达90%和62%，优于基线

## 摘要（原文）

> Workflow automation promises substantial productivity gains in everyday document-related tasks. While prior agentic systems can execute isolated instructions, they struggle with automating multi-step, session-level workflows due to limited control over the operational process. To this end, we introduce AutoDW, a novel execution framework that enables stepwise, rollback-enabled operation orchestration. AutoDW incrementally plans API actions conditioned on user instructions, intent-filtered API candidates, and the evolving states of the document. It further employs robust rollback mechanisms at both the argument and API levels, enabling dynamic correction and fault tolerance. These designs together ensure that the execution trajectory of AutoDW remains aligned with user intent and document context across long-horizon workflows. To assess its effectiveness, we construct a comprehensive benchmark of 250 sessions and 1,708 human-annotated instructions, reflecting realistic document processing scenarios with interdependent instructions. AutoDW achieves 90% and 62% completion rates on instruction- and session-level tasks, respectively, outperforming strong baselines by 40% and 76%. Moreover, AutoDW also remains robust for the decision of backbone LLMs and on tasks with varying difficulty. Code and data will be open-sourced. Code: https://github.com/YJett/AutoDW

