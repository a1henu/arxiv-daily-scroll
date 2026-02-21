---
layout: default
title: FLoRG: Federated Fine-tuning with Low-rank Gram Matrices and Procrustes Alignment
---

# FLoRG: Federated Fine-tuning with Low-rank Gram Matrices and Procrustes Alignment
**arXiv**：[2602.17095v1](https://arxiv.org/abs/2602.17095) · [PDF](https://arxiv.org/pdf/2602.17095.pdf)  
**作者**：Chuiyang Meng, Ming Tang, Vincent W. S. Wong  

**一句话要点**：提出FLoRG框架，通过单低秩矩阵与Gram矩阵聚合解决联邦微调中的聚合误差与分解漂移问题。

**关键词**：联邦学习, 低秩适应, Gram矩阵, Procrustes对齐, 大语言模型微调, 通信效率

## 3 点简述
- LoRA在联邦微调中因双低秩矩阵聚合导致误差与分解漂移，影响模型性能。
- FLoRG采用单低秩矩阵并聚合其Gram矩阵，结合Procrustes对齐减少分解漂移，降低通信开销。
- 实验表明FLoRG在多个基准上优于现有方法，下游任务准确率提升，通信开销最多减少2041倍。

## 摘要（原文）

> Parameter-efficient fine-tuning techniques such as low-rank adaptation (LoRA) enable large language models (LLMs) to adapt to downstream tasks efficiently. Federated learning (FL) further facilitates this process by enabling collaborative fine-tuning across distributed clients without sharing private data. However, the use of two separate low-rank matrices in LoRA for federated fine-tuning introduces two types of challenges. The first challenge arises from the error induced by separately aggregating those two low-rank matrices. The second challenge occurs even when the product of two low-rank matrices is aggregated. The server needs to recover factors via matrix decomposition, which is non-unique and can introduce decomposition drift. To tackle the aforementioned challenges, we propose FLoRG, a federated fine-tuning framework which employs a single low-rank matrix for fine-tuning and aggregates its Gram matrix (i.e., the matrix of inner products of its column vectors), eliminating the aggregation error while also reducing the communication overhead. FLoRG minimizes the decomposition drift by introducing a Procrustes alignment approach which aligns the decomposed matrix between consecutive fine-tuning rounds for consistent updates. We theoretically analyze the convergence of FLoRG and prove that adopting the Procrustes alignment results in a tighter convergence bound. Experimental results across multiple LLM fine-tuning benchmarks demonstrate that FLoRG outperforms five state-of-the-art baseline schemes in the downstream task accuracy and can reduce the communication overhead by up to 2041$\times$.

