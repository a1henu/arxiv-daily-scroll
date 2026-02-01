---
layout: default
title: Breaking the Reasoning Horizon in Entity Alignment Foundation Models
---

# Breaking the Reasoning Horizon in Entity Alignment Foundation Models
**arXiv**：[2601.21174v1](https://arxiv.org/abs/2601.21174) · [PDF](https://arxiv.org/pdf/2601.21174.pdf)  
**作者**：Yuanning Cui, Zequn Sun, Wei Hu, Kexuan Xin, Zhangjie Fu  

**一句话要点**：提出基于并行编码的实体对齐基础模型，以解决图基础模型在长距离依赖推理上的不足

**关键词**：实体对齐, 图基础模型, 并行编码, 长距离依赖, 知识图谱融合

## 3 点简述
- 核心问题：图基础模型直接用于实体对齐时，因推理视野不足，难以处理稀疏异构知识图谱的长距离依赖
- 方法要点：利用种子对齐对作为局部锚点，通过并行编码策略缩短推理轨迹，并整合全局关系图和交互模块
- 实验或效果：实验验证了模型的有效性，展现出对未见知识图谱的强泛化能力

## 摘要（原文）

> Entity alignment (EA) is critical for knowledge graph (KG) fusion. Existing EA models lack transferability and are incapable of aligning unseen KGs without retraining. While using graph foundation models (GFMs) offer a solution, we find that directly adapting GFMs to EA remains largely ineffective. This stems from a critical "reasoning horizon gap": unlike link prediction in GFMs, EA necessitates capturing long-range dependencies across sparse and heterogeneous KG structuresTo address this challenge, we propose a EA foundation model driven by a parallel encoding strategy. We utilize seed EA pairs as local anchors to guide the information flow, initializing and encoding two parallel streams simultaneously. This facilitates anchor-conditioned message passing and significantly shortens the inference trajectory by leveraging local structural proximity instead of global search. Additionally, we incorporate a merged relation graph to model global dependencies and a learnable interaction module for precise matching. Extensive experiments verify the effectiveness of our framework, highlighting its strong generalizability to unseen KGs.

