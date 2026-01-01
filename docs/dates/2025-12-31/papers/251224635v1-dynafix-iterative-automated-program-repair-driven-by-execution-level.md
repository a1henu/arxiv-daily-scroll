---
layout: default
title: DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information
---

# DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information
**arXiv**：[2512.24635v1](https://arxiv.org/abs/2512.24635) · [PDF](https://arxiv.org/pdf/2512.24635.pdf)  
**作者**：Zhili Huang, Ling Xu, Chao Liu, Weifeng Sun, Xu Zhang, Yan Lei, Meng Yan, Hongyu Zhang  

**一句话要点**：提出DynaFix以解决自动程序修复中动态信息利用不足的问题，通过迭代执行级信息驱动修复。

**关键词**：自动程序修复, 动态信息驱动, 迭代修复, 执行级分析, 大语言模型, 缺陷修复

## 3 点简述
- 核心问题：现有方法依赖静态分析或粗粒度反馈，忽略运行时行为，限制复杂bug修复效果。
- 方法要点：迭代捕获变量状态、控制流路径等执行级信息，转化为结构化提示指导LLM生成补丁。
- 实验或效果：在Defects4J基准上修复186个bug，提升10%，减少70%补丁搜索空间，效率高。

## 摘要（原文）

> Automated Program Repair (APR) aims to automatically generate correct patches for buggy programs. Recent approaches leveraging large language models (LLMs) have shown promise but face limitations. Most rely solely on static analysis, ignoring runtime behaviors. Some attempt to incorporate dynamic signals, but these are often restricted to training or fine-tuning, or injected only once into the repair prompt, without iterative use. This fails to fully capture program execution. Current iterative repair frameworks typically rely on coarse-grained feedback, such as pass/fail results or exception types, and do not leverage fine-grained execution-level information effectively. As a result, models struggle to simulate human stepwise debugging, limiting their effectiveness in multi-step reasoning and complex bug repair.
>   To address these challenges, we propose DynaFix, an execution-level dynamic information-driven APR method that iteratively leverages runtime information to refine the repair process. In each repair round, DynaFix captures execution-level dynamic information such as variable states, control-flow paths, and call stacks, transforming them into structured prompts to guide LLMs in generating candidate patches. If a patch fails validation, DynaFix re-executes the modified program to collect new execution information for the next attempt. This iterative loop incrementally improves patches based on updated feedback, similar to the stepwise debugging practices of human developers. We evaluate DynaFix on the Defects4J v1.2 and v2.0 benchmarks. DynaFix repairs 186 single-function bugs, a 10% improvement over state-of-the-art baselines, including 38 bugs previously unrepaired. It achieves correct patches within at most 35 attempts, reducing the patch search space by 70% compared with existing methods, thereby demonstrating both effectiveness and efficiency in repairing complex bugs.

