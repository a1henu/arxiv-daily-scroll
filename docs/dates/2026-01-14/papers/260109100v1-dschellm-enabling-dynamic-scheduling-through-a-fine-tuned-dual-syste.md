---
layout: default
title: DScheLLM: Enabling Dynamic Scheduling through a Fine-Tuned Dual-System Large language Model
---

# DScheLLM: Enabling Dynamic Scheduling through a Fine-Tuned Dual-System Large language Model
**arXiv**：[2601.09100v1](https://arxiv.org/abs/2601.09100) · [PDF](https://arxiv.org/pdf/2601.09100.pdf)  
**作者**：Lixiang Zhang, Chenggong Zhao, Qing Gao, Xiaoke Zhao, Gengyi Bai, Jinhu Lv  

**一句话要点**：提出DScheLLM，通过微调双系统大语言模型实现动态生产调度优化

**关键词**：动态调度, 大语言模型, 双系统推理, 微调, 作业车间调度, 智能优化

## 3 点简述
- 核心问题：生产调度易受动态干扰，传统方法适应性差，难以泛化到未知扰动。
- 方法要点：构建基于大语言模型的统一框架，采用快慢双系统推理架构，利用LoRA微调华为OpenPangu模型。
- 实验或效果：在标准作业车间调度基准测试中，快思模式高效生成高质量调度，慢思模式产生与求解器兼容的决策输入。

## 摘要（原文）

> Production scheduling is highly susceptible to dynamic disruptions, such as variations in processing times, machine availability, and unexpected task insertions. Conventional approaches typically rely on event-specific models and explicit analytical formulations, which limits their adaptability and generalization across previously unseen disturbances. To overcome these limitations, this paper proposes DScheLLM, a dynamic scheduling approach that leverages fine-tuned large language models within a dual-system (fast-slow) reasoning architecture to address disturbances of different scales. A unified large language model-based framework is constructed to handle dynamic events, where training datasets for both fast and slow reasoning modes are generated using exact schedules obtained from an operations research solver. The Huawei OpenPangu Embedded-7B model is subsequently fine-tuned under the hybrid reasoning paradigms using LoRA. Experimental evaluations on standard job shop scheduling benchmarks demonstrate that the fast-thinking mode can efficiently generate high-quality schedules and the slow-thinking mode can produce solver-compatible and well-formatted decision inputs. To the best of our knowledge, this work represents one of the earliest studies applying large language models to job shop scheduling in dynamic environments, highlighting their considerable potential for intelligent and adaptive scheduling optimization.

