---
layout: default
title: Breaking the Reasoning Horizon in Entity Alignment Foundation Models
---

# Breaking the Reasoning Horizon in Entity Alignment Foundation Models
**arXiv**：[2601.21174v1](https://arxiv.org/abs/2601.21174) · [PDF](https://arxiv.org/pdf/2601.21174.pdf)  
**作者**：Yuanning Cui, Zequn Sun, Wei Hu, Kexuan Xin, Zhangjie Fu  

**一句话要点**：提出基于并行编码的实体对齐基础模型，以解决知识图谱融合中的长距离依赖问题。

**关键词**：实体对齐, 知识图谱融合, 图基础模型, 并行编码, 长距离依赖, 泛化能力

## 3 点简述
- 核心问题：现有实体对齐模型缺乏可迁移性，且图基础模型直接应用于实体对齐时存在推理视野差距，难以捕获稀疏异构知识图谱的长距离依赖。
- 方法要点：采用并行编码策略，利用种子对齐对作为局部锚点引导信息流，结合合并关系图建模全局依赖和可学习交互模块实现精确匹配。
- 实验或效果：大量实验验证了框架的有效性，显示出对未见知识图谱的强泛化能力。

## 摘要（原文）

> Entity alignment (EA) is critical for knowledge graph (KG) fusion. Existing EA models lack transferability and are incapable of aligning unseen KGs without retraining. While using graph foundation models (GFMs) offer a solution, we find that directly adapting GFMs to EA remains largely ineffective. This stems from a critical "reasoning horizon gap": unlike link prediction in GFMs, EA necessitates capturing long-range dependencies across sparse and heterogeneous KG structuresTo address this challenge, we propose a EA foundation model driven by a parallel encoding strategy. We utilize seed EA pairs as local anchors to guide the information flow, initializing and encoding two parallel streams simultaneously. This facilitates anchor-conditioned message passing and significantly shortens the inference trajectory by leveraging local structural proximity instead of global search. Additionally, we incorporate a merged relation graph to model global dependencies and a learnable interaction module for precise matching. Extensive experiments verify the effectiveness of our framework, highlighting its strong generalizability to unseen KGs.

