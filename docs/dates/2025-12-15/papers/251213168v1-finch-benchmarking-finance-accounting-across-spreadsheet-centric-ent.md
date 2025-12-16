---
layout: default
title: Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows
---

# Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows
**arXiv**：[2512.13168v1](https://arxiv.org/abs/2512.13168) · [PDF](https://arxiv.org/pdf/2512.13168.pdf)  
**作者**：Haoyu Dong, Pengkun Zhang, Yan Gao, Xuanyu Dong, Yilin Cheng, Mingzhe Lu, Adina Yakefu, Shuxin Zheng  

**一句话要点**：提出Finch基准以评估AI代理在真实企业财务与会计工作流中的性能

**关键词**：财务基准, 企业工作流, 多模态评估, 电子表格分析, AI代理测试

## 3 点简述
- 核心问题：现有AI评估缺乏真实企业级财务工作流基准，涉及多模态、长时程和协作任务
- 方法要点：基于真实企业数据，结合LLM辅助发现与专家标注，构建172个复合工作流
- 实验或效果：评估前沿AI系统，GPT 5.1 Pro仅通过38.4%工作流，凸显企业工作流对AI的挑战

## 摘要（原文）

> We introduce a finance & accounting benchmark (Finch) for evaluating AI agents on real-world, enterprise-grade professional workflows -- interleaving data entry, structuring, formatting, web search, cross-file retrieval, calculation, modeling, validation, translation, visualization, and reporting. Finch is sourced from authentic enterprise workspaces at Enron (15,000 spreadsheets and 500,000 emails from 150 employees) and other financial institutions, preserving in-the-wild messiness across multimodal artifacts (text, tables, formulas, charts, code, and images) and spanning diverse domains such as budgeting, trading, and asset management.
>   We propose a workflow construction process that combines LLM-assisted discovery with expert annotation: (1) LLM-assisted, expert-verified derivation of workflows from real-world email threads and version histories of spreadsheet files, and (2) meticulous expert annotation for workflows, requiring over 700 hours of domain-expert effort. This yields 172 composite workflows with 384 tasks, involving 1,710 spreadsheets with 27 million cells, along with PDFs and other artifacts, capturing the intrinsically messy, long-horizon, knowledge-intensive, and collaborative nature of real-world enterprise work.
>   We conduct both human and automated evaluations of frontier AI systems including GPT 5.1, Claude Sonnet 4.5, Gemini 3 Pro, Grok 4, and Qwen 3 Max, and GPT 5.1 Pro spends 48 hours in total yet passes only 38.4% of workflows, while Claude Sonnet 4.5 passes just 25.0%. Comprehensive case studies further surface the challenges that real-world enterprise workflows pose for AI agents.

