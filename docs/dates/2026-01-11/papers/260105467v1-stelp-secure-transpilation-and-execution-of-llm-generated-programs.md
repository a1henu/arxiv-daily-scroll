---
layout: default
title: STELP: Secure Transpilation and Execution of LLM-Generated Programs
---

# STELP: Secure Transpilation and Execution of LLM-Generated Programs
**arXiv**：[2601.05467v1](https://arxiv.org/abs/2601.05467) · [PDF](https://arxiv.org/pdf/2601.05467.pdf)  
**作者**：Swapnil Shinde, Sahil Wadhwa, Andy Luo, Emily Chen  

**一句话要点**：提出STELP安全转译执行器，以安全可控方式执行LLM生成代码，解决生产AI系统代码安全问题。

**关键词**：LLM代码生成, 安全执行, 转译器, 生产AI系统, 代码安全, 多智能体框架

## 3 点简述
- 核心问题：LLM生成代码存在不稳定、错误和漏洞，如数据中毒和恶意攻击，阻碍其在生产AI系统中的直接应用。
- 方法要点：设计STELP安全转译执行器，在受控环境中执行LLM生成代码，弥补传统安全测试和人工监督的不足。
- 实验或效果：基于人工验证的不安全代码数据集和公开数据集进行基准测试，在安全性、正确性和延迟方面显著优于现有方法。

## 摘要（原文）

> Rapid evolution of Large Language Models (LLMs) has achieved major advances in reasoning, planning, and function-calling capabilities. Multi-agentic collaborative frameworks using such LLMs place them at the center of solving software development-related tasks such as code generation. However, direct use of LLM generated code in production software development systems is problematic. The code could be unstable or erroneous and contain vulnerabilities such as data poisoning, malicious attacks, and hallucinations that could lead to widespread system malfunctions. This prohibits the adoption of LLM generated code in production AI systems where human code reviews and traditional secure testing tools are impractical or untrustworthy. In this paper, we discuss safety and reliability problems with the execution of LLM generated code and propose a Secure Transpiler and Executor of LLM-Generated Program (STELP), capable of executing LLM-generated code in a controlled and safe manner. STELP secures autonomous production AI systems involving code generation, filling the critical void left by the impracticality or limitations of traditional secure testing methodologies and human oversight. This includes applications such as headless code generation-execution and LLMs that produce executable code snippets as an action plan to be executed in real time. We contribute a human-validated dataset of insecure code snippets and benchmark our approach on publicly available datasets for correctness, safety, and latency. Our results demonstrate that our approach outperforms an existing method by a significant margin, particularly in its ability to safely execute risky code snippets. Warning: This paper contains malicious code snippets that should be run with caution.

