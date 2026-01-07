---
layout: default
title: DiffBench Meets DiffAgent: End-to-End LLM-Driven Diffusion Acceleration Code Generation
---

# DiffBench Meets DiffAgent: End-to-End LLM-Driven Diffusion Acceleration Code Generation
**arXiv**：[2601.03178v1](https://arxiv.org/abs/2601.03178) · [PDF](https://arxiv.org/pdf/2601.03178.pdf)  
**作者**：Jiajun jiao, Haowei Zhu, Puyuan Yang, Jianghui Wang, Ji Liu, Ziqiong Liu, Dong Li, Yuejian Fang, Junhai Yong, Bin Wang, Emad Barsoum  

**一句话要点**：提出DiffBench与DiffAgent框架，通过LLM驱动自动生成扩散模型加速代码以解决计算开销问题。

**关键词**：扩散模型加速, LLM驱动代码生成, 自动化评估基准, 遗传算法优化, 闭环工作流

## 3 点简述
- 扩散模型多步推理导致高计算开销，阻碍实际部署，需结合多种加速技术。
- DiffBench提供三阶段自动化评估基准，DiffAgent采用闭环工作流生成优化加速策略与代码。
- 实验表明DiffBench全面评估生成代码，DiffAgent在生成有效加速策略上显著优于现有LLM。

## 摘要（原文）

> Diffusion models have achieved remarkable success in image and video generation. However, their inherently multiple step inference process imposes substantial computational overhead, hindering real-world deployment. Accelerating diffusion models is therefore essential, yet determining how to combine multiple model acceleration techniques remains a significant challenge. To address this issue, we introduce a framework driven by large language models (LLMs) for automated acceleration code generation and evaluation. First, we present DiffBench, a comprehensive benchmark that implements a three stage automated evaluation pipeline across diverse diffusion architectures, optimization combinations and deployment scenarios. Second, we propose DiffAgent, an agent that generates optimal acceleration strategies and codes for arbitrary diffusion models. DiffAgent employs a closed-loop workflow in which a planning component and a debugging component iteratively refine the output of a code generation component, while a genetic algorithm extracts performance feedback from the execution environment to guide subsequent code refinements. We provide a detailed explanation of the DiffBench construction and the design principles underlying DiffAgent. Extensive experiments show that DiffBench offers a thorough evaluation of generated codes and that DiffAgent significantly outperforms existing LLMs in producing effective diffusion acceleration strategies.

