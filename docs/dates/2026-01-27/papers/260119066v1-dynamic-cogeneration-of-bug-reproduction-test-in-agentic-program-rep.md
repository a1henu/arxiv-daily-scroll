---
layout: default
title: Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair
---

# Dynamic Cogeneration of Bug Reproduction Test in Agentic Program Repair
**arXiv**：[2601.19066v1](https://arxiv.org/abs/2601.19066) · [PDF](https://arxiv.org/pdf/2601.19066.pdf)  
**作者**：Runxiang Cheng, Michele Tufano, José Cambronero, Renyao Wei, Sherry Shi, Grant Uy, Pat Rondon, Franjo Ivančić  

**一句话要点**：提出动态协同生成策略，在代理式自动程序修复中同时生成错误复现测试与修复补丁

**关键词**：代理式自动程序修复, 错误复现测试, 协同生成, 补丁选择, 软件工程自动化, 人工智能辅助开发

## 3 点简述
- 研究代理式自动程序修复中协同生成问题，即在同一补丁中生成修复和错误复现测试
- 评估不同协同生成策略在120个谷歌报告错误上的效果，并开发考虑测试变更信息的补丁选择器
- 实验表明协同生成在不降低修复率下，能生成至少与专用测试代理相当的错误复现测试，减少工程维护成本

## 摘要（原文）

> Bug Reproduction Tests (BRTs) have been used in many agentic Automated Program Repair (APR) systems, primarily for validating promising fixes and aiding fix generation. In practice, when developers submit a patch, they often implement the BRT alongside the fix. Our experience deploying agentic APR reveals that developers similarly desire a BRT within AI-generated patches to increase their confidence. However, canonical APR systems tend to generate BRTs and fixes separately, or focus on producing only the fix in the final patch. In this paper, we study agentic APR in the context of cogeneration, where the APR agent is instructed to generate both a fix and a BRT in the same patch. We evaluate the effectiveness of different cogeneration strategies on 120 human-reported bugs at Google and characterize different cogeneration strategies by their influence on APR agent behavior. We develop and evaluate patch selectors that account for test change information to select patches with plausible fixes (and plausible BRTs). Finally, we analyze the root causes of failed cogeneration trajectories. Importantly, we show that cogeneration allows the APR agent to generate BRTs for at least as many bugs as a dedicated BRT agent, without compromising the generation rate of plausible fixes, thereby reducing engineering effort in maintaining and coordinating separate generation pipelines for fix and BRT at scale.

