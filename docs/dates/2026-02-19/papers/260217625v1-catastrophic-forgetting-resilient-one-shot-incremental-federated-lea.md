---
layout: default
title: Catastrophic Forgetting Resilient One-Shot Incremental Federated Learning
---

# Catastrophic Forgetting Resilient One-Shot Incremental Federated Learning
**arXiv**：[2602.17625v1](https://arxiv.org/abs/2602.17625) · [PDF](https://arxiv.org/pdf/2602.17625.pdf)  
**作者**：Obaidullah Zaland, Zulfiqar Ahmad Khan, Monowar Bhuyan  

**一句话要点**：提出OSI-FL框架以解决联邦学习中通信开销与灾难性遗忘的双重挑战

**关键词**：联邦学习, 灾难性遗忘, 单轮通信, 扩散模型, 增量学习

## 3 点简述
- 核心问题：联邦学习在增量数据流中面临高通信开销和灾难性遗忘问题
- 方法要点：使用VLM生成嵌入，扩散模型合成数据，结合SSR选择性保留样本
- 实验或效果：在三个基准数据集上优于传统和单轮联邦学习方法

## 摘要（原文）

> Modern big-data systems generate massive, heterogeneous, and geographically dispersed streams that are large-scale and privacy-sensitive, making centralization challenging. While federated learning (FL) provides a privacy-enhancing training mechanism, it assumes a static data flow and learns a collaborative model over multiple rounds, making learning with \textit{incremental} data challenging in limited-communication scenarios. This paper presents One-Shot Incremental Federated Learning (OSI-FL), the first FL framework that addresses the dual challenges of communication overhead and catastrophic forgetting. OSI-FL communicates category-specific embeddings, devised by a frozen vision-language model (VLM) from each client in a single communication round, which a pre-trained diffusion model at the server uses to synthesize new data similar to the client's data distribution. The synthesized samples are used on the server for training. However, two challenges still persist: i) tasks arriving incrementally need to retrain the global model, and ii) as future tasks arrive, retraining the model introduces catastrophic forgetting. To this end, we augment training with Selective Sample Retention (SSR), which identifies and retains the top-p most informative samples per category and task pair based on sample loss. SSR bounds forgetting by ensuring that representative retained samples are incorporated into training in further iterations. The experimental results indicate that OSI-FL outperforms baselines, including traditional and one-shot FL approaches, in both class-incremental and domain-incremental scenarios across three benchmark datasets.

