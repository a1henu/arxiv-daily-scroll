---
layout: default
title: Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub
---

# Where Do AI Coding Agents Fail? An Empirical Study of Failed Agentic Pull Requests in GitHub
**arXiv**：[2601.15195v1](https://arxiv.org/abs/2601.15195) · [PDF](https://arxiv.org/pdf/2601.15195.pdf)  
**作者**：Ramtin Ehsani, Sakshi Pathak, Shriya Rawal, Abdullah Al Mujahid, Mia Mohammad Imran, Preetha Chatterjee  

**一句话要点**：实证研究GitHub中AI编码代理失败原因，分析未合并PR的定量与定性特征

**关键词**：AI编码代理, GitHub拉取请求, 实证研究, 代码变更分析, 人机协作, 软件工程

## 3 点简述
- 核心问题：AI编码代理提交的PR为何失败，缺乏实际行为与合并失败原因的系统研究
- 方法要点：大规模分析33k个代理PR，定量评估合并结果、代码变更、CI构建和评审动态
- 实验或效果：发现文档和CI任务成功率最高，性能修复最差；定性分析揭示拒绝模式如重复PR和代理错位

## 摘要（原文）

> AI coding agents are now submitting pull requests (PRs) to software projects, acting not just as assistants but as autonomous contributors. As these agentic contributions are rapidly increasing across real repositories, little is known about how they behave in practice and why many of them fail to be merged. In this paper, we conduct a large-scale study of 33k agent-authored PRs made by five coding agents across GitHub. (RQ1) We first quantitatively characterize merged and not-merged PRs along four broad dimensions: 1) merge outcomes across task types, 2) code changes, 3) CI build results, and 4) review dynamics. We observe that tasks related to documentation, CI, and build update achieve the highest merge success, whereas performance and bug-fix tasks perform the worst. Not-merged PRs tend to involve larger code changes, touch more files, and often do not pass the project's CI/CD pipeline validation. (RQ2) To further investigate why some agentic PRs are not merged, we qualitatively analyze 600 PRs to derive a hierarchical taxonomy of rejection patterns. This analysis complements the quantitative findings in RQ1 by uncovering rejection reasons not captured by quantitative metrics, including lack of meaningful reviewer engagement, duplicate PRs, unwanted feature implementations, and agent misalignment. Together, our findings highlight key socio-technical and human-AI collaboration factors that are critical to improving the success of future agentic workflows.

