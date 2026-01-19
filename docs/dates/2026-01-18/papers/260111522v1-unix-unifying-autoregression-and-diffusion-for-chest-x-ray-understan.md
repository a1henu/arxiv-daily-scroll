---
layout: default
title: UniX: Unifying Autoregression and Diffusion for Chest X-Ray Understanding and Generation
---

# UniX: Unifying Autoregression and Diffusion for Chest X-Ray Understanding and Generation
**arXiv**：[2601.11522v1](https://arxiv.org/abs/2601.11522) · [PDF](https://arxiv.org/pdf/2601.11522.pdf)  
**作者**：Ruiheng Zhang, Jingfeng Yao, Huangxuan Zhao, Hao Yan, Xiao He, Lei Chen, Zhou Wei, Yong Luo, Zengmao Wang, Lefei Zhang, Dacheng Tao, Bo Du  

**一句话要点**：提出UniX模型，通过解耦自回归与扩散分支统一胸部X光理解与生成任务。

**关键词**：医学基础模型, 胸部X光分析, 自回归模型, 扩散模型, 跨模态注意力, 多任务统一

## 3 点简述
- 核心问题：医学基础模型难以统一视觉理解与生成，因任务目标冲突导致性能妥协。
- 方法要点：采用自回归分支处理理解任务，扩散分支负责高保真生成，并引入跨模态自注意力机制动态引导生成。
- 实验或效果：在基准测试中，理解性能提升46.1%，生成质量提高24.2%，参数仅为LLM-CXR的四分之一。

## 摘要（原文）

> Despite recent progress, medical foundation models still struggle to unify visual understanding and generation, as these tasks have inherently conflicting goals: semantic abstraction versus pixel-level reconstruction. Existing approaches, typically based on parameter-shared autoregressive architectures, frequently lead to compromised performance in one or both tasks. To address this, we present UniX, a next-generation unified medical foundation model for chest X-ray understanding and generation. UniX decouples the two tasks into an autoregressive branch for understanding and a diffusion branch for high-fidelity generation. Crucially, a cross-modal self-attention mechanism is introduced to dynamically guide the generation process with understanding features. Coupled with a rigorous data cleaning pipeline and a multi-stage training strategy, this architecture enables synergistic collaboration between tasks while leveraging the strengths of diffusion models for superior generation. On two representative benchmarks, UniX achieves a 46.1% improvement in understanding performance (Micro-F1) and a 24.2% gain in generation quality (FD-RadDino), using only a quarter of the parameters of LLM-CXR. By achieving performance on par with task-specific models, our work establishes a scalable paradigm for synergistic medical image understanding and generation. Codes and models are available at https://github.com/ZrH42/UniX.

