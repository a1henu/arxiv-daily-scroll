---
layout: default
title: Massive Editing for Large Language Models Based on Dynamic Weight Generation
---

# Massive Editing for Large Language Models Based on Dynamic Weight Generation
**arXiv**：[2512.14395v1](https://arxiv.org/abs/2512.14395) · [PDF](https://arxiv.org/pdf/2512.14395.pdf)  
**作者**：Wentao Wan, Qiqing Lao, Zhiwei Xie, Hefeng Wu, Runnan Lin, Liang Lin, Keze Wang  

**一句话要点**：提出基于动态权重生成的大规模编辑方法MeG，以低成本实现大语言模型知识编辑

**关键词**：知识编辑, 大语言模型, 动态权重生成, 扩散模型, 大规模编辑

## 3 点简述
- 核心问题：大规模知识编辑在可靠性、泛化性和局部性指标上仍具挑战
- 方法要点：在特定层附加动态权重神经元，利用扩散模型条件生成权重
- 实验或效果：MeG显著提升大规模编辑性能，尤其在局部性指标上优势明显

## 摘要（原文）

> Knowledge Editing (KE) is a field that studies how to modify some knowledge in Large Language Models (LLMs) at a low cost (compared to pre-training). Currently, performing large-scale edits on LLMs while ensuring the Reliability, Generality, and Locality metrics of the edits remain a challenge. This paper proposes a Massive editing approach for LLMs based on dynamic weight Generation (MeG). Our MeG involves attaching a dynamic weight neuron to specific layers of the LLMs and using a diffusion model to conditionally generate the weights of this neuron based on the input query required for the knowledge. This allows the use of adding a single dynamic weight neuron to achieve the goal of large-scale knowledge editing. Experiments show that our MeG can significantly improve the performance of large-scale KE in terms of Reliability, Generality, and Locality metrics compared to existing knowledge editing methods, particularly with a high percentage point increase in the absolute value index for the Locality metric, demonstrating the advantages of our proposed method.

