---
layout: default
title: AutoBaxBuilder: Bootstrapping Code Security Benchmarking
---

# AutoBaxBuilder: Bootstrapping Code Security Benchmarking
**arXiv**：[2512.21132v1](https://arxiv.org/abs/2512.21132) · [PDF](https://arxiv.org/pdf/2512.21132.pdf)  
**作者**：Tobias von Arx, Niels Mündler, Mark Vero, Maximilian Baader, Martin Vechev  

**一句话要点**：提出AutoBaxBuilder框架以自动生成代码安全基准测试任务

**关键词**：代码安全基准测试, LLM生成代码评估, 自动化任务生成, 安全漏洞探测, 基准测试框架

## 3 点简述
- 核心问题：手动构建代码安全基准测试存在数据污染、任务扩展和难度提升不足的挑战
- 方法要点：利用LLM的代码理解能力，通过细粒度合理性检查生成功能测试和安全探测利用
- 实验或效果：生成任务成本低于10美元且耗时少于2小时，与专家构建任务对比验证质量

## 摘要（原文）

> As LLMs see wide adoption in software engineering, the reliable assessment of the correctness and security of LLM-generated code is crucial. Notably, prior work has demonstrated that security is often overlooked, exposing that LLMs are prone to generating code with security vulnerabilities. These insights were enabled by specialized benchmarks, crafted through significant manual effort by security experts. However, relying on manually-crafted benchmarks is insufficient in the long term, because benchmarks (i) naturally end up contaminating training data, (ii) must extend to new tasks to provide a more complete picture, and (iii) must increase in difficulty to challenge more capable LLMs. In this work, we address these challenges and present AutoBaxBuilder, a framework that generates tasks and tests for code security benchmarking from scratch. We introduce a robust pipeline with fine-grained plausibility checks, leveraging the code understanding capabilities of LLMs to construct functionality tests and end-to-end security-probing exploits. To confirm the quality of the generated benchmark, we conduct both a qualitative analysis and perform quantitative experiments, comparing it against tasks constructed by human experts. We use AutoBaxBuilder to construct entirely new tasks and release them to the public as AutoBaxBench, together with a thorough evaluation of the security capabilities of LLMs on these tasks. We find that a new task can be generated in under 2 hours, costing less than USD 10.

