---
layout: default
title: MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecular Dynamics
---

# MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecular Dynamics
**arXiv**：[2601.02075v1](https://arxiv.org/abs/2601.02075) · [PDF](https://arxiv.org/pdf/2601.02075.pdf)  
**作者**：Zhuofan Shi, Hubao A, Yufei Shao, Mengyan Dai, Yadong Yu, Pan Xiang, Dongliang Huang, Hongxu An, Chunxiao Xin, Haiyang Shen, Zhenyu Wang, Yunshan Na, Gang Huang, Xiang Jing  

**一句话要点**：提出MDAgent2框架，通过领域适应训练解决分子动力学代码生成与知识问答难题

**关键词**：分子动力学模拟, 代码生成, 领域适应训练, 强化学习, 多智能体系统, LAMMPS脚本

## 3 点简述
- 核心问题：分子动力学模拟中LAMMPS脚本编写专业性强、耗时，且现有LLMs因领域数据稀缺、部署成本高和代码可执行性低而受限
- 方法要点：构建高质量领域数据集，采用三阶段后训练策略（CPT、SFT、RL）训练MD-Instruct和MD-Code模型，并引入MD-GRPO闭环强化学习方法
- 实验或效果：在MD-EvalBench基准测试中，模型和系统性能超越多个基线，展示了LLMs在工业模拟任务中的适应性和泛化能力

## 摘要（原文）

> Molecular dynamics (MD) simulations are essential for understanding atomic-scale behaviors in materials science, yet writing LAMMPS scripts remains highly specialized and time-consuming tasks. Although LLMs show promise in code generation and domain-specific question answering, their performance in MD scenarios is limited by scarce domain data, the high deployment cost of state-of-the-art LLMs, and low code executability. Building upon our prior MDAgent, we present MDAgent2, the first end-to-end framework capable of performing both knowledge Q&A and code generation within the MD domain. We construct a domain-specific data-construction pipeline that yields three high-quality datasets spanning MD knowledge, question answering, and code generation. Based on these datasets, we adopt a three stage post-training strategy--continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL)--to train two domain-adapted models, MD-Instruct and MD-Code. Furthermore, we introduce MD-GRPO, a closed-loop RL method that leverages simulation outcomes as reward signals and recycles low-reward trajectories for continual refinement. We further build MDAgent2-RUNTIME, a deployable multi-agent system that integrates code generation, execution, evaluation, and self-correction. Together with MD-EvalBench proposed in this work, the first benchmark for LAMMPS code generation and question answering, our models and system achieve performance surpassing several strong baselines.This work systematically demonstrates the adaptability and generalization capability of large language models in industrial simulation tasks, laying a methodological foundation for automatic code generation in AI for Science and industrial-scale simulations. URL: https://github.com/FredericVAN/PKU_MDAgent2

