---
layout: default
title: Beyond the Benchmark: Innovative Defenses Against Prompt Injection Attacks
---

# Beyond the Benchmark: Innovative Defenses Against Prompt Injection Attacks
**arXiv**：[2512.16307v1](https://arxiv.org/abs/2512.16307) · [PDF](https://arxiv.org/pdf/2512.16307.pdf)  
**作者**：Safwan Shaheer, G. M. Refatul Islam, Mohammad Rafid Hamid, Tahsin Zaman Jilan  

**一句话要点**：提出基于种子防御的迭代框架，以增强小型开源LLMs在边缘设备上抵御提示注入攻击的能力。

**关键词**：提示注入攻击, 小型开源LLMs, 边缘设备部署, 防御机制, 目标劫持检测, 迭代优化

## 3 点简述
- 核心问题：提示注入攻击对小型开源LLMs（如LLaMA系列）构成安全风险，尤其在资源受限的边缘部署场景中。
- 方法要点：引入新防御机制，利用种子防御（如思维链）迭代优化防御提示，自动生成有效防御。
- 实验或效果：系统评估显示，该方法显著降低攻击成功率与误检率，有效检测目标劫持漏洞，提升模型安全性。

## 摘要（原文）

> In this fast-evolving area of LLMs, our paper discusses the significant security risk presented by prompt injection attacks. It focuses on small open-sourced models, specifically the LLaMA family of models. We introduce novel defense mechanisms capable of generating automatic defenses and systematically evaluate said generated defenses against a comprehensive set of benchmarked attacks. Thus, we empirically demonstrated the improvement proposed by our approach in mitigating goal-hijacking vulnerabilities in LLMs. Our work recognizes the increasing relevance of small open-sourced LLMs and their potential for broad deployments on edge devices, aligning with future trends in LLM applications. We contribute to the greater ecosystem of open-source LLMs and their security in the following: (1) assessing present prompt-based defenses against the latest attacks, (2) introducing a new framework using a seed defense (Chain Of Thoughts) to refine the defense prompts iteratively, and (3) showing significant improvements in detecting goal hijacking attacks. Out strategies significantly reduce the success rates of the attacks and false detection rates while at the same time effectively detecting goal-hijacking capabilities, paving the way for more secure and efficient deployments of small and open-source LLMs in resource-constrained environments.

