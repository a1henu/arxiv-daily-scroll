---
layout: default
title: From Memorization to Creativity: LLM as a Designer of Novel Neural-Architectures
---

# From Memorization to Creativity: LLM as a Designer of Novel Neural-Architectures
**arXiv**：[2601.02997v1](https://arxiv.org/abs/2601.02997) · [PDF](https://arxiv.org/pdf/2601.02997.pdf)  
**作者**：Waleed Khalid, Dmitry Ignatov, Radu Timofte  

**一句话要点**：提出基于代码导向LLM的闭环合成框架，以自主设计新颖神经网络架构。

**关键词**：神经架构设计, LLM代码合成, 闭环框架, 监督微调, 结构新颖性, 性能驱动生成

## 3 点简述
- 核心问题：LLM在神经架构设计中平衡语法可靠性、性能和结构新颖性的能力未知。
- 方法要点：通过22轮监督微调循环，结合执行反馈和MinHash-Jaccard过滤，迭代优化架构生成。
- 实验或效果：生成率稳定在50.6%，平均单轮准确率从28.06%提升至50.99%，产生455个高性能新架构。

## 摘要（原文）

> Large language models (LLMs) excel in program synthesis, yet their ability to autonomously navigate neural architecture design--balancing syntactic reliability, performance, and structural novelty--remains underexplored. We address this by placing a code-oriented LLM within a closed-loop synthesis framework, analyzing its evolution over 22 supervised fine-tuning cycles. The model synthesizes PyTorch convolutional networks which are validated, evaluated via low-fidelity performance signals (single-epoch accuracy), and filtered using a MinHash-Jaccard criterion to prevent structural redundancy. High-performing, novel architectures are converted into prompt-code pairs for iterative fine-tuning via parameter-efficient LoRA adaptation, initialized from the LEMUR dataset. Across cycles, the LLM internalizes empirical architectural priors, becoming a robust generator. The valid generation rate stabilizes at 50.6 percent (peaking at 74.5 percent), while mean first-epoch accuracy rises from 28.06 percent to 50.99 percent, and the fraction of candidates exceeding 40 percent accuracy grows from 2.04 percent to 96.81 percent. Analyses confirm the model moves beyond replicating existing motifs, synthesizing 455 high-performing architectures absent from the original corpus. By grounding code synthesis in execution feedback, this work provides a scalable blueprint for transforming stochastic generators into autonomous, performance-driven neural designers, establishing that LLMs can internalize empirical, non-textual rewards to transcend their training data.

