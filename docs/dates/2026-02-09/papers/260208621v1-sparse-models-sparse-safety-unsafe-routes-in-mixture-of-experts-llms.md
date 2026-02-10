---
layout: default
title: Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs
---

# Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs
**arXiv**：[2602.08621v1](https://arxiv.org/abs/2602.08621) · [PDF](https://arxiv.org/pdf/2602.08621.pdf)  
**作者**：Yukun Jiang, Hai Huang, Mingjie Li, Yage Zhang, Michael Backes, Yang Zhang  

**一句话要点**：提出不安全路由概念与F-SOUR框架，揭示MoE LLMs稀疏架构的安全风险

**关键词**：混合专家模型, 路由安全, 攻击框架, 安全风险, 大语言模型, 稀疏架构

## 3 点简述
- 核心问题：MoE LLMs稀疏架构中路由配置可能被操纵，导致安全输出转为有害内容
- 方法要点：引入RoSais评分量化路由器安全关键性，并开发F-SOUR框架发现具体不安全路由
- 实验或效果：在多个MoE LLM上，F-SOUR在JailbreakBench和AdvBench上攻击成功率分别达0.90和0.98

## 摘要（原文）

> By introducing routers to selectively activate experts in Transformer layers, the mixture-of-experts (MoE) architecture significantly reduces computational costs in large language models (LLMs) while maintaining competitive performance, especially for models with massive parameters. However, prior work has largely focused on utility and efficiency, leaving the safety risks associated with this sparse architecture underexplored. In this work, we show that the safety of MoE LLMs is as sparse as their architecture by discovering unsafe routes: routing configurations that, once activated, convert safe outputs into harmful ones. Specifically, we first introduce the Router Safety importance score (RoSais) to quantify the safety criticality of each layer's router. Manipulation of only the high-RoSais router(s) can flip the default route into an unsafe one. For instance, on JailbreakBench, masking 5 routers in DeepSeek-V2-Lite increases attack success rate (ASR) by over 4$\times$ to 0.79, highlighting an inherent risk that router manipulation may naturally occur in MoE LLMs. We further propose a Fine-grained token-layer-wise Stochastic Optimization framework to discover more concrete Unsafe Routes (F-SOUR), which explicitly considers the sequentiality and dynamics of input tokens. Across four representative MoE LLM families, F-SOUR achieves an average ASR of 0.90 and 0.98 on JailbreakBench and AdvBench, respectively. Finally, we outline defensive perspectives, including safety-aware route disabling and router training, as promising directions to safeguard MoE LLMs. We hope our work can inform future red-teaming and safeguarding of MoE LLMs. Our code is provided in https://github.com/TrustAIRLab/UnsafeMoE.

