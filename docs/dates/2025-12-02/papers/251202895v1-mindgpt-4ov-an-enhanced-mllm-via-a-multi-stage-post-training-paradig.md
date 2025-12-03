---
layout: default
title: MindGPT-4ov: An Enhanced MLLM via a Multi-Stage Post-Training Paradigm
---

# MindGPT-4ov: An Enhanced MLLM via a Multi-Stage Post-Training Paradigm
**arXiv**：[2512.02895v1](https://arxiv.org/abs/2512.02895) · [PDF](https://arxiv.org/pdf/2512.02895.pdf)  
**作者**：Wei Chen, Chaoqun Du, Feng Gu, Wei He, Qizhen Li, Zide Liu, Xuhao Pan, Chang Ren, Xudong Rao, Chenfeng Wang, Tao Wei, Chengjun Yu, Pengfei Yu, Yufei Zheng, Chunpeng Zhou, Pan Zhou, Xuhan Zhu  

**一句话要点**：提出多阶段后训练范式以增强多模态大语言模型能力与部署效率

**关键词**：多模态大语言模型, 后训练范式, 数据生成, 监督微调, 强化学习, 高效部署

## 3 点简述
- 核心问题：如何低成本提升MLLM基础能力与泛化性，实现学术到工业的无缝过渡
- 方法要点：基于信息密度的数据生成、协作课程监督微调、混合强化学习优化推理与多目标
- 实验或效果：在MMBench等基准上超越SOTA，用户体验优异，开源模型权重与代码

## 摘要（原文）

> We present MindGPT-4ov, a multimodal large language model (MLLM) that introduces a general post-training paradigm spanning data production, model training, and efficient deployment. It achieves state-of-the-art performance across multiple benchmarks at low cost, effectively enhancing the foundational capabilities of MLLMs and the generalization ability. Focusing on data construction, supervised fine-tuning strategies, and multimodal reinforcement learning methods, this work proposes three key innovations: (1) An information density-based data generation scheme, integrated with a dual-dimensional tree-structured label system, enabling automated generation of high-quality cross-domain data. (2) A collaborative curriculum supervised fine-tuning approach that balances the injection of domain-specific knowledge with the preservation of general capabilities. (3) A hybrid reinforcement learning paradigm that enhances reasoning ability while simultaneously addressing multi-objective optimization such as diversity exploration, maintenance of multimodal perception, and response conciseness. Moreover, we implement a series of infrastructure optimizations, such as 5D parallel training, operator optimization, and inference quantization to enhance training and inference efficiency while reducing the cost of domain adaptation. Experimental results demonstrate that the MindGPT-4ov model outperforms state-of-the-art models on benchmarks such as MMBench, MMStar, MathVision, and MathVista. In addition, MindGPT-4ov also demonstrates superior user experience in vertical domain tasks, enabling a seamless transition from academic research to industrial deployment. MindGPT-4ov provides a general post-training paradigm applicable to a wide range of MLLMs. The model weights, datasets, and code for the Qwen3-VL-based variants will be recently open-sourced to support the community's development of MLLMs.

