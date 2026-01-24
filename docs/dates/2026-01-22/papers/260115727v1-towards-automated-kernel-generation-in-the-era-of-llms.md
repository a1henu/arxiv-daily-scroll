---
layout: default
title: Towards Automated Kernel Generation in the Era of LLMs
---

# Towards Automated Kernel Generation in the Era of LLMs
**arXiv**：[2601.15727v1](https://arxiv.org/abs/2601.15727) · [PDF](https://arxiv.org/pdf/2601.15727.pdf)  
**作者**：Yang Yu, Peiyu Zang, Chi Hsu Tsai, Haiming Wu, Yixin Shen, Jialing Zhang, Haoyu Wang, Zhiyou Xiao, Jingze Shi, Yuyu Luo, Wentao Zhang, Chunlei Men, Guang Liu, Yonghua Lin  

**一句话要点**：综述LLM驱动的自动化内核生成方法，以解决内核工程耗时且不可扩展的问题。

**关键词**：内核生成, 大语言模型, 自动化优化, 代理系统, 硬件加速, AI系统性能

## 3 点简述
- 核心问题：内核工程依赖专家知识，耗时且不可扩展，制约AI系统性能。
- 方法要点：利用LLM压缩专家知识，结合代理系统实现迭代优化，自动化内核生成。
- 实验或效果：系统梳理现有方法、数据集和基准，为领域提供结构化参考和开源资源。

## 摘要（原文）

> The performance of modern AI systems is fundamentally constrained by the quality of their underlying kernels, which translate high-level algorithmic semantics into low-level hardware operations. Achieving near-optimal kernels requires expert-level understanding of hardware architectures and programming models, making kernel engineering a critical but notoriously time-consuming and non-scalable process. Recent advances in large language models (LLMs) and LLM-based agents have opened new possibilities for automating kernel generation and optimization. LLMs are well-suited to compress expert-level kernel knowledge that is difficult to formalize, while agentic systems further enable scalable optimization by casting kernel development as an iterative, feedback-driven loop. Rapid progress has been made in this area. However, the field remains fragmented, lacking a systematic perspective for LLM-driven kernel generation. This survey addresses this gap by providing a structured overview of existing approaches, spanning LLM-based approaches and agentic optimization workflows, and systematically compiling the datasets and benchmarks that underpin learning and evaluation in this domain. Moreover, key open challenges and future research directions are further outlined, aiming to establish a comprehensive reference for the next generation of automated kernel optimization. To keep track of this field, we maintain an open-source GitHub repository at https://github.com/flagos-ai/awesome-LLM-driven-kernel-generation.

