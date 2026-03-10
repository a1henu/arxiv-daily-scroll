---
layout: default
title: Covenant-72B: Pre-Training a 72B LLM with Trustless Peers Over-the-Internet
---

# Covenant-72B: Pre-Training a 72B LLM with Trustless Peers Over-the-Internet
**arXiv**：[2603.08163v1](https://arxiv.org/abs/2603.08163) · [PDF](https://arxiv.org/pdf/2603.08163.pdf)  
**作者**：Joel Lidin, Amir Sarfi, Erfan Miahi, Quentin Anthony, Shivam Chauhan, Evangelos Pappas, Benjamin Thérien, Eugene Belilovsky, Samuel Dare  

**一句话要点**：提出Covenant-72B，通过区块链协议实现无许可全球分布式预训练，验证大规模模型可行性。

**关键词**：全球分布式训练, 大规模语言模型, 区块链协议, 无许可参与, SparseLoCo优化器

## 3 点简述
- 核心问题：现有全球分布式训练模型规模小且依赖白名单，未实现完全民主化参与。
- 方法要点：采用SparseLoCo优化器支持动态参与，结合区块链协议确保开放无许可训练。
- 实验或效果：在1.1T tokens上预训练，性能与集中式模型竞争，证明大规模民主化训练可行。

## 摘要（原文）

> Recently, there has been increased interest in globally distributed training, which has the promise to both reduce training costs and democratize participation in building large-scale foundation models. However, existing models trained in a globally distributed manner are relatively small in scale and have only been trained with whitelisted participants. Therefore, they do not yet realize the full promise of democratized participation. In this report, we describe Covenant-72B, an LLM produced by the largest collaborative globally distributed pre-training run (in terms of both compute and model scale), which simultaneously allowed open, permissionless participation supported by a live blockchain protocol. We utilized a state-of-the-art communication-efficient optimizer, SparseLoCo, supporting dynamic participation with peers joining and leaving freely. Our model, pre-trained on approximately 1.1T tokens, performs competitively with fully centralized models pre-trained on similar or higher compute budgets, demonstrating that fully democratized, non-whitelisted participation is not only feasible, but can be achieved at unprecedented scale for a globally distributed pre-training run.

