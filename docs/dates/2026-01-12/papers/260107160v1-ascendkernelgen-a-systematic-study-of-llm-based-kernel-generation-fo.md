---
layout: default
title: AscendKernelGen: A Systematic Study of LLM-Based Kernel Generation for Neural Processing Units
---

# AscendKernelGen: A Systematic Study of LLM-Based Kernel Generation for Neural Processing Units
**arXiv**：[2601.07160v1](https://arxiv.org/abs/2601.07160) · [PDF](https://arxiv.org/pdf/2601.07160.pdf)  
**作者**：Xinzi Cao, Jianyang Zhai, Pengfei Li, Zhiheng Hu, Cen Yan, Bingxu Mu, Guanghuan Fang, Bin She, Jiayu Li, Yihan Su, Dongyang Tao, Xiansong Huang, Fan Xu, Feidiao Yang, Yao Lu, Chang-Dong Wang, Yutong Lu, Weicheng Xue, Bin Zhou, Yonghong Tian  

**一句话要点**：提出AscendKernelGen框架，基于LLM生成NPU高性能计算内核，解决硬件特定代码生成难题。

**关键词**：NPU内核生成, 大语言模型, 领域自适应, 强化学习, 代码生成评估

## 3 点简述
- 核心问题：通用LLM在NPU领域因严格约束和数据稀缺，生成复杂内核成功率近零。
- 方法要点：构建Ascend-CoT数据集和KernelGen-LM模型，结合监督微调与强化学习，集成生成-评估框架。
- 实验或效果：在复杂内核上，编译成功率从0%提升至95.5%，功能正确率达64.3%。

## 摘要（原文）

> To meet the ever-increasing demand for computational efficiency, Neural Processing Units (NPUs) have become critical in modern AI infrastructure. However, unlocking their full potential requires developing high-performance compute kernels using vendor-specific Domain-Specific Languages (DSLs), a task that demands deep hardware expertise and is labor-intensive. While Large Language Models (LLMs) have shown promise in general code generation, they struggle with the strict constraints and scarcity of training data in the NPU domain. Our preliminary study reveals that state-of-the-art general-purpose LLMs fail to generate functional complex kernels for Ascend NPUs, yielding a near-zero success rate. To address these challenges, we propose AscendKernelGen, a generation-evaluation integrated framework for NPU kernel development. We introduce Ascend-CoT, a high-quality dataset incorporating chain-of-thought reasoning derived from real-world kernel implementations, and KernelGen-LM, a domain-adaptive model trained via supervised fine-tuning and reinforcement learning with execution feedback. Furthermore, we design NPUKernelBench, a comprehensive benchmark for assessing compilation, correctness, and performance across varying complexity levels. Experimental results demonstrate that our approach significantly bridges the gap between general LLMs and hardware-specific coding. Specifically, the compilation success rate on complex Level-2 kernels improves from 0% to 95.5% (Pass@10), while functional correctness achieves 64.3% compared to the baseline's complete failure. These results highlight the critical role of domain-specific reasoning and rigorous evaluation in automating accelerator-aware code generation.

