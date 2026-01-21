---
layout: default
title: HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation
---

# HardSecBench: Benchmarking the Security Awareness of LLMs for Hardware Code Generation
**arXiv**：[2601.13864v1](https://arxiv.org/abs/2601.13864) · [PDF](https://arxiv.org/pdf/2601.13864.pdf)  
**作者**：Qirui Chen, Jingxian Shuai, Shuangwu Chen, Shenghao Ye, Zijian Wen, Xufei Su, Jie Jin, Jiangming Li, Jun Chen, Xiaobin Tan, Jian Yang  

**一句话要点**：提出HardSecBench以评估LLM在硬件代码生成中的安全认知能力

**关键词**：硬件代码生成, 安全基准, LLM评估, Verilog RTL, CWE条目, 多智能体管道

## 3 点简述
- 现有研究多关注LLM生成代码的功能正确性，忽视其潜在安全风险
- 构建包含924个任务的基准，覆盖Verilog RTL和C代码，涉及76个硬件相关CWE条目
- 评估发现LLM常满足功能需求但遗留安全漏洞，提示方式影响安全结果

## 摘要（原文）

> Large language models (LLMs) are being increasingly integrated into practical hardware and firmware development pipelines for code generation. Existing studies have primarily focused on evaluating the functional correctness of LLM-generated code, yet paid limited attention to its security issues. However, LLM-generated code that appears functionally sound may embed security flaws which could induce catastrophic damages after deployment. This critical research gap motivates us to design a benchmark for assessing security awareness under realistic specifications. In this work, we introduce HardSecBench, a benchmark with 924 tasks spanning Verilog Register Transfer Level (RTL) and firmware-level C, covering 76 hardware-relevant Common Weakness Enumeration (CWE) entries. Each task includes a structured specification, a secure reference implementation, and executable tests. To automate artifact synthesis, we propose a multi-agent pipeline that decouples synthesis from verification and grounds evaluation in execution evidence, enabling reliable evaluation. Using HardSecBench, we evaluate a range of LLMs on hardware and firmware code generation and find that models often satisfy functional requirements while still leaving security risks. We also find that security results vary with prompting. These findings highlight pressing challenges and offer actionable insights for future advancements in LLM-assisted hardware design. Our data and code will be released soon.

