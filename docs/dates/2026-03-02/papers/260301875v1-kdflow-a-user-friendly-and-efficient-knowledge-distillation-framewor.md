---
layout: default
title: KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models
---

# KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models
**arXiv**：[2603.01875v1](https://arxiv.org/abs/2603.01875) · [PDF](https://arxiv.org/pdf/2603.01875.pdf)  
**作者**：Songming Zhang, Xue Zhang, Tong Zhang, Bojie Hu, Yufeng Chen, Jinan Xu  

**一句话要点**：提出KDFlow框架以解决大语言模型知识蒸馏中训练效率低下的问题

**关键词**：知识蒸馏, 大语言模型, 训练效率, 解耦架构, 零拷贝传输, 用户友好框架

## 3 点简述
- 核心问题：现有框架对师生模型使用同质训练后端，导致训练效率不佳
- 方法要点：采用解耦架构，结合FSDP2训练和SGLang推理，通过零拷贝传输隐藏状态平衡通信与性能
- 实验或效果：相比现有框架实现1.44倍至6.36倍加速，支持跨分词器蒸馏和快速原型开发

## 摘要（原文）

> Knowledge distillation (KD) is an essential technique to compress large language models (LLMs) into smaller ones. However, despite the distinct roles of the student model and the teacher model in KD, most existing frameworks still use a homogeneous training backend (e.g., FSDP and DeepSpeed) for both models, leading to suboptimal training efficiency. In this paper, we present a novel framework for LLM distillation, termed \textbf{KDFlow}, which features a decoupled architecture and employs SGLang for teacher inference. By bridging the training efficiency of FSDP2 and the inference efficiency of SGLang, KDFlow achieves full utilization of both advantages in a unified system. Moreover, instead of transferring full logits across different processes, our framework only transmits the teacher's hidden states using zero-copy data transfer and recomputes the logits on the student side, effectively balancing the communication cost and KD performance. Furthermore, our framework supports both off-policy and on-policy distillation and incorporates KD algorithms for cross-tokenizer KD through highly extensible and user-friendly APIs. Experiments show that KDFlow can achieve \textbf{1.44$\times$ to 6.36$\times$} speedup compared to current KD frameworks, enabling researchers to rapidly prototype and scale LLM distillation with minimal engineering overhead. Code is available at: https://github.com/songmzhang/KDFlow

