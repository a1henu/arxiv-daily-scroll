---
layout: default
title: ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development
---

# ProjDevBench: Benchmarking AI Coding Agents on End-to-End Project Development
**arXiv**：[2602.01655v1](https://arxiv.org/abs/2602.01655) · [PDF](https://arxiv.org/pdf/2602.01655.pdf)  
**作者**：Pengrui Lu, Shiqi Zhang, Yunzhong Hou, Lyumanshan Ye, Chaoyi Huang, Zixi Chen, Ji Zeng, Hantao Jiang, Pengfei Liu, Yiwei Wang, Ming-Hsuan Yang  

**一句话要点**：提出ProjDevBench基准以评估AI编码代理在端到端项目开发中的能力

**关键词**：AI编码代理, 端到端项目开发, 基准测试, 系统架构设计, 功能正确性评估, LLM辅助代码审查

## 3 点简述
- 现有评估聚焦于问题级bug修复，缺乏端到端开发评估
- 结合在线评测与LLM辅助代码审查，评估系统设计、功能正确性和迭代优化
- 在20个编程问题上测试6个代理，总体接受率为27.38%，显示复杂设计挑战

## 摘要（原文）

> Recent coding agents can generate complete codebases from simple prompts, yet existing evaluations focus on issue-level bug fixing and lag behind end-to-end development. We introduce ProjDevBench, an end-to-end benchmark that provides project requirements to coding agents and evaluates the resulting repositories. Combining Online Judge (OJ) testing with LLM-assisted code review, the benchmark evaluates agents on (1) system architecture design, (2) functional correctness, and (3) iterative solution refinement. We curate 20 programming problems across 8 categories, covering both concept-oriented tasks and real-world application scenarios, and evaluate six coding agents built on different LLM backends. Our evaluation reports an overall acceptance rate of 27.38%: agents handle basic functionality and data structures but struggle with complex system design, time complexity optimization, and resource management. Our benchmark is available at https://github.com/zsworld6/projdevbench.

