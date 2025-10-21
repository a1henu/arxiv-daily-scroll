---
layout: default
title: Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain
---

# Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain
**arXiv**：[2510.17801v1](https://arxiv.org/abs/2510.17801) · [PDF](https://arxiv.org/pdf/2510.17801.pdf)  
**作者**：Yulin Luo, Chun-Kai Fan, Menghang Dong, Jiayu Shi, Mengdi Zhao, Bo-Wen Zhang, Cheng Chi, Jiaming Liu, Gaole Dai, Rongyu Zhang, Ruichuan An, Kun Wu, Zhengping Che, Shaoxuan Xie, Guocai Yao, Zhongxia Zhao, Pengwei Wang, Guang Liu, Zhongyuan Wang, Tiejun Huang, Shanghang Zhang  

**一句话要点**：提出RoboBench基准以系统评估多模态大语言模型在具身机器人中的认知能力

**关键词**：多模态大语言模型, 具身智能, 机器人基准, 认知评估, 规划模拟, 失败分析

## 3 点简述
- 现有基准在评估具身大脑时存在执行成功偏重和任务真实性不足的问题
- 定义五个维度评估多模态大语言模型，涵盖指令理解、感知推理等能力
- 实验揭示模型在隐式指令理解和时空推理等方面存在根本性局限

## 摘要（原文）

> Building robots that can perceive, reason, and act in dynamic, unstructured
> environments remains a core challenge. Recent embodied systems often adopt a
> dual-system paradigm, where System 2 handles high-level reasoning while System
> 1 executes low-level control. In this work, we refer to System 2 as the
> embodied brain, emphasizing its role as the cognitive core for reasoning and
> decision-making in manipulation tasks. Given this role, systematic evaluation
> of the embodied brain is essential. Yet existing benchmarks emphasize execution
> success, or when targeting high-level reasoning, suffer from incomplete
> dimensions and limited task realism, offering only a partial picture of
> cognitive capability. To bridge this gap, we introduce RoboBench, a benchmark
> that systematically evaluates multimodal large language models (MLLMs) as
> embodied brains. Motivated by the critical roles across the full manipulation
> pipeline, RoboBench defines five dimensions-instruction comprehension,
> perception reasoning, generalized planning, affordance prediction, and failure
> analysis-spanning 14 capabilities, 25 tasks, and 6092 QA pairs. To ensure
> realism, we curate datasets across diverse embodiments, attribute-rich objects,
> and multi-view scenes, drawing from large-scale real robotic data. For
> planning, RoboBench introduces an evaluation framework,
> MLLM-as-world-simulator. It evaluate embodied feasibility by simulating whether
> predicted plans can achieve critical object-state changes. Experiments on 14
> MLLMs reveal fundamental limitations: difficulties with implicit instruction
> comprehension, spatiotemporal reasoning, cross-scenario planning, fine-grained
> affordance understanding, and execution failure diagnosis. RoboBench provides a
> comprehensive scaffold to quantify high-level cognition, and guide the
> development of next-generation embodied MLLMs. The project page is in
> https://robo-bench.github.io.

